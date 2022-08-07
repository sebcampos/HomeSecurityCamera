import json
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators import gzip
from django.views.decorators.clickjacking import xframe_options_exempt
from django.template import loader
from django.http import HttpResponse, StreamingHttpResponse, JsonResponse
from . import stream


def login_page(request):
    """
    Login page authenticates user then redirects to the
    camera system
    """
    if request.method == "GET":
        return render(request, 'login_page.html', context={})
    # collect user credentials from the post method and authenticate
    username = request.POST.get("username", False)
    password = request.POST.get("password", False)
    user = authenticate(request, username=username, password=password)
    
    # redirect if user is authenticated
    if user is not None:
        login(request, user)
        return redirect("view/")
    else:
        # create error pop up
        return render(request, 'login_page.html', context={"error":True})
    
def log_out(request):
    logout(request)
    return redirect("/cam")

@login_required
def view_cam_page(request):
    return render(request, 'view_cam_page.html', context={"tracking": stream.get_track_list(),"objects":stream.get_labels()})


@require_POST
@login_required
def update_stream(request):
    body = json.loads(request.body.decode('utf-8'))
    stream.add_to_tracking(body["labels"])
    return HttpResponse(200)

"""
uncomment if you installed pijuice
@login_required
def battery_stream(request):
    return JsonResponse({"charge_level" :stream.battery.check_charge_level()}) 
"""

@xframe_options_exempt
@login_required
def stream_log(request):
    try:
        return StreamingHttpResponse(stream.log_feed())
    except:
        pass
        
@login_required
@gzip.gzip_page
def camera_stream(request):
    """
    """
    try:
        return StreamingHttpResponse(stream.video_camera.feed(), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass
