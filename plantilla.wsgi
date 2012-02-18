# This is usefull if you're hosting your project on Webfaction
# you can create copies from plantilla, change its name, customize the templates
# and make it manage your site requests

# Sustituir PLANTILLA por el nombre que se le haya dado a la carpeta

import os
import sys

sys.path = ['/path/to/your/project', '/path/to/your/project/libs/lib/python2.7', '/path/to/your/project/minicms', '/path/to/your/project/PLANTILLA'] + sys.path
from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'PLANTILLA.settings'
application = WSGIHandler()

