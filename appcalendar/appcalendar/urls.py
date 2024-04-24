"""
URL configuration for appcalendar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.contrib import admin
from django.urls import path , include
from .views import IndexView , LogOut ,SignIn , SignUp


urlpatterns = [
    path("", IndexView.as_view(), name='home'),
    path("admin/", admin.site.urls),
    path('', include('cal.urls')),
    path('sign_in/', SignIn.sign_in, name='sign_in'),
    path('sign_up/', SignUp.sign_up, name='sign_up'),
    path('log_out/', LogOut.log_out, name='sign_out'),
]
