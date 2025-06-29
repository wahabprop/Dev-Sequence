# Dev Sequence (OEIS Draft A385438)

A mathematically constrained sequence where:
- All terms are of the form `9k + 6`
- Digit sums are exactly 6
- Consecutive gaps have digit sum 9

## Repository Guide
| Folder | Contents |
|--------|----------|
| [`/proofs`](proofs/) | Mathematical proofs |
| [`/data`](data/) | Term lists (b-file) |
| [`/scripts`](scripts/) | Python generators |

## How to Use
1. Generate terms:
   ```bash
   python3 scripts/generate_bfile.py
