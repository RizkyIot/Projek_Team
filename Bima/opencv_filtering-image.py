import cv2
import numpy as np

class ImageFilter:
    def __init__(self, image_path):
        self.image_path = image_path

    def apply_filter(self):
        # Baca gambar
        image = cv2.imread(self.image_path)

        # Ubah ukuran frame menjadi lebih kecil
        resized_image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

        # Pemfilteran warna
        lower_red = np.array([0, 0, 0])
        upper_red = np.array([50, 50, 255])
        mask = cv2.inRange(resized_image, lower_red, upper_red)
        result = cv2.bitwise_and(resized_image, resized_image, mask=cv2.bitwise_not(mask))

        # Konversi gambar ke grayscale
        gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

        # Terapkan filter blur Gaussian
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Terapkan filter Canny untuk deteksi tepi
        edges = cv2.Canny(blurred, 30, 150)

        return edges

    def show_image(self, image):
        cv2.imshow('Filtered Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Usage example
image_path = 'opencv/bima.jpg'
image_filter = ImageFilter(image_path)
filtered_image = image_filter.apply_filter()
image_filter.show_image(filtered_image)
