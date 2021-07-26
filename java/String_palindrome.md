## Palindrome(회문)
---
왼쪽부터 읽으나 오른쪽부터 읽으나 같은 문자열
   
<br>

```java
while(s.charAt(left) == s.charAt(right)){
    left--;
    right++;
}
```
왼쪽 값과 오른쪽 값이 같은 경우에만 양 옆으로 이동한다.

<br>

```java
if (end < right - left - 1) {
			start = left + 1;
			end = right - left - 1;
	}
```
end 값은 palindrome에 해당하는 문자열의 길이를 뜻한다.

따라서 조건문은 문자열 길이를 비교하기 위해 end값을 비교하는 것이다.

<br>
<br>
<br>


출처

* 인프런 - 코딩테스트 전 꼭 알아야 할 개념과 문제(with 자바)