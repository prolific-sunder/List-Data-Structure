from slist import SList
from course import Course

def calculate_gpa(courseList):
    sumGrades = 0
    credits = 0
    for course in courseList:
        sumGrades += course.grade() * course.credit_hr()
        credits += course.credit_hr()
    if credits == 0:
        return 0
    return sumGrades / credits

def is_sorted(lyst):
    for i in range(0, lyst.size()  - 1):
        if lyst[i] > lyst[i + 1]:
            return False
    return True

def main():
    CS2370 = Course(2370, "something", 3.0, 3.72)

if __name__ == "__main__":
    main()
