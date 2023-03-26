from ultralytics import YOLO
import cv2

stream = "rtmp://127.0.0.1/live/gopro9" # stream link
cap = cv2.VideoCapture(stream) # open stream
model1 = YOLO("yolov8n.pt") # load first model

while True: #
    succes, img = cap.read() # read frame
    res = model1(img, device='mps') # predict for first model
    res_plotted = res[0].plot() # plot results for first model
    cv2.imshow("Yolo v8", res_plotted) # show results for first model
    if cv2.waitKey(1) & 0xFF == ord('q'): # press q to stop
        break