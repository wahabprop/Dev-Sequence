def digit_sum(n):
    return sum(int(d) for d in str(n))

def is_valid(val, last):
    return digit_sum(val) == 6 and (last is None or digit_sum(val - last) == 9)

def a(n_terms):
    seq = []
    n = 0
    last = None
    while len(seq) < n_terms:
        val = 9 * n + 6
        if is_valid(val, last):
            seq.append(val)
            last = val
        n += 1
    return seq
