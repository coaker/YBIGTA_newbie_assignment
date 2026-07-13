from lib import SegmentTree
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