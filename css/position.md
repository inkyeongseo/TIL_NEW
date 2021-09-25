## __position 속성__

<br>


```css
position : relative | absolute | fixed | sticky 
```

<br>

__1.static__

position을 지정하지 않으면 static이 지정된다.

지정된 자리에 위치하며 top,bottom,left,right 값을 지정해도 움직이지 않는다.

<br>

__2.relative__

static 위치를 기반으로 top,bottom,left,right에 지정된 값으로 위치를 변경한다.

<br>

__3.absolute__

조상의 position을 기준으로 top,bottom,left,right을 적용한다.

absolute를 지정하면 부모-자식간의 관계가 끊어진다.

따라서 부모에서 설정한 값이 적용되지 않는다.

