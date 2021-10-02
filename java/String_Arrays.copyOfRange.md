## Arrays.copyOfRange

<br>

배열의 지정된 범위를 복사하여 반환한다.

__Arrays.copyOfRange(원본 배열, 시작 인덱스, 끝 인덱스)__

```java
int[] a = {1,2,3,4,5,6,7,8,9};
		
		
	int[] b = Arrays.copyOfRange(a,2,5);
		
	for(int i = 0; i < b.length;i++) {
		System.out.print(b[i]);
	}
```

<출력 결과>

```java
345
```
배열 a의 2번부터 5번 바롱 앞까지 복사한다.

끝 인덱스에 바로 앞까지 복사하는 것을 주의해야한다.

<br>
<br>


__기타__


copyOfRange를 사용하며 substring과 차이점을 찾아보았다.

둘다 [시작인덱스, 끝인덱스] 사이의 값을 가져오는 것은 같으나 substring은 문자열에서 copyOfRange는 배열에서 사용한다는 점이 다르다.

```java
String d = "123456789";
String c = d.substring(2,5);
		
System.out.print(c);
```
<출력 결과>
```java
345
```

copyOfRange와 subString의 결과는 같으나 둘의 타입이 다르다는 것을 주목해야한다.




