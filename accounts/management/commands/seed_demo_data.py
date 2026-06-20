from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from doctors.models import Doctor

User = get_user_model()


class Command(BaseCommand):
    help = "Create demo admin, doctors, and receptionist staff for the hospital system"

    def handle(self, *args, **options):
        admin, created = User.objects.get_or_create(
            username="admin",
            defaults={
                "email": "admin@hospital.com",
                "first_name": "System",
                "last_name": "Admin",
                "role": User.Role.ADMIN,
                "is_staff": True,
                "is_superuser": True,
                "is_approved": True,
            },
        )
        if created:
            admin.set_password("admin123")
            admin.save()
            self.stdout.write(self.style.SUCCESS("Created admin user (admin / admin123)"))
        else:
            self.stdout.write("Admin user already exists")

        doctors = [
            ("dr_smith", "John", "Smith", "Cardiology", "LIC-001"),
            ("dr_bekele", "Tesfa", "Bekele", "General Medicine", "LIC-002"),
        ]

        for username, first, last, specialization, license_number in doctors:
            user, user_created = User.objects.get_or_create(
                username=username,
                defaults={
                    "email": f"{username}@hospital.com",
                    "first_name": first,
                    "last_name": last,
                    "role": User.Role.DOCTOR,
                    "is_approved": True,
                },
            )
            if user_created:
                user.set_password("doctor123")
                user.save()

            doctor, doc_created = Doctor.objects.get_or_create(
                user=user,
                defaults={
                    "specialization": specialization,
                    "license_number": license_number,
                    "experience_years": 5,
                    "is_available": True,
                },
            )
            if doc_created:
                self.stdout.write(self.style.SUCCESS(f"Created doctor: Dr. {first} {last}"))

        receptionist, rec_created = User.objects.get_or_create(
            username="reception",
            defaults={
                "email": "reception@hospital.com",
                "first_name": "Sara",
                "last_name": "Kebede",
                "role": User.Role.RECEPTIONIST,
                "is_approved": True,
            },
        )
        if rec_created:
            receptionist.set_password("reception123")
            receptionist.save()
            self.stdout.write(self.style.SUCCESS("Created receptionist (reception / reception123)"))

        self.stdout.write(self.style.SUCCESS("Demo data ready. Login with admin / admin123"))
