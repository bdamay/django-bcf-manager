import os, sys
from datetime import datetime
proj_path = '/'.join(os.getcwd().split('\\')[:-2])+'/myproject'
# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
sys.path.append(proj_path)

# This is so my local_settings.py gets loaded.
os.chdir(proj_path)
# This is so models get loaded.

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()