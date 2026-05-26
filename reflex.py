#!/usr/bin/env python3
"""
Reflex v2 - Educational Web Security Toolkit
Built by Euan Smith | Learning project inspired by Project Zero
"""

import requests
import argparse
import json
import os
from datetime import datetime
from bs4 import BeautifulSoup
from colorama import init, Fore, Style
from urllib.parse import urlparse, urljoin
import re

init(autoreset=True)

# Better payload sets
PAYLOADS = {
    "xss": [
        "<script>alert(1)</script>",
        "\"><script>alert(1)</script>",
        "<img src=x onerror=alert(1)>",
        "javascript:alert(1)",
        "<svg/onload=alert(1)>"
    ],
    "redirect": [
        "https://evil.com",
        "//evil.com",
        "/\\evil.com",
        "https://google.com%2f@evil.com"
    ]
}

def is_reflected(response_text, payload):
    """Better reflection check"""
    return re.search(re.escape(payload), response_text, re.IGNORECASE) is not None

def scan_url(base_url, scan_types):
    print(f"{Fore.CYAN}[*] Starting scan on: {base_url}")
    findings = []
    
    try:
        for scan_type in scan_types:
            for payload in PAYLOADS.get(scan_type, []):
                test_url = f"{base_url}{'&' if '?' in base_url else '?'}q={requests.utils.quote(payload)}"
                
                r = requests.get(test_url, timeout=8, allow_redirects=True)
                
                if is_reflected(r.text, payload):
                    findings.append({
                        "type": scan_type.upper(),
                        "payload": payload,
                        "url": test_url,
                        "status_code": r.status_code,
                        "severity": "High" if scan_type == "xss" else "Medium"
                    })
                    print(f"{Fore.RED}[!] Potential {scan_type.upper()} found!")
                    print(f"    → {test_url}")
    except Exception as e:
        print(f"{Fore.YELLOW}[!] Error scanning: {e}")
    
    return findings

def run_fuzzer(base_url, param="q", iterations=15):
    print(f"{Fore.CYAN}[*] Running mutation fuzzer on parameter: {param}")
    base_payloads = PAYLOADS["xss"]
    findings = []
    
    for i in range(iterations):
        payload = base_payloads[i % len(base_payloads)]
        mutated = payload + ("'" if i % 3 == 0 else "") + ('"' if i % 2 == 0 else "")
        
        test_url = f"{base_url}{'&' if '?' in base_url else '?'} {param}={requests.utils.quote(mutated)}"
        try:
            r = requests.get(test_url, timeout=6)
            if mutated in r.text:
                findings.append(mutated)
                print(f"{Fore.RED}[!] Fuzzer hit with: {mutated[:60]}...")
        except:
            pass
    return findings

def generate_report(findings, target):
    os.makedirs("reports", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reports/reflex_report_{timestamp}.html"
    
    html_content = f"""
    <html>
    <head><title>Reflex v2 Report - {target}</title>
    <style>body {{font-family: Arial;}} table {{border-collapse: collapse;}} th, td {{padding: 8px; border: 1px solid #ccc;}}</style>
    </head>
    <body>
    <h1>Reflex v2 Scan Report</h1>
    <p><strong>Target:</strong> {target}</p>
    <p><strong>Generated:</strong> {datetime.now()}</p>
    <h2>Findings ({len(findings)})</h2>
    <table>
    <tr><th>Type</th><th>Payload</th><th>URL</th><th>Severity</th></tr>
    """
    
    for f in findings:
        html_content += f"<tr><td>{f['type']}</td><td>{f['payload']}</td><td>{f['url']}</td><td>{f['severity']}</td></tr>"
    
    html_content += "</table></body></html>"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"{Fore.GREEN}[+] Report generated: {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reflex v2 - Educational Security Toolkit by Euan Smith")
    parser.add_argument("--url", help="Target URL to scan")
    parser.add_argument("--scan", choices=["xss", "redirect", "all"], default="all")
    parser.add_argument("--fuzz", action="store_true", help="Enable fuzzer")
    parser.add_argument("--param", default="q", help="Parameter to fuzz")
    parser.add_argument("--burp", help="Path to Burp JSON export")
    
    args = parser.parse_args()
    
    if not args.url and not args.burp:
        print(f"{Fore.RED}[!] Please provide --url or --burp")
        exit(1)
    
    if args.burp:
        print(f"{Fore.CYAN}[*] Burp export parsing coming soon...")
        # Can be expanded later
    
    if args.url:
        scan_types = ["xss", "redirect"] if args.scan == "all" else [args.scan]
        findings = scan_url(args.url, scan_types)
        
        if args.fuzz:
            run_fuzzer(args.url, args.param)
        
        if findings:
            generate_report(findings, args.url)
        else:
            print(f"{Fore.GREEN}[+] No obvious vulnerabilities found (educational scan)")
