# 💼 LinkedIn Profile Scraper & Verified Email Extractor Pro

Extract bulk LinkedIn profiles, work experience, education history, skills, and verified decision-maker emails without cookies or account login. Just $1.99/1k results—50% cheaper than legacy scrapers!

## 🚀 Usage & Input Parameters

| Field | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `profile_url` | string | LinkedIn profile URL | `https://www.linkedin.com/in/williamhgates` |
| `search_query` | string | Search query | `VP of Engineering San Francisco` |
| `extract_email` | boolean | Verify decision-maker email | `true` |
| `max_profiles` | integer | Max profiles to extract | `20` |

## 📤 Output Format

```json
{
  "profile_id": "williamhgates",
  "linkedin_url": "https://www.linkedin.com/in/williamhgates",
  "full_name": "Bill Gates",
  "first_name": "Bill",
  "last_name": "Gates",
  "headline": "Co-chair, Bill & Melinda Gates Foundation.",
  "current_title": "Co-chair",
  "current_company": "Bill & Melinda Gates Foundation",
  "location": "Seattle, Washington, United States",
  "verified_email": "bill.gates@gatesfoundation.org",
  "email_status": "✅ Verified (SMTP Socket Passed)",
  "work_experience": [
    {
      "title": "Co-chair",
      "company": "Bill & Melinda Gates Foundation",
      "duration": "2000 - Present"
    }
  ],
  "education": [
    {
      "school": "Harvard University",
      "degree": "Honorary Doctorate"
    }
  ],
  "skills": ["Software Engineering", "Philanthropy", "AI Strategy"],
  "ai_lead_score": "Tier 1 High-Intent Leader (98/100 Lead Score)."
}
```
