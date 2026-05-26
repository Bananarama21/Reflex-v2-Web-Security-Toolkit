#!/usr/bin/env python3
"""
Reflex v2 - Educational Web Security Toolkit
Built by Euan Smith
"""

import requests
import argparse
import os
from datetime import datetime
from colorama import init, Fore
from urllib.parse import quote
import re

init(autoreset=True)

PAYLOADS = {
    "xss": [
        "<script>alert(1)</script>",
        "\"><img src=x onerror=alert(1)>",
        "<svg/onload=alert(1)>",
        "javascript:alert(1)"
    ],
    "redirect": [
        "//evil.com",
        "https://evil.com",
        "/\\evil.com"
    ]
}

def scan_url(url, scan_types):
    print(f"{Fore.CYAN}[*] Scanning {url}")
    findings = []
    
    for stype in scan_types:
        for payload in PAYLOADS.get(stype, []):
            try:
                test_url = f"{url}{'&' if '?' in url else '?'}q={quote(payload)}"
                r = requests.get(test_url, timeout=10, allow_redirects=True)
                
                if re.search(re.escape(payload), r.text, re.IGNORECASE):
                    findings.append({
                        "type": stype.upper(),
                        "payload": payload,
                        "url": test_url,
                        "status": r.status_code
                    })
                    print(f"{Fore.RED}[!] Potential {stype.upper()} → {test_url}")
            except Exception as e:
                print(f"{Fore.YELLOW}[!] Error: {e}")
    return findings

def run_fuzzer(url, param="q"):
    print(f"{Fore.CYAN}[*] Running fuzzer on parameter '{param}'...")
    base = PAYLOADS["xss"][0]
    for i in range(12):
        mutated = base + ("'" * (i%3)) + ('"' * (i%2))
        try:
            test_url = f"{url}{'&' if '?' in url else '?'} {param}={quote(mutated)}"
            r = requests.get(test_url, timeout=8)
            if mutated[:20] in r.text:
                print(f"{Fore.RED}[!] Fuzzer hit with mutation!")
        except:
            pass

def generate_report(findings, target_url):
    os.makedirs("reports", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M")
    filename = f"reports/reflex_report_{timestamp}.html"
    
    with open(filename, "w") as f:
        f.write(f"<h1>Reflex v2 Report - {target_url}</h1>")
        f.write(f"<p>Generated: {datetime.now()}</p>")
        f.write("<h2>Findings</h2><ul>")
        for fnd in findings:
            f.write(f"<li><b>{fnd['type']}</b> - {fnd['payload']}</li>")
        f.write("</ul>")
    
    print(f"{Fore.GREEN}[+] Report saved → {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reflex v2 by Euan Smith")
    parser.add_argument("--url", help="Target URL")
    parser.add_argument("--scan", choices=["xss", "redirect", "all"], default="all")
    parser.add_argument("--fuzz", action="store_true")
    parser.add_argument("--param", default="q")
    
    args = parser.parse_args()
    
    if not args.url:
        print(f"{Fore.RED}[!] Please provide --url")
        exit(1)
    
    scan_types = ["xss", "redirect"] if args.scan == "all" else [args.scan]
    findings = scan_url(args.url, scan_types)
    
    if args.fuzz:
        run_fuzzer(args.url, args.param)
    
    if findings:
        generate_report(findings, args.url)
    else:
        print(f"{Fore.GREEN}[+] Scan finished - no obvious issues found (educational tool)")
