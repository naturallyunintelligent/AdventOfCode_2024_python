

def load_data(input_text_file):
    with open(input_text_file) as input_file:
        return [line.strip() for line in input_file]


def day_a(data):
    answer_a = ""
    if input_text_file == "sample.txt":
        assert answer_a == 42
    return answer_a

def day_b(data):

    answer_b = ""
    if input_text_file == "sample.txt":
        assert answer_b == 42
    return answer_b


if __name__ == '__main__':

    input_text_file = "sample.txt"
    # input_text_file = "input.txt"
    data = load_data(input_text_file)

    answer_a = day_a(data)
    print(f"day_a: {answer_a=}")

    answer_b = day_b(data)
    print(f"day_b {answer_b=}")

    #store answer as a comment
    #a:
    #b: