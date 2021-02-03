import cv2

camera = cv2.VideoCapture(0) # Get Camera as an object
return_value, image = camera.read() # Take the image
# cv2.imwrite('image.png', image) # Save the image
del(camera) # Remove camera object

with open(image, "rb") as f:
    information = f.read()

print(information)
