import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()
Faker.seed(42)
np.random.seed(42)
random.seed(42)

# ---------------------------
# CONFIGURATION
# ---------------------------
n_trips = 2500
n_feedbacks = 2000
cities = ["Hyderabad", "Bangalore", "Mumbai", "Delhi", "Pune", "Chennai"]
payment_types = ["Cash", "UPI", "Card"]
platforms = ["Twitter", "Reddit", "In-App Feedback"]

# ---------------------------
# DATASET 1: taxi_trip_data
# ---------------------------
trip_data = []

for i in range(n_trips):
    driver_id = random.randint(1000, 1100)
    trip_id = i + 1

    # Random trip start & end
    start_time = fake.date_time_between(start_date="-15d", end_date="now")
    duration = random.randint(5, 60)
    end_time = start_time + timedelta(minutes=duration)

    # Distance & fare
    distance = round(random.uniform(1.0, 25.0), 2)
    fare = round(distance * random.uniform(10, 25), 2)

    # Idle time before next trip
    idle_time = random.randint(2, 60)

    # Random coordinates (simulate same city area)
    pickup_lat = round(random.uniform(17.35, 17.50), 5)
    pickup_lon = round(random.uniform(78.45, 78.55), 5)
    drop_lat = pickup_lat + random.uniform(-0.05, 0.05)
    drop_lon = pickup_lon + random.uniform(-0.05, 0.05)

    trip_data.append([
        driver_id, trip_id, start_time, end_time, duration, distance,
        pickup_lat, pickup_lon, drop_lat, drop_lon, fare,
        idle_time, random.choice(payment_types),
        round(random.uniform(3, 5), 1)
    ])

trip_df = pd.DataFrame(trip_data, columns=[
    "driver_id", "trip_id", "start_time", "end_time", "trip_duration_min",
    "distance_km", "pickup_lat", "pickup_lon", "drop_lat", "drop_lon",
    "fare_amount", "idle_time_min", "payment_type", "customer_rating"
])

# ---------------------------
# DATASET 2: driver_feedback_data
# ---------------------------
feedback_texts = [
    "Too much traffic near airport area.",
    "Passengers not available at night.",
    "App payment failed multiple times.",
    "Long waiting time near station.",
    "Low demand in industrial area.",
    "Good passenger experience today!",
    "Traffic jam reduced earning.",
    "Fuel cost too high this week.",
    "Pickup location far from hotspot.",
    "Too many cancellations this morning."
]

feedback_data = []
for i in range(n_feedbacks):
    driver_id = random.randint(1000, 1100)
    feedback = random.choice(feedback_texts)
    feedback_data.append([
        driver_id,
        fake.date_time_between(start_date="-15d", end_date="now"),
        feedback,
        random.choice(platforms),
        random.choice(cities)
    ])

feedback_df = pd.DataFrame(feedback_data, columns=[
    "driver_id", "timestamp", "feedback_text", "platform", "city"
])

# ---------------------------
# SAVE FILES
# ---------------------------
trip_df.to_csv("taxi_trip_data.csv", index=False)
feedback_df.to_csv("driver_feedback_data.csv", index=False)

print("✅ Datasets generated successfully!")
print(f"taxi_trip_data.csv → {trip_df.shape}")
print(f"driver_feedback_data.csv → {feedback_df.shape}")



