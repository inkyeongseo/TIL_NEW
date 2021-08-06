## Dynaimic Programming (동적 계획법)

<br>

__큰 문제를 작은 문제로 나누어 해결하는 방법__


<br>

__특징__

* 빠른 속도로 최적의 해를 구할 수 있다.
* 특정 규칙을 찾아내 적용하며 재사용 가능하다.
* 구간의 값을 배열을 이용해 저장한다
* Top Down방식과 Bottom Up 방식이 있다.
* 메모리에 저장된 값이 중복 호출되었을 때 저장해 둔 것을 재활용하는 memoization 기법을 사용한다.
* 

__Top Down__

큰 문제를 작은 문제로 풀어가며 해결하며 재귀로 구현한다.

<br>

__Bottom Up__

작은 문제를 차례대로 풀며 반복문으로 구현한다.

<br>


<br>

__Dynamic Programming 문제 풀이 방법__

1. 값에서 규칙을 찾아낸다.<br> 피보나치 수열을 예로 들 수 있다. f[i] = f[i-1] + f[i-2]
2. dp배열을 생성한 후 Bottom Up 방식으로 문제를 접근한다.

<br>
<br>
<br>


출처

* 인프런 - 코딩테스트 전 꼭 알아야 할 개념과 문제(with 자바)
* https://www.inflearn.com/course/코딩테스트-자바-개념/dashboard
