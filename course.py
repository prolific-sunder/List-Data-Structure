''' Course Class for Project 4 of CS 2420 '''

class Course:
    ''' Course object '''
    def __init__(self, number = 0, name = "", credit_hour = 0.0, grade = 0.0):
        if not isinstance(number, int) or (not(number >= 0)):
            raise ValueError("Course number must be an integer and greater than 0")
            
        if not isinstance(name, str):
            raise ValueError("Course name must be a string")
            
        if not isinstance(credit_hour, float) or credit_hour < 0:
            raise ValueError("Credit hours must be a float")
            
        if not isinstance(grade, float) or grade < 0:
            raise ValueError("Grade must be a float and not negative") 
        self._number = number
        self._name = name
        self._credit_hr = credit_hour
        self._grade = grade

    def number(self):
        return int(self._number)
    
    def name(self):
        return f"{self._name}"
    
    def credit_hr(self):
        return float(self._credit_hr)
    
    def grade(self):
        return float(self._grade)
  
    def __eq__(self, other):
        cnumb = other
        if isinstance(other, Course):
            cnumb = other.number()
        return self.number() == cnumb
        
    def __ne__(self, other):
        cnumb = other
        if isinstance(other, Course):
            cnumb = other.number()
        return self.number() != cnumb
        
    def __lt__(self, other):
        cnumb = other
        if isinstance(other, Course):
            cnumb = other.number()
        return self.number() < cnumb
        
    def __gt__(self, other):
        cnumb = other
        if isinstance(other, Course):
            cnumb = other.number()
        return self.number() > cnumb
        
    def __le__(self, other):
        cnumb = other
        if isinstance(other, Course):
            cnumb = other.number()
        return self.number() <= cnumb  
        
    def __ge__(self, other):
        cnumb = other
        if isinstance(other, Course):
            cnumb = other.number()
        return self.number() >= cnumb
        
    def __str__(self):
        return f"cs{self._number} {self._name} Grade: {self.grade()} Credit Hours: {self._credit_hr}"
    
