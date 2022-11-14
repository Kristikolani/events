"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from events import views as eventsViews
from accounts import views as accountsViews
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("register/", accountsViews.register, name="register"),
    path("admin/", admin.site.urls),
    path("", eventsViews.home, name='home'),
    path("about/", eventsViews.about, name='about'),
    path("events/", eventsViews.events, name='events'),
    path("add_event/", eventsViews.add_event, name="add_event"),
    path("profile/", accountsViews.profile, name='profile'),
    path('login/', accountsViews.login, name="login"),
    path('logout', accountsViews.logout, name="logout"),
    path('delete/<id>', accountsViews.delete, name="delete"),
    path('edit/<id>', eventsViews.edit, name="edit"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
