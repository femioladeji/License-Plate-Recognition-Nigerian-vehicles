from sklearn.naive_bayes import GaussianNB
from ml_config import MachineLearningConfig
from ml_validation import AccuracyValidation

config = MachineLearningConfig()

image_data, target_data = config.read_training_data(config.training_data[0])

gaussian_naive_bayes = GaussianNB()

gaussian_naive_bayes.fit(image_data, target_data)

#config.save_model(gaussian_naive_bayes, 'GaussianNB')


###############################################
# for validation and testing purposes
###############################################

validate = AccuracyValidation()

validate.split_validation(gaussian_naive_bayes, image_data, target_data, True)

validate.cross_validation(gaussian_naive_bayes, 3, image_data,
    target_data)

###############################################
# end of validation and testing
###############################################