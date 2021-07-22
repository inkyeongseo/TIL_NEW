# __미디어쿼리__
### 화면 크기마다 스타일을 적용하는 CSS 속성 중 하나이다.
<br>
그리고 이것은 테스트이다.


@media [only 또는 not] [미디어 유형] [and 또는 콤마] (조건문){실행문}<br>
미디어 쿼리 구문은 대소문자를 구별하지 않는다.<br>
문법 사이 __띄어쓰기__ 를 주의해야 한다.
<br><br>
## @media<br>
* 미디어 쿼리 문법의 시작을 알린다.
<br><br>

## 미디어 유형
기기 명 | 내용 
------------ | ------------- 
all | 모든 장치 
print | 인쇄 장치
screen | 컴퓨터 또는 __스마트 기기__ 화면
tv | 영상과 음성이 동시 출력되는 장치
handheld | 손에 들고 다니는 기기
<br>
## 작성예시
`@media all and(min-width:320px){
#div{
Width:100%;
}
}
`

<br>
<br>

# __뷰포트__
화면에서 실제 내용이 표시되는 영역
<br>
<br>
`<meta name =”viewport” content=”width=device-width,initial-scale=1,minimum-scal=1,maximum-scal=1,user-scalable=no”>`

<br><br><br><br>
출처 : Do it! 반응형 웹 만들기
