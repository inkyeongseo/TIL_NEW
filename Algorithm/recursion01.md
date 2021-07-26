# 순환이란? 

자기 자신을 호출하는 함수 / 재귀함수
<br><br><br>
__항상 무한루프에 빠지는 것은 아니다__
* 적절한 구조를 가지면 무한루프에 빠지지 않는다
    * base case : 적어도 하나의 recursion에 빠지지 않는 경우가 존재해야 한다.
    * recursive case : recursion을 반복하다보면 결국 base case로 수렴해야 한다.
```java
 private static void func(int n) {
    if (n <= 0)
      return;  //base case
    else {
      System.out.println("Hello...");
      func(n - 1); recursive case
    }
  }
```
<br><br>

__순환을 이용해 1~n까지 합 구하기__

```java
public static int func(int n){
    if(n == 0)
        return 0; //n=0이라면 합은 0이다.
    else
        return n + func(n-1);
}
```
* n이 0보다 크다면 0에서 n까지 합은 0에서 n-1까지으 합게 n을 더한 것이다.
* 수학적귀납법과 동일한 방법이다.

__Factorial :  n!__
* 0! = 1
* n! = n*(n-1)!    n>0경우

```java
public static int factorial(int n){
    if(n==0)
        return 1;
    else
        return n*factorial(n-1);
}
```
<br>
<br>

__Xn__
* X0 = 1
* Xn = X*Xn-1 if n>0
```java
public static double power(double x, int n) {
  if (n == 0)
    return 1;
  else
    return x * power(x, n-1);
}
```
<br>
<br>

__Fibonacci Number__

```java
public int fibonacci(int n){
    if(n<2>)
        return n;
    else
        return fibonacci(n-1) + fibonacci(n-2);
}
```
<br>
<br>

출처 : 인프런<영리한 프로그램을 위한 알고리즘 강좌>