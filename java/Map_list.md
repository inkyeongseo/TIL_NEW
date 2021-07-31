## __map -> list__

<br>

__List 컬렉션__

* 데이터를 일렬로 나열하는 구조이며 인덱스 순서로 저장된다.
* 동일한 값을 저장할 수 있으며 null값도 허용한다.
* 객체의 번지를 참조한다.
* 대표적인 클래스는 ArrayList, Vector, LinkedList이 있다.


<br>
<br>

__ArrayList__

* List컬렉션 인터페이스를 구현한 클래스이다.
* 배열과 달리 크기를 동적으로 조절할 수 있다.
```java
ArrayList<Integer> a = new ArrayList<>();
```
<br>
<br>

__Map에 있는 값을 list로 변환하는 예시__

```java
for(int key : map.keySet()){
    int topFrequent = map.get(key); // value
    if(list[topFrequent]== null){
        list[topFrequent] = new ArrayList<>();
    }
    list[topFrequent].add(key); // key
}
```
map에 있는 key값으로 value를 알아낸 뒤 list에 ArrayList를 만들어 key 값을 집어 넣는다.


<br>

<br><br>

출처

* 인프런 - 코딩테스트 전 꼭 알아야 할 개념과 문제(with 자바)
