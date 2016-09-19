from sklearn.ensemble import RandomForestClassifier
from ml_config import MachineLearningConfig
from ml_validation import AccuracyValidation

config = MachineLearningConfig()

image_data, target_data = config.read_training_data(config.training_data[0])

rand_forest_classifier = RandomForestClassifier()

rand_forest_classifier.fit(image_data, target_data)

#config.save_model(rand_forest_classifier, 'RandomForest')


###############################################
# for validation and testing purposes
###############################################

validate = AccuracyValidation()

validate.split_validation(rand_forest_classifier, image_data, target_data, True)

validate.cross_validation(rand_forest_classifier, 3, image_data,
    target_data)

###############################################
# end of validation and testing
###############################################