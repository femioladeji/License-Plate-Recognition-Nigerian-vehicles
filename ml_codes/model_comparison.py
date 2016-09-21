import numpy as np
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from ml_config import MachineLearningConfig
from sklearn.cross_validation import train_test_split
from ml_validation import AccuracyValidation
import templatematching

config = MachineLearningConfig()
validate = AccuracyValidation()

training_directory = config.training_data[0]

image_data, target_data = config.read_training_data(training_directory)  

sv_model1 = SVC(kernel='linear', probability=True)
sv_model2 = SVC(kernel='rbf', probability=True)
n_model = KNeighborsClassifier(n_neighbors=3)
n_model2 = KNeighborsClassifier(n_neighbors=4)

models = {
    'rbfsvm':sv_model2, 'linearsvm':sv_model1,
    '3-neighbor':n_model, '4-neighbor':n_model2
}



img_train, img_test, target_train, target_test = train_test_split(image_data,
    target_data, test_size=0.4, train_size=0.6)

prediction2dlist = []

for a_model_name, a_model in models.items():
    print a_model_name
    print '-------------------------------'
    a_model.fit(img_train, target_train)
    prediction = a_model.predict(img_test)
    prediction2dlist.append(prediction)
    accuracy = (float(np.sum(prediction == target_test)) / len(target_test))
    print str(round(accuracy * 100, 2))+ "% accuracy was recorded"
    print '-------------------------------'

num_of_test = len(img_test)

for index in range(num_of_test):
    if prediction2dlist[2][index] != target_test[index]:
        print 'Based on LinearSVM'
        print 'Actual Label : '+ target_test[index]+' Predicted Label: '+prediction2dlist[1][index]
        for a_model_name in models:
            print a_model_name
            print '-------------------------------'
            prob_predictions = models[a_model_name].predict_proba(
                img_test[index].reshape(1, -1))
            validate.top_predictions(prob_predictions)
            print '-------------------------------'

        if prediction2dlist[1][index] in config.ascertain_characters:
            print 'Prediction by template matching'
            print '-------------------------------'
            print templatematching.template_match(prediction2dlist[1][index],
                img_test[index], training_directory)
            print '-------------------------------'