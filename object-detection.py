from ultralytics import YOLO
import cv2

stream = "rtmp://127.0.0.1/live/gopro9" # stream link
cap = cv2.VideoCapture(stream) # open stream

model1 = YOLO("yolov8n.pt") # load first model
model2 = YOLO("yolov5su.pt") # load second model

while True: 
    succes, img = cap.read() # read frame from stream
    res1 = model1(img, device='mps') # predict for first model, replace mps with cuda for nvidia gpu
    res_plotted = res1[0].plot() # plot results for first model 

    res2 = model2(img, device='mps') # predict for second model, replace mps with cuda for nvidia gpu
    res2_plotted = res2[0].plot() # plot results for second model

    cv2.imshow("Yolo v8 - first model", res_plotted) # show results for first model
    cv2.imshow("Yolo v5 - second model", res2_plotted) # show results for second model

    if cv2.waitKey(1) & 0xFF == ord('q'): # press q to stop
        break