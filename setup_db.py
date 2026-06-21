# setup_db.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# This automatically creates your admin user if it doesn't exist yet
username = "admin"
email = "admin@example.com"
password = "admin1@3$" # Change this to a password you want!

if not User.objects.filter(username=username).exists():
    print(f"Creating superuser account for {username}...")
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Superuser created successfully!")
else:
    print(f"Superuser {username} already exists.")