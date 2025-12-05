#input_text_file = "sample.txt"
input_text_file = "input.txt"

def load_data(input_text_file):
    with open(input_text_file) as input_file:
        data = []
        for index, line in enumerate(input_file):
            data.append(line.strip())
    return data


def day1_a(left_list, right_list):
    sorted_left_list = sorted(left_list)
    sorted_right_list = sorted(right_list)
    zipped_list = zip(sorted_left_list, sorted_right_list)
    list_of_differences = []
    for left, right in zipped_list:
        difference = max(left, right) - min(left, right)
        list_of_differences.append(difference)
    answer_a = sum(list_of_differences)
    if input_text_file == "sample.txt":
        assert answer_a == 11
    return answer_a

def day1_b(left_list, right_list):
    similarity_scores = []
    for value in left_list:
        count = 0
        for value_right in right_list:
            if value == value_right:
                count += 1
        similarity_scores.append(value * count)
    answer_b = sum(similarity_scores)
    if input_text_file == "sample.txt":
        assert answer_b == 31
    return answer_b

def data_loader():
    data = load_data(input_text_file)
    left_list = []
    right_list = []
    for line in data:
        left_list.append(int(line.split("  ")[0]))
        right_list.append(int(line.split("   ")[1]))
    return left_list, right_list


if __name__ == '__main__':

    left_list, right_list = data_loader()

    answer_a = day1_a(left_list, right_list)
    print(f"day1_a: {answer_a=}")

    answer_b = day1_b(left_list, right_list)
    print(f"day1_b {answer_b=}")

    #store answer as a comment
    #a:2285373
    #b:21142653