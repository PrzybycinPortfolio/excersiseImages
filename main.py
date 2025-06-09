import ImageProcessor
import Draw
import os

input_images = []
size = 3
mode = "reflect"

directory = ".\\images\\input"
for file in os.listdir(directory):
    file_path = os.path.join(directory, file)
    input_images.append(file_path)

images = ImageProcessor.ImageProcessor(input_images)
images.mean_filter_convert(size,mode) # 2 zadanie
images.min_filter_convert(size,mode) # 3 zadanie część 1
images.max_filter_convert(size,mode) # 3 zadanie część 2
images.median_filter_convert(size,mode) # 4 zadanie
images.prewitt_convert(mode) # 5 zadanie 1 część
images.sobel_convert(mode) # 5 zadanie 2 część
Draw.draw_image(300,400) #6 zadanie





