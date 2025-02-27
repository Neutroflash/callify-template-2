from django.contrib import admin
from django.urls import path, include
from dashboard.views import dashboard_view  # Importamos la vista del dashboard

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("", dashboard_view, name="home"),  # Esto hace que "/" cargue el dashboard
]
