# __플렉서블 박스(Flexible Box)__
가변적인 박스를 쉽게 만들 수 있어 반응형 웹에 사용한다.

<br><br>

### __기본개념__
* 부모 박스
    * 모든 요소를 감싸고 있는 존재
    * 부모 박스에 새로 생긴 특정 속성값을 적용해야 함
* 플렉스 아이템
    * 부모 박스안에 자식 박스들이 플렉스 아이템
* 주축과 교차출
    * 주축의 방향에 따라 플렉스 아이템이 배치된다.
    * 주축이 가로일 경우 박스들이 왼쪽에서 오른쪽으로 배치, 주축이 세로일 경우 박스들이 위에서 아래로 배치
    * 교차축은 주축과 교차하는 축

<br><br>

### __기본 설정__
display 속성을 변경해줘야 한다.

`
display : flex;
`

* 플렉스 아이템 방향 설정
    * 박스를 왼쪽에서 오른쪽, 위에서 아래로 등 방향을 설정한다.
    * __flex-direction__
    * row | rows-reverse | column | column-reverse
<br>
<br>

* 플렉스 아이템 여러 줄 배치
    * 기본적으로 한 줄로 배치되는데 여러 줄로 배치하기 위해 설정한다.
    * __flex-wrap__
    * nowrap | wrap | wrap-reverse
    * wrap : 박스를 여러 줄로 배치한다.
<br><br>

* 플렉스 아이템 방향 & 여러 줄 배치
    * 플렉스 아이템의 방향과 여러 줄 배치를 한 번에 작성할 수 있다.
    *  flex=flow : [flex-direction] [flex-wrap]
    * 속성 사이에 __띄어쓰기__ 를 꼭 해야한다.
<br><br>

* 주축 방향 아이템 배치
    * 주축을 시작점으로 플렉스 아이템 배치
    * __jusrify-content__
    * flex-start | flex-end | center | space-between | space-aroud
<br><br>

* 교차축 방향 아이템 배치
    * 교차축을 방향으로 플렉스 아이템 배치
    * __align-items__
    * stretch | flex-stat | flex-end | center | baseline
    * 특정 플렉스 아이템의 배치를 변경하기 위해서는 align-self 속성을 사용한다.
<br><br>

* 플렉스 아이템 배치 순서
    * 플렉스 아이템 밗의 배치 순서를 자유롭게 정할 수 있다.
    * __order__
    * 0이 기본값이며 정수값을 사용해야 한다.
<br><br>

* 플렉스 아이템 크기 
    * 플렉스 아이템이 플렉서블 박스보다 크거나 작을 경우 플렉스 아이템 박스의 크기를 늘이거나 줄여 가변적으로 작동한다.
    * __flex : [flex-grow] [flex-shrink] [flex-basis]l__

<br><Br>

### 예시 
---
```
div{
    display : flex;
    order : 1;
    justify-content : flex-end;
}
```
<br><br><br> 

출처 : Do it! 반응형 웹 만들기
