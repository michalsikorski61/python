# set don't allow duplicates
# set is unordered
# set is mutable
# set is iterable
grades = {1, 2, 3, 4, 5, 5, 5, 5, 5, 5}
grades_list = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]
print(grades_list)
grades_set = set(grades_list)
print(grades_set)

print('-----------------')
marks_grades = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]
anne_grades = [1,2,1,2,3,1,1,2,2,2]
# grades that are in both lists
marek_set = set(marks_grades)
anne_set = set(anne_grades)
print(marek_set.intersection(anne_set)) # {1, 2, 3} # grades that are the same in both lists
print(marek_set.union(anne_set)) # {1, 2, 3, 4, 5} # grades that are in both lists
print(marek_set.difference(anne_set)) # {4, 5} # grades that are in first list but not in second list
print(anne_set.difference(marek_set)) # {3} # grades that are in second list but not in first list

