import re  # Importing the `re` module for regular expression matching

class StudentScores:
    def __init__(self):
        """
        Initialize the class with an empty dictionary to store students and their scores.
        """
        self.students = {}  # A dictionary to store student names and their respective scores

    def validate_name(self, name):
        """
        Validate a student's name using a regular expression.
        - Only allows letters, spaces, hyphens, and apostrophes.
        - Example: "Harvey Specter", "Jessica Pearson" -> valid.
        """
        # Regular expression to match a valid name format (letters, hyphens, apostrophes)
        return bool(re.match(r"^[a-zA-Z]+(['-][a-zA-Z]+)*$", name))

    def add_score(self, name, score):
        """
        Adds a test score for a student.
        - Validates the name and ensures the score is between 0 and 100.
        - If the student doesn't already exist in the dictionary, it adds them.
        """
        # Validate name using regular expression
        if not self.validate_name(name):
            raise ValueError(f"Invalid name: {name}")  # Raise error for invalid name
        
        # Ensure score is between 0 and 100
        if not (0 <= score <= 100):
            raise ValueError(f"Invalid score: {score}")  # Raise error for invalid score
        
        # Add score to the student's list, if the student doesn't exist, add them with an empty list
        self.students.setdefault(name, []).append(score)

    def calculate_average(self, name):
        """
        Calculate the average score for a student.
        - If the student has no scores, raises an error.
        - Returns the average of the student's scores.
        """
        # Check if the student exists and has scores
        if name not in self.students or not self.students[name]:
            raise ValueError(f"No scores for {name}")  # Raise error if no scores
        
        # Calculate and return the average score of the student
        return sum(self.students[name]) / len(self.students[name])

    def rank_students(self):
        """
        Rank students by their average score in descending order.
        - Returns a sorted list of tuples: [(name, average_score), ...].
        """
        # Create a sorted list of students based on their average score, sorted in descending order
        ranked_students = sorted(
            ((name, self.calculate_average(name)) for name in self.students),  # (name, average) pairs
            key=lambda x: x[1],  # Sort by the average score (second element of the tuple)
            reverse=True  # Sort in descending order (highest average first)
        )

        # Print ranked students with their rank
        print("\nRanked Students:")
        for rank, (name, avg) in enumerate(ranked_students, 1):  # Enumerate to display rank
            print(f"{rank}. {name}: {avg:.2f}")  # Print rank, name, and average score

    def display_students(self):
        """
        Display each student's name and their scores.
        """
        print("\nStudents and their scores:")
        for name, scores in self.students.items():  # Loop through all students and their scores
            print(f"{name}: {scores}")  # Print each student's name and list of scores

