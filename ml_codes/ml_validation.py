import numpy as np
from sklearn.cross_validation import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score

class AccuracyValidation():

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
            self.print_wrong_predictions(prediction, target_test)

    def print_wrong_predictions(self, predictions, correct_labels):
        """
        prints all the wrong predictions made by the model
        """
        print 'Here are the wrong predictions'
        print 'Prediction\tCorrect Label'
        print '------------------------------'

        for i in range(len(predictions)):
            if predictions[i] != correct_labels[i]:
                print predictions[i]+'\t\t'+correct_labels[i]

        print '------------------------------'


    def cross_validation(self, model, num_of_fold, train_data, train_label):
        accuracy_result = cross_val_score(model, train_data, train_label,
            cv = num_of_fold)
        print "Cross Validation Result for "+str(num_of_fold)+"-fold"

        print accuracy_result * 100
