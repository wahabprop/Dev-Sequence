🔢 Dev Sequence (OEIS Draft A385438)

This repository contains the logic and generation code for a unique numerical sequence — the Dev Sequence — currently submitted to OEIS.
📌 Definition

Dev Sequence:
Numbers of the form 9n + 6 where:

    The digit sum of each number is exactly 6, and

    The digit sum of the gap between consecutive terms is exactly 9.

✅ Example Terms:

6, 15, 24, 33, 42, 51, 60, 114, 123, 132, 141, ...

📐 Mathematical Filters

    The sequence begins with 9×0 + 6 = 6.

    Every next number must have:

        digit_sum(n) == 6

        digit_sum(n - previous_valid) == 9

This creates non-continuous, digit-controlled patterns unlike the original A017233.
🧠 Why It Matters

    🔢 Filtered Subset of A017233 using symbolic logic

    🔁 Stops and resumes based on internal constraints

    🔍 Explores digit-root meta-structure, rarely seen in OEIS sequences

    🔒 Self-limiting: halts naturally when conditions break

    📊 A candidate for advanced exploration in symbolic systems or number theory

📁 File Overview

    dev_sequence.py: Python script that generates the Dev Sequence

    README.md: This documentation

🧪 Run It

# Run the Python code to get first N terms
from dev_sequence import dev_sequence
print(dev_sequence(100))

🌐 OEIS Draft

Submitted to OEIS:
🔗 OEIS A385438 Draft
✍️ Author

Abdul Wahab Khan
GitHub: @wahabprop
