from abc import ABC, abstractmethod

class StudentAttendenceInterface(ABC):
    @classmethod
    @abstractmethod
    def get_all_attendence(cls):
        return

    @classmethod
    @abstractmethod
    def save_attendence(cls, studentAtttendence):
        pass

