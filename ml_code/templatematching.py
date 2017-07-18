from skimage.feature import match_template
from skimage.filters import threshold_otsu
from skimage.io import imread
import os.path

# characters that should be clearly examined using template matching
confusing_chars = {'2', 'Z', 'B', '8', 'D', '0', '5', 'S', 'Q', 'R', '7'}

# a dictionary that keeps track of characters that are similar to the
# confusing characters
similar_characters = {
    '2':['Z'], 'Z':['2', '7'], '8':['B'], 'B':['8', 'R'], '5':['S'], 'S':['5'],
    '0':['D', 'Q'], 'D':['0', 'Q'], 'Q':['D', '0'], '7':['Z']
}

def template_match(predicted_label, image_data, training_dir):
    """
    applies the concept of template matching to determine the
    character among the similar ones that have the highest match and
    returns the label

    Parameters:
    ------------
    predicted_label: str; the character that was predicted by the machine
        learning model
    image_data: 2D numpy array image of the character that was predicted
    training_dir: the directory for the images that will be used in matching

    Returns:
    ---------
    The label with the highest match value
    """
    image_data = image_data.reshape(20, 20)
    prediction_fraction = fraction_match(predicted_label, training_dir,
        image_data)
    highest_fraction = prediction_fraction
    highest_fraction_label = predicted_label
    similar_labels_list = similar_characters[predicted_label]

    for each_similar_label in similar_labels_list:
        match_value = fraction_match(each_similar_label, training_dir,
            image_data)
        if match_value > highest_fraction:
            highest_fraction = match_value
            highest_fraction_label = each_similar_label

    return highest_fraction_label


def fraction_match(label, training_dir, image_data):
    fraction = 0
    for i in range(10):
        image_dir = os.path.join(training_dir, label, label+'_'+str(i)+'.jpg')
        image_sample = imread(image_dir, as_grey=True)
        image_sample = image_sample < threshold_otsu(image_sample)
        match_fraction = match_template(image_data, image_sample)

        fraction += (match_fraction[0, 0] / 10)
    return fraction