courses = ["Introduction to Philosophy", "Data Structures and Algorithms", "Calculus I", "Biology I", "Physics I", "Microeconomics", "Calculus II", "Linear Algebra", "History I", "Chemistry I", "Psychology I", "Macroeconomics", "English Composition I", "Introduction to Programming", "Discrete Mathematics"]
withdrawn_course = "History I"
new_course = "Advanced Calculus"
index = courses.index(withdrawn_course)
courses[index] = new_course
print(f"\nThe course '{withdrawn_course}' has been withdrawn and replaced by '{new_course}'.")
