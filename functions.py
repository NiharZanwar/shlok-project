import pymysql


def sql_connection():
    try:
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='toor',
                                     db='school',
                                     port=int('6000'))
        return connection
    except pymysql.Error as e:
        print(e)
        return 0


# connection = sql_connection()
# cursor = connection.cursor()
#
# for i in range(0, 10):
#
#     cursor.execute("INSERT INTO `student`(`age`,`name`,`marks`) VALUES('{}','nihar','55')".format(i))
#
# connection.commit()


def add_user(name, age, marks):

    connection = sql_connection()
    cursor = connection.cursor()


    cursor.execute("INSERT INTO `student`(`age`,`name`,`marks`) VALUES('5','{}','55')".format(name))

    connection.commit()
    connection.close()


