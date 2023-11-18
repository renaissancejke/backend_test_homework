# номер успешной посылки: 97854199

from typing import List

weights = list(map(int, input().split()))
limit = int(input())


def main(weights: List[int], limit: int) -> int:
    if min(weights) >= limit:
        return len(weights)

    weights.sort()
    count = 0
    left, right = 0, len(weights) - 1

    while left <= right:
        if weights[left] + weights[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        count += 1

    return count


print(main(weights, limit))
