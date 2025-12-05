import re


def load_data(input_text_file):
    with open(input_text_file) as input_file:
    return [line.strip() for line in input_file]


def day_a(data):
    rules = [line for line in data if re.match("\d\d|\d\d", line)]
    updates = [line for line in data if re.match("(\d\d,)+", line)]

    valid_middle_page_numbers = []
    for update in updates:
        for rule in rules:
            if insert_rule_logic_here in update:
                break
        valid_middle_page_numbers.append(update[len(update)/2]) # prob need use of modulo to make sure it's an int


    answer_a = ""
    if input_text_file == "sample.txt":
        assert answer_a == 143
    return answer_a


if __name__ == '__main__':

    input_text_file = "sample.txt"
    # input_text_file = "input.txt"
    data = load_data(input_text_file)

    answer_a = day_a(data)
    print(f"day_a: {answer_a=}")


    #store answer as a comment
    #a:
    #b: