# setup_db.py
import os
import django
from datetime import date

# 1. Initialize Django ecosystem environment configuration mappings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.contrib.auth import get_user_model
# ✅ CORRECTED IMPORTS: Doctor imported cleanly from its own proper app domain
from appointments.models import Appointment 
from doctors.models import Doctor 
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

patient_profile, p_created = Patient.objects.get_or_create(
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
doctor_profile = Doctor.objects.first()

if doctor_profile and patient_profile:
    print("\nSeeding medical event logs into appointment timeline...")
    
    from datetime import timedelta
    from django.utils import timezone
    
    # Get tomorrow's date dynamically to satisfy validation requirements
    tomorrow_date = timezone.now().date() + timedelta(days=1)
    
    appointment_exists = Appointment.objects.filter(
        doctor=doctor_profile, 
        appointment_date=tomorrow_date
    ).exists()
    
    if not appointment_exists:
        Appointment.objects.create(
            patient=patient_profile, 
            doctor=doctor_profile,   
            appointment_date=tomorrow_date, 
            appointment_time="09:00:00",        
            reason="Hypertension Follow-up Check Routine Evaluation",
            status="Scheduled" # ✅ FIXED: Set to Scheduled since future appointments can't logically be completed yet
        )
        print(f"✓ Successfully injected 'Hypertension Follow-up' baseline log item for {tomorrow_date}!")
    else:
        print("i Appointment timeline event log entry already populated.")
else:
    print("\n⚠️ Skipping timeline generation step: Missing active Doctor or Patient row entities.")

print("\n==================================================")
print("  ALL SYSTEMS ALIGNED AND DATABASE SEED COMPLETE   ")
print("==================================================")

















"""
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

patient_profile, p_created = Patient.objects.get_or_create(
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
doctor_profile = Doctor.objects.first()

if doctor_profile and patient_profile:
    print("\nSeeding medical event logs into appointment timeline...")
    
    # Bug Fix: Use a dynamic date (tomorrow) so it never triggers the "past date" validation block
    from datetime import timedelta
    from django.utils import timezone
    
    # Get the date for tomorrow relative to the server runtime environment
    tomorrow_date = timezone.now().date() + timedelta(days=1)
    
    appointment_exists = Appointment.objects.filter(
        doctor=doctor_profile, 
        appointment_date=tomorrow_date
    ).exists()
    
    if not appointment_exists:
        Appointment.objects.create(
            patient=patient_profile, 
            doctor=doctor_profile,   
            appointment_date=tomorrow_date, # Dynamic future date
            appointment_time="09:00:00",        
            reason="Hypertension Follow-up Check Routine Evaluation",
            status="Completed"
        )
        print(f"✓ Successfully injected 'Hypertension Follow-up' baseline log item for {tomorrow_date}!")
    else:
        print("i Appointment timeline event log entry already populated.")
else:
    print("\n⚠️ Skipping timeline generation step: Missing active Doctor or Patient row entities.")

print("\n==================================================")
print("  ALL SYSTEMS ALIGNED AND DATABASE SEED COMPLETE   ")
print("==================================================")

"""