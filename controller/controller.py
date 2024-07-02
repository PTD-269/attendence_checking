from db.studentAttendence import StudentAttendence
from db.studentAttendenceCRUD import StudentAttendenceCRUD
from model.inference import detect
import datetime

rooms = ["P37","P38", "P39"]

class AttendenceController:
    @staticmethod
    def get_all_attendence():
        studentAttendences = StudentAttendenceCRUD.get_all_attendence()
        return [s.__dict__ for s in studentAttendences]


    def __save_attendence(cls, name, room, date):
        if not cls.__isRoomValid(room):
            return
        if not cls.__isDateValid(date):
            return
        if not cls.__isNameValid(name):
            return
        
         # Check if attendance already exists in database
        if StudentAttendenceCRUD.is_attendance_exist(name=name, room=room, date=date):
            print(f"Attendance for {name} in room {room} on {date} already exists. Skipping insertion.")
            return
        studentAttendences = StudentAttendence(name=name, room=room, date=date)
        StudentAttendenceCRUD.save_attendence(studentAttendences)
        print("Added")

    @staticmethod
    def __isNameValid(name):
        return True

    @staticmethod
    def __isRoomValid(room):
        return True

    @staticmethod
    def __isDateValid(date):
        return True

    @classmethod
    def detect_img(cls, img, room="Hi", date=datetime.datetime(1999,9,26,12,30,22)):
        obj = detect(img=img)
        name = obj['name']
        cls.__save_attendence(cls, name=name, room=room, date=date)
