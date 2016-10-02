import numpy as np
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from ml_config import MachineLearningConfig
from sklearn.cross_validation import cross_val_score
from ml_validation import AccuracyValidation
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import time

config = MachineLearningConfig()
validate = AccuracyValidation()

training_directory = config.training_data[0]

image_data, target_data = config.read_training_data(training_directory)  

sv_model1 = SVC(kernel='linear')
sv_model2 = SVC(kernel='rbf')
sv_model3 = SVC(kernel='poly')
n_model = KNeighborsClassifier(n_neighbors=3)
n_model2 = KNeighborsClassifier(n_neighbors=4)
n_model3 = KNeighborsClassifier(n_neighbors=5)
gnb = GaussianNB()
dec_tree = DecisionTreeClassifier()
rand_forest = RandomForestClassifier()

models = {
    'rbfsvm':sv_model2, 'linearsvm':sv_model1,
    '3-neighbor':n_model, '4-neighbor':n_model2,
    '5 neighbors':n_model3, 'Gaussian Naive Bayes':gnb,
    'Decision Tree':dec_tree, 'Random Forest':rand_forest,
    'Polynomial SVM':sv_model3
}


for a_model_name, a_model in models.items():
    print a_model_name
    print '-------------------------------'
    start = time.time()
    scores = cross_val_score(a_model, image_data, target_data, cv=4)
    timediff = time.time() - start
    print 'Accuracy = '+ str(np.mean(scores)*100) + 'Time = '+str(timediff)
    print '-------------------------------'