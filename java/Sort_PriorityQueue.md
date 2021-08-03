## Priority Queue(우선순위 큐)
<br>

* 일반적인 큐(FIFO)와 달리 우선순위에 따라 구조를 가진다.
* 내부 구조가 minHeap으로 되어 있다.
* 시간 복잡도는 logN 

___
__Heap__
* 최솟값 또는 최댓값을 빠르게 찾아내기 위해 만들어진 완전 이진트리
* 힙의 종류는 max heap과 min heap이 있다.

<br>

선언과 데이터 추가, 삭제
```java
PriorityQueue<Integer> pq = new PriorityQueue<>();

pq.offer(1); // 큐에 1을 삽입
pq.poll(); // 큐에 있는 값을 하나 꺼내옴
```
<br>

__map과 priority큐를 이용하여 정렬하는 방법__

|key|value|
|:---:|:---:|
|a|2|
|b|2|

<br>

문제 : value의 값을 기준으로 내림차순하고 value가 같을 경우 key의 알파벳을 기준으로 정렬해야 할 때

<br>

```java
Queue<Map.Entry<String, Integer>> pq = new PriorityQueue<>((a,b)-> a.getValue()==b.getValue ? a.getKey().compareTo(b.getKey()):b.getValue-a.getValue());
```


<br>
<br>
<br>


출처

* 인프런 - 코딩테스트 전 꼭 알아야 할 개념과 문제(with 자바)