import numpy as np
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from ml_config import MachineLearningConfig
from sklearn.cross_validation import train_test_split

sv_model1 = SVC(kernel='linear', probability=True)
sv_model2 = SVC(kernel='rbf', probability=True)
n_model = KNeighborsClassifier(n_neighbors=3)
n_model2 = KNeighborsClassifier(n_neighbors=4)

models = {
    'linearsvm':sv_model1, 'rbfsvm':sv_model2,
    '2-neighbor':n_model, '4-neighbor':n_model2
}

config = MachineLearningConfig()

image_data, target_data = config.read_training_data(config.training_data[0])

img_train, img_test, target_train, target_test = train_test_split(image_data, target_data)

for a_model_name, a_model in models.items():
    print a_model_name
    print '-------------------------------'
    a_model.fit(img_train, target_train)
    prediction = a_model.predict(img_test)
    accuracy = (float(np.sum(prediction == target_test)) / len(target_test))
    print str(round(accuracy * 100, 2))+ "% accuracy was recorded"
    #self.print_wrong_predictions(prediction, target_test, img_test, a_model)
    print '-------------------------------'

