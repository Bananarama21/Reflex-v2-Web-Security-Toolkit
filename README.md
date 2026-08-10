# Reflex

Small Python toolkit for poking at web apps for the classics: reflected XSS, open redirects, DOM XSS, and basic payload mutation for when the classics don't land first try.

Built to actually learn how these vulnerabilities work, not just read about them. Point it at something you own or have permission to test — [testphp.vulnweb.com](http://testphp.vulnweb.com) is a good default if you don't have a target handy.

## What it does

- Scans for reflected XSS and open redirects
- DOM XSS demo (safe, local, no live exploitation)
- Basic mutation fuzzer for parameter values
- Colour-coded terminal output
- Dumps findings to an HTML report, so you're not squinting at scrollback

## Setup

```bash
git clone https://github.com/EuanSmith2/reflex.git
cd reflex
pip install -r requirements.txt
```

## Usage

```bash
python reflex.py --url https://testphp.vulnweb.com --scan all
python reflex.py --url https://example.com/search --fuzz --param q
python dom_xss_sim.py
```

## Ethics, briefly

Don't run this against anything you don't own or don't have written permission to test. Not a legal disclaimer — just how you stay out of trouble.
