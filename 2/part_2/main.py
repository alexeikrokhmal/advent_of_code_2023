with open("input.txt", "r") as input_file:
    input_file_data = input_file.readlines()

sum_of_powers = 0
possible_colors = ["red", "green", "blue"]

for game_string in input_file_data:
    split_game_string = game_string.split(":")
    game_id = int(split_game_string[0].split(" ")[1])
    draws = split_game_string[1].split(";")

    min_num_of_cubes_dict = {color: 0 for color in possible_colors}
    for draw in draws:
        for num_of_cubes_shown_and_color_string in draw.split(","):
            num_of_cubes_shown_and_color_list = (
                num_of_cubes_shown_and_color_string.strip().split(" ")
            )

            num_of_cubes = int(num_of_cubes_shown_and_color_list[0])
            color = num_of_cubes_shown_and_color_list[1]

            min_num_of_cubes_dict[color] = max(
                min_num_of_cubes_dict[color], num_of_cubes
            )

    power = 1
    for min_number_of_cube in min_num_of_cubes_dict.values():
        power *= min_number_of_cube

    sum_of_powers += power

print(sum_of_powers)
