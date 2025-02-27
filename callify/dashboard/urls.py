from django.urls import path
from .views import dashboard_view, profile_view, phone_numbers_view, integrations_view, plans_view, support_view

urlpatterns = [
    path("", dashboard_view, name="dashboard"),
    path("profile/", profile_view, name="profile"),
    path("numbers/", phone_numbers_view, name="phone_numbers"),
    path("integrations/", integrations_view, name="integrations"),
    path("plans/", plans_view, name="plans"),
    path("support/", support_view, name="support")
]
