"""
Time Complexity of Solution:
Worst case scenario occurs when all the elements are placed in a single bucket.

The overall performance would then be dominated by the algorithm used to sort each
bucket. In this case, O(n log n), because of TimSort
Average Case O(n + (n^2)/k + k), where k is the number of buckets

If k = O(n), time complexity is O(n)
"""

DEFAULT_BUCKET_SIZE = 5


def bucket_sort(my_list: list, bucket_size: int = DEFAULT_BUCKET_SIZE) -> list:
    
    if len(my_list) == 0:
        raise Exception("Please add some elements in the array.")

    min_value, max_value = (min(my_list), max(my_list))
    bucket_count = (max_value - min_value) // bucket_size + 1
    buckets = [[] for _ in range(int(bucket_count))]

    for i in range(len(my_list)):
        buckets[int((my_list[i] - min_value) // bucket_size)].append(my_list[i])

    return sorted(
        buckets[i][j] for i in range(len(buckets)) for j in range(len(buckets[i]))
    )


if __name__ == "__main__":
    assert bucket_sort([4, 5, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert bucket_sort([0, 1, -10, 15, 2, -2]) == [-10, -2, 0, 1, 2, 15]
