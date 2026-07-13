from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Iterable


"""
TODO:
- Trie.push 구현하기
- (필요할 경우) Trie에 추가 method 구현하기
"""


T = TypeVar("T")


@dataclass
class TrieNode(Generic[T]):
    body: Optional[T] = None
    children: list[int] = field(default_factory=lambda: [])
    is_end: bool = False


class Trie(list[TrieNode[T]]):
    def __init__(self) -> None:
        super().__init__()
        self.append(TrieNode(body=None))

    def push(self, seq: Iterable[T]) -> None:
        """
        seq: T의 열 (list[int]일 수도 있고 str일 수도 있고 등등...)

        action: trie에 seq을 저장하기
        """
        # 구현하세요!
        """
        root node(0번 index)부터 시작해서 input parameter로 받은 seq의 각 element를 
        순회하면서 current node의 chlildren 중에서 해당 element를 body로 가진 node가
        있는지 확인하고, 있으면 그 node로 이동하고, 없으면 새 node를 만들어서 current node
        의 children에 추가하고, 새 node로 이동한다. 
        """
        current = 0
        for i in seq:
            found = False
            for child_index in self[current].children:
                if self[child_index].body == i:
                    current = child_index
                    break
            else:
                new_node = TrieNode(body=i)
                self.append(new_node)
                self[current].children.append(len(self) - 1)
                current = len(self) - 1
        self[current].is_end = True












import sys


"""
TODO:
- 일단 lib.py의 Trie Class부터 구현하기
- main 구현하기

힌트: 한 글자짜리 자료에도 그냥 str을 쓰기에는 메모리가 아깝다...
"""
MOD = 10**9 + 7

def main() -> None:
    """
    data를 통해서 trie를 만들고, 각 node의 자식 수를 통해서 경우의 수를 계산한다.
    """
    data = sys.stdin.read().split()
    n = int(data[0])
    names = data[1:1 + n]

    trie: Trie = Trie()
    for name in names:
        seq = [ord(c) - ord('A') for c in name]   # 대문자라 'A' 기준
        trie.push(seq)

    # 0! ~ 26! 미리 계산 (자식 수는 알파벳 26개가 최대이므로 이 정도면 충분)
    factorial = [1] * 27
    for i in range(1, 27):
        factorial[i] = (factorial[i - 1] * i) % MOD

    answer = 1
    for node in trie:
        k = len(node.children)
        answer = (answer * factorial[k]) % MOD

    print(answer)


if __name__ == "__main__":
    main()