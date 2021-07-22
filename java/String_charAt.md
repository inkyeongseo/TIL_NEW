## charAt()
---
특정 위치에 있는 문자를 알아낼 수 있다.

<br>

__charAt(i) - '0';__
```java
int num = str.char(i) - '0';
```
특정 문자의 값을 Integer 형식으로 가져올 수 있다.

```java
return sb.reverse().toString();
```
문자열의 순서를 반대로 가져온다. -> __reverse()__

<br>

__String vs StringBuilder/StringBuffer__
* String
    *  한 번 생성한 문자열을 변경하지 못하는 불변의 속성을 가졌다.
    * 변하지 않는 문자열을 읽어들일 때 용이하다.
    * 잦은 문자열 추가,삭제는 힙(Heap)에 많은 가비지를 생성한다.
* StringBuilder/StringBuffer
    * 가변성을 가진다.
    * .append() .delete() 등의 API를 이용하여 동일 객체내에서 문자열을 변경하는 것이 가능하다
    
<br>

__StringBuilder vs StringBuffer__
* StringBuffer
    * 동기화 키워드를 지원하여 멀티쓰레드 환경에서 안전하다.


* StringBuilder
    * 동기화를 지원하지 않기때문에 멀티쓰레드 환경에서 사용하는 것은 적합하지 않다
    * 동기화를 고려하지 않는 만큼 단일쓰레드에서의 성능은 StringBuffer 보다 뛰어나다






