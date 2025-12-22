# MUMBAI-GYM-LISTINGS
This project helps the client to get information about all the gyms in Mumbai, basically a lead generation task.


# Project Brief: High-Quality Lead List for Fitness Marketing

**Client:** Apex Fitness Solutions
**Date:** December 22, 2025
**Deadline:** 24 Hours

## 1. Objective
We are launching a B2B cold-calling campaign for fitness equipment in India. We need a fresh, verified list of **Gyms and Fitness Centers located in Mumbai**. We are specifically targeting businesses to sell them commercial treadmills.

## 2. Target Data Source
* **Source:** Google Maps
* **Search Query:** "Gyms in Mumbai" / "Fitness Centers in Mumbai"
* **Location:** Mumbai, India

## 3. Data Requirements (The Columns)
I need a `.csv` file with exactly these headers. Do not include extra junk data.

| Column Name | Description | Requirement |
| :--- | :--- | :--- |
| `Business Name` | Name of the gym | Must be clean (remove emojis if any) |
| `Phone Number` | Primary contact number | **CRITICAL.** Must include country code (+91) |
| `Address` | Full physical address | |
| `Website` | Link to their website | If no website, leave blank |
| `Rating` | Google Review Score (e.g., 4.5) | Optional but preferred |

## 4. Technical Constraints & Quality Control
* **No Duplicates:** I don't want to call the same "Gold's Gym" branch twice. Deduplicate based on Phone Number or Address.
* **Volume:** I need a sample batch of **50 verified leads** to start. If the quality is good, I will order 5,000.
* **Delivery Format:** `leads_mumbai_v1.csv`

## 5. Acceptance Criteria (How you pass)
1.  The CSV opens in Excel without formatting errors.
2.  At least 80% of rows must have a valid **Phone Number**.
3.  No "Permanently Closed" businesses (if possible to filter).

---

### Client Note:
> *"I've hired scrapers before who gave me a list full of null values and duplicates. If you can automate the scrolling to get deep into the results list and parse the phone numbers correctly, you're hired for the long term."*