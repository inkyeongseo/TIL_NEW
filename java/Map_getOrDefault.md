## getOrDefault

<br>

__getOrDefault(Object key, V defaultValue)__

찾는 키가 있으면 그 키의 값을 반환하고 없으면 default로 지정한 값을 반환하는 함수

<br>
<br>

__사용 예시__

알파벳의 빈도수를 map에 저장하는 예시이다.


```java
if(!map.containsKey(ch)){
    map.put(ch,1);
}else{
    map.put(ch, map.get(ch)+1);
}
```
위의 코드를 getOrDefault 함수를 사용해 아래와 같이 쓸 수 있다.

<br>

```java
map.put(ch,map.getOrDefault(ch,0)+1);
```
map.getOrDefault(ch,0)에서 map에 ch 키가 있으면 map.get(ch)를 돌린 결과 값이 나오고 ch 키가 없으면 0을 출력한다.

그리고 개수를 세기 위해 값을 1씩 증가시킨다.

<br>
그리고 
<br>

__toCharArray__

문자열을 char형 배열로 변환한다.

```java
String s = "example";

for(char ch : s.toCharArray()){
    .
    .
}
```
example이라는 문자를 순서대로 char배열로 만들어 for문을 돌릴 수 있다.


<br>
<br>


출처

* 인프런 - 코딩테스트 전 꼭 알아야 할 개념과 문제(with 자바)