# setup_db.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.contrib.auth import get_user_model
# ⚠️ Import your actual Doctor model here. 
# (Change 'apps.appointments.models' to match your actual Django app structure!)
#from apps.appointments.models import Doctor 
# Change this line in your setup_db.py:
from appointments.models import Doctor

User = get_user_model()

# 1. Create Admin User
username = "admin"
email = "admin@example.com"
password = "admin1@3$"

if not User.objects.filter(username=username).exists():
    print(f"Creating superuser account for {username}...")
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Superuser created successfully!")
else:
    print(f"Superuser {username} already exists.")

# 2. Create Demo Doctors for your Appointment Dropdown
print("Checking for demo doctors...")

# Dummy doctor data list
demo_doctors = [
    {"first_name": "Dawit", "last_name": "Girma", "specialty": "Cardiology", "phone": "0911223344"},
    {"first_name": "Selam", "last_name": "Alemu", "specialty": "Pediatrics", "phone": "0922334455"},
    {"first_name": "Michael", "last_name": "Tadesse", "specialty": "General Medicine", "phone": "0933445566"}
]

for doc_data in demo_doctors:
    # Check if doctor already exists by phone or name to avoid duplication
    if not Doctor.objects.filter(phone_number=doc_data["phone"]).exists():
        print(f"Seeding doctor profile: Dr. {doc_data['first_name']}...")
        Doctor.objects.create(
            first_name=doc_data["first_name"],
            last_name=doc_data["last_name"],
            specialty=doc_data["specialty"],
            phone_number=doc_data["phone"]
        )
        print(f"Dr. {doc_data['first_name']} added successfully!")

print("Database seeding operations completed successfully!")