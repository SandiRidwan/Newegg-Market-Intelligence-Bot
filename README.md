# 🦅 Newegg Market Intelligence Bot
**Autonomous High-Volume E-commerce Extraction Engine**

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?style=for-the-badge&logo=python)
![Selenium](https://img.shields.io/badge/Automation-Selenium-red.svg?style=for-the-badge&logo=selenium)
![E-commerce](https://img.shields.io/badge/Target-Newegg-orange.svg?style=for-the-badge)
![Database](https://img.shields.io/badge/Output-Excel/CSV-green.svg?style=for-the-badge&logo=microsoft-excel)

---

## ⚡ The "Predator-Search" Logic
This isn't a basic scraper. Built with a **Predator-Search Architecture**, this bot is designed to hunt down product data across complex navigational structures. It bypasses shallow scraping limitations to extract deep-level market intelligence.

> **Current Scale:** 4,000+ Unique Product Records across 100+ Tech Categories.

---

## 🚀 Performance Metrics

* **🛰️ Scope:** 100+ Categories (from High-End GPUs to Smart Home IoT).
* **🏎️ Speed:** Optimized concurrent-ready processing with recursive pagination.
* **📦 Reliability:** Built-in **Checkpoint System** to resume from the last successful category.
* **🛠️ Architecture:** Full **Modular OOP (Object-Oriented Programming)** for easy scaling.

---

## 🛠️ Key Technical Features

### 🔍 Seed-Based Discovery
Uses a proprietary list of **100 master keywords** to ensure 100% site coverage, capturing products that traditional category-browsing might miss.

### 🛡️ Anti-Detection Suite
* **User-Agent Rotation:** Mimics various modern browsers to avoid fingerprinting.
* **Randomized Jitter:** Implements human-mimicry sleep intervals between 3s to 8s.
* **Remote Debugging:** Operates via established browser sessions to bypass initial bot-checks.

### 🔄 Recursive Pagination
Automatically detects and traverses "Next Page" buttons across thousands of results until the last record is captured.

---

## 📂 Project Structure

```text
├── src/
│   ├── main_scraper.py      # Entry point for the bot
│   ├── logic_engine.py      # Predator-Search algorithms
│   └── data_handler.py      # Excel Checkpoint & Formatting
├── data/                    # Auto-saved category results
├── requirements.txt         # Dependency list
└── README.md
