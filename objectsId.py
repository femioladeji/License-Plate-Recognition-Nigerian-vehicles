from skimage.measure import regionprops
class ObjectIdentification:
    
    def getAllObjects(self, labelImage, borders, image):
        labelImage[borders] = -1
        cord = []
        counter=0
        
        for regions in regionprops(labelImage):
            if regions.area > 10:
                minimumRow, minimumCol, maximumRow, maximumCol = regions.bbox
                roi = image[minimumRow:maximumRow, minimumCol:maximumCol]
                if roi.shape[0]*roi.shape[1] == 0:
                    continue
                else:
                    if counter==0:
                        samples = resize(roi, (20,20))
                        cord.append(regions.bbox)
                        counter+=1
                    elif counter==1:
                        roismall = resize(roi, (20,20))
                        samples = np.concatenate((samples[None,:,:], roismall[None,:,:]), axis=0)
                        cord.append(regions.bbox)
                        counter+=1
                    else:
                        roismall = resize(roi, (20,20))
                        samples = np.concatenate((samples[:,:,:], roismall[None,:,:]), axis=0)
                        cord.append(regions.bbox)
        self.candidates = {
                    'fullscale': samples,          
                    'flattened': samples.reshape((samples.shape[0], -1)),
                    'coordinates': np.array(cord)
                    }
                    
        print 'Images After Contour Detection'
        print 'Fullscale: ', self.candidates['fullscale'].shape
        print 'Flattened: ', self.candidates['flattened'].shape
        print 'Contour Coordinates: ', self.candidates['coordinates'].shape
        print '============================================================'
        
        return self.candidates
    
    def plot_to_check(self, what_to_plot, title):
        """
        plots images at several steps of the whole pipeline, just to check output.
        what_to_plot is the name of the dictionary to be plotted
        """
        n_images = what_to_plot['fullscale'].shape[0]
        
        fig = plt.figure(figsize=(12, 12))

        if n_images <=100:
            if n_images < 100:
                total = range(n_images)
            elif n_images == 100:
                total = range(100)
           
            for i in total:
                ax = fig.add_subplot(10, 10, i + 1, xticks=[], yticks=[])
                ax.imshow(what_to_plot['fullscale'][i], cmap="Greys_r")  
                if 'predicted_char' in what_to_plot:
                    ax.text(-6, 8, str(what_to_plot['predicted_char'][i]), fontsize=22, color='red')
            plt.suptitle(title, fontsize=20)
            plt.show()  
        else:
            total = list(np.random.choice(n_images, 100)) 
            for i, j in enumerate(total):
                ax = fig.add_subplot(10, 10, i + 1, xticks=[], yticks=[])
                ax.imshow(what_to_plot['fullscale'][j], cmap="Greys_r")  
                if 'predicted_char' in what_to_plot:
                    ax.text(-6, 8, str(what_to_plot['predicted_char'][j]), fontsize=22, color='red')
            plt.suptitle(title, fontsize=20)
            plt.show() 