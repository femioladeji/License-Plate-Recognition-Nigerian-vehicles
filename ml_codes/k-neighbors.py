from sklearn.neighbors import KNeighborsClassifier
from ml_config import MachineLearningConfig
from ml_validation import AccuracyValidation

config = MachineLearningConfig()

image_data, target_data = config.read_training_data(config.training_data[0])

# sklearn default is 5 but I made this 3
neighbor_model = KNeighborsClassifier(n_neighbors=3)

neighbor_model.fit(image_data, target_data)

#config.save_model(neighbor_model, 'KNeighbors3')


###############################################
# for validation and testing purposes
###############################################

validate = AccuracyValidation()

validate.split_validation(neighbor_model, image_data, target_data, True)

validate.cross_validation(neighbor_model, 3, image_data,
    target_data)

###############################################
# end of validation and testing
###############################################