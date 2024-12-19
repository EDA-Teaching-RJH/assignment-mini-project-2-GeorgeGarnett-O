from student_scores_lib import StudentScores  # Import your custom library

if __name__ == "__main__":
    scores = StudentScores()  # Create an instance of the class

    # Adding scores for students
    scores.add_score("Harvey Specter", 95)
    scores.add_score("Jessica Pearson", 87)
    scores.add_score("Mike Ross", 78)
    scores.add_score("Rachel Zane", 90)

    # Displaying all students and their scores
    scores.display_students()

    # Ranking students
    scores.rank_students()

    # Calculating and displaying the average for a single student
    print(f"\nAverage score for Harvey Specter: {scores.calculate_average('Harvey Specter'):.2f}")

