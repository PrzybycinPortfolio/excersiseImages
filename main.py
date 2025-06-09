import ImageProcessor
import os

input_images = []
size = 3
mode = "reflect"

directory = ".\\images\\input"
for file in os.listdir(directory):
    file_path = os.path.join(directory, file)
    input_images.append(file_path)

images = ImageProcessor.ImageProcessor(input_images)
images.mean_filter_convert(size,mode)
images.min_filter_convert(size,mode)
images.max_filter_convert(size,mode)
images.median_filter_convert(size,mode)
images.prewitt_convert(mode)
images.sobel_convert(mode)



