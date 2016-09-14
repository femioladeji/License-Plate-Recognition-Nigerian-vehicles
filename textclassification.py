class TextClassification:
    
    '''def classifyText(self, objects, modelfile):
        model = joblib.load(modelfile)
        plateString = ''
        for eachObject in objects:
            eachObject = binary_closing(eachObject)
            eachObject = np.reshape(eachObject, -1)
            aCharacter = model.predict(eachObject)
            plateString += aCharacter[0]
        
        return plateString'''
    
    def getText(self, machineLearningResult):
        plateString = ''
        for eachPredict in machineLearningResult:
            plateString += eachPredict[0]
            
        return plateString
    
    def textReconstruction(self, plateString, positionList):
        posListCopy = positionList[:]
        positionList.sort()
        rightPlateString = ''
        for each in positionList:
            rightPlateString += plateString[posListCopy.index(each)]
            
        return rightPlateString