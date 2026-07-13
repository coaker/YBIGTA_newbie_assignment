from lib import Trie
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