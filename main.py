import sys
from collections import Counter, defaultdict, deque  # pylint: disable=unused-import
from heapq import heappop, heappush  # pylint: disable=unused-import
from bisect import bisect_left, bisect_right  # pylint: disable=unused-import

input = sys.stdin.readline

def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    print(sum(a))


if __name__ == "__main__":
    main()