from django.urls import path
from . import views

urlpatterns = [
            path("", views.homepage, name='homepage'),
            path("automation/", views.automation, name='automation'),
            path("data-science/", views.data_science, name='data-science'),
            path("web-development/", views.web_development, name='web-dev'),
            path("backend/", views.backend, name='backend'),
            path("app-development/", views.app_development, name='app-dev'),
            path("machine-learning/", views.machine_learning, name='machine-learning')
        ]
