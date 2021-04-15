import cv2
import numpy as np
import utils

questions = 20
choices = 5
path = 'ms.png'
widthImg = 566
heightImg = 800
img = cv2.imread(path)
#widthImg = img.shape[1]
#heightImg = img.shape[0]
img = cv2.resize(img, (widthImg, heightImg))
imgFinal = img.copy()
imgContours = img.copy()
imgBiggestContours = img.copy()
ans = [0, 4, 3, 1, 0, 3, 2, 4, 2, 2, 3, 1, 2, 1, 2, 1, 3, 4, 0, 0]

# image preprocessing
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
imgCanny = cv2.Canny(imgBlur, 10, 50)

# finding all contours
contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 2)

# find rectangles
rectCon = utils.rectContours(contours)
biggestContour = utils.getCornerPoints(rectCon[0])
gradePoints = utils.getCornerPoints(rectCon[1])
# print(biggestContour.shape)

if biggestContour.size != 0 and gradePoints.size != 0:
    cv2.drawContours(imgBiggestContours, biggestContour, -1, (0, 255, 0), 20)
    cv2.drawContours(imgBiggestContours, gradePoints, -5, (0, 0, 255), 20)
    biggestContour = utils.reorder(biggestContour)
    gradePoints = utils.reorder(gradePoints)

    pt1 = np.float32(biggestContour)
    pt2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
    matrix = cv2.getPerspectiveTransform(pt1, pt2)
    imgWarpColored = cv2.warpPerspective(img, matrix, (widthImg, heightImg))

    ptg1 = np.float32(gradePoints)
    ptg2 = np.float32([[0, 0], [325, 0], [0, 150], [325, 150]])
    matrixG = cv2.getPerspectiveTransform(ptg1, ptg2)
    imgGradeDisplay = cv2.warpPerspective(img, matrixG, (325, 150))

    # apply threshold
    imgWarpGray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
    imgThresh = cv2.threshold(imgWarpGray, 200, 255, cv2.THRESH_BINARY_INV)[1]
    boxes = utils.splitBoxes(imgThresh, choices, questions)

    myPixelVal = np.zeros((questions, choices))
    myZeroPixelVal = np.zeros((questions, choices))
    countC = 0
    countR = 0
    for image in boxes:
        totalPixel = cv2.countNonZero(image)
        myPixelVal[countR][countC] = totalPixel
        myZeroPixelVal[countR][countC] = image.shape[0]* image.shape[1] - totalPixel
        countC += 1
        if countC == choices:
            countR += 1
            countC = 0
    print(myPixelVal)
    print(myZeroPixelVal)

    # Finding index values of the markings
    myIndex = []
    for x in range(0, questions):
        arr = myPixelVal[x]
        # print(arr)
        myIndexVal = np.where(arr == np.amax(arr))
        # print(myIndexVal[0])
        myIndex.append(myIndexVal[0][0])
    print(myIndex)

    # Grading
    grading = []
    for x in range(0, questions):
        if ans[x] == myIndex[x]:
            grading.append(1)
        else:
            grading.append(0)

    print(grading)
    score = (sum(grading)/questions)*100
    score = (score*questions)/100
    print(score)
    d = sum(grading)
    print(d, '/', questions)
    print(imgThresh.shape)

    # DISPLAY ANSWERS
    imgResult = imgWarpColored.copy()
    imgResult = utils.showAnswers(imgResult, myIndex, grading, ans, questions, choices)
    cv2.imwrite('you.png',imgResult)
    imRawDrawing = np.zeros_like(imgWarpColored)
    imRawDrawing = utils.showAnswers(imRawDrawing, myIndex, grading, ans, questions, choices)
    #cv2.imshow('raw', imRawDrawing)
    invMatrix = cv2.getPerspectiveTransform(pt2, pt1)
    imInvWarp = cv2.warpPerspective(imRawDrawing, invMatrix, (widthImg, heightImg))
    imgFinal = cv2.addWeighted(imgFinal,1,imInvWarp,1,0)
    cv2.imshow('final result', imgFinal)
    cv2.imwrite('final-result.png', imgFinal)
    #imageArray = ([img, imgThresh, imgWarpColored, imgResult])
    #imgStacked = utils.stackImages(imageArray, 0.2)

    cv2.imshow('thresh', imgResult)
    print(imgResult.shape)


cv2.waitKey(0)
