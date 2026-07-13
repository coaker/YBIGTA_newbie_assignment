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
- 일단 Trie부터 구현하기
- count 구현하기
- main 구현하기
"""


def count(trie: Trie, query_seq: str) -> int:
    """
    trie - 이름 그대로 trie
    query_seq - 단어 ("hello", "goodbye", "structures" 등)

    returns: query_seq의 단어를 입력하기 위해 버튼을 눌러야 하는 횟수
    """
    pointer = 0
    cnt = 0

    for element in query_seq:
        if len(trie[pointer].children) > 1 or trie[pointer].is_end:
            cnt += 1

        new_index = -1
        for child_index in trie[pointer].children:
            if trie[child_index].body == element:
                new_index = child_index
                break

        pointer = new_index

    return cnt + int(len(trie[0].children) == 1)


def main() -> None:
    """
    data: 입력 데이터 (표준 입력)
    idex: data에서 현재 처리할 위치
    results: 각 테스트 케이스의 결과를 담을 list
    """
    data = sys.stdin.read().split()
    idx = 0
    results = []

    while idx < len(data):
        n = int(data[idx])
        idx += 1

        words = data[idx:idx + n]
        idx += n

        trie: Trie= Trie()
        for word in words:
            trie.push(word)

        total = sum(count(trie, word) for word in words)
        avg = total / n
        results.append(f"{avg:.2f}")

    print("\n".join(results))


if __name__ == "__main__":
    main()