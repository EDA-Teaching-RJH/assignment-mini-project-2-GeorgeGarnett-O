 import re 

class studentscores 

    def_init_(self):

    self.students = {}

def validate_name(self,name):

    """
    validate a students name using a regular expression .

    -only allow letters,spaces,hyphens,and apostrophes
    
    -example: "harvely specter",jessica pearson" -> valid.

    """

    return bool(re.match(r"^[a-zA-Z]+(['-][a-zA-Z]+)*$"),name))

    def add_score(self,name,score):

        """
        adds a test score for a student.
        -validate the name and esures the score is between 0 and 100.
        -if the student doesnt already exist in the dictionary,it adds them.
        """ 
        if not self.validate_name(name):
            raise value ValueError(f"invalid name: {name}")
        if not (0 <= score <= 100):
            raise ValueError(f"invalid score: {score}")
        self.student.setdefault(name, []).append(score)

    def calculate_average(self,name)


    """"
    calucate the average score for students 
    -if the student has no scores,raises an error.
    -returns the average of the students scores.
    """

    if name not in self.students or not self.students[name]:
        raise ValueError(f"no scores for {name}")

    return sum(self.students[name]) / len(self.students[name])

def rank_students(self):

""" 
rank students by their avarage score in decending order.
-returns a sorted list of tuples: [(names,avarage_score),...].
"""

ranked_students = sorted(((name,self.calculate_avarage)name)) for name in self.students),
key=lambda x:[1],
reverse=True
    )
print("\nranked students:")
for rank, (name,avg) in enumerate(ranked_students,1):
    print(f"{rank}.{name}: {avg:2f}")

def display_students(self):
"""
display each students and their scores.
""" 
print("\nstudents and their scores:")

for name,scores in self.students.items():

print(f"{name}:{score}")

