from skimage.feature import match_template
import os.path


# template = imread("C:\\Users\\Oladeji Femi\\Documents\\programs\\python\\License-Plate-Recognition-Nigerian-vehicles-\\training_data\\train20X20\\S\\S_9.jpg", as_grey=True)

# template = template < threshold_otsu(template)

# sum = 0.0

# for i in range(9):
#     image = imread("C:\\Users\\Oladeji Femi\\Documents\\programs\\python\\License-Plate-Recognition-Nigerian-vehicles-\\training_data\\train20X20\\5\\5_"+str(i)+".jpg", as_grey=True)

#     image = image < threshold_otsu(image)

#     v = match_template(image, template)
    
#     sum += v[0, 0]

# print sum / 9

similar_characters = {
    '2':'Z', 'Z':'2', '8':'B', 'B':'8', '5':'S', 'S':'5','0':'D', 'D':'0'
}

def template_match(predicted_label, image_data, training_dir):
    prediction_fraction = fraction_match(predicted_label)
    similar_label = similar_characters[predicted_label]
    similar_label_fraction = fraction_match(similar_label)

    if similar_label_fraction > prediction_fraction:
        return similar_label_fraction

    return predicted_label

def fraction_match(label):
    fraction = 0
    for i in range(10):
        match_fraction = match_template(os.path.join(training_dir),
            label, label+'_'+str(i)+'.jpg')

        fraction += (match_fraction / 10)
    return fraction