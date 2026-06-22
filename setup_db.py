# setup_db.py
import os
import django
from datetime import date

# 1. Initialize Django ecosystem environment configuration mappings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.contrib.auth import get_user_model
# Import your structural data models safely
from appointments.models import Doctor, Appointment 
from patients.models import Patient 

User = get_user_model()

print("==================================================")
print("     STARTING HOSPITAL DATABASE SEEDING ENGINE    ")
print("==================================================")

# ---------------------------------------------------------------- ACTION 1: ADMIN SUPERUSER
username = "admin"
email = "admin@example.com"
password = "admin1@3$"

if not User.objects.filter(username=username).exists():
    print(f"Creating superuser account for {username}...")
    User.objects.create_superuser(username=username, email=email, password=password)
    print("✓ Superuser created successfully!")
else:
    print(f"i Superuser {username} already exists.")

# ---------------------------------------------------------------- ACTION 2: MEDICAL STAFF (DOCTORS)
print("\nChecking for demo doctors...")

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
    # Safely secure or verify base user instance record anchors
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
    
    # Check if accompanying structural Doctor row exists, if not, link them
    if not Doctor.objects.filter(user=user_record).exists():
        print(f"Linking clinical Doctor record with specialization: {doc_data['specialization']}...")
        Doctor.objects.create(
            user=user_record,
            specialization=doc_data["specialization"],
            license_number=doc_data["license"],
            experience_years=5,
            is_available=True
        )
        print(f"✓ Dr. {doc_data['first_name']} {doc_data['last_name']} added successfully!")
    else:
        print(f"i Doctor profile for Dr. {doc_data['first_name']} already exists.")

# ---------------------------------------------------------------- ACTION 3: PATIENTS & TIMELINE RECORDS
print("\nChecking for sample patient logs...")

# Ensure at least one test patient exists within core system authentication tables
patient_user, created = User.objects.get_or_create(
    username="hidaya_seid",
    defaults={
        "first_name": "Hidaya",
        "last_name": "Seid",
        "email": "hidaya@example.com",
        "password": "PatientPassword123!"
    }
)

if created:
    print("✓ Created new core user profile for Hidaya Seid.")
else:
    print("i Base user profile for Hidaya Seid already exists.")

# Ensure the corresponding profile row entry exists within your specialized Patient data table
patient_profile, p_created = Patient.objects.get_or_create(
    # Depending on your specific database schema, adjust fields to point directly to user=patient_user 
    # or map flat string fields if your Patient model uses independent columns:
    first_name="Hidaya",
    last_name="Seid",
    defaults={
        "phone_number": "0911223344",
        "gender": "F",
        "date_of_birth": date(1998, 5, 14),
        "medical_history": "Hypertension trace markers documented historically."
    }
)

if p_created:
    print("✓ Registered Hidaya Seid into active medical records table.")
else:
    print("i Medical record registry sheet for Hidaya Seid already exists.")

# ---------------------------------------------------------------- ACTION 4: RECONCILE TIMELINE RELATIONSHIPS
# Select the first seeded doctor profile to act as the consulting practitioner
doctor_profile = Doctor.objects.first()

if doctor_profile and patient_profile:
    print("\nSeeding medical event logs into appointment timeline...")
    
    # Verify if an appointment sequence already exists to prevent duplicate timeline logging blocks
    # Note: If your model filters by 'patient_id' or 'patient', adjust the query keyword filter directly.
    appointment_exists = Appointment.objects.filter(
        doctor=doctor_profile, 
        date=date(2026, 6, 10)
    ).exists()
    
    if not appointment_exists:
        Appointment.objects.create(
            patient=patient_profile, # Maps directly to your Patient model record instance
            doctor=doctor_profile,   # Links directly to Dr. Dawit's profile record row instance
            date=date(2026, 6, 10),
            time="09:00:00",
            reason="Hypertension Follow-up Check Routine Evaluation",
            status="Completed"
        )
        print("✓ Successfully injected 'Hypertension Follow-up' baseline log item into active timelines!")
    else:
        print("i Appointment timeline event log entry already populated.")
else:
    print("\n⚠️ Skipping timeline generation step: Missing active Doctor or Patient row entities.")

print("\n==================================================")
print("  ALL SYSTEMS ALIGNED AND DATABASE SEED COMPLETE   ")
print("==================================================")