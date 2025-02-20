import os
import sys
import time
import cv2 as cv

class CaptureImage:
    def __init__(self, camera_index=0, output_folder=None, image_name=None):
        self.camera_index = camera_index
        self.output_folder = output_folder
        self.image_name = image_name

    def capture(self): 
        cap = cv.VideoCapture(self.camera_index)
        if not cap.isOpened():
            print("Error: Could not open camera.")
            exit()
        
        while True: 
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame.")
            cv.imshow('frame', frame)

            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv.destroyAllWindows() 

if __name__ == "__main__":
    capture_image = CaptureImage(camera_index=0, output_folder='output', image_name='captured_image.jpg')
    capture_image.capture()