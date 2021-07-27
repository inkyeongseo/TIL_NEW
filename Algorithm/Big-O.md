# __Big-O__

알고리즘의 성능을 수학적으로  표현해주는 표기법

알고리즘의 시간과 공간 복잡도를 표현

데이터나 사용자의 증가율에 따른 알고리즘의 성능을 예측하는 것이 목표 

<br>
<br>

## __O(1)__

입력 데이터에 크게 상관없이 언제나 일정한 시간이 걸리는 알고리즘
```java
F(int[] n){
    return (n[0] == 0) ? true:false;
}
```
인자로 받는 배열 방의 크기와 상관없이 결과를 반환

<br>

## __O(n)__

입력 데이터의 크기에 비례해서 처리 시간이 걸리는 알고리즘
```java
F(int[] n){
    for i = 0 to n.length
        print i;
}
```
루프를 돌 때마다 n개의 개수가 늘어남

데이터의 개수가 늘어날 때마다 처리시간도 증가(비례)

<br>

## __O(n²)__

```java
F(int[] n) {
    for i = 0 to n.length
        for j = 0 to n.length
            print i + j;
}
```
n*n번 돌려야 하므로 데이터가 많아질수록 점점 처리시간도 증가

<br>

## __O(nm)__
```java
F(int [] n, int[] m) {
    for i = 0 to n.length
        for j = 0 to m.length
            pring i + j;
}
```
n을 m만큼 돌리는 것

<br>

## _O(n³)__

n을 3중으로 돌리는 것

데이터가 증가하면 할수록 처리시간이 급격히 증가

<br>

## __O(2ⁿ)__

피보나치 수열이 해당됨
```java
F(n,r){
    if(n <= 0) return 0;
    else if (n == 1) return r[n] = 1;
    return r[n] = F(n-1, r) + F(n-2, r);
}
```
트리의 높이 만큼 여러번 재귀호출을 하기 때문에 다른 것보다 데이터의 증가에 따라 처리시간이 급하게 증가

<br>

## __O(mⁿ)__

m개씩 n번 늘어나는 알고리즘

<br>

## __O(log n)__

대표적인 예는 __이진검색__

처리가 진행될 때마다 검색해야하는 데이터의 양이 절반씩 줄어드는 알고리즘

```java
F(k, arr, s, e) {
    if(s>e) return -1;
    m = (s+e) / 2;
    if (arr[m] == k) return m;
    else if (arr[m] > k) return F(k, arr, s, m-1);
    else return F(k, arr, m+1, e);
}
```

<br>

## _O(sqrt(n))__

제곱근을 구하는 알고리즘

<br>



## Big-O 표기법 주의사항
---


__상수는 버린다.__

* O(2n)은 O(n)으로 표시한다. 
* 실제 알고리즘의 러닝타임을 알아내기 위한 것이 아닌 장기적으로 데이터 증가에 따른 처리 시간에 증가율을 예측하기 위해 만들어진 표기법
* 상수는 고정된 숫자이므로 언제나 고정된 상수만큼만 영향을 미치기 때문에 증가하지 않는 숫자를 신경쓰지 않음
* O(n²+n²) 또한 O(n²)으로 표시

<br>
<br>
<br>

출처

* [자료구조 알고리즘] 빅오(Big-O)표기법 완전정복 (유튜브 채널 : 엔지니어대한민국)
* https://www.youtube.com/watch?v=6Iq5iMCVsXA
