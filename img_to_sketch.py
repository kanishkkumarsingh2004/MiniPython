import cv2 
# image = cv2.imread('kanishk.JPG')
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# inverted = 255 - gray_image
# blur = cv2.GaussianBlur(inverted, (21, 21), 0)
# invertedBlur = 255 - blur
# sketch = cv2.divide(gray_image, invertedBlur, scale=256.0)
# cv2.imwrite("Sketch_image.png", sketch)
# cv2.imshow("image", sketch)

def image_to_sketch(file_location):
    image = cv2.imread(file_location)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted = 255 - gray_image
    blur = cv2.GaussianBlur(inverted, (21, 21), 0)
    invertedBlur = 255 - blur
    sketch = cv2.divide(gray_image, invertedBlur, scale=256.0)
    cv2.imwrite("Sketch_image.png", sketch)

file_location = 'file location'
image_to_sketch(file_location)