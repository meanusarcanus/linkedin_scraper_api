#!/usr/bin/env python3
"""
Automated Test Suite for LinkedIn Profile Scraper & Verified Email Extractor API
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "api"))

from index import app, read_root, scrape_linkedin, LinkedInScrapeRequest

def test_suite():
    print("==================================================")
    print(" 💼 TESTING LINKEDIN PROFILE SCRAPER & EMAIL API")
    print("==================================================")

    # Test 1: Root Health Check
    print("\n[Test 1] Health Check Endpoint (GET /)...")
    res_root = read_root()
    assert res_root.get("status") == "online"
    print("✓ Health Check Passed!")

    # Test 2: Scrape Profile URL
    print("\n[Test 2] Scrape Profile URL (POST /scrape-linkedin)...")
    res_url = scrape_linkedin(LinkedInScrapeRequest(
        profile_url="https://www.linkedin.com/in/williamhgates",
        extract_email=True
    ))
    print("Query Type:", res_url.query_type)
    print("Target Query:", res_url.target_query)
    print("Total Scraped Profiles:", res_url.total_scraped)
    print("Sample Profile Name:", res_url.profiles[0].full_name if res_url.profiles else "None")
    print("Verified Email:", res_url.profiles[0].verified_email if res_url.profiles else "None")
    assert res_url.total_scraped > 0
    assert "linkedin.com" in res_url.profiles[0].linkedin_url
    assert "@" in res_url.profiles[0].verified_email
    print("✓ Profile URL Scrape Passed!")

    # Test 3: Scrape Search Query
    print("\n[Test 3] Scrape Search Query (POST /scrape-linkedin)...")
    res_search = scrape_linkedin(LinkedInScrapeRequest(
        search_query="VP of Engineering San Francisco",
        max_profiles=5
    ))
    assert res_search.total_scraped > 0
    print("✓ Search Query Scrape Passed!")

    print("\n==================================================")
    print(" 🎉 ALL LINKEDIN SCRAPER TESTS PASSED 100%!")
    print("==================================================")

if __name__ == "__main__":
    test_suite()
