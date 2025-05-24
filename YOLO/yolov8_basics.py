from ultralytics import YOLO
import numpy

# load d  pretrained YOLOv8n model

model = YOLO("yolov8n.pt", "v8")

#predict on an image
detection_output = model.predict(source = r"C:\Users\vineet\Downloads\sexy.jpg", conf = 0.25, save =  True)

#Display Tensor Array
print(detection_output)

#Display a numpy array

print(detection_output[0].numpy())