from .studentAttendenceInterface import StudentAttendenceInterface
from .studentAttendence import StudentAttendence
import mysql.connector
import datetime
class StudentAttendenceCRUD(StudentAttendenceInterface):
    host = "localhost"
    user = "root"
    password = ""
    database = "attendence"

    @classmethod
    def is_attendance_exist(cls, name, room, date):
        """Checks if an attendance record exists for the given name, room, and date within a 45-minute window.

        Args:
            name (str): Name of the student.
            room (str): Room where the attendance was taken.
            date (str|datetime.datetime): Date of the attendance (can be a string or datetime object).

        Returns:
            bool: True if the attendance record exists within the window, False otherwise.
        """

        db = mysql.connector.connect(
            host=cls.host, user=cls.user, password=cls.password, database=cls.database
        )
        cursor = db.cursor()

        # Handle potential datetime object for date
        if isinstance(date, datetime.datetime):
            date = date.strftime("%Y-%m-%d")  # Convert datetime object to string format

        # Calculate the window boundaries (45 minutes before and after the given date)
        window_start = (datetime.datetime.strptime(date, "%Y-%m-%d") - datetime.timedelta(minutes=45)).strftime("%Y-%m-%d %H:%M:%S")
        window_end = (datetime.datetime.strptime(date, "%Y-%m-%d") + datetime.timedelta(minutes=45)).strftime("%Y-%m-%d %H:%M:%S")

        sql = "SELECT EXISTS(SELECT 1 FROM StudentAttendence WHERE name = %s AND room = %s AND date BETWEEN %s AND %s)"
        val = (name, room, window_start, window_end)
        cursor.execute(sql, val)

        exists = cursor.fetchone()[0]  # Get the first element from the result (boolean value)

        db.close()
        return exists


    @classmethod
    def get_all_attendence(cls) -> list[StudentAttendence]:
        db = mysql.connector.connect(
            host=cls.host,
            user=cls.user,
            password=cls.password,
            database=cls.database
        )

        cursor = db.cursor()
        cursor.execute("SELECT * FROM StudentAttendence")
        result = cursor.fetchall()
        db.close()
        objs = cls.__convert_db_return_to_objs(result)
        return objs
    @classmethod
    def save_attendence(cls, studentAtttendence: StudentAttendence):
        db = mysql.connector.connect(
            host=cls.host,
            user=cls.user,
            password=cls.password,
            database=cls.database
        )
        cursor = db.cursor()
        sql = "INSERT INTO StudentAttendence (name, room, date) VALUES (%s, %s, %s)"
        val = (studentAtttendence.name, studentAtttendence.room, studentAtttendence.date)
        cursor.execute(sql, val)
        db.commit()
        db.close()

    @classmethod
    def get_cursor(cls):
        db = mysql.connector.connect (
            host = cls.host,
            user = cls.user,
            password = cls.password,
            database = cls.database
        )

        cursor = db.cursor()
        return cursor

    @classmethod
    def __convert_db_return_to_obj(cls, singleResult):
        id = singleResult[0]
        name = singleResult[1]
        room = singleResult[2]
        date = singleResult[3]
        return StudentAttendence(id=id, name=name, room=room, date=date)
    @classmethod
    def __convert_db_return_to_objs(cls, result):
        return [cls.__convert_db_return_to_obj(singleResult) for singleResult in result]

