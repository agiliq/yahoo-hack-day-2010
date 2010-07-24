import os,sys
sys.path.insert(1,'/home/lakshman/www/flickrcommerce')
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
sys.stdout = sys.stderr
