## NumberOfIsland

__문제설명__

주어진 2차원 배열에서 서로 연결된 섬의 개수를 찾는 문제

BFS, DFS 두 가지의 방법으로 해결할 수 있다

<br>
<br>

__BFS,DFS 공통 준비__

```java
int m,n;
m = grid.length;     //행의 개수
n = grid[0].length;  //열의 개수
int[][] dirs = {{-1,0},{1,0},{0,1},{0,-1}};
```


### BFS

__해결 방법__

1. 큐에 출발값인 (0,0)넣어 시작한다. 
2. 동서남북 4방향을 체크한다.
3. 땅이 이어질 경우 해당 좌표로 큐에 넣는다.

<br>

```java
while(!queue.isEmpty()) {
			int[] cur = queue.poll();
			
			for(int[] dir : dirs) {
				int x1 = cur[0] + dir[0];
				int y1 = cur[1] + dir[1];
			
				if(x1 >= 0 && y1 >= 0 && x1 <m && y1 < n && grid[x1][y1] == '1') {
					grid[x1][y1] = 'X';
					queue.offer(new int[] {x1,y1});
				}
			}
		}
```
<br>

1. 현재 좌표값을 cur배열에 담는다.
2. cur값에서 동서남북 4방향을 탐생하기 위해 for문을 돌린다.
3. 4가지 방향에서 조건문에 해당하면 그 좌표를 방문했으므로 방문 표시를 한다.
4. 방문한 좌표를 큐에 넣는다. 

<br>
<br>

__시간 복잡도__

O(M*N) 

:이중 for문 이지만 m,n의 길이가 다른 경우

<br>

__공간 복잡도__

O(min(m,n))

:이 문제의 경우 땅('1')인 경우가 최대값(5)인 경우가 없기 때문에 위 공간 복잡도를 가진다

:큐에 좌표값을 저장하여 계산하는 경우 O(max(m,n))또는 O(min(m,n)) 두 가지 중 하나이다.


<br>
<br>

### DFS

__해결 방법__

1. 스택에 출발값인 (0,0)넣어 시작한다. 
2. 동서남북 4방향을 체크한다.
3. 땅이 이어질 경우 해당 좌표로 스택에 넣고 재귀함수를 호출한다. 

```java
if(i < 0 || i >=m || j < 0 || j >=n|| grid[i][j] != '1') {
			return;
		}
		
		grid[i][j] = 'X';  // VISITED
		
		for(int[] dir : dirs) {
			dfs(grid, i+dir[0], j+dir[1]);
		}
```
<br>

1. 들어온 값을 조건문으로 에러체크를 한다.
2. 방문한 좌표값에 방문 표시를한다.
3. 4가지 방향으로 돌리면서 재귀함수를 호출한다.
4. 값이 없으면 bfs를 빠져나온다.
<br>
<br>

__시간 복잡도__
O(M*N) 

:이중 for문 이지만 m,n의 길이가 다른 경우

<br>

__공간 복잡도__

O(M*N)

: 최악의 경우 내부의 모든 값을 확인해야 하므로 위 공간 복잡도를 가진다.

<br>
<br>
<br>


출처

* 인프런 - 코딩테스트 전 꼭 알아야 할 개념과 문제(with 자바)
* https://www.inflearn.com/course/%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%9E%90%EB%B0%94-%EA%B0%9C%EB%85%90/dashboard