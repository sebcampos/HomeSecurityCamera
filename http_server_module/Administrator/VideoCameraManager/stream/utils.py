from . import constants
from . import variables

import datetime
import tflite_runtime.interpreter as tflite
import numpy as np


def get_np() -> np:
    """
    return numpy
    :return: np
    """
    return np


def get_date() -> datetime.datetime:
    """
    This method gets the current date
    :return: date object
    """
    return datetime.datetime.now().date()


def get_date_and_time() -> datetime.datetime:
    """
    This method returns the date and time
    :return: date object
    """
    return datetime.datetime.now()


def write(line: str, filename: str, log_file: bool = False, **kwargs) -> None:
    """
    this method is used to add an entry to a log or write a file
    :param line: line or string to add to the file
    :param filename: name of the file to add to
    :param log_file: boolean defining whether the file is a logfile
    :param kwargs: kword arguments Dictionary
    :return:
    """
    if log_file:
        with open(f"{constants.LOG_DIR}{filename}.txt", "a") as f:
            f.write(line + "\n")
            set_last_logged(line + "\n")
            return
    with open(f"{constants.ROOT}{filename}", kwargs.get("open_arg"), None):
        f.write(line)


def set_last_logged(line: str)  -> None:
    """
    saves a copy of the last line entered in
    a log as a variable
    :param line: the last line to have been entered in a log
    :return: void
    """
    variables.last_logged = line


def get_last_logged() -> str:
    """
    retrieves the last logged string
    :return: str
    """
    return variables.last_logged


def read(filename: str, log_file: bool = False, model: bool = False) -> str:
    """
    reads a file, if it is a logfile it retrieves the last line of
    the file. If the file is marked as model true the method will
    search the model directory. else it will search the root
    :param filename: name of the file to open
    :param log_file: flag for log file
    :param model: flag for model
    :return: text from the file as a string
    """
    if log_file:
        with open(f"{constants.LOG_DIR}{filename}.txt", "r") as f:
            string = f.read()
        return string.split("\n")[-2]
    elif model:
        with open(f"{constants.MODEL_DIR}{filename}.txt", "r") as f:
            string = f.read()
        return string
    with open(f"{constants.ROOT}{filename}", "r") as f:
        return f.read()


def get_recording_frame_count() -> int:
    """
    retrieve the recording frame counter
    :return: integer
    """
    return variables.recording_frame_count


def reset_recording_frame_count() -> None:
    """
    Resets the recording frame counter to its original
    count
    :return: void
    """
    variables.recording_frame_count = constants.RECORDING_FRAME_COUNT


def decrement_recording_frame_count() -> None:
    """
    Decrements the recording frame counter
    :return: void
    """
    variables.recording_frame_count -= 1


def get_recorder() -> object:
    """
    Returns the instance of the video recorder
    :return: VideoWriter
    """
    return variables.recorder


def get_recording_status() -> bool:
    """
    Returns  boolean based on whether
    there is a recording in progress
    :return: boolean
    """
    return variables.recording_in_progress


def set_recording_status(status: bool) -> None:
    """
    Sets the recording status to True or false
    :param status:
    :return: void
    """
    variables.recording_in_progress = status


def get_video_log_dir() -> str:
    """
    This returns the video logging
    directory as a string
    :return: string
    """
    return constants.VIDEO_TAPES_DIR


def set_output(new_output: str):
    """
    modifies the output variable to be compared with
    the last logged
    :param new_output:
    :return:
    """
    variables.output = new_output


def get_labels(main_labels: bool = False) -> list:
    """
    returns the raw list of labels
    or a list to present to the user
    :param main_labels:
    :return: list
    """
    if main_labels:
        return variables.labels
    else:
        return [i for i in variables.labels if i != "???"]


def set_labels() -> None:
    """
    Used to set our initial labels variable.
    :return: void
    """
    labels_txt = read("labelmap", model=True)
    labels = [line.strip() for line in labels_txt.split("\n")]
    if labels[0] == '???':
        del (labels[0])
    variables.labels = labels


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
