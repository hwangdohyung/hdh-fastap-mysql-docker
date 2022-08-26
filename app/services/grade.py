from app.models.grade import Grade
class GradeService(object):
    def __init__(self) -> None:
        self.credit = 0
        
    def set_score(self, name, kor, eng, math):
        grade = Grade(name, kor, eng, math)
        grade.set_avg()
        avg = grade.get_avg()    
    
        if avg >=90:
            self.credit = 'A'
        elif avg >=90:
            self.credit = 'B'
        elif avg >=90:
            self.credit = 'C'
        elif avg >=90:
            self.credit = 'D'
        elif avg >=90:
            self.credit = 'E'
        else:
            self.credit = 'F'       
             
             
    def get_grade(self, name, kor, eng, math):
        self.set_score(name, kor, eng, math)
        return self.credit
        name, kor, eng, math