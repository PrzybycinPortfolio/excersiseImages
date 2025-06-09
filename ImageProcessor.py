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
        self.min_filter_converted_images = []
        self.max_filter_converted_images = []
        self.median_filter_converted_images = []
        self.prewitt_images = []
        self.sobel_images = []

        for img_path in self.my_images:
            img = Image.open(img_path).convert("L")
            self.opened_images.append(img)

    def mean_filter_convert(self, size, mode="reflect"):
        if size % 2 == 0:
            size += 1

        self.mean_filter_converted_images = []

        for img in self.opened_images:
            img_array = np.array(img)
            filtered_array = ndi.uniform_filter(img_array, size=size, mode=mode)
            filtered_img = Image.fromarray(filtered_array)
            self.mean_filter_converted_images.append(filtered_img)
        self.save_to_directory("images\\mean_filter", self.mean_filter_converted_images)

    def min_filter_convert(self,size,mode="reflect"):
        if size % 2 == 0:
            size = size + 1

        self.min_filter_converted_images = []

        for img in self.opened_images:
            img_array = np.array(img)
            filtered_array = ndi.minimum_filter(img_array, size=size, mode=mode)
            filtered_img = Image.fromarray(filtered_array)
            self.min_filter_converted_images.append(filtered_img)

        self.save_to_directory("images\\min_filter",self.min_filter_converted_images)

    def max_filter_convert(self,size,mode="reflect"):
        if size % 2 == 0:
            size = size + 1

        self.max_filter_converted_images = []

        for img in self.opened_images:
            img_array = np.array(img)
            filtered_array = ndi.maximum_filter(img_array, size=size, mode=mode)
            filtered_img = Image.fromarray(filtered_array)
            self.max_filter_converted_images.append(filtered_img)

        self.save_to_directory("images\\max_filter",self.max_filter_converted_images)

    def median_filter_convert(self,size,mode="reflect"):
        if size % 2 == 0:
            size = size + 1

        self.median_filter_converted_images = []

        for img in self.opened_images:
            img_array = np.array(img)
            filtered_array = ndi.median_filter(img_array, size=size, mode=mode)
            filtered_img = Image.fromarray(filtered_array)
            self.median_filter_converted_images.append(filtered_img)

        self.save_to_directory("images\\median_filter",self.median_filter_converted_images)

    def prewitt_convert(self, mode="reflect"):
        self.prewitt_images = []

        for img in self.opened_images:
            img_array = np.array(img)
            dx = ndi.prewitt(img_array, axis=0, mode=mode)
            dy = ndi.prewitt(img_array, axis=1, mode=mode)
            magnitude = np.hypot(dx, dy).astype(np.uint8)
            filtered_img = Image.fromarray(magnitude)
            self.prewitt_images.append(filtered_img)

        self.save_to_directory("images\\prewitt", self.prewitt_images)

    def sobel_convert(self, mode="reflect"):
        self.sobel_images = []

        for img in self.opened_images:
            img_array = np.array(img)
            dx = ndi.sobel(img_array, axis=0, mode=mode)
            dy = ndi.sobel(img_array, axis=1, mode=mode)
            magnitude = np.hypot(dx, dy).astype(np.uint8)
            filtered_img = Image.fromarray(magnitude)
            self.sobel_images.append(filtered_img)

        self.save_to_directory("images\\sobel", self.sobel_images)

    def save_to_directory(self, directory_name,set):
        os.makedirs(directory_name, exist_ok=True)

        for original_path, filtered_img in zip(self.my_images, set):
            base_name = os.path.splitext(os.path.basename(original_path))[0]
            extension = os.path.splitext(original_path)[1]
            timestamp = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
            filename = f"{base_name}_{timestamp}{extension}"
            save_path = os.path.join(directory_name, filename)
            filtered_img.save(save_path)
