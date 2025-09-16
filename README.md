# 🕵️‍♂️ Wolf Proxy

![Python](https://img.shields.io/badge/python-3.x-blue.svg)

A simple and clean tool to scrape public proxies from [us-proxy.org](https://www.us-proxy.org/), test which ones work, and save the valid ones.

---

## ✨ Features

- 🔍 **Automatically fetches proxy list** from `us-proxy.org`
- 🛠️ **Tests each proxy** by accessing `google.com`
- 💾 **Saves valid proxies** to `valid_proxy.txt`
- 🎨 **Colorful interface** with custom ASCII art
- ⏳ **Random delays** between requests to avoid blocking

---

## 🚀 How to Use

### 📦 Option 1: Run with Python

```bash
python proxymain.py
```

### 📦 Option 2: Use the executable (after building)

1. Give permission and build:
   ```bash
   chmod +x build.sh
   ./build.sh
   ```

2. Run:
   ```bash
   ./dist/ProxyCheckerTool.exe
   ```

---

## 📌 Details

- 🌐 Proxies are tested against: `http://www.google.com`
- ⏲️ Default timeout: **3 seconds**
- 🕑 Random delay between **1 to 2 seconds** between tests

---

## 💻 Requirements

- Python 3.x
- Libraries:
  - `requests`
  - `colorama`
  - `beautifulsoup4`

> 📦 Tip: Install everything with  
> ```bash
> pip install -r requirements.txt
> ```

---

made with <3 by hax
