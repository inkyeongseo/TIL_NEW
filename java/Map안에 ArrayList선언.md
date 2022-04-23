## Map안에 ArrayList 선언하기

<br>

아래와 같이 하나의 키 값에 여러개의 value들을 선언하고 싶을 때 사용한다.

|||
|------|---|
|KEY|VALUE|
|A|1,2,3|
|B|6,8|
|B|2,3,6|

<br>

__Map안에 ArrayList를 선언__

```java
HashMap<String, ArrayList<Integer>> hashMap = new HashMap<>();
.
.
.
ArrayList<Integer> arr = hashMap.getOrDefault(key, new ArrayList<Integer>());
arr.add(value);
hashMap.put(key, arr);
```
(프로그래머스 level2 순위검색 문제 풀이 중)

1) hashmap안에 타입을 arraylist로 지정한다.
2) hashmap에 찾는 키 값이 없다면 arraylist를 생성한다.<br>있다면 원래 list에 값 추가
3) arraylist에 값을 넣어준다
4) hashmap에 key와 value(arraylist)를 넣어준다.



