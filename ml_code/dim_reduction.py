from sklearn.decomposition import PCA
from ml_config import MachineLearningConfig
import matplotlib.pyplot as plt

config = MachineLearningConfig()

image_data, target_data = config.read_training_data(config.training_data[0])

pca = PCA(2)

new_image_data = pca.fit_transform(image_data)

print new_image_data.shape

plt.scatter(new_image_data[:, 0], new_image_data[:, 1])
plt.show()