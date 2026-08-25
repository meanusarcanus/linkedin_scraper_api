# 💼 LinkedIn Profile Scraper & Verified Email Extractor Pro Python SDK

Official Python SDK for `linkedin-scraper-api`. Extract LinkedIn profiles, work experience, education, skills, verified emails, and AI lead scores in 1 line of Python code.

## 🚀 Installation
```bash
pip install linkedin-scraper-api
```

## 💻 Quick Usage
```python
from linkedin_scraper import LinkedInScraperClient

client = LinkedInScraperClient(api_key="YOUR_RAPIDAPI_KEY")
res = client.scrape_linkedin(profile_url="https://www.linkedin.com/in/williamhgates", extract_email=True)

for profile in res["profiles"]:
    print(f"Name: {profile['full_name']} | Title: {profile['current_title']} | Verified Email: {profile['verified_email']}")
```
