# Map

key값과 value값을 대응시켜 나타내는 자료형이다.

key값을 알면 value를 알 수 있기 때문에 시간복잡도는 O(1))이다.

Map자료형에는 HashMap, LinkedHashMap, TreeMap이 있다.

<br>
<br>

```java
Map<Integer, String> map = new HashMap<>();

map.put(1, "A");
```
key,value의 자료형을 각각 선언한다.

<br>

## __HashMap__

* value는 중복저장될 수 있으나 key는 중복저장될 수 없다.
* 해싱을 사용해 많은 양의 데이터를 검색하는데 성능이 뛰어나다.
* 저장되는 순서가 없다.
* 


### __keySet__

```java
for(Stringkey:map.keySet()){
    System.out.println("key :" + key);
}
```
map의 저장되어 있는 key의 값을 출력

<br>

### __entrySet__
```java
for(Map.Entey<string, string> elem : map.entrySet()){
    System.out.pritln("key :" + elem.getKey() + "value:" + elem.getValue());
}
```
map에 있는 key와 value를 짝지어 출력

<br>

<br><br>

출처

* 인프런 - 코딩테스트 전 꼭 알아야 할 개념과 문제(with 자바)
