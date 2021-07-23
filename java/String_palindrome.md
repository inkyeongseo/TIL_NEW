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

