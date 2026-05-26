#!/usr/bin/env python3
"""
Reflex v2 - Educational Web Security Toolkit
Built by Euan Smith
"""

import requests
import argparse
import json
from bs4 import BeautifulSoup
from colorama import init, Fore
import datetime
from jinja2 import Template
import os

init(autoreset=True)

PAYLOADS = {
    "xss": ["<script>alert(1)</script>", "\"><img src=x onerror=alert(1)>", "javascript:alert(1)"],
    "redirect": ["https://evil.com", "//evil.com"],
}

def scan_url(url, scan_types):
    print(f"{Fore.CYAN}[*] Scanning {url}")
    results = []
    
    try:
        for ptype in scan_types:
            for payload in PAYLOADS.get(ptype, []):
                test_url = f"{url}?q={payload}" if "?" not in url else f"{url}&q={payload}"
                r = requests.get(test_url, timeout=5)
                
                if payload in r.text:
                    results.append({"type": ptype, "payload": payload, "url": test_url, "status": "Potential"})
                    print(f"{Fore.RED}[!] Potential {ptype} found with {payload}")
    except Exception as e:
        print(f"{Fore.YELLOW}[!] Error: {e}")
    
    return results

def run_fuzzer(url, param, payloads_type):
    print(f"{Fore.CYAN}[*] Fuzzing parameter: {param}")
    # Simple mutation fuzzer
    base_payloads = PAYLOADS.get(payloads_type, ["test"])
    for base in base_payloads:
        mutated = base + "'\"<"
        test_url = f"{url}?{param}={mutated}"
        requests.get(test_url)

def generate_report(results, url):
    os.makedirs("reports", exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"reports/reflex_{timestamp}.html"
    
    html = f"""
    <h1>Reflex Scan Report</h1>
    <p>Target: {url}</p>
    <p>Time: {datetime.datetime.now()}</p>
    <h2>Findings</h2>
    <ul>
    """
    for r in results:
        html += f"<li><b>{r['type']}</b> - {r['payload']}</li>"
    html += "</ul>"
    
    with open(filename, "w") as f:
        f.write(html)
    print(f"{Fore.GREEN}[+] Report saved: {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Reflex - Educational Security Scanner")
    parser.add_argument("--url", required=True, help="Target URL")
    parser.add_argument("--scan", choices=["xss", "redirect", "all"], default="all")
    parser.add_argument("--fuzz", action="store_true")
    parser.add_argument("--param", default="q")
    parser.add_argument("--payloads", choices=["xss", "redirect"], default="xss")
    parser.add_argument("--burp", help="Path to Burp JSON export")
    
    args = parser.parse_args()
    
    if args.burp:
        print(f"{Fore.CYAN}[*] Loading Burp export: {args.burp}")
        # Basic stub - can be expanded
        pass
    
    results = scan_url(args.url, ["xss", "redirect"] if args.scan == "all" else [args.scan])
    
    if args.fuzz:
        run_fuzzer(args.url, args.param, args.payloads)
    
    generate_report(results, args.url)
    print(f"{Fore.GREEN}[✓] Scan completed!")
