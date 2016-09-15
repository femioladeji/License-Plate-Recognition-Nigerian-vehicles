class TextClassification:
    
    def get_text(self, machine_learning_result):
        """
        combines the text classification from the machine machine learning 
        model

        Parameters:
        -----------
        machine_learning_result: 2D array of the machine learning
        model classification 

        Returns:
        --------
        string of the license plate but not in the right positioning
        """
        plate_string = ''
        for eachPredict in machine_learning_result:
            plate_string += eachPredict[0]
            
        return plate_string
    
    def text_reconstruction(self, plate_string, position_list):
        """
        returns the plate characters in the right order by using
        the starting columns of the character region

        Parameters:
        -----------
        plate_string: str; the license plate string in scatterred manner 
        position_list: 1D array of the starting columns of the character
        region

        Returns:
        --------
        String; the correctly ordered license plate text
        """
        posListCopy = position_list[:]
        position_list.sort()
        rightplate_string = ''
        for each in position_list:
            rightplate_string += plate_string[posListCopy.index(each)]
            
        return rightplate_string