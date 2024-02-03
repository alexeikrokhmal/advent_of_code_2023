# Sample data
input_file_data = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]

# with open("input.txt", "r") as input_file:
#     input_file_data = input_file.readlines()


sum_of_values = 0
for line in input_file_data:
    for left_char in line:
        if left_char.isnumeric():
            break

    for right_char in reversed(line):
        if right_char.isnumeric():
            break

    sum_of_values += int(left_char + right_char)

print(sum_of_values)
