"""
Official Python SDK Client for LinkedIn Profile Scraper & Verified Email Extractor Pro
"""

import requests
from typing import Optional, Dict, Any

class LinkedInScraperClient:
    """
    Python SDK Client for LinkedIn Scraper API.
    """
    def __init__(self, api_key: str, base_url: str = "https://microsaas-agent-api.vercel.app"):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "X-RapidAPI-Key": self.api_key,
            "Content-Type": "application/json"
        }

    def scrape_linkedin(self, profile_url: Optional[str] = None, search_query: Optional[str] = None, extract_email: bool = True, max_profiles: int = 10) -> dict:
        """
        Scrape LinkedIn profiles, work experience, education, skills, and verified emails.
        """
        url = f"{self.base_url}/scrape-linkedin"
        payload = {
            "profile_url": profile_url,
            "search_query": search_query,
            "extract_email": extract_email,
            "max_profiles": max_profiles
        }
        response = requests.post(url, json=payload, headers=self.headers, timeout=30)
        response.raise_for_status()
        return response.json()
