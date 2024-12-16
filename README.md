
---

# License Plate Detection using OpenCV

This project uses OpenCV's Haar Cascade Classifier to detect license plates in an image. The code reads an image, converts it to grayscale, and applies a pre-trained Haar Cascade model to detect license plates. Detected license plates are highlighted with green rectangles.

## Requirements

- Python 3.x
- `opencv-python`

You can install the required dependency using `pip`:

```bash
pip install opencv-python
```

## How It Works

1. **Read the Image**: The image is read using `cv2.imread()` and stored in the variable `test_img`.
2. **Convert to Grayscale**: The image is then converted to grayscale using `cv2.cvtColor()`, as the Haar Cascade classifier works on grayscale images.
3. **License Plate Detection**: The program uses a pre-trained Haar Cascade model (`haarcascade_russian_plate_number.xml`) to detect license plates in the grayscale image with `detectMultiScale()`.
4. **Drawing Rectangles**: For each detected license plate, the program draws a green rectangle on the original image using `cv2.rectangle()`.
5. **Display Image**: The processed image is displayed with `cv2.imshow()` and waits for a key press to close the window.

## Features

- Detects Russian license plates using Haar Cascade.
- Highlights detected plates with green rectangles.
- Works with images that are available locally.

## Usage

1. **Clone the Repository**: First, clone this repository to your local machine.

   ```bash
   git clone https://github.com/Abdulraheem232/Car-Numberplate-detector.git
   ```

2. **Prepare the Image**: Ensure you have a local image file (e.g., `test.jpg`) containing a license plate.

3. **Run the Script**: Navigate to the project directory and run the Python script to detect license plates in the image.

   ```bash
   cd car-number-plate-detector
   python main.py
   ```

   The script will load the image, process it, and display the results with rectangles around detected license plates.

4. **Expected Output**: The output will be the input image with green rectangles drawn around any detected license plates.

## Notes

- The program uses OpenCV’s Haar Cascade Classifier (`haarcascade_russian_plate_number.xml`) for license plate detection. This model is specific to Russian plates, but similar models are available for other regions.
- Make sure the input image (`test.jpg`) is in the same directory or provide the correct path to the image file.
- The `haarcascade_russian_plate_number.xml` file is included with OpenCV but can be found at `cv2.data.haarcascades`.

## Troubleshooting

- **No plates detected**: Ensure the image has a clear view of a license plate. Poor lighting or blurry images may reduce detection accuracy.
- **File not found error**: If `haarcascade_russian_plate_number.xml` is missing, ensure OpenCV is installed properly. This file should be present by default with OpenCV.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
