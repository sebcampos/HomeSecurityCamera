import threading
import cv2
from . import variables
from . import utils


def start_thread() -> None:
    """
    Creates a thread using the threading module invoking the update_frame method
    as its target. Then saves this thread into our variables.thread variable.
    :return: void
    """
    variables.thread = threading.Thread(target=update_frame, args=())
    variables.thread.daemon = True
    variables.thread.start()


def start_video() -> None:
    """
    Starts the video camera and saves it in our variables
    object along with its related width and height
    :return: void
    """
    video = cv2.VideoCapture(0)
    variables.video_width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
    variables.video_height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    variables.video = video


def format_frame(frame: list) -> bytes:
    """
    This method formats the array into
    bytes in the form of a .jpg image
    :param frame: array from the cv2 read method
    :return: jpg bytes
    """
    _, jpg = cv2.imencode(".jpg", frame)
    return jpg.tobytes()


def feed() -> bytes:
    """
    This returns a stream of bytes in the
    form of a jpeg for the iframe feed
    :return: bytes
    """
    while utils.get_thread().is_alive():
        frame = utils.get_main_frame()
        frame = format_frame(frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def check_track_list(label: str) -> bool:
    """
    This method checks the track list variable to see if the current label should
    be tracked. If so it will log the start and begin a recording, or reset the recording counter
    :param label:
    :return:
    """
    if utils.get_recording_status() and utils.get_recording_frame_count() <= 0:
        end_recording()
        utils.write(f"[{utils.get_date_and_time()}] recording ended", utils.get_date(), log_line=True)
        return False
    if label in utils.get_track_list() and utils.get_recording_status() is False:
        start_recording()
        utils.write(f"[{utils.get_date_and_time()}] recording started", utils.get_date(), log_line=True)
        return True
    elif label in utils.get_track_list() and utils.get_recording_status() is True:
        utils.reset_recording_frame_count()
        return True
    elif label not in utils.get_track_list() and utils.get_recording_status() is True:
        utils.decrement_recording_frame_count()
        return False
    else:
        return False


def start_recording() -> None:
    """
    This method when invoked begins a recording
    with the name of the recording being the current date and time.
    it is saved to our variables.recorder and we set the recording status
    to True
    :return: void
    """
    size = (int(utils.get_video_width()), int(utils.get_video_height()))
    variables.recorder = cv2.VideoWriter(
        f"{utils.get_video_log_dir()}{utils.get_date_and_time()}.avi",
        cv2.VideoWriter_fourcc(*'MJPG'),
        10,
        size
    )
    utils.set_recording_status(True)


def end_recording() -> None:
    """
    This method when invoked closes or `releases` our
    recorder variable, resets the frame count, and
    sets our recording status to False
    :return: void
    """
    variables.recorder.release()
    utils.reset_recording_frame_count()
    utils.set_recording_status(False)


def update_frame() -> None:
    """
    This method uses open-cv and tensorflow to augment a live stream
    and draw boxes around recognized objects if the object is within our
    tracking list.
    :return: void
    """
    while utils.get_thread().is_alive():

        # Acquire frame and resize to expected shape [1xHxWx3]
        ret, frame = utils.get_video().read()
        if not ret:
            break
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_resized = cv2.resize(frame_rgb, (utils.get_model_height(), utils.get_model_width()))
        input_data = utils.get_np().expand_dims(frame_resized, axis=0)

        # Normalize pixel values if using a floating model (i.e. if model is non-quantized)
        if utils.is_floating_model():
            input_data = (utils.get_np().float32(input_data) - utils.get_input_mean()) / utils.get_input_std()

        # Perform the actual detection by running the model with the image as input
        utils.get_interpreter().set_tensor(utils.get_input_details()[0]['index'], input_data)
        utils.get_interpreter().invoke()

        # Retrieve detection results
        boxes = utils.get_interpreter().get_tensor(
            utils.get_output_details()[utils.get_box_idx()]['index'])[0]  # Bounding box coordinates of detected objects
        classes = utils.get_interpreter().get_tensor(
            utils.get_output_details()[utils.get_classes_idx()]['index'])[0]  # Class index of detected objects
        scores = utils.get_interpreter().get_tensor(
            utils.get_output_details()[utils.get_scores_idx()]['index'])[0]  # Confidence of detected objects

        # Loop over all detections and draw detection box if confidence is above minimum threshold
        imW = utils.get_video_width()
        imH = utils.get_video_height()
        for i in range(len(scores)):
            if (scores[i] > utils.get_min_conf_threshold()) and (scores[i] <= 1.0):
                object_name = utils.get_labels(main_labels=True)[
                    int(classes[i])]  # Look up object name from "labels" array using class index

                # entry point to check lables
                if check_track_list(object_name):
                    pass
                else:
                    continue
                # Get bounding box coordinates and draw box
                # Interpreter can return coordinates that are outside of image dimensions, need to force them to be within image using max() and min()
                ymin = int(max(1, (boxes[i][0] * imH)))
                xmin = int(max(1, (boxes[i][1] * imW)))
                ymax = int(min(imH, (boxes[i][2] * imH)))
                xmax = int(min(imW, (boxes[i][3] * imW)))

                cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (10, 255, 0), 4)

                # Draw label
                label = '%s: %d%%' % (object_name, int(scores[i] * 100))  # Example: 'person: 72%'
                label_size, base_line = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)  # Get font size
                label_ymin = max(ymin, label_size[1] + 10)  # Make sure not to draw label too close to top of window
                cv2.rectangle(frame, (xmin, label_ymin - label_size[1] - 10),
                              (xmin + label_size[0], label_ymin + base_line - 10), (255, 255, 255),
                              cv2.FILLED)  # Draw white box to put label text in
                cv2.putText(frame, label, (xmin, label_ymin - 7), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0),
                            2)  # Draw label text

        if utils.get_recording_status():
            utils.get_recorder().write(frame)
        utils.set_main_frame(frame)
