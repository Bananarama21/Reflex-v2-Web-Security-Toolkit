# 🛡️ Reflex

Educational Python toolkit for discovering and understanding common web vulnerabilities — reflected XSS, open redirects, DOM XSS, and mutation-based fuzzing — with colored terminal output and HTML reports.

**Ethical use only.** Built for learning and authorized testing (CTFs, your own test targets, permitted engagements). Do not point this at systems you don't have permission to test.

## Features

- Reflected XSS & open redirect scanner
- DOM XSS simulation (safe demo target, no live exploitation)
- Mutation-based fuzzer
- Colored terminal output + HTML report generation

## Quick start

```bash
git clone https://github.com/EuanSmith2/reflex.git
cd reflex
pip install -r requirements.txt
```

## Usage

```bash
# Full scan
python reflex.py --url https://testphp.vulnweb.com --scan all

# With fuzzer
python reflex.py --url https://example.com/search --fuzz --param q

# DOM XSS simulator
python dom_xss_sim.py
```
