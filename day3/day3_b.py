import re
from operator import concat


def load_data(input_text_file):
    with open(input_text_file) as input_file:
        data = []
        for index, line in enumerate(input_file):
            data.append(line)#.strip()
    return data


def day_b(data):
    single_string_data = ""
    all_values = []
    for i, line in enumerate(data):
        single_string_data = concat(single_string_data, line)

    # find the enabled slices
    enabled_slices = find_the_enabled_slices(single_string_data)

    # for each slice, process the muls
    for slice in enabled_slices:
        all_values = all_values + process_muls(single_string_data[slice[0]:slice[1]])

    answer = sum(all_values)
    if input_text_file == "sample.txt":
        assert answer == 48
    return answer

def find_the_enabled_slices(cleaned_data):
    enablers = [0]
    enablers.extend(m.start(0) for m in re.finditer(r'do\(\)', (cleaned_data)))
    disablers = [m.end(0) for m in re.finditer(r'don\'t\(\)', (cleaned_data))]
    disablers.append(len(cleaned_data))

    enabled_slices = []
    do = True
    while len(enablers) > 1:
        if enablers[0] < disablers[0] and enablers[1] > disablers[0]:
            while enablers[1] > disablers[1]:
                disablers.pop(1)
            enabled_slices.append((enablers.pop(0), disablers.pop(0)))
        elif enablers[0] < disablers[0] and enablers[1] < disablers[0]:
            while enablers[1] < disablers[0]:
                enablers.pop(1)
    if enablers[0] < disablers[0]:
        enabled_slices.append((enablers.pop(0), disablers.pop(0)))
    assert len(enablers) == 0

    return enabled_slices

def process_muls(slice):
    valid_muls = find_muls(slice)
    values = multiply_muls(valid_muls)
    return values


def multiply_muls(valid_muls):
    values = []
    for mul in valid_muls:
        a, b = map(int, mul[4:-1].split(","))
        values.append(a * b)
    return values


def find_muls(cleaned_data):
    valid_muls = re.findall(r'mul\(\d+\,\d+\)', (cleaned_data))
    return valid_muls




if __name__ == '__main__':

    #input_text_file = "sample_b.txt"
    input_text_file = "input.txt"
    data = load_data(input_text_file)


    answer_b = day_b(data)
    print(f"day1_b {answer_b=}")

    #store answer as a comment
    #a:
    #b: