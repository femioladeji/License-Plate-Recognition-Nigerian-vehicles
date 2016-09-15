import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score
from ml_config import MachineLearningConfig

config = MachineLearningConfig()

image_data, target_data = config.read_training_data(config.training_data[0])

print image_data.shape
# img_train, img_test, target_train, target_test = train_test_split(image_data, target_data)
# print img_train.shape
# print img_test.shape

for number_of_neighbors in range(3, 8):
    neighbor_model = KNeighborsClassifier(n_neighbors = number_of_neighbors)

    print cross_val_score(neighbor_model, image_data, target_data)
    # neighbor_model.fit(img_train, target_train)

    # prediction = neighbor_model.predict(img_test)

    # for i in range(len(prediction)):
    #     if prediction[i] != target_test[i]:
    #         print prediction[i], target_test[i]

    # print neighbor_model.score(img_test, target_test)
    # print (float(np.sum(prediction == target_test)) / len(target_test)) * 100
    # perc_accuracy = accuracy_score(img_test, prediction)

    # print perc_accuracy