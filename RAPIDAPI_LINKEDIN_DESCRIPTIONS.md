# 📝 RapidAPI Short & Long Descriptions for LinkedIn Scraper Pro

Below are the pre-written **Short Description** and **Long Description** formatted specifically for your RapidAPI listing.

---

## 📌 1. Short Description (Tagline / Summary - Under 250 Chars)

```text
Extract bulk LinkedIn profiles, work experience, education, skills, and verified decision-maker emails without cookies or login. Enriched with AI lead scoring at 50% lower cost.
```

---

## 📜 2. Long Description (Full RapidAPI Overview Markdown)

```markdown
# 💼 LinkedIn Profile Scraper & Verified Email Extractor Pro

Extract bulk LinkedIn profile data, career history, skills, education, decision-maker contacts, and verified email addresses by profile URL or search query in real-time.

---

## 🚀 Key Features & Extracted Data Fields

* **👤 Profile & Contact Metrics**: Full Name, Current Title, Current Company, Location, Summary Bio, and Connections Count.
* **✉️ Real-Time Email Verification**: Live SMTP socket validation for decision-maker business email addresses (`verified_email`).
* **💼 Career & Education History**: Complete Work Experience timeline (title, company, duration) and Education degrees.
* **🎯 AI Lead Scoring**: Automated lead intent rating (e.g. `"Tier 1 High-Intent Leader (98/100)"`).
* **⚡ No Cookies or Login Required**: High-performance serverless engine designed for B2B sales automation and recruitment outreach.

---

## 🛠️ Example Use Cases

1. **B2B Outbound Sales & Prospecting**: Find verified email addresses of decision-makers (CTOs, VPs, Founders).
2. **Talent Acquisition & Recruiting**: Scrape candidate work histories, skills, and contact details automatically.
3. **Market & Competitor Intelligence**: Monitor executive movement and leadership changes across companies.

---

## 📥 Sample Request JSON

```json
{
  "profile_url": "https://www.linkedin.com/in/williamhgates",
  "extract_email": true
}
```

## 📤 Sample Response JSON

```json
{
  "status": "success",
  "query_type": "url",
  "target_query": "https://www.linkedin.com/in/williamhgates",
  "total_scraped": 1,
  "profiles": [
    {
      "profile_id": "williamhgates",
      "linkedin_url": "https://www.linkedin.com/in/williamhgates",
      "full_name": "Bill Gates",
      "first_name": "Bill",
      "last_name": "Gates",
      "headline": "Co-chair, Bill & Melinda Gates Foundation. Founder, Breakthrough Energy. Co-founder, Microsoft.",
      "current_title": "Co-chair",
      "current_company": "Bill & Melinda Gates Foundation",
      "location": "Seattle, Washington, United States",
      "verified_email": "bill.gates@gatesfoundation.org",
      "email_status": "✅ Verified (SMTP Socket Passed)",
      "work_experience": [
        {
          "title": "Co-chair",
          "company": "Bill & Melinda Gates Foundation",
          "duration": "2000 - Present",
          "description": "Global health and development initiatives."
        }
      ],
      "education": [
        {
          "school": "Harvard University",
          "degree": "Honorary Doctorate",
          "field_of_study": "Computer Science & Law"
        }
      ],
      "skills": ["Software Engineering", "Philanthropy", "Venture Capital", "AI Strategy"],
      "summary_bio": "Co-chair of the Bill & Melinda Gates Foundation.",
      "connections_count": 500,
      "ai_lead_score": "Tier 1 High-Intent Leader (98/100 Lead Score)."
    }
  ]
}
```
```
