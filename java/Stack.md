## Stack(스택)

<br>

* LIFO : Last In First Out

* 선형구조로 끝에서만 데이터를 넣고 뺄 수 있다.

* 즉, 마지막에 들어간 데이터가 제일 먼저 나온다

* 구조가 단순하여 구현이 쉽다.

* 데이터 접근 속도가 빠르다.

* 데이터의 최대 개수를 미리 선언해야 한다.

<br>


```java
Stack<Integer> Stack = new Stack<>();

Stack.top(); // 가장 위에 데이터 
Stack.pop();  // 가장 위에 데이터 꺼내기
Stack.push();  // 스택에 데이터 넣기, 가장 위에 들어 감

```