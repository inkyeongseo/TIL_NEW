# 이차원 배열
 
## 선언
```java
int[][] array = new int[2][5];
```

```java
int[][] grid = new int[3][];
```
위와 같이 선언 한 경우 행의 개수만 설정할 수 있다.

```java
grid[0] = new int[1];
grid[1] = new int[2];
```
다음과 같이 각 행의 열의 개수를 정할 수 있다.

<br>
<br>

__i.length__

2차원 배열의 행의 개수

<br>

__i[0].length__

0번째 행에 있는 열의 개수

<br>

### __이차원 배열 -> List__
```java
List<List<Integer>> result = new ArrayList<>();
    for(int i = 0; i < a.length; i++){
        List<Integer> b = new ArrayList<>();
        for(int j =0; j <a[i].length; j++){
            b.add(a[i][j]);
        }
        result.add(list);
    }
```
i번째 행에 있는 값을 list에 담기 위해 b 리스트를 만든다.

<br>

### __List -> 이차원 배열__
```java
int[][] result = new int[list.size()][];
```
행의 개수는 무조건 선언해야 한다.

```java
for(int i = 0; i < result.length; i++){
    result[i] = new int[list.get(i).size()];
}
```
각 행의 열의 size를 알아내서 열의 개수를 선언한다.

<br>
<br>

## __ArrayList<E>__

* 가변 크기의 배열을 구현한 컬렉션 클래스
* 스레드 간 동기화를 지원하지 않기 때문에 다수의 스레드가 동시에 삽입하거나 삭제할 때 ArrayList의 데이터가 회손될 수 이다.
* 멀티스레드 동기화를 위한 시간 소모가 없어 속도가 빠르고 단일 스레드 응용에 효과적인다.

<br>


```java
ArrayList<String> a = new ArrayList<String>();
```
문자열을 다루는 ArrayList 생성
 
<br>
<br>
<br>


출처

* 인프런 - 코딩테스트 전 꼭 알아야 할 개념과 문제(with 자바)
* 명품 JAVA Programming [황기태 / 김효수 지음]
