from . import constants
from . import variables

import datetime
import tflite_runtime.interpreter as tflite
import numpy as np

def get_np():
    return np

def get_date():
    return datetime.datetime.now().date()

def get_date_and_time():
    return datetime.datetime.now()

def write(line, filename, log_line=False, **kwargs):
    if log_line:
        with open(f"{constants.LOG_DIR}{filename}.txt", "a") as f:
            f.write(line + "\n")
            set_last_logged(line + "\n")
            return
    with open(f"{constants.ROOT}{filename}", kwargs.get("open_arg"), None):
        f.write(line)

def set_last_logged(line):
    variables.last_logged = line

def get_last_logged():
    return variables.last_logged

def read(filename, log_line=False, model=False):
    if log_line:
        with open(f"{constants.LOG_DIR}{filename}.txt", "r") as f:
            string = f.read()
        return string.split("\n")[-2]
    elif model:
        with open(f"{constants.MODEL_DIR}{filename}.txt", "r") as f:
            string = f.read()
        return string       
    with open(f"{constants.ROOT}{filename}", "r") as f:
        return f.read()


def get_recording_frame_count():
    return variables.recording_frame_count

def reset_recording_frame_count():
    variables.recording_frame_count = constants.RECORDING_FRAME_COUNT

def decrement_recording_frame_count():
    variables.recording_frame_count -= 1

def get_recorder():
    return variables.recorder

def get_recording_status():
    return variables.recording_in_progress

def set_recording_status(status):
    variables.recording_in_progress = status
    
def get_video_log_dir():
    return constants.VIDEO_TAPES_DIR

def edit_output(new_output):
    variables.output = new_output


def get_output():
    return variables.output


def get_labels(main_labels=False):
    if main_labels:
        return variables.labels
    else:
        return [i for i in variables.labels if i != "???"]


def set_labels():
    labels_txt = read("labelmap", model=True)
    labels = [line.strip() for line in labels_txt.split("\n")]
    if labels[0] == '???':
        del(labels[0])
    variables.labels = labels

def set_output(new_output):
    variables.output = new_output

def get_track_list():
    return variables.track_list

def set_track_list(lst):
    variables.track_list = lst

def init_interpreter():
    interpreter = tflite.Interpreter(model_path=f"{constants.MODEL_DIR}detect.tflite")
    interpreter.allocate_tensors()

    # get model details
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    variables.model_height = input_details[0]['shape'][1]
    variables.model_width = input_details[0]['shape'][2]
    variables.floating_model = (input_details[0]['dtype'] == np.float32)
    variables.input_details = input_details

    # Check output layer name to determine if this model was created with TF2 or TF1,
    # because outputs are ordered differently for TF2 and TF1 models
    outname = output_details[0]['name']

    if ('StatefulPartitionedCall' in outname):  # This is a TF2 model
        boxes_idx, classes_idx, scores_idx = 1, 3, 0
    else:  # This is a TF1 model
        boxes_idx, classes_idx, scores_idx = 0, 1, 2

    variables.boxes_idx = boxes_idx
    variables.classes_idx = classes_idx
    variables.scores_idx = scores_idx
    variables.output_details = output_details
    variables.interpreter = interpreter


def get_model_height():
    return variables.model_height

def get_video_height():
    return variables.video_height
    
def get_video_width():
    return variables.video_width

def get_model_width():
    return variables.model_width

def get_min_conf_threshold():
    return constants.MIN_CONF_THRESHOLD

def get_input_mean():
    return constants.INPUT_MEAN

def get_input_std():
    return constants.INPUT_STD

def get_interpreter():
    return variables.interpreter

def get_thread():
    return variables.thread

def get_video():
    return variables.video

def is_floating_model():
    return variables.floating_model

def get_input_details():
    return variables.input_details

def get_output_details():
    return variables.output_details

def get_box_idx():
    return variables.boxes_idx

def get_classes_idx():
    return variables.classes_idx

def get_scores_idx():
    return variables.scores_idx

def get_main_frame():
    return variables.main_frame

def set_main_frame(frame):
    variables.main_frame = frame

def log():
    while variables.thread.is_alive():
        item = read()
        if item != get_output():
            set_output(item)
            yield f"{item}<br>"
