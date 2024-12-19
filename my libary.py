import re

class StudentScores:
    def __init__(self):
        """Initialize the class with an empty dictionary to store students and their scores."""
        self.students = {}

    def validate_name(self, name):
        """
        Validate a student's name using a regular expression.
        - Only allows letters, spaces, hyphens, and apostrophes.
        """
        return bool(re.match(r"^[a-zA-Z]+(['-][a-zA-Z]+)*$", name))

    def add_score(self, name, score):
        """
        Adds a test score for a student.
        - Validates the name and ensures the score is between 0 and 100.
        - If the student doesn't exist in the dictionary, it adds them.
        """
        if not self.validate_name(name):
            raise ValueError(f"Invalid name: {name}")
        if not (0 <= score <= 100):
            raise ValueError(f"Invalid score: {score}")
        self.students.setdefault(name, []).append(score)

    def calculate_average(self, name):
        """
        Calculate the average score for a student.
        - If the student has no scores, raises an error.
        - Returns the average of the student's scores.
        """
        if name not in self.students or not self.students[name]:
            raise ValueError(f"No scores for {name}")
        return sum(self.students[name]) / len(self.students[name])

    def rank_students(self):
        """
        Rank students by their average score in descending order.
        - Returns a sorted list of tuples: [(name, average_score), ...].
        """
        ranked_students = sorted(
            ((name, self.calculate_average(name)) for name in self.students),
            key=lambda x: x[1],  # Sort by average score
            reverse=True         # Descending order
        )
        print("\nRanked Students:")
        for rank, (name, avg) in enumerate(ranked_students, 1):
            print(f"{rank}. {name}: {avg:.2f}")

    def display_students(self):
        """
        Display each student's name and their scores.
        """
        print("\nStudents and Their Scores:")
        for name, scores in self.students.items():
            print(f"{name}: {scores}")
            