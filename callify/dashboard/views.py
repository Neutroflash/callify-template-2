from django.shortcuts import render

def dashboard_view(request):
    return render(request, "dashboard/dashboard.html")  # Renderiza el HTML

def profile_view(request):
    return render(request, "dashboard/profile.html")

def phone_numbers_view(request):
    return render(request, "dashboard/phone_numbers.html")

def integrations_view(request):
    return render(request, "dashboard/integrations.html")

def plans_view(request):
    return render(request, "dashboard/plans.html")

def support_view(request):
    return render(request, "dashboard/support.html")