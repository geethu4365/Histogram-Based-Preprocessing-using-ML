import cv2
import matplotlib.pyplot as plt
import os

def equalize_and_display(image_path):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply histogram equalization
    equalized_image = cv2.equalizeHist(image)

    # Display the original and equalized image
    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(equalized_image, cmap='gray')
    plt.title('Equalized Image')

    # Display histograms
    plt.figure(figsize=(12, 6))

    plt.subplot(2, 2, 1)
    plt.hist(image.ravel(), 256, [0, 256], color='r')
    plt.title('Original Image Histogram')

    plt.subplot(2, 2, 2)
    plt.hist(equalized_image.ravel(), 256, [0, 256], color='b')
    plt.title('Equalized Image Histogram')

    plt.show()

# List of image paths
image_paths = ['image1.jpg', 'image2.jpg', 'image3.jpg']

# Apply equalization and display for each image
for image_path in image_paths:
    equalize_and_display(image_path)