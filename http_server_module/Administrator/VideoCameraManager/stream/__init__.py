import atexit
from . import utils
from . import video_camera
from . import battery



def get_labels():
	return utils.get_labels()

def tear_down():
	utils.get_video().release()
	utils.get_thread().join()

def get_track_list():
	return utils.get_track_list()

def add_to_tracking(labels):
	tracking_list = get_track_list()
	labels = [i for i in labels.strip().split(",") if i != ""]
	utils.set_track_list(labels)
	

def log_feed():
	while True:
		last_logged = utils.read(f"{utils.get_date()}", log_line=True)		
		if last_logged == utils.get_last_logged():
			yield ""
		else:
			utils.set_last_logged(last_logged)
			yield last_logged+"<br>"

utils.set_labels()
utils.reset_recording_frame_count()
utils.init_interpreter()

utils.write(f"[{utils.get_date_and_time()}] START", f"{utils.get_date()}", log_line=True)

video_camera.start_video()
video_camera.start_thread()

atexit.register(tear_down)
