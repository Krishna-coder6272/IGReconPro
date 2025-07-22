# IGReconPro 🕵️‍♂️

IGReconPro is a powerful Instagram OSINT (Open Source Intelligence) tool designed for security researchers, red teamers, and digital investigators. It allows you to extract deep-level public information about Instagram users using their **username** or **user ID**.

---

## 🔍 Features

- 🔎 Extract detailed profile information from Instagram
- 🕵️ Obfuscated email/phone guessing
- 📷 Profile picture retrieval
- 🧾 Follower/following stats & public data
- 🧪 User ID and Username lookup support
- 📄 Export results to file (planned)
- ✅ Simple CLI-based interface (GUI coming soon!)

---

## ⚙️ Installation

```bash
git clone https://github.com/Krishna-coder6272/IGReconPro.git
cd IGReconPro
pip install -r requirements.txt
```

---
## 🚀 Usage

```
python core.py --username target_username --sessionid (target session id)
```

---

## 📁 Folder Structure

```

IGReconPro/
├── core.py                # Main entry point / CLI tool
├── export.py              # Export related functions (CSV, JSON etc.)
├── fetcher.py             # Functions to fetch data from Instagram
├── parser.py              # Parsing logic for the fetched data
├── utils.py               # Helper/util functions (logging, formatting etc.)
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── .gitignore             # To ignore cache, env files, etc.
├── LICENSE                # (Optional) License file (MIT recommended)
├── tests/                 # (Optional) Unit tests for modules
│   ├── test_fetcher.py
│   ├── test_parser.py
│   └── ...
└── docs/                  # (Optional) Extra documentation, usage guides
    └── usage.md
```


---

## 🛡️ Use Cases


- **Cybersecurity Recon:** Public Instagram data gather karna, email/phone leaks check karna.  
- **Red Team:** Target profiles analyze kar ke social engineering plans banana.  
- **Threat Intel:** Suspicious accounts monitor karna aur behavior analyze karna.  
- **Investigations:** Digital footprint mapping for law enforcement.  
- **Brand Protection:** Fake accounts aur info leaks detect karna.  
- **Bug Bounty:** Sensitive info leaks aur Instagram API misconfigurations dhundna.

---


## 🛠️ Tech Stack

- **Language:** Python 3.8+  
- **HTTP Requests:** `requests` library  
- **HTML Parsing:** `beautifulsoup4`  
- **Command-line Interface:** `argparse`  
- **Output Formatting & Colors:** `colorama`  
- **Data Handling:** Built-in `json`, `time` modules  
- **Version Control:** Git & GitHub  


---

## 👨‍💻 Developed By:

- Krishna Sahu
- Cybersecurity Intern | Red Teamer | Python Developer
- GitHub: Krishna-coder6272
- LinkedIn: https://www.linkedin.com/in/krishna-sahu-66a1b7275/



