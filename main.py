import cv2
import numpy as np
import utils

questions = 20
choices = 5
path = '20.png'
img = cv2.imread(path)
widthImg = img.shape[1]
heightImg = img.shape[0]
img = cv2.resize(img, (widthImg, heightImg))
imgFinal = img.copy()
imgContours = img.copy()
imgBiggestContours = img.copy()
ans = np.zeros((questions, choices))

ans = [[1, 0, 0, 0, 0],  # 1
       [1, 0, 0, 1, 0],  # 2
       [1, 0, 0, 1, 0],  # 2
       [1, 1, 0, 0, 0],  # 2
       [0, 1, 0, 0, 1],  # 1
       [1, 0, 0, 1, 0],  # 2
       [0, 0, 0, 1, 1],  # 2
       [0, 0, 0, 0, 1],  # 1
       [0, 1, 0, 0, 0],  # 1
       [0, 0, 1, 0, 0],  # 1
       [1, 1, 0, 0, 0],  # 2
       [0, 1, 0, 0, 0],  # 1
       [1, 0, 0, 0, 0],  # 1
       [0, 0, 0, 0, 1],  # 1
       [0, 1, 0, 0, 1],  # 2
       [0, 1, 0, 0, 0],  # 1
       [1, 0, 0, 0, 0],  # 1
       [0, 0, 0, 0, 1],  # 1
       [0, 0, 0, 1, 0],  # 1
       [1, 0, 0, 0, 0]]  # 1

nbrChoices = np.sum(ans, axis=1)
nbrChoices = nbrChoices.tolist()

bareme = [0.5, 1.5, 0.5, 1.5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1.5, 1, 0.5]


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

    # Count NonZeroPixels and Detect empty and full cells
    myPixelVal = np.zeros((questions, choices))
    empty = np.zeros((questions, choices))
    Full = np.zeros((questions, choices))
    countC = 0
    countR = 0
    for image in boxes:
        totalPixel = cv2.countNonZero(image)
        myPixelVal[countR][countC] = totalPixel
        if myPixelVal[countR][countC] < image.shape[0] * image.shape[1] * 30 / 100:
            empty[countR][countC] = 1
            Full[countR][countC] = 0
        else:
            empty[countR][countC] = 0
            Full[countR][countC] = 1
        countC += 1
        if countC == choices:
            countR += 1
            countC = 0

    # Getting the Sum of Each line values
    sumLineFull = np.sum(Full,axis=1)
    sumLineFull = sumLineFull.tolist()
    sumLineAns = np.sum(ans,axis=1)
    sumLineAns = sumLineAns.tolist()

    # Grading
    grading = []
    score = []
    gradingType = 1  # 0==moderate 1==strict
    # Strict Grading
    if gradingType == 1:
        grading = (ans == Full).all(axis=1)
        for item in range(questions):
            if grading[item] == True:
                score.append(bareme[item])
            else:
                score.append(0)
        sumScore = sum(score)
        print(score)
        print(sumScore)
    
    # Moderate Grading
    elif gradingType == 0:
        grading = np.zeros((questions,choices))
        score = []
        for j in range(questions):
            for i in range(choices):
                if ans[j][i] == Full[j][i] and Full[j][i] and empty[j][i] == 0:
                    grading[j][i] = bareme[j]/nbrChoices[j]
                else:
                    grading[j][i] = 0
        score = np.sum(grading, axis=1)
        sumScore = sum(score)
        print(score)
        print(sumScore)
    #print(sum(score))
    cv2.imwrite("you.png", imgWarpColored)

    """
    # Finding index values of the markings
    myIndex = []
    myPixelVal = np.zeros((questions,3))
    for x in range(0, questions):
        arr = Full[x]
        myIndexVal = np.where(arr == np.amax(arr))
        myIndex.append(myIndexVal[0][0])
    print("myindex",myIndex)

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

"""


cv2.waitKey(0)

