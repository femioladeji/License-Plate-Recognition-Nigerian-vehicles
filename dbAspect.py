import pymysql.cursors

class DBConnection():
    def __init__(self):
        self.connection = pymysql.connect(host='localhost', user='root',
            password='', db='alpr')

    def save_alpr(self, license_plate_text, moment):
        """
        Saves the license plate text in the database table
        
        Parameters:
        -----------
        license_plate_text: str; the text on the license plate
        moment: str; the current date and time
        """
        try:
            with self.connection.cursor() as cursor:
                #insert record
                sql = "INSERT INTO alpr (plate_text, moment) VALUES(%s, %s)"
                cursor.execute(sql, (license_plate_text, moment))
            self.connection.commit()

        finally:
            pass