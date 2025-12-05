#input_text_file = "sample.txt"
input_text_file = "input.txt"

def load_data(input_text_file):
    with open(input_text_file) as input_file:
        data = []
        for index, line in enumerate(input_file):
            data.append(line.strip())
    return data

# def strictly_increasing(L):
#     return all(x<y for x, y in zip(L, L[1:]))

# def strictly_decreasing(L):
#     return all(x>y for x, y in zip(L, L[1:]))

def strictly_increasing(L):
    mylist = []
    dampener = 0
    for x, y in zip(L, L[1:]):
        if x < y and (y - x) <= 3:
            mylist.append(True)
        if x < y and (y - x) > 3:
            return False
        if x == y:
            return False
        if x > y:
            return False
    return True

def strictly_decreasing(L):
    mylist = []
    dampener = 0
    for x, y in zip(L, L[1:]):
        if x > y and (x - y) <= 3:
            mylist.append(True)
        if x > y and (x - y) > 3:
            return False
        if x == y:
            return False
        if x < y:
            return False
    return True

def strictly_monotonic(L):
    return strictly_increasing(L) or strictly_decreasing(L)


def day1_b(reports):

    safe_count = 0

    for report in reports:
        safe = False
        report_list = report.split(" ")
        report_ints = [int(x) for x in report_list]
        safe = strictly_monotonic(report_ints)
        if safe == True:
            safe_count += 1
        if safe == False:
            for i, level in enumerate(report_ints):
                new_list = report_ints.copy()
                del new_list[i]
                new_safe = strictly_monotonic(new_list)
                if new_safe == True:
                    safe_count += 1
                    break

    answer_b = safe_count
    if input_text_file == "sample.txt":
        assert answer_b == 2
    return answer_b


def data_loader():
    data = load_data(input_text_file)
    return data

if __name__ == '__main__':

    data = data_loader()

    # answer_a = day1_a(data)
    # print(f"day1_a: {answer_a=}")

    answer_b = day1_b(data)
    print(f"day1_b {answer_b=}")

    #store answer as a comment
    #a:369
    #b: