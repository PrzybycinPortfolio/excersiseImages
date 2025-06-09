# excersiseImages
Homework for studies

# 🖼️ Image Processing with Filters and Edge Detection

This Python project provides an `ImageProcessor` class that applies various image processing techniques—including mean, min, max, median filters, and edge detection (Prewitt and Sobel operators)—to grayscale images. It also includes a simple image generation utility for visualization.

## 📁 Project Structure

```
project/
│
├── images/
│   ├── input/                  # Place your input images here
│   ├── mean_filter/            # Saved outputs of mean filter
│   ├── min_filter/             # Saved outputs of min filter
│   ├── max_filter/             # Saved outputs of max filter
│   ├── median_filter/          # Saved outputs of median filter
│   ├── prewitt/                # Saved outputs of Prewitt edge detection
│   └── sobel/                  # Saved outputs of Sobel edge detection
│
├── ImageProcessor.py           # Main image processing module
├── Draw.py                     # Random RGB image generator
└── main.py                     # Entry point script
```

## 🧰 Features

- ✅ Load and convert images to grayscale.
- ✅ Apply **mean filter** using `scipy.ndimage.uniform_filter`.
- ✅ Apply **min filter** using `scipy.ndimage.minimum_filter`.
- ✅ Apply **max filter** using `scipy.ndimage.maximum_filter`.
- ✅ Apply **median filter** using `scipy.ndimage.median_filter`.
- ✅ Perform **edge detection** using **Prewitt** and **Sobel** operators.
- ✅ Save processed images with timestamped filenames.
- ✅ Random image generator for testing (`Draw.py`).

## 🚀 Getting Started

### 1. Install Requirements

Make sure you have the following Python packages installed:

```bash
pip install numpy Pillow scipy matplotlib
```

### 2. Add Input Images

Place your input images inside the `images/input/` directory.

### 3. Run the Script

Execute the main script to process all images:

```bash
python main.py
```

## 🧪 Functionality Overview

| Method                          | Description                                 |
|--------------------------------|---------------------------------------------|
| `mean_filter_convert(size, mode)`   | Applies uniform/mean filter                |
| `min_filter_convert(size, mode)`    | Applies minimum filter                     |
| `max_filter_convert(size, mode)`    | Applies maximum filter                     |
| `median_filter_convert(size, mode)` | Applies median filter                      |
| `prewitt_convert(mode)`             | Detects edges using Prewitt operator       |
| `sobel_convert(mode)`               | Detects edges using Sobel operator         |
| `draw_image(x, y)`                  | Generates a random RGB image of shape `(x, y, 3)` for display |

## 📝 Notes

- All filters and edge detection operations are performed on grayscale versions of the images.
- Filter size must be odd; if even, it is automatically incremented.
- Processed images are saved to separate directories under `images/`.

## 📸 Example Output

Each processed image is saved in the corresponding folder with a filename pattern like:

```
originalname_09_06_2025_14_30_01.png
```

## 📂 Author & License

**Author:** *Karol Przybycin*

