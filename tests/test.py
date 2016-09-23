#import nose
from textclassification import TextClassification
from preprocess import PreProcess
import os.path as path

class TestTextClassification():

    @classmethod
    def setup_class(self):
        self.text_class_instance = TextClassification()

    def test_get_text(self):
        print 'Testing the get_text method'
        print 'A string should be displayed from a 2D array'
        # print "get_text([['A'], ['5'], ['D'], ['B']]) = A5DB"
        text = self.text_class_instance.get_text([['A'], ['5'], ['D'], ['B']])
        assert text == 'A5DB'

    def test_text_reconstruction(self):
        print 'Testing the text_reconstruction method'
        print 'It should re arrange the string based on the 1D array of x-axis'
        # print "text_reconstruction('DACB', [10, 1, 6, 4])"
        new_text = self.text_class_instance.text_reconstruction('DACB',
            [10, 1, 6, 4])
        assert new_text == 'ABCD'

class TestPreProcess():

    @classmethod
    def setup_class(self):
        image_path = path.join(path.dirname(path.realpath(__file__)))
        image_path = path.join(path.split(image_path)[0], 'test_images',
            'car6.jpg')
        self.pre_process = PreProcess(image_path)

    def test_threshold(self):
        print 'Testing the threshold function'
        bin_image = self.pre_process.threshold(self.pre_process.full_car_image)
        assert bin_image.shape == (548, 700)