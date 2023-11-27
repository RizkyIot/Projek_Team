import numpy as np
import cv2

class TemplateMatcher:
    def __init__(self, image_path, template_path):
        self.image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        self.template = cv2.imread(template_path, cv2.IMREAD_COLOR)

    def match_templates(self):
        img_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        template_gray = cv2.cvtColor(self.template, cv2.COLOR_BGR2GRAY)
        h, w = template_gray.shape

        methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
                   cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

        for method in methods:
            img = self.image.copy()
            template = self.template.copy()

            img_gray2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            template_gray2 = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

            result = cv2.matchTemplate(img_gray2, template_gray2, method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                location = min_loc
            else:
                location = max_loc

            bottom_right = (location[0] + w, location[1] + h)
            cv2.rectangle(img, location, bottom_right, (0, 0, 255), 5)

            cv2.imshow('Match', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

# Gunakan contoh penggunaan
matcher = TemplateMatcher('opencv/soccer_practice.jpg', 'opencv/ball.PNG')
matcher.match_templates()
