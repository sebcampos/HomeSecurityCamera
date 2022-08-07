from django.urls import path
from . import views

urlpatterns = [
            path("", views.login_page, name='login_page'),
            path("view/", views.view_cam_page, name="view_cam_page"),
            path("view/stream", views.camera_stream, name='camera_stream'),
            path("view/log", views.stream_log, name='stream_log'),
            path("view/update", views.update_stream, name='update_stream'),
          # uncomment if you installed pijuice
          # path("view/battery", views.battery_stream, name="battery_stream"),
            path("view/logout", views.log_out, name="logout") 
        ]
