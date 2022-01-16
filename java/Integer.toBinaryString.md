## 이진수 변환

Integer 클래스를 사용하여 변환

```java
int n = 70;

String num = Integer.toBinaryString(n);
```
<br>

__10진수 -> 8진수, 16진수 변환__
```java
String octal = Integer.toOctalString(decimal); // 8진수 변환
String hexaDecimal = Integer.toHexString(decimal); // 16진수 변환
```
<br>
<Br>

__Integer.bitCount__

10진수를 2진수로 변환한 뒤 1의 개수를 세어주는 함수
```java
int n = 70;

int count = Integer.bitCount(n);
```
70을 이진수로 변환하면 01000110 이므로 count는 4이다.

<br>


---

<br>


### 프로그래머스 [다음 큰 숫자] 문제 수정

<br>

__이전(Before)__

```java
int a = 0;
while(true){
    n++;
    a = 0;
    String ch = Integer.toBinaryString(n);
    for(int i = 0; i < ch.length(); i++){
        if(ch.charAt(i) == '1'){
            a++;
        }
    }
    if(count == a){
        answer = n;
        break;
    }
}
```
이전에는 값을 이진수로 변환한 뒤 charAt을 통해 1의 개수를 카운드하여 문제를 해결하였다.

<br>

__수정(After)__

```java
int a = 0;
while(true){
    n++;
    a = Integer.bitCount(n);

    if(count == a){
        answer = n;
        break;
    }
}
```
1의 개수를 세는 부분을 bitCount 함수로 수정하여 코드의 길이와 효율성을 증가시켰다.
