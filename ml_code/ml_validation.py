import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score
from operator import itemgetter

class AccuracyValidation():
    def __init__(self):
        self.letters = [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z'
        ]


    def split_validation(self, model, image_data, target_data, wrong_predictions = False):
        """
        uses the train_test_split method of sklearn cross validation
        Divides the training data into 75% : 25%. 75% for training
        25% for testing
        The method prints the percentage of correct predictions
        Parameters:
        -----------
        model: the machine learning model object
        image_data: 2D Numpy array of the training data with its features
        target_data: 1D numpy array of the labels
        wrong_predictions: Boolean (default is False), if true
        all the wrong predictions will be displayed for further
        investigation

        """
        img_train, img_test, target_train, target_test = train_test_split(image_data, target_data)
        model.fit(img_train, target_train)
        prediction = model.predict(img_test)
        accuracy = (float(np.sum(prediction == target_test)) / len(target_test))

        print str(round(accuracy * 100, 2))+ "% accuracy was recorded"

        if wrong_predictions:
            self.print_wrong_predictions(prediction, target_test, img_test, model)


    def print_wrong_predictions(self, predictions, correct_labels, img_test, model):
        """
        prints all the wrong predictions made by the model
        """
        print 'Here are the wrong predictions'
        print 'Prediction\tCorrect Label'
        print '------------------------------'

        for i in range(len(predictions)):
            if predictions[i] != correct_labels[i]:
                probabilities = model.predict_proba(img_test[i].reshape(1, -1))
                print 'Predicted: '+predictions[i]+'\t\t Actual:'+correct_labels[i]
                print 'Probability Distribution'
                self.top_predictions(probabilities)
                print '------------------------'

        print '------------------------------'


    def cross_validation(self, model, num_of_fold, train_data, train_label):
        accuracy_result = cross_val_score(model, train_data, train_label,
            cv = num_of_fold)
        print "Cross Validation Result for "+str(num_of_fold)+"-fold"

        print accuracy_result * 100

    def top_predictions(self, probabilities_prediction):
        predictions = probabilities_prediction.reshape(-1).tolist()
        predictions_label = []
        for index in range(len(predictions)):
            predictions_label.append((self.letters[index], predictions[index]))

        predictions_label = sorted(predictions_label, key=itemgetter(1), reverse=True)

        print predictions_label[:5]