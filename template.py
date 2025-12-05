

def load_data(input_text_file):
    with open(input_text_file) as input_file:
        data = []
        for index, line in enumerate(input_file):
            data.append(line.strip())
    return data


def day(reports):

    answer = ""
    if input_text_file == "sample.txt":
        assert answer == 42
    return answer


if __name__ == '__main__':

    input_text_file = "sample.txt"
    # input_text_file = "input.txt"
    data = load_data(input_text_file)

    answer = day(data)
    print(f"day: {answer=}")


    #store answer as a comment
    #a:
    #b: