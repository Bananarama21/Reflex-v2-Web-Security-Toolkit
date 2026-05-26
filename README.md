# Reflex v2 — Web Security Toolkit 🛡️

**Hey, I'm Euan Smith** — Recent HCETSS graduate and incoming Cybersecurity student at TU Dublin.

This is my hands-on web security project. Inspired by Google's Project Zero.

### Quick Start
```bash
git clone https://github.com/Bananarama21/Reflex-v2-Web-Security-Toolkit.git
cd Reflex-v2-Web-Security-Toolkit
pip install -r requirements.txt
Example Commands
Bashpython reflex.py --url https://testphp.vulnweb.com --scan all

python reflex.py --url https://example.com/search --fuzz --param q

python dom_xss_sim.py
Euan Smith | Dublin
text6. Scroll down and click **"Commit changes"**

---

### Step 2: Create requirements.txt

1. On the main repo page, click **"Add file"** → **"Create new file"**
2. In the file name box, type exactly: `requirements.txt`
3. Copy and paste this:

```txt
requests>=2.32.0
beautifulsoup4>=4.12.0
colorama>=0.4.6
pywebview>=5.0
