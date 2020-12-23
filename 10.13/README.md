# 백준_1260번(DFS와 BFS)

### 문제

그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

### 입력

첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

### 출력

첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.



#### 풀이

```python
from _collections import deque

N,M,V=map(int,input().split())
node=[[] for _ in range(N+1)]
visited=[0 for _ in range(N)]

for _ in range(M):
    a,b=map(int,input().split())
    node[a].append(b)
    node[b].append(a)

for i in range(1,N+1):
    node[i].sort()

def dfs(i): #노드를 방문하는 함수
    visited[i]=1
    print(i,end=' ')
    for next_node in node[i]:
        if visited[next_node]==0:
            dfs(next_node)

def bfs(i):
    visited=[0 for _ in range(N+1)]
    q=deque()
    q.appendleft(i)
    visited[i]=1

    while q: #q가 있을 때까지 루프를 돈다.
        cur=q.pop()
        print(cur,end=' ')

        for next_node in node[cur]:
            if visited[next_node]==0:
                q.append(next_node)
                visited[next_node]=1

dfs(V)
print()
bfs(V)
```

