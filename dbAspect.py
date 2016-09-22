import pymysql.cursors

class DBConnection():
    def __init__(self):
        self.connection = pymysql.connect(host='localhost', user='root',
            password='')

        with self.connection.cursor() as cursor:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alpr")

        self.connection.commit()

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
                table_sql = "CREATE TABLE IF NOT EXISTS `alpr`.`alpr` ( `id` INT NOT NULL AUTO_INCREMENT , `plate_text` VARCHAR(15) NOT NULL , `moment` VARCHAR(30) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;"
                cursor.execute(table_sql)
                #insert record
                sql = "INSERT INTO `alpr`.`alpr` (plate_text, moment) VALUES(%s, %s)"
                cursor.execute(sql, (license_plate_text, moment))
            self.connection.commit()

        finally:
            pass