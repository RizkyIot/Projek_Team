import numpy as np
import cv2

class ChessboardDetector:
    def __init__(self, image_path):
        self.image_path = image_path
        self.img = None
        self.gray = None
        self.corners = None

    def load_image(self):
        self.img = cv2.imread(self.image_path)
        self.img = cv2.resize(self.img, (0, 0), fx=0.75, fy=0.75)
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

    def detect_corners(self):
        self.corners = cv2.goodFeaturesToTrack(self.gray, 100, 0.01, 10)
        self.corners = np.intp(self.corners)

    def draw_corners(self):
        for corner in self.corners:
            x, y = corner.ravel()
            cv2.circle(self.img, (x, y), 5, (255, 0, 0), -1)

    def draw_lines(self):
        for i in range(len(self.corners)):
            for j in range(i + 1, len(self.corners)):
                corner1 = tuple(self.corners[i][0])
                corner2 = tuple(self.corners[j][0])
                color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
                cv2.line(self.img, corner1, corner2, color, 1)

    def show_image(self):
        cv2.imshow('Frame', self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Usage example
image_path = 'opencv/chessboard.png'
chessboard_detector = ChessboardDetector(image_path)
chessboard_detector.load_image()
chessboard_detector.detect_corners()
chessboard_detector.draw_corners()
chessboard_detector.draw_lines()
chessboard_detector.show_image()
