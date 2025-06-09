import os
import numpy as np
from PIL import Image
import scipy.ndimage as ndi
from datetime import datetime


class ImageProcessor:
    def __init__(self, my_images):
        self.my_images = my_images
        self.opened_images = []
        self.mean_filter_converted_images = []

        for img_path in self.my_images:
            img = Image.open(img_path).convert("L")
            self.opened_images.append(img)

    def mean_filter_convert(self, size, mode="reflect"):
        if size % 2 == 0:
            size += 1

        self.mean_filter_converted_images = []

        for img in self.opened_images:
            img_array = np.array(img)
            filtered_array = ndi.median_filter(img_array, size=size, mode=mode)
            filtered_img = Image.fromarray(filtered_array)
            self.mean_filter_converted_images.append(filtered_img)

        self.save_to_directory("images\\mean_filter")

    def save_to_directory(self, directory_name):
        os.makedirs(directory_name, exist_ok=True)

        for original_path, filtered_img in zip(self.my_images, self.mean_filter_converted_images):
            base_name = os.path.splitext(os.path.basename(original_path))[0]
            extension = os.path.splitext(original_path)[1]
            timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
            filename = f"{base_name}_{timestamp}{extension}"
            save_path = os.path.join(directory_name, filename)
            filtered_img.save(save_path)
