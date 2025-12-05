from tabulate import tabulate

def load_data(input_text_file):
    with open(input_text_file) as input_file:
        data = []
        for index, line in enumerate(input_file):
            data.append(line.strip())
    return data


def check_for_x_mas(i, j, data):
    direction = (1,1)
    other_direction = (-1, 1)
    this_count = 0
    # debug_display = []
    # for x in range(len(data)):
    #     debug_display.append([])
    #     for y in range(len(data[0])):
    #         debug_display[x].append(".")
    if i + direction[0] < len(data) and j + direction[1] < len(data[0]) and i + direction[0] >= 0 and j + direction[
        1] >= 0 and i - direction[0] < len(data) and j - direction[1] < len(data[0]) and i - direction[0] >= 0 and j - direction[
        1] >= 0 and i + other_direction[0] < len(data) and j + other_direction[1] < len(data[0]) and i + other_direction[0] >= 0 and j + other_direction[
        1] >= 0 and i - other_direction[0] < len(data) and j - other_direction[1] < len(data[0]) and i - other_direction[0] >= 0 and j - other_direction[
        1] >= 0:
        letter_1 = data[i + direction[0]][j + direction[1]]
        letter_3 = data[i - direction[0]][j - direction[1]]
        word_1 = letter_1 + data[i][j] + letter_3
        if word_1 in ["MAS", "SAM"]:
            letter_5 = data[i + other_direction[0]][j + other_direction[1]]
            letter_7 = data[i - other_direction[0]][j - other_direction[1]]
            word_2 = letter_5 + data[i][j] + letter_7
            if word_2 in ["MAS", "SAM"]:
                this_count += 1

                # debug_display[i][j] = data[i][j]
                # debug_display[i + direction[0]][j + direction[1]] = letter_1
                # debug_display[i - direction[0]][j - direction[1]] = letter_3
                # debug_display[i + other_direction[0]][j + other_direction[1]] = letter_5
                # debug_display[i - other_direction[0]][j - other_direction[1]] = letter_7
                #
                # tabulated_debug = tabulate(debug_display)
                # print(tabulated_debug)

    return this_count


def day_b(reports):
    x_mas_count = 0

    for i, row in enumerate(data):
        for j, letter in enumerate(row):
            if letter == "A":
                x_mas_count += check_for_x_mas(i, j, data)
                print(f"xmas_count={x_mas_count}")


    if input_text_file == "sample.txt":
        assert x_mas_count == 9
    return x_mas_count


if __name__ == '__main__':

    #input_text_file = "sample.txt"
    input_text_file = "input.txt"
    data = load_data(input_text_file)

    answer_b = day_b(data)
    print(f"day_b: {answer_b=}")


    #store answer as a comment
    #a:
    #b: