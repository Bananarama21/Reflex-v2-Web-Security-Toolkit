# Reflex v2 — Web Security Toolkit 🛡️

**Hey, I'm Euan Smith** — Recent HCETSS graduate (Class of 2025) and incoming BSc Cybersecurity & Digital Forensics student at Technological University Dublin (Blanchardstown).

This repository shows hands-on learning in web security. Inspired by Google's Project Zero.

---

## 🚀 Reflex v2

An educational Python toolkit for learning common web vulnerabilities.

### Features
- Reflected XSS & Open Redirect Scanner
- DOM XSS Simulation (safe demo)
- Mutation Fuzzer
- Colored output + HTML reports

### Quick Start

```bash
git clone https://github.com/Bananarama21/Reflex-v2-Web-Security-Toolkit.git
cd Reflex-v2-Web-Security-Toolkit
pip install -r requirements.txt
Example Commands
Bash# Full scan
python reflex.py --url https://testphp.vulnweb.com --scan all

# With fuzzer
python reflex.py --url https://example.com/search --fuzz --param q

# DOM XSS Simulator
python dom_xss_sim.py

LinkedIn: https://www.linkedin.com/in/euan-smith-4295123a6/
