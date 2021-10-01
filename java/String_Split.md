## Split

<br>

이미 TIL에 split 개념정리를 해놓으나 응용 문제를 풀며 추가적인 사항이 있어 정리함.

[split 개념 정리](https://github.com/inkyeongseo/TIL_NEW/blob/master/java/Sort_compareto.md)

<br>
<br>

```java
for(String email : emails) {
	String[] parts = email.split("@");
	String[] localName = parts[0].split("\\+");
		
	set.add(localName[0].replace(".", "") + "@" + parts[1]);
			
	}

```
split으로 문자열을 쪼개면 앞에서부터 배열 형태로 저장된다.

따라서 이것을 이용하여 특정문자가 반복되어 사용되는 문제에서 기준으로 설정하여 해결할 수 있다.

새로운 문제를 풀며 새로운 주의사항을 알게되었다.

일반적으로 split("문자") 형식으로 작성하는데 문자만 쓰면 아래와 같은 오류가 발생한다.

Dangling meta character '+' near index 0

이를 해결하기위해 split("\\+") 또는 split("[+]")로 작성해야 한다.

<br><br>

출처

* 인프런 - 정말 쉽게 풀어보는 코딩 테스트 top 기본 문제 (with 자바)
