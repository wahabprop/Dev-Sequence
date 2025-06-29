def digit_sum(n):
    return sum(int(d) for d in str(n))

def wahab_seq(n_terms):
    seq, n = [], 0
    last = None

    while len(seq) < n_terms:
        val = 9 * n + 6
        if digit_sum(val) == 6:
            if last is None or digit_sum(val - last) == 9:
                seq.append(val)
                last = val
        n += 1

    return seq

if __name__ == "__main__":
    sequence = wahab_seq(60)  # Get first 60 valid entries
    print("Dev Sequence (filtered 9n+6):")
    print(sequence)
