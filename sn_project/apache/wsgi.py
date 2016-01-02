"""
WSGI config for sn_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
import site
import pwd

USER_HOME_DIR = pwd.getpwuid(os.getuid()).pw_dir

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sn_project.settings")

# add site-packages of the chosen virtualenv to work with
site.addsitedir(os.path.join(USER_HOME_DIR, '.virtualenvs/sn_project/lib/python2.7/site-packages'))

# add the app's directory to the home path
sys.path.append(os.path.join(USER_HOME_DIR,'django_projects/sergey-nikiforov.com'))
sys.path.append(os.path.join(USER_HOME_DIR,'django_projects/sergey-nikiforov.com/sn_project'))


application = get_wsgi_application()
