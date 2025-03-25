from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Définir le module de paramètres Django par défaut pour le 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trashpickup.settings')

app = Celery('trash')

# Charger les configurations de Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodécouverte des tâches
app.autodiscover_tasks()