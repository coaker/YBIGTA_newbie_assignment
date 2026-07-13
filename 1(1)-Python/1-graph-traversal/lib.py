from __future__ import annotations
import copy
from collections import deque
from collections import defaultdict
from typing import DefaultDict, List


"""
TODO:
- __init__ 구현하기
- add_edge 구현하기
- dfs 구현하기 (재귀 또는 스택 방식 선택)
- bfs 구현하기
"""


class Graph:
    def __init__(self, n: int) -> None:
        """
        그래프 초기화
        n: 정점의 개수 (1번부터 n번까지)
        """
        self.n = n
        # 구현하세요!
        """
        정점의 개수를 intput으로 받아서 그래프를 초기화, dictionary를 이용하여 인접 리스트를 구현
        """
        self.adj : DefaultDict[int, List[int]] = defaultdict(list)

    
    def add_edge(self, u: int, v: int) -> None:
        """
        양방향 간선 추가
        """
        # 구현하세요!
        """
        dictionary를 이용하여 양방향 간선을 추가, u와 v를 서로의 인접 리스트에 추가
        """
        self.adj[u].append(v)
        self.adj[v].append(u)

    
    def dfs(self, start: int) -> list[int]:
        """
        깊이 우선 탐색 (DFS)
        
        구현 방법 선택:
        1. 재귀 방식: 함수 내부에서 재귀 함수 정의하여 구현
        2. 스택 방식: 명시적 스택을 사용하여 반복문으로 구현
        """
        """
        재귀 방식으로 DFS를 구현 visited_nodes라는 set을 만들어서 방문한 노드를 기록하고,
        result라는 output에 쓰일 list를 만들어서 방문한 노드를 기록, visit이라는 재귀 함수를
        만들어서 현재 노드를 방문하고, 인접한 노드들을 정렬하여 재귀적으로 방문
        """
        # 구현하세요!
        visited_nodes = set()
        result = []
        def visit(node: int) -> None:
            if node in visited_nodes:
                return
            visited_nodes.add(node)
            result.append(node)
            for i in sorted(self.adj[node]):
                visit(i)
        visit(start)
        return result
    
    def bfs(self, start: int) -> list[int]:
        """
        너비 우선 탐색 (BFS)
        큐를 사용하여 구현
        """
        """
        큐를 이용하여 BFS를 구현 visited_nodes라는 set을 만들어서 방문한 노드를 기록하고,
        result라는 output에 쓰일 list를 만들어서 방문한 노드를 기록, queue라는 deque를
        만들어서 시작 노드를 넣고, 큐가 빌 때까지 반복하면서 인접한 노드를 정렬하여 큐에 넣어가면서
        방문
        """
        # 구현하세요!
        visited_nodes = set()
        result = []
        queue : deque[int] = deque()
        queue.append(start)
        while queue:
            node = queue.popleft()
            if node in visited_nodes:
                continue
            visited_nodes.add(node)
            result.append(node)
            for i in sorted(self.adj[node]):
                if i not in visited_nodes:
                    queue.append(i)
        return result

    def search_and_print(self, start: int) -> None:
        """
        DFS와 BFS 결과를 출력
        """
        dfs_result = self.dfs(start)
        bfs_result = self.bfs(start)
        
        print(' '.join(map(str, dfs_result)))
        print(' '.join(map(str, bfs_result)))
