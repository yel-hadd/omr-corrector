import cv2
import numpy as np

# detect rectangle contour
def rectContours(contours):
    rectCon = []
    for i in contours:
        area = cv2.contourArea(i)
        #print('Area:', area)
        if area>50:
            peri = cv2.arcLength(i,True)
            approx = cv2.approxPolyDP(i,0.02*peri,True)
            #print("Corner Points", len(approx))
            if len(approx)==4:
                rectCon.append(i)
    rectCon = sorted(rectCon,key= cv2.contourArea,reverse=True)
    return rectCon

def getCornerPoints(cont):
    peri = cv2.arcLength(cont, True)
    approx = cv2.approxPolyDP(cont, 0.02 * peri, True)
    return approx

def reorder(myPoints):
    myPoints = myPoints.reshape((4,2))
    myPointsNew = np.zeros((4,1,2),np.int32)
    add = myPoints.sum(1)
    #print(myPoints)
    #print(add)
    myPointsNew[0] = myPoints[np.argmin(add)] # [0, 0]
    myPointsNew[3] = myPoints[np.argmax(add)] # [w, h]
    diff = np.diff(myPoints,axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)] # [w, 0]
    myPointsNew[2] = myPoints[np.argmax(diff)] # [0, h]
    return myPointsNew

def round_down(num, divisor):
    return num - (num%divisor)

def splitBoxes(img,choices,questions):
    multipleW = round_down(img.shape[1],choices)
    multipleH = round_down(img.shape[0],questions)
    img = cv2.resize(img, (multipleW, multipleH))

    rows = np.vsplit(img,questions)
    boxes = []
    for r in rows:
        cols = np.hsplit(r,choices)
        for box in cols:
            boxes.append(box)
    return boxes




