from django.apps import AppConfig

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    
    # Grade 6 tip: This is a setup room where we tell the app to load custom system behaviors
    def ready(self):
        # This is where we will load automatic system rules later as we scale
        pass





"""
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
"""