# 💼 RapidAPI Master Listing & Documentation Kit: LinkedIn Scraper Pro

Complete, standalone documentation kit for publishing **LinkedIn Profile Scraper & Verified Email Extractor Pro (`POST /scrape-linkedin`)** on **RapidAPI Studio** ([provider.rapidapi.com](https://provider.rapidapi.com)).

---

## 📌 1. RapidAPI Listing Metadata

- **API Name**: `LinkedIn Profile Scraper & Verified Email Extractor Pro`
- **Category**: `Lead Generation` / `Data` / `Business`
- **Base URL**: `https://microsaas-agent-api.vercel.app`
- **Endpoint**: `POST /scrape-linkedin`

---

## 📝 2. Short Description (Tagline / Summary - Under 250 Chars)

```text
Extract bulk LinkedIn profiles, work experience, education, skills, and verified decision-maker emails without cookies or login. Enriched with AI lead scoring at 50% lower cost.
```

---

## 📜 3. Long Description (RapidAPI Overview Tab)

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

---

## 💰 4. Recommended RapidAPI Pricing Tiers

| Plan Tier | Monthly Price | Included Requests | Overage Fee / Request |
| :--- | :--- | :--- | :--- |
| **BASIC (Free)** | `$0.00 / mo` | 20 requests | Hard Cap (No Overages) |
| **PRO** | **`$29.00 / mo`** | 2,500 requests | `$0.015 / request` |
| **ULTRA** | **`$79.00 / mo`** | 10,000 requests | `$0.010 / request` |
| **MEGA** | **`$199.00 / mo`** | 30,000 requests | `$0.008 / request` |
