marks_list = [78, 35, 92, 40, 61]
marks_tuple = tuple(marks_list)

print("Marks list :", marks_list, "->", type(marks_list))
print("Marks tuple:", marks_tuple, "->", type(marks_tuple))

highest_mark = max(marks_list)
lowest_mark = min(marks_list)
print("Highest mark:", highest_mark)
print("Lowest mark :", lowest_mark)

passed_count = (
    (marks_list[0] >= 40)
    + (marks_list[1] >= 40)
    + (marks_list[2] >= 40)
    + (marks_list[3] >= 40)
    + (marks_list[4] >= 40)
)
print("Students who scored at least 40:", passed_count)
all_marks_valid = lowest_mark >= 0 and highest_mark <= 100
print("All marks within 0 to 100:", all_marks_valid)

marks_list[1] = 50
print("List after change :", marks_list)

try:
    marks_tuple[1] = 50
except TypeError as error:
    print("Tuple change failed:", error)
