from sklearn.svm import SVC
from ml_config import MachineLearningConfig
from ml_validation import AccuracyValidation

config = MachineLearningConfig()

image_data, target_data = config.read_training_data(config.training_data[0])

# kernel can be linear, rbf e.t.c
svc_model = SVC(kernel='linear', probability=True)

svc_model.fit(image_data, target_data)

#config.save_model(svc_model, 'SVC_model')

###############################################
# for validation and testing purposes
###############################################

validate = AccuracyValidation()

validate.split_validation(svc_model, image_data, target_data, True)

validate.cross_validation(svc_model, 3, image_data,
    target_data)

###############################################
# end of validation and testing
###############################################