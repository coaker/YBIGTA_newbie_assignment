from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Callable


"""
TODO:
- SegmentTree 구현하기
"""


T = TypeVar("T")
U = TypeVar("U")


class SegmentTree(Generic[T, U]):
    # 구현하세요!
    def __init__(
        self,
        arr: list[T],
        default: U,
        f_conv: Callable[[T], U],
        f_merge: Callable[[U, U], U],
    ) -> None:
        """
        arr: 원본 배열
        default: "아무것도 없을 때"의 값 (합이면 0, Pair면 Pair(0,0) 등)
        f_conv: 원본 원소(T) 하나를 집계값(U)으로 바꾸는 함수
        f_merge: 집계값 두 개를 하나로 합치는 함수 (구간 합이면 덧셈)
        """
        self.n = len(arr)
        self.default = default
        self.f_conv = f_conv
        self.f_merge = f_merge

        """size: n 이상인 가장 작은 2의 거듭제곱 (완전이진트리를 배열로 표현하려면 필요)"""
        self.size = 1
        while self.size < self.n:
            self.size *= 2

        """tree[1]이 루트, tree[size]~가 리프(맨 아래층)"""
        self.tree: list[U] = [default] * (2 * self.size)

        """리프에 원본값 채우기 (변환해서)"""
        for i, v in enumerate(arr):
            self.tree[self.size + i] = f_conv(v)

        """아래에서 위로 올라가며 부모 = 자식 둘을 merge"""
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = f_merge(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, i: int, value: T) -> None:
        """i번째(0-indexed) 원소를 value로 갱신 (point update)"""
        pos = self.size + i
        self.tree[pos] = self.f_conv(value)
        pos //= 2
        while pos >= 1:
            self.tree[pos] = self.f_merge(self.tree[2 * pos], self.tree[2 * pos + 1])
            pos //= 2

    def query(self, l: int, r: int) -> U:
        """[l, r) 구간의 집계값 반환 (0-indexed, r은 미포함)"""
        res_l, res_r = self.default, self.default
        l += self.size
        r += self.size
        while l < r:
            if l & 1:
                res_l = self.f_merge(res_l, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res_r = self.f_merge(self.tree[r], res_r)
            l //= 2
            r //= 2
        return self.f_merge(res_l, res_r)


import sys


"""
TODO:
- 일단 SegmentTree부터 구현하기
- main 구현하기
"""

MAXV = 1_000_000

def find_kth(st: SegmentTree, k: int) -> int:
    """
    st.tree 내부 구조를 직접 타고 내려가며 k번째로 작은 값(맛)을 찾음
    node=1(루트)에서 시작, 리프(node >= size)에 도달할 때까지 반복
    """
    node = 1
    while node < st.size:
        left = 2 * node
        if st.tree[left] >= k:
            # 왼쪽 서브트리에 k개 이상 있음 -> 정답이 왼쪽에 있음
            node = left
        else:
            # 왼쪽에 있는 개수만큼 k를 깎고 오른쪽으로 이동
            k -= st.tree[left]
            node = left + 1
    return node - st.size + 1  # 리프 인덱스를 실제 맛 값(1-indexed)으로 변환

def main() -> None:
    # 구현하세요!
    input = sys.stdin.readline
    n = int(input())

    counts = [0] * (MAXV + 1)          # counts[맛] = 현재 그 맛 사탕 개수
    st: SegmentTree[int, int] = SegmentTree([0] * MAXV, 0, lambda x: x, lambda a, b: a + b)

    out = []
    for _ in range(n):
        query = list(map(int, input().split()))
        if query[0] == 1:
            k = query[1]
            taste = find_kth(st, k)
            out.append(str(taste))
            counts[taste] -= 1
            st.update(taste - 1, counts[taste])   # 개수 하나 빼고 갱신
        else:
            _, b, c = query
            counts[b] += c
            st.update(b - 1, counts[b])            # 개수 c만큼 더하고 갱신

    print("\n".join(out))
    


if __name__ == "__main__":
    main()