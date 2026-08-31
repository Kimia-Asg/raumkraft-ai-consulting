"""
Generate synthetic datasets for the RaumKraft BI dashboard.
All data is fictional — no real personal data is used.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

random.seed(42)
np.random.seed(42)

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# --- Helper data ---
DISTRICTS = [
    "Hamburg-Eimsbüttel", "Hamburg-Altona", "Hamburg-Eppendorf",
    "Hamburg-Winterhude", "Hamburg-Ottensen", "Hamburg-Barmbek",
    "Hamburg-HafenCity", "Hamburg-Blankenese", "Hamburg-Wandsbek",
    "Hamburg-Bergedorf", "Hamburg-Harburg", "Hamburg-St. Pauli"
]

PROPERTY_TYPES = ["Apartment", "House", "Commercial", "Penthouse", "Studio"]
PROPERTY_WEIGHTS = [0.50, 0.25, 0.12, 0.05, 0.08]

ENERGY_CLASSES = ["A+", "A", "B", "C", "D", "E", "F"]
ENERGY_WEIGHTS = [0.05, 0.10, 0.25, 0.30, 0.15, 0.10, 0.05]

CHANNELS = ["Email", "Contact Form", "WhatsApp", "Phone"]
CHANNEL_WEIGHTS = [0.35, 0.25, 0.25, 0.15]

ENQUIRY_TYPES = ["Viewing Request", "Pricing Question", "Availability Check",
                 "Design Consultation", "General Enquiry", "Complaint"]
ENQUIRY_WEIGHTS = [0.30, 0.20, 0.20, 0.10, 0.15, 0.05]

SERVICE_LINES = ["Brokerage", "Interior Design", "Property Management"]

AGENT_FIRST_NAMES = [
    "Anna", "Max", "Lena", "Felix", "Sarah", "Jonas", "Marie", "Tim",
    "Laura", "David", "Julia", "Niklas", "Sophia", "Leon", "Emma",
    "Moritz", "Lea", "Finn", "Clara", "Paul", "Mia", "Lukas",
    "Hannah", "Ben", "Amelie", "Jan", "Lisa", "Tom", "Nora", "Erik",
    "Katharina", "Florian", "Johanna", "Philipp", "Carla", "Tobias",
    "Helena", "Sebastian", "Lina", "Christian", "Eva", "Matthias",
    "Antonia", "Patrick", "Marlene", "Henrik", "Theresa", "Robert",
    "Charlotte", "Oliver"
]

PROJECT_STATUSES = ["Active", "Pending Approval", "Completed", "On Hold"]

# --- 1. Properties dataset ---
def generate_properties(n=500):
    start_date = datetime(2024, 1, 1)
    rows = []
    for i in range(n):
        ptype = np.random.choice(PROPERTY_TYPES, p=PROPERTY_WEIGHTS)
        if ptype == "Apartment":
            size = np.random.randint(40, 130)
            rooms = np.random.choice([1, 2, 3, 4], p=[0.1, 0.3, 0.4, 0.2])
            price = size * np.random.randint(3800, 6200)
        elif ptype == "House":
            size = np.random.randint(100, 280)
            rooms = np.random.choice([4, 5, 6, 7], p=[0.3, 0.35, 0.25, 0.1])
            price = size * np.random.randint(4200, 7500)
        elif ptype == "Commercial":
            size = np.random.randint(60, 500)
            rooms = np.random.choice([1, 2, 3, 4, 5])
            price = size * np.random.randint(2500, 5000)
        elif ptype == "Penthouse":
            size = np.random.randint(90, 200)
            rooms = np.random.choice([3, 4, 5], p=[0.3, 0.5, 0.2])
            price = size * np.random.randint(6000, 9000)
        else:  # Studio
            size = np.random.randint(20, 45)
            rooms = 1
            price = size * np.random.randint(4000, 6000)

        listed_date = start_date + timedelta(days=np.random.randint(0, 730))
        intake_date = listed_date - timedelta(days=np.random.randint(1, 21))
        days_to_publish = (listed_date - intake_date).days
        agent = f"Agent_{np.random.randint(1, 51):02d}"

        rows.append({
            "property_id": f"RK-{i+1:04d}",
            "property_type": ptype,
            "district": np.random.choice(DISTRICTS),
            "size_sqm": size,
            "rooms": rooms,
            "energy_class": np.random.choice(ENERGY_CLASSES, p=ENERGY_WEIGHTS),
            "asking_price_eur": round(price, -3),
            "intake_date": intake_date.strftime("%Y-%m-%d"),
            "listed_date": listed_date.strftime("%Y-%m-%d"),
            "days_to_publish": days_to_publish,
            "agent_id": agent,
            "status": np.random.choice(["Active", "Sold", "Withdrawn"], p=[0.3, 0.55, 0.15])
        })
    return pd.DataFrame(rows)


# --- 2. Enquiries dataset ---
def generate_enquiries(n=1200):
    start_date = datetime(2024, 1, 1)
    rows = []
    for i in range(n):
        created = start_date + timedelta(days=np.random.randint(0, 730))
        channel = np.random.choice(CHANNELS, p=CHANNEL_WEIGHTS)
        enquiry_type = np.random.choice(ENQUIRY_TYPES, p=ENQUIRY_WEIGHTS)

        # Response time varies by agent load and channel
        if channel == "WhatsApp":
            response_hours = max(0.5, np.random.exponential(3))
        elif channel == "Phone":
            response_hours = max(0.1, np.random.exponential(1))
        else:
            response_hours = max(1, np.random.exponential(8))

        rows.append({
            "enquiry_id": f"ENQ-{i+1:05d}",
            "date": created.strftime("%Y-%m-%d"),
            "channel": channel,
            "enquiry_type": enquiry_type,
            "response_time_hours": round(response_hours, 1),
            "agent_id": f"Agent_{np.random.randint(1, 51):02d}",
            "property_id": f"RK-{np.random.randint(1, 501):04d}",
            "converted": np.random.choice([True, False], p=[0.15, 0.85])
        })
    return pd.DataFrame(rows)


# --- 3. Design projects dataset ---
def generate_projects(n=80):
    start_date = datetime(2024, 1, 1)
    rows = []
    project_types = ["Residential Renovation", "Office Fit-Out", "New Build Interior",
                     "Retail Space Design", "Show Apartment Staging"]
    for i in range(n):
        ptype = np.random.choice(project_types)
        start = start_date + timedelta(days=np.random.randint(0, 700))
        duration_weeks = np.random.randint(4, 20)
        budget = np.random.randint(15000, 150000)
        status = np.random.choice(PROJECT_STATUSES, p=[0.35, 0.15, 0.40, 0.10])

        rows.append({
            "project_id": f"PROJ-{i+1:03d}",
            "project_type": ptype,
            "district": np.random.choice(DISTRICTS),
            "start_date": start.strftime("%Y-%m-%d"),
            "duration_weeks": duration_weeks,
            "budget_eur": round(budget, -2),
            "status": status,
            "designer_id": f"Designer_{np.random.randint(1, 21):02d}",
            "brief_hours": round(np.random.uniform(1.5, 4.5), 1)
        })
    return pd.DataFrame(rows)


# --- 4. Agents summary dataset ---
def generate_agents(n=50):
    rows = []
    for i in range(n):
        listings_per_month = max(1, int(np.random.normal(4, 1.5)))
        avg_response_hrs = max(0.5, np.random.normal(8, 4))

        rows.append({
            "agent_id": f"Agent_{i+1:02d}",
            "name": AGENT_FIRST_NAMES[i],
            "office": np.random.choice(["Hamburg-City", "Hamburg-West", "Hamburg-North", "Hamburg-South"]),
            "avg_listings_per_month": listings_per_month,
            "avg_response_time_hours": round(avg_response_hrs, 1),
            "avg_days_to_publish": np.random.randint(3, 18),
            "satisfaction_score": round(np.random.uniform(3.0, 5.0), 1)
        })
    return pd.DataFrame(rows)


# --- 5. Monthly revenue dataset ---
def generate_revenue():
    rows = []
    base = {"Brokerage": 280000, "Interior Design": 120000, "Property Management": 50000}
    for month_offset in range(24):
        date = datetime(2024, 1, 1) + timedelta(days=month_offset * 30)
        for service, base_rev in base.items():
            seasonal = 1 + 0.15 * np.sin(2 * np.pi * month_offset / 12)
            trend = 1 + 0.01 * month_offset
            noise = np.random.uniform(0.9, 1.1)
            revenue = base_rev * seasonal * trend * noise
            rows.append({
                "month": date.strftime("%Y-%m"),
                "service_line": service,
                "revenue_eur": round(revenue, -2)
            })
    return pd.DataFrame(rows)


# --- 6. LangSmith evaluation examples ---
def generate_langsmith_eval():
    examples = []
    sample_properties = [
        {
            "input": {
                "property_type": "Apartment", "district": "Hamburg-Eimsbüttel",
                "size_sqm": 85, "rooms": 3, "floor": 2, "total_floors": 5,
                "features": ["balcony", "fitted kitchen", "hardwood floors"],
                "energy_class": "B", "asking_price": 385000,
                "target_audience": "young professionals"
            }
        },
        {
            "input": {
                "property_type": "House", "district": "Hamburg-Blankenese",
                "size_sqm": 210, "rooms": 6, "floor": None, "total_floors": 2,
                "features": ["garden", "garage", "fireplace", "terrace"],
                "energy_class": "C", "asking_price": 1250000,
                "target_audience": "families"
            }
        },
        {
            "input": {
                "property_type": "Commercial", "district": "Hamburg-HafenCity",
                "size_sqm": 180, "rooms": 4, "floor": 3, "total_floors": 8,
                "features": ["open plan", "meeting room", "harbor view"],
                "energy_class": "A", "asking_price": 650000,
                "target_audience": "SME companies"
            }
        },
        {
            "input": {
                "property_type": "Studio", "district": "Hamburg-St. Pauli",
                "size_sqm": 32, "rooms": 1, "floor": 4, "total_floors": 6,
                "features": ["built-in storage", "modern bathroom"],
                "energy_class": "B", "asking_price": 165000,
                "target_audience": "students or investors"
            }
        },
        {
            "input": {
                "property_type": "Penthouse", "district": "Hamburg-Eppendorf",
                "size_sqm": 145, "rooms": 4, "floor": 7, "total_floors": 7,
                "features": ["roof terrace", "floor-to-ceiling windows", "2 bathrooms", "private elevator"],
                "energy_class": "A+", "asking_price": 980000,
                "target_audience": "luxury buyers"
            }
        }
    ]
    return sample_properties


if __name__ == "__main__":
    print("Generating synthetic datasets...")

    properties = generate_properties()
    properties.to_csv(os.path.join(OUTPUT_DIR, "properties.csv"), index=False)
    print(f"  properties.csv: {len(properties)} rows")

    enquiries = generate_enquiries()
    enquiries.to_csv(os.path.join(OUTPUT_DIR, "enquiries.csv"), index=False)
    print(f"  enquiries.csv: {len(enquiries)} rows")

    projects = generate_projects()
    projects.to_csv(os.path.join(OUTPUT_DIR, "projects.csv"), index=False)
    print(f"  projects.csv: {len(projects)} rows")

    agents = generate_agents()
    agents.to_csv(os.path.join(OUTPUT_DIR, "agents.csv"), index=False)
    print(f"  agents.csv: {len(agents)} rows")

    revenue = generate_revenue()
    revenue.to_csv(os.path.join(OUTPUT_DIR, "revenue_monthly.csv"), index=False)
    print(f"  revenue_monthly.csv: {len(revenue)} rows")

    import json
    eval_data = generate_langsmith_eval()
    with open(os.path.join(OUTPUT_DIR, "langsmith_eval_dataset.json"), "w") as f:
        json.dump(eval_data, f, indent=2)
    print(f"  langsmith_eval_dataset.json: {len(eval_data)} examples")

    print("\nDone! All files saved to data/ folder.")
