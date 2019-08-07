import cv2


def split_video(file_path):
    """Split a video into frames."""
    video_capture = cv2.VideoCapture(file_path)

    images = []
    success, image = video_capture.read()
    while success:
        images.append(image)
        success, image = video_capture.read()

    return images
