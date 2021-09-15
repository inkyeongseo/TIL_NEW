## QUEUE(큐)

<br>

* FIFO(First-In-First-Out) : 먼저 들어가 데이터가 먼저 나온다.

* 삭제는 front에서 삽입은 rear에서만 이루어진다.

* 중간에 있는 데이터를 파악하기 어렵다

* 순서대로 진행하는 것에 사용한다. (BFS)

<br>
<br>


```java
Queue<TreeNode> queue = new LinkedList<>();

queue.offer(root); //root값 큐에 넣기

while(!queue.isEmpty()) {
    // 큐가 비어있는지 확인하기
}

queue.poll();  // 큐 front값 꺼내기

queue.peek(); // 큐의 front값을 보여주기 , 삭제는 x

```

<br>

__ArrayList.add(int index, E e)__

<br>

```java
list.add(0,"a"); // a
list.add(0,"b"); // b,a 순서로 들어감
```
리스트에 값을 넣으면 순서대로 들어간다.

이 방법을 사용하면 원하는 인덱스 위치에 값을 넣을 수 있다.


