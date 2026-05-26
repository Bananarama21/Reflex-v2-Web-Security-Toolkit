# Reflex v2 — Web Security Toolkit 🛡️

**Hey, I'm Euan Smith** 

This repository contains my hands-on security tools. Inspired by Google's Project Zero and open security research, I'm building practical projects to deepen my understanding of web vulnerabilities.

---

## 🚀 Reflex v2

An educational Python toolkit for learning and testing common web security issues.

### ✨ Key Features
- Reflected XSS, Open Redirect, and Information Leak detection
- **Improved DOM XSS Simulation** (interactive and educational)
- **Smart Mutation Fuzzer** with payload encoding
- Basic Burp Suite JSON export support
- Clean CLI with colored output + HTML reports
- GitHub Actions CI/CD

### 🛠 Quick Start

```bash
git clone https://github.com/Bananarama21/Reflex-v2-Web-Security-Toolkit.git
cd Reflex-v2-Web-Security-Toolkit
pip install -r requirements.txt
python reflex.py --help

examples

# Full scan
python reflex.py --url https://testphp.vulnweb.com --scan all

# Run fuzzer
python reflex.py --url https://example.com/search --fuzz --param search

# DOM XSS Simulator
python dom_xss_sim.py

# Scan from Burp export
python reflex.py --burp burp_export.json
