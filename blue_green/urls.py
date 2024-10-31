from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

from blue_green.apps.accounts import views as account_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", account_views.user_list, name="users")
]
