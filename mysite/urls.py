"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.http import HttpResponse
from django.urls import path


def home(request):
    return HttpResponse("""
        <html>
        <head><title>Azure Django Lab</title></head>
        <body style="font-family: Arial; padding: 40px;">
            <h1 style="color: #0066cc;">Version 2 - Updated Automatically!</h1>
            <p>This change was deployed with zero manual server work.</p>
            <p>The CI/CD pipeline handled everything.</p>
        </body>
        </html>
    """)


urlpatterns = [
    path('', home),
]