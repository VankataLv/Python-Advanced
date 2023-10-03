def students_credits(*data_courses):
    std_total_credits = 0
    std_courses = {}
    for course in data_courses:
        course_name, credits_course, max_points, std_points = course.split("-")
        credits_course = int(credits_course)
        max_points = int(max_points)
        std_points = int(std_points)
        cur_course_credits = credits_course * (std_points / max_points)
        std_total_credits += cur_course_credits
        std_courses[course_name] = cur_course_credits
    result = ""
    if std_total_credits >= 240:
        result += f"Diyan gets a diploma with {std_total_credits:.1f} credits.\n"
    else:
        result += f"Diyan needs {240 - std_total_credits:.1f} credits more for a diploma.\n"
    std_courses = sorted(std_courses.items(), key=lambda x: -x[1])
    for course in std_courses:
        result += f"{course[0]} - {course[1]:.1f}\n"
    return result

# print(
#     students_credits(
#         "Computer Science-12-300-250",
#         "Basic Algebra-15-400-200",
#         "Algorithms-25-500-490"
#     )
# )

# print(
#     students_credits(
#         "Discrete Maths-40-500-450",
#         "AI Development-20-400-400",
#         "Algorithms Advanced-50-700-630",
#         "Python Development-15-200-200",
#         "JavaScript Development-12-500-480",
#         "C++ Development-30-500-405",
#         "Game Engine Development-70-100-70",
#         "Mobile Development-25-250-225",
#         "QA-20-300-300",
#     )
# )

# print(
#     students_credits(
#         "Python Development-15-200-200",
#         "JavaScript Development-12-500-480",
#         "C++ Development-30-500-405",
#         "Java Development-10-300-150"
#     )
# )