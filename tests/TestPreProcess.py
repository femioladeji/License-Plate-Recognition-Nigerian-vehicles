from preprocess import PreProcess
import os.path as path
from skimage.io import imread
class TestPreProcess():

    @classmethod
    def setup_class(self):
        image_path = path.join(path.dirname(path.realpath(__file__)))
        image_path = path.join(path.split(image_path)[0], 'test_images',
            'car6.jpg')
        self.image_array = imread(image_path, as_grey=True)
        self.pre_process = PreProcess(image_path)

    def test_resize_if_necessary(self):
        print 'Testing the resize function'
        resized_image = self.pre_process.resize_if_necessary(
            self.image_array)
        assert resized_image.shape == (470, 600)