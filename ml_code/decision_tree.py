from sklearn.tree import DecisionTreeClassifier
from ml_config import MachineLearningConfig
from ml_validation import AccuracyValidation

config = MachineLearningConfig()

image_data, target_data = config.read_training_data(config.training_data[0])

tree_classifier = DecisionTreeClassifier()

tree_classifier.fit(image_data, target_data)

#config.save_model(tree_classifier, 'Tree')


###############################################
# for validation and testing purposes
###############################################

validate = AccuracyValidation()

validate.split_validation(tree_classifier, image_data, target_data, True)

validate.cross_validation(tree_classifier, 3, image_data,
    target_data)

###############################################
# end of validation and testing
###############################################