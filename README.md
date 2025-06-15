# goit-algo-hw-04

| Sorting Algorithm | Data 10 | Data 100 | Data 1000 | Data 10,000 |
| ----------------- | ------- | -------- | --------- | ----------- |
| insertion_sort    | 0.00001 | 0.00011  | 0.01343   | 1.55158     |
| merge_sort        | 0.00004 | 0.00009  | 0.00112   | 0.01570     |
| sorted            | 0.00000 | 0.00001  | 0.00010   | 0.00118     |

**Brief conclusion on the use of the three sorting methods:**

- **`insertion_sort`** — performs well on very small datasets but becomes significantly slower as data size increases (about 100× slower than `sorted` on 10,000 elements).
- **`merge_sort`** — a stable and consistently fast algorithm, much more efficient than `insertion_sort` on larger datasets.
- **`sorted` (Python built-in)** — delivers the best performance across all data sizes due to its highly optimized implementation (Timsort). Recommended in most cases.

**Conclusion:**  
Any method works for small datasets, but for medium and large sizes, use `merge_sort` or, preferably, Python’s built-in `sorted`.
