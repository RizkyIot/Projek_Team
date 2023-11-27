import numpy as np
import cv2

class VideoProcessor:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def process_video(self):
        while True:
            ret, frame = self.cap.read()
            width = int(self.cap.get(3))
            height = int(self.cap.get(4))

            image = np.zeros(frame.shape, np.uint8)
            smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
            image[:height // 2, :width // 2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
            image[height // 2:, :width // 2] = smaller_frame
            image[:height // 2, width // 2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
            image[height // 2:, width // 2:] = smaller_frame

            cv2.imshow('frame', image)

            if cv2.waitKey(1) == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

# Usage example
video_processor = VideoProcessor()
video_processor.process_video()
