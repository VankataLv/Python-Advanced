def gather_credits(credits_needed: int, *courses_availlable):
    my_courses = []
    my_credits = 0
    for course_data in courses_availlable:
        if credits_needed > my_credits:
            if course_data[0] not in my_courses:
                my_credits += course_data[1]
                my_courses.append(course_data[0])
    my_courses.sort()
    if credits_needed <= my_credits:
        return f"Enrollment finished! Maximum credits: {my_credits}.\n\
Courses: {', '.join(my_courses)}"
    else:
        return f"You need to enroll in more courses! You have to gather {credits_needed - my_credits} credits more."

# print(gather_credits(
#     80,
#     ("Basics", 27),
# ))

# print(gather_credits(
#     80,
#     ("Advanced", 30),
#     ("Basics", 27),
#     ("Fundamentals", 27),
# ))

# print(gather_credits(
#     60,
#     ("Basics", 27),
#     ("Fundamentals", 27),
#     ("Advanced", 30),
#     ("Web", 30)
# ))