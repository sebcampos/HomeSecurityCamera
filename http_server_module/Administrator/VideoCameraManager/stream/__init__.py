import atexit
from . import utils
from . import video_camera
# uncomment if you installed pijuice
# from . import battery



def get_labels() -> list:
	"""
	return a list of the labels from
	labels.txt
	:return: list
	"""
	return utils.get_labels()

def tear_down() -> None:
	"""
	release video and join thread
	before end of script
	"""
	utils.get_video().release()
	utils.get_thread().join()
	utils.get_thread().release()

def get_track_list() -> list:
	"""
	get the list used for objects of interest
	"""
	return utils.get_track_list()

def add_to_tracking(labels: list) -> None:
	"""
	a new list of labels to replace our current 
	objects of interest list for tracking
	:param labels: list of labels from labels.txt
	"""
	tracking_list = get_track_list()
	labels = [i for i in labels.strip().split(",") if i != ""]
	utils.set_track_list(labels)
	

def log_feed() -> str:
	"""
	This generator reads the last logged line in our log
	if it is different from the previously saved last entry then 
	it is yielded. If not an empty string is yielded
	"""
	while True:
		last_logged = utils.read(f"{utils.get_date()}", log_line=True)		
		if last_logged == utils.get_last_logged():
			yield ""
		else:
			utils.set_last_logged(last_logged)
			yield last_logged+"<br>"

# set our labels variable 			
utils.set_labels()

# set/reset the recording frame count variable
utils.reset_recording_frame_count()

# start the tf interpreter
utils.init_interpreter()

# begin the log file 
utils.write(f"[{utils.get_date_and_time()}] START", f"{utils.get_date()}", log_line=True)

# start the video and thread related to this video
video_camera.start_video()
video_camera.start_thread()

# register our tear down method to be used when the script exits
atexit.register(tear_down)
