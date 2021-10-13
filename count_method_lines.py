#!/bin/python

# Source:
# https://github.com/bbelderbos/Codesnippets/blob/master/python/countMethodLines.py
import sys

MAX_LEN = 15
PRINT_OK = False


def file2list(file_name):
    with open(file_name) as f:
        lines_list = [li.strip() for li in f.readlines()]
    return lines_list


def line_is_comment(li):
    if li.startswith("#"):
        return True
    return False


def get_method_name(li):
    return li.split("(")[0].replace("def ", "")


def end_of_method(line):
    # if empty line encounted - new method is assumed
    is_end = not line.strip()

    # TODO: KS: 29 Jun 2018: check function body indentation and
    # TODO: KS: 29 Jun 2018: see: http://code-monkey.readthedocs.io/en/latest/index.html
    return is_end


def count_method_len(lines_list):
    methods_dict = {}
    method_name = None
    for li in lines_list:
        if end_of_method(line=li):
            method_name = None
        elif line_is_comment(li):
            continue
        elif li.startswith("def "):
            method_name = get_method_name(li)
            methods_dict[method_name] = 0
        else:
            if method_name in methods_dict:
                methods_dict[method_name] += 1
    return methods_dict


def print_line(method_name, score):
    if score <= MAX_LEN:
        if PRINT_OK:
            print("v) ", end='')
            print("%-25s | %d" % (method_name, score))
    else:
        print("x) ", end='')
        print("%-25s | %d" % (method_name, score))


if __name__ == "__main__":
    nargs = len(sys.argv)
    if nargs < 2:
        sys.exit("Provide input file please")

    for file_idx in range(1, nargs):
        f_name = sys.argv[file_idx]
        print("")
        print(f"Processing: {f_name}")
        lines = file2list(f_name)
        methods = count_method_len(lines)
        for method, count in methods.items():
            print_line(method, count)
