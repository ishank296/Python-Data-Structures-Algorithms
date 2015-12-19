def print_subsets(sofar,rest):
    if rest == "":
        print sofar
    else:
        print_subsets(sofar+rest[0],rest[1:])
        print_subsets(sofar,rest[1:])

print_subsets("","abc")