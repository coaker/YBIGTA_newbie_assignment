from lib import Trie
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