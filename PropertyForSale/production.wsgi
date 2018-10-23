import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/home/venv/lib/python3.5/site-packages')

# Add the app's directory to the PYTHONPATH
SOURCE_ROOT = os.path.realpath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, SOURCE_ROOT)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')

# Activate your virtual env
activate_env=os.path.expanduser("/home/venv/bin/activate_this.py")
with open(activate_env) as file_:
    exec(file_.read(), dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()