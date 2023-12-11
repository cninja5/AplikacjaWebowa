from django.urls import path

from register import views as v

urlpatterns = [
    path('register/', v.register, name="register"),
    path('login/', v.login_view, name="login_view"),
]
