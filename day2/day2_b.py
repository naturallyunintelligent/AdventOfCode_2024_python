
#input_text_file = "sample.txt"
input_text_file = "input.txt"

def load_data(input_text_file):
    with open(input_text_file) as input_file:
        data = []
        for index, line in enumerate(input_file):
            data.append(line.strip())
    return data

def list_dampner(i, L):
    return L[:i+1] + L[i+2:]

def strictly_increasing(dampener, L):
    safe_list = []
    for i, (x, y) in enumerate(zip(L, L[1:])):
        if x == y:
            dampener += 1
            if dampener > 1:
                return False, L
            dampened_list = list_dampner(i, L)
            return strictly_increasing(dampener, dampened_list)
        if x < y and (y - x) <= 3:
            safe_list.append(True)
        if x < y and (y - x) > 3:
            dampener += 1
            if dampener > 1:
                return False, L
            dampened_list = list_dampner(i, L)
            return strictly_increasing(dampener, dampened_list)
        if x > y:
            dampener += 1
            if dampener > 1:
                return False, L
            dampened_list = list_dampner(i, L)
            return strictly_increasing(dampener, dampened_list)
    if dampener > 1:
        return False, L
    return True, L

def strictly_decreasing(dampener, L):
    safe_list = []
    for i, (x, y) in enumerate(zip(L, L[1:])):
        if x == y:
            dampener += 1
            if dampener > 1:
                return False, L
            dampened_list = list_dampner(i, L)
            return strictly_decreasing(dampener, dampened_list)
        if x > y and (x - y) <= 3:
            safe_list.append(True)
        if x > y and (x - y) > 3:
            dampener += 1
            if dampener > 1:
                return False, L
            dampened_list = list_dampner(i, L)
            return strictly_decreasing(dampener, dampened_list)
        if x < y:
            dampener += 1
            if dampener > 1:
                return False, L
            dampened_list = list_dampner(i, L)
            return strictly_decreasing(dampener, dampened_list)
    if dampener > 1:
        return False, L
    return True, L

def strictly_monotonic(L):
    dampener = 0
    this_report_is_safe_inc, L = strictly_increasing(dampener, L)
    print(L)
    print(f"inc: {this_report_is_safe_inc}")
    print("__")
    if this_report_is_safe_inc == True:
        print("__________________")
        return True
    this_report_is_safe_dec, L = strictly_decreasing(dampener, L)
    print(L)
    print(f"dec: {this_report_is_safe_dec}")
    print("__")
    if this_report_is_safe_dec == True:
        print("__________________")
        return True
    print("__________________")
    return False

# def day1_a(reports):
#
#     safe_count = 0
#
#     for report in reports:
#         safe = False
#         report_list = report.split(" ")
#         report_ints = [int(x) for x in report_list]
#         safe = strictly_monotonic(report_ints)
#         if safe == True:
#             safe_count += 1
#
#     answer_a = safe_count
#     if input_text_file == "sample.txt":
#         assert answer_a == 2
#     return answer_a

def day1_b(reports):
    safe_count = 0
    debug_safe_list = []
    for report in reports:
        safe = False
        report_list = report.split(" ")
        report_ints = [int(x) for x in report_list]
        print(report_ints)
        safe = strictly_monotonic(report_ints)
        debug_safe_list.append(safe)

        if safe == True:
            safe_count += 1
    answer_b = safe_count
    print(f"day1_b {answer_b=}")
    if input_text_file == "sample.txt":
        assert answer_b == 4
    return answer_b

if __name__ == '__main__':

    data = load_data(input_text_file)

    # answer_a = day1_a(data)
    # print(f"day1_a: {answer_a=}")

    answer_b = day1_b(data)
    print(f"day1_b {answer_b=}")

    #store answer as a comment
    #a:369
    #b: