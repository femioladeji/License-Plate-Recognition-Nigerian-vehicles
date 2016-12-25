from skimage.transform import resize
from sklearn.externals import joblib
import templatematching
import os.path
class DeepMachineLearning():
    
    def __init__(self):
        self.letters = [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z'
        ]

    def learn(self, objects_to_classify, modelDir, tuple_size):
        model = self.load_model(modelDir)
        return self.classify_objects(objects_to_classify, model, tuple_size)
        
    def classify_objects(self, objects, model, tuple_resize):
        """
        uses the predict method in the model to predict the category(character)
        that the image belongs to

        Parameters
        ___________
        objects: Numpy array
        """
        classificationResult = []
        for eachObject in objects:
            eachObject = resize(eachObject, tuple_resize)
            eachObject = eachObject.reshape(1, -1)
            result = model.predict(eachObject)
            probabilities = model.predict_proba(eachObject)
            result_index = self.letters.index(result[0])
            prediction_probability = probabilities[0, result_index]
            # template matching when necessary
            if result[0] in templatematching.confusing_chars and prediction_probability < 0.15:
                print 'here'
                result[0] = templatematching.template_match(result[0],
                    eachObject, os.path.join(os.path.dirname(os.path.realpath(
                        __file__)), 'training_data', 'train20X20'))
            classificationResult.append(result)
        
        return classificationResult
        
    def load_model(self, model_dir):
        """
        loads the machine learning using joblib package
        model_dir is the directory for the model
        loading of the model has nothing to do with the classifier used
        """
        model = joblib.load(model_dir)
        return model