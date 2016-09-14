import numpy as np
from skimage.transform import resize
from sklearn.externals import joblib
class DeepMachineLearning():
    
    def learn(self, objectsToBeClassified, modelDir, tupleSize):
        model = self.loadModel(modelDir)
        return self.classifyObjects(objectsToBeClassified, model, tupleSize)
        
    def classifyObjects(self, objects, model, tupleResize):
        classificationResult = []
        for eachObject in objects:
            eachObject = resize(eachObject, tupleResize)
            eachObject = np.reshape(eachObject, -1)
            result = model.predict(eachObject)
            classificationResult.append(result)
        
        return classificationResult
        
    def loadModel(self, modelDir):
        model = joblib.load(modelDir)
        return model