if course_id_input == 0:
    print("Course ID is out of range (1-15), try again.")
else:
    for course in courses:
        if course[0] == course_id_input:
            print(f"Course ID {course_id_input} is in the {course[1]} department.")
            found = True
            break
    
    if not found:
        print(f"Course ID {course_id_input} is not found.")
