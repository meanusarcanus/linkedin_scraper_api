# 💼 LinkedIn Profile Scraper & Verified Email Extractor Pro API

High-performance API engine and Apify Actor designed to scrape LinkedIn profiles, career experience, education, skills, verified decision-maker emails, and AI lead intent scores without cookies or login.

---

## 🚀 Quick Start

### 1. Run Locally
```bash
pip install -r requirements.txt
uvicorn api.index:app --reload
```

### 2. Run Tests
```bash
python3 test_api.py
```

### 3. API Endpoint (`POST /scrape-linkedin`)
```json
{
  "profile_url": "https://www.linkedin.com/in/williamhgates",
  "extract_email": true
}
```
