with open("input.txt", "r") as input_file:
    input_file_data = input_file.readlines()

sum_of_valid_game_ids = 0
max_cubes_dict = {"red": 12, "green": 13, "blue": 14}

for game_string in input_file_data:
    split_game_string = game_string.split(":")
    game_id = int(split_game_string[0].split(" ")[1])
    draws = split_game_string[1].split(";")

    is_game_possible = True
    for draw in draws:
        draw_dict = {color: 0 for color in max_cubes_dict.keys()}

        for num_of_cubes_shown_and_color_string in draw.split(","):
            num_of_cubes_shown_and_color_list = (
                num_of_cubes_shown_and_color_string.strip().split(" ")
            )

            num_of_cubes = int(num_of_cubes_shown_and_color_list[0])
            color = num_of_cubes_shown_and_color_list[1]

            draw_dict[color] += num_of_cubes

        for color in max_cubes_dict.keys():
            if draw_dict[color] > max_cubes_dict[color]:
                is_game_possible = False

    if is_game_possible:
        sum_of_valid_game_ids += game_id

print(sum_of_valid_game_ids)
