# setup_db.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.contrib.auth import get_user_model
# Import your exact app modules safely
from appointments.models import Doctor 

User = get_user_model()

# 1. Create Admin Superuser Account
username = "admin"
email = "admin@example.com"
password = "admin1@3$"

if not User.objects.filter(username=username).exists():
    print(f"Creating superuser account for {username}...")
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Superuser created successfully!")
else:
    print(f"Superuser {username} already exists.")

# 2. Create Demo Doctors
print("Checking for demo doctors...")

demo_doctors = [
    {
        "username": "dr_dawit",
        "first_name": "Dawit",
        "last_name": "Girma",
        "email": "dawit@hospital.com",
        "specialization": "Cardiology",
        "license": "MD-12345"
    },
    {
        "username": "dr_selam",
        "first_name": "Selam",
        "last_name": "Alemu",
        "email": "selam@hospital.com",
        "specialization": "Pediatrics",
        "license": "MD-67890"
    }
]

for doc_data in demo_doctors:
    # Check if user already exists to avoid throwing duplicate errors
    user_record = User.objects.filter(username=doc_data["username"]).first()
    
    if not user_record:
        print(f"Creating user profile for Dr. {doc_data['first_name']}...")
        user_record = User.objects.create_user(
            username=doc_data["username"],
            email=doc_data["email"],
            password="DoctorPassword123!",
            first_name=doc_data["first_name"],
            last_name=doc_data["last_name"]
        )
    
    # Check if the accompanying Doctor profile row exists
    if not Doctor.objects.filter(user=user_record).exists():
        print(f"Linking clinical Doctor record with specialization: {doc_data['specialization']}...")
        Doctor.objects.create(
            user=user_record,
            specialization=doc_data["specialization"],
            license_number=doc_data["license"],
            experience_years=5,
            is_available=True
        )
        print(f"Dr. {doc_data['first_name']} {doc_data['last_name']} added successfully!")

print("Database seeding operations completed successfully!")