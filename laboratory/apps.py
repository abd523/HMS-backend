# the firsst feature is become deleted i add the new feature




from django.apps import AppConfig

class LaboratoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'laboratory'

    # Grade 6 tip: This is the system's "power switch" room. 
    # When the app turns on, it sets up automatic connections here.
    def ready(self):
        # Future automatic triggers (like sending lab results to doctors) go here!
        pass

