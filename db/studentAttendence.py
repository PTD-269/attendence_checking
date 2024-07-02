class StudentAttendence:
    tableName = "StudentAtttendence"
    def __init__(self, name, room, date, id=None):
        self.id = id
        self.name = name
        self.room = room
        self.date = date

