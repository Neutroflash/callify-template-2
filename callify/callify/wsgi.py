import os
import sys

sys.path.append("/app/CALLIFY")  # Ajusta la ruta según cómo Railway monta tu código

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "callify.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
