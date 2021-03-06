## BFS - Breadth First Search(너비 우선 탐색)

* 루트 노드에서 근처에 있는 것부터 찾는 알고리즘

* 다익스트라 알고리즘이 BFS에 해당한다.

* 구현하기 위해 __큐__ 를 이용하며 즉 FIFO 선입선출로 탐색한다.

* 출발 노드부터 목표 노드까지의 최단 거리를 보장한다.
* 경로가 늘어가면 탐색해야하는 가지가 급격히 증가해 많은 기억 공간이 필요하다.


<br>

## DFS - Depth First Search(깊이 우선 탐색)
* 루트노드에서 시작하여 다음 분기로 넘어가기 전 해당 분기를 완벽하게 탐색하는 알고리즘
* 스택이나 재귀함수로 구현할 수 있다.

* 깊이 우선순위 탐색, 체그, 장기가 DFS에 해당한다.
* BFS보다 구현이 간단하다.
* 현재 경로에 있는 노드만 기억하면 되므로 많은 기억 공간이 필요하지 않다.
* 구한 해가 최단 거리가 아닐 수 있다.
* 노드에 방문하였는지 여부를 꼭 검사해야 하며 검사하지 않으면 무한루프에 빠질 수 있다.

