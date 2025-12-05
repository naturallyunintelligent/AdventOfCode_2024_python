import re
from operator import concat


def load_data(input_text_file):
    with open(input_text_file) as input_file:
        data = []
        for index, line in enumerate(input_file):
            data.append(line)#.strip()
    return data


def day_a(data):
    values = []
    cleaned_data = ""
    for i, line in enumerate(data):
        #cleaned_line = line.strip
        # cleaned_data = f"{cleaned_data}{cleaned_line}"
        cleaned_data = concat(cleaned_data, line)
    valid_muls = re.findall('mul\(\d+\,\d+\)', (cleaned_data))
    for mul in valid_muls:
        a, b = map(int, mul[4:-1].split(","))
        values.append(a * b)
    answer_a = sum(values)
    if input_text_file == "sample.txt":
        assert answer_a == 161
    return answer_a



if __name__ == '__main__':

    #input_text_file = "sample.txt"
    input_text_file = "input.txt"
    data = load_data(input_text_file)

    answer_a = day_a(data)
    print(f"day1_a: {answer_a=}")



    #store answer as a comment
    #a:
    #b: