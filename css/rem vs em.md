# CSS 단위(rem vs em)

## em
<br>

* 부모의 폰트 사이즈를 곱한 값으로 계산된다. 

* 브라우저의 기본 폰트 사이즈는 16px이다.

* 이때 부모를 8em으로 설정하면 16*8 =128px로 나타내 준다. 

* 부모 안에 자식 폰트를 0.5em으로설정하며 부모의 값, 즉 128px을 이용하여 128*0.5 = 64하여 64px로 나타낸다.

<br>
<br>

## rem
<br>

* r은 root의 약자로 em은 부모에 영향을 받는다면 rem은 root에 영향을 받아 계산한다. 

* 예를 들어 브라우저의 기본 픽셀인 16px을 기준으로 부모를 8rem으로 설정하며 16*8 = 128px이 된다.

* 자식에 0.5rem을 준 경우 em과 달리 부모의 영향을 받지 않고 root의 값과 계산하여 16*0.5 = 8px이 된다.


<br>
<Br>

## 단위 선택하는 방법
<br>

1. 부모요소의 사이즈에 따라 사이즈가 변경되어야 한다면 : %, em

2. 부모와 상관없이 브라우저 사이즈에 대해서 반응 : v*, rem

3. 요소의 너비와 높이에 따라서 사이즈가 변경 : %, v*

4. 폰트 사이즈에 따라서 사이즈가 변경 : em, rem


<br>
<br>
<br>

출처 
* 드림코딩 by 엘리 [프론트엔드 필수 반응형 CSS 단위 총정리 (EM과 REM) | Responsive CSS Units]
