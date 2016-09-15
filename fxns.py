import math
def variationCal(imgArray):
    variation = 0
    for rowIndex in range(len(imgArray)):
        for colIndex in range(len(imgArray[rowIndex])):
            if colIndex < len(imgArray[rowIndex])-1:
                variation += abs(imgArray[rowIndex][colIndex+1] - imgArray[rowIndex][colIndex])
            if rowIndex < len(imgArray)-1:
                variation += abs(imgArray[rowIndex+1][colIndex] - imgArray[rowIndex][colIndex])
                
    print variation
    
def histogramGeneration(imgArray):
    histogramList = []
    #if the imgarray is 3D with RGB channel
    for eachRow in imgArray:
        for eachCol in eachRow:
            grayValue = (eachCol[0]+eachCol[1]+eachCol[2]) / 3
            try:
                histogramList[int(round(grayValue))] += 1
            except IndexError:
                histogramList.insert(int(round(grayValue)), 1)
    
    return histogramList
    
def thresholdCalc(histogram, numberOfPixels):
    summ = 0; sumB = 0; wB = 0; wF = 0; maximum = 0; threshold = 0
    #''' , mB, mF, between '''
    for i in range(256):
        try:
            summ += i * histogram[i];
        except IndexError:
            continue
    for i in range(256):
        wB += histogram[i]
        if wB == 0:
            continue
        wF = numberOfPixels - wB
        if wF == 0:
            break
        sumB += i * histogram[i]
        mB = sumB / wB
        mF = (summ - sumB) / wF
        between = wB * wF * math.pow(mB - mF, 2);
        if between > maximum:
            maximum = between
            threshold = i
    print threshold