from tabulate import tabulate

def load_data(input_text_file):
    with open(input_text_file) as input_file:
        data = []
        for index, line in enumerate(input_file):
            data.append(line.strip())
    return data


def check_all_around_for_m(i, j, data):
    directions = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    this_count = 0
    # debug_display = []
    # for x in range(len(data)):
    #     debug_display.append([])
    #     for y in range(len(data[0])):
    #         debug_display[x].append(".")
    for direction in directions:
        if i + direction[0] < len(data) and j + direction[1] < len(data[0]) and i + direction[0] >= 0 and j + direction[1] >= 0:
            if data[i + direction[0]][j + direction[1]] == "M":
                if i + (2*direction[0]) < len(data[0]) and j + (2*direction[1]) < len(data) and i + (2*direction[0]) >= 0 and j + (2*direction[1]) >= 0:
                    found_a = check_next_letter(i + (direction[0]), j + (direction[1]), direction, "A", data)
                    if found_a is True:
                        if i + (3*direction[0]) < len(data[0]) and j + (3*direction[1]) < len(data) and i + (3*direction[0]) >= 0 and j + (3*direction[1]) >= 0:
                            found_s = check_next_letter(i + (2 * direction[0]), j + (2 * direction[1]), direction, "S",
                                                        data)
                            if found_s is True:
                                this_count += 1
                                # debug_display[i][j] = data[i][j]
                                # debug_display[i + direction[0]][j + direction[1]] = data[i + direction[0]][
                                #     j + direction[1]]
                                # debug_display[i + (2 * direction[0])][j + (2 * direction[1])] = \
                                # data[i + (2 * direction[0])][j + (2 * direction[1])]
                                # debug_display[i + (3 * direction[0])][j + (3 * direction[1])] = \
                                # data[i + (3 * direction[0])][j + (3 * direction[1])]
                                # tabulated_debug = tabulate(debug_display)
                                # print(tabulated_debug)
                            else:
                                is_xmas = False
                        else:
                            is_xmas = False
                    else:
                        is_xmas = False
    return this_count

def check_next_letter(i, j, direction, letter, data):
    if i + direction[0] < len(data) and j + direction[1] < len(data[0]):
        if data[i + direction[0]][j + direction[1]] == letter:
            return True
    return False


def check_for_rest_of_word(i, j, data):
    this_count = check_all_around_for_m(i, j, data)


    return this_count

def day_a(reports):
    xmas_count = 0

    for i, row in enumerate(data):
        for j, letter in enumerate(row):
            if letter == "X":
                xmas_count += check_for_rest_of_word(i, j, data)
                print(f"xmas_count={xmas_count}")


    if input_text_file == "sample.txt":
        assert xmas_count == 18
    return xmas_count


if __name__ == '__main__':

    #input_text_file = "sample.txt"
    input_text_file = "input.txt"
    data = load_data(input_text_file)

    answer_a = day_a(data)
    print(f"day_a: {answer_a=}")


    #store answer as a comment
    #a:
    #b: