import os
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
# Make sure to replace 'your_project.settings' with the appropriate settings module for your Django project.

# Configure Django settings
settings.configure()

# Now you can perform Django-related operations, such as running migrations
