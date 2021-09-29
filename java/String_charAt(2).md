## CharAt 사용 예시

<br>

주어진 문자열에서 .을 만나면 무시하고 넘어가고 +를 만나면 그 이후 문자는 무시한다.

<br>

```java
private String makeLocalName(String email) {
	StringBuilder sb = new StringBuilder();
		
	for(int i = 0; i < email.length(); i++) {
			
		if(email.charAt(i) == '.') {
			continue;
		}
		if(email.charAt(i)=='+' || email.charAt(i)=='@') {
			break;
		}
			
		sb.append(email.charAt(i));
			
	}
		
	return sb.toString();
}
```

charAt을 이용하여 순서대로 문자열의 값을 확인할 수 있다.


<br>
<br>

__substring 과 indexOf__

```java
return email.substring(email.indexOf("@"));
```
substring은 문자열의 특정위치부터 끝까지(또는 정해진 위치까지) 출력할 수 있다.

@이후의 문자열을 가져오기 위해 @의 위치를 가져와야하므로 indexOf를 사용하여 각 문자열마다 @의 위치를 가져온다.

<br>
<br>

__기타(정리)__

charAt - 문자열의 특정 위치의 값을 알고 싶을 때
substring - 문자열의 특정 부분을 가져오고 싶을 때
indexOf - 특정 값의 위치를 알고 싶을 때

<br>
String문제를 여러번 풀면서 각 함수의 사용방법을 익힐 수 있었다.


<br><br>

출처

* 인프런 - 정말 쉽게 풀어보는 코딩 테스트 top 기본 문제 (with 자바)

