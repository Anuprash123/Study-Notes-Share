"""NotesShare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from notes import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about,name='about'),
    path('', views.index,name='index'),
    path('contact', views.contact,name='contact'),
    path('login_user', views.login_user,name='login_user'),
    path('login_admin', views.login_admin,name='login_admin'),
    path('user_signup', views.user_signup,name='user_signup'),
    path('admin_home', views.admin_home,name='admin_home'),
    path('admin_logout', views.admin_logout,name='admin_logout'),
    path('profile/', views.profile,name='profile'),
    path('change_password', views.change_password,name='change_password'),
    path('edit_profile', views.edit_profile,name='edit_profile'),
    path('upload_notes', views.upload_notes,name='upload_notes'),
    path('mynotes/', views.my_notes,name='mynotes'),
    path('view_users/', views.view_users,name='view_users'),
    path('pending/', views.pending,name='pending'),
    path('reject/', views.reject,name='reject'),
    path('all_notes/', views.all_notes,name='all_notes'),
    path('view_all_notes/', views.view_all_notes,name='view_all_notes'),
    path('Accept/', views.Accept,name='Accept'),
    path('delete/<int:pid>/', views.delete,name='delete'),
    path('delete_user/<int:pid>/', views.delete_user,name='delete_user'),
    path('delete_notes/<int:pid>/', views.delete_notes,name='delete_notes'),
    path('change_status/<int:pid>/', views.change_status,name='change_status'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
