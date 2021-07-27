## Matrix Zero
---
행렬에서 값이 0이면 그 행과 열의 값을 모두 0으로 바꾸는 문제

<br>


__HashSet__

* Set 인터페이스의 구현 클래스
* 요소를 순서에 상관없이 저장
* 중복된 값을 허용하지 않음


```java
Set<Integer> rowSet = new HashSet<>();
```

<br>
<br>

__문제 풀이__
```java
if(grid[i][j] ==0){
    rowSet.add(i);
    colSet.add(j);
}
```
행렬의 값이 0인 경우 그 좌표 값을 각각 넣어준다.


<br>

```java
if(rowSet.contains(i) || colSet.contains(j)){
    grid[i][j] = 0;
}
```
행과 열이 저장되어 있으면 그 좌표의 값을 0으로 바꾼다.
<br>
<br>
<br>


__contains__

* 특정 문자열이 포함되어 있는지 확인하는 함수
* 대/소문자 구분
* 공백도 포함하여 구분

<br>
<br>
<br>


출처

* 인프런 - 코딩테스트 전 꼭 알아야 할 개념과 문제(with 자바)