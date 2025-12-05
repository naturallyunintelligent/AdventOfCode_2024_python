
input_text_file = "sample.txt"
#input_text_file = "input.txt"

def load_data(input_text_file):
    with open(input_text_file) as input_file:
        data = []
        for index, line in enumerate(input_file):
            data.append(line.strip())
    return data

def list_dampner():
    return

def undo_dampener():
    return

def strictly_increasing(dampener, L):
    safe_list = []
    for i, (x, y) in enumerate(zip(L, L[1:])):
        if x == y:
            dampener += 1
            if dampener > 1:
                return False, L
            dampened_list = list_dampner(i, L)
            return strictly_increasing(dampener, final_report)
        if x < y and (y - x) <= 3:
            safe_list.append(True)
        if x < y and (y - x) > 3:
            dampener += 1
            if dampener > 1:
                return False, L
            dampened_list = list_dampner(i, L)
            return strictly_increasing(dampener, final_report)
        if x > y:
            dampener += 1
            if dampener > 1:
                return False, L
            dampened_list = list_dampner(i, L)
            return strictly_increasing(dampener, final_report)
    if dampener > 1:
        return False, L
    return True, L

def strictly_decreasing(dampener, L):
    safe_list = []
    final_report = L
    for i, (x, y) in enumerate(zip(L, L[1:])):
        if x == y:
            dampener += 1
            if dampener > 1:
                return False, final_report
            final_report = list_dampner(i, L)
            return strictly_decreasing(dampener, final_report)
        if x > y and (x - y) <= 3:
            safe_list.append(True)
        if x > y and (x - y) > 3:
            dampener += 1
            if dampener > 1:
                return False, final_report
            final_report = list_dampner(i, L)
            return strictly_decreasing(dampener, final_report)
        if x < y:
            dampener += 1
            if dampener > 1:
                return False, final_report
            final_report = list_dampner(i, L)
            return strictly_decreasing(dampener, final_report)
    if dampener > 1:
        return False, final_report
    return True, final_report

def strictly_monotonic(L):
    dampener = 0
    this_report_is_safe_inc, final_report = strictly_increasing(dampener, L)
    print(L)
    print(f"inc: {this_report_is_safe_inc}")
    print("__")
    if this_report_is_safe_inc == True:
        print("__________________")
        return True, final_report
    this_report_is_safe_dec, final_report = strictly_decreasing(dampener, L)
    print(L)
    print(f"dec: {this_report_is_safe_dec}")
    print("__")
    if this_report_is_safe_dec == True:
        print("__________________")
        return True, final_report
    print("__________________")
    return False, final_report


def day1_b(reports):
    safe_count, debug_safe_list,  = count_safe_reports(reports)

    answer_b = safe_count
    print(f"day1_b {answer_b=}")
    if input_text_file == "sample.txt":
        assert answer_b == 4
    return answer_b


def count_safe_reports(debug_safe_list, reports, safe_count):
    safe_count = 0
    debug_safe_list = []
    final_reports = []

    for report in reports:
        safe = False
        report_list = report.split(" ")
        report_ints = [int(x) for x in report_list]
        print(report_ints)
        safe, final_report = strictly_monotonic(report_ints)
        debug_safe_list.append(safe)
        final_reports.append(final_report)
        if safe == True:
            safe_count += 1

    return safe_count, debug_safe_list, final_reports


if __name__ == '__main__':

    data = load_data(input_text_file)

    # answer_a = day1_a(data)
    # print(f"day1_a: {answer_a=}")

    answer_b = day1_b(data)
    print(f"day1_b {answer_b=}")

    #store answer as a comment
    #a:369
    #b:

    # Additional test case:
    # 15 12 11 9 6 4