def digit_sum(n):
    return sum(int(d) for d in str(n))

def is_valid(a, prev_a):
    return digit_sum(a) == 6 and (prev_a is None or digit_sum(a - prev_a) == 9)

def generate_bfile():
    k, prev, count = 0, None, 0
    with open("../data/bfile_terms.txt", "w") as f:
        while count < 1000:  # First 1000 terms
            a = 9 * k + 6
            if is_valid(a, prev):
                f.write(f"{count + 1} {a}\n")
                prev, count = a, count + 1
            k += 1

generate_bfile()
