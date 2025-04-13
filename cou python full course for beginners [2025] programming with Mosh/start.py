course = "python programming"
print(course.strip())
print(course[0:3])  # pyt
# rstrip
print(course.rstrip())  # python programming
# find
print(course.find("Beginners"))  # 7
print(course.find("Beginnerss"))  # -1
# replace
print(course.replace("p", "j"))  # jython programming
print("pro" in course)  # True
print("swift" not in course)  # False
