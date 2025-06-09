import ImageProcessor
import os

input_images = []

directory = ".\\images\\input"
for file in os.listdir(directory):
    file_path = os.path.join(directory, file)
    input_images.append(file_path)

images = ImageProcessor.ImageProcessor(input_images)
images.mean_filter_convert(3,"reflect")



