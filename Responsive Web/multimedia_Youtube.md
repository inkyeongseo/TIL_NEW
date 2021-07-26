# 멀티미디어(유튜브) 가변적으로 만들기
* 멀티미디어 중 동영상은 대부분 16:9 비율이다.
```css
#wrap{
    position : relative;
    padding-bottom : 56.25%;
    height : 0;
    overflow: hidden;
}

iframe{
    position : absolute;
    top:0;
    left:0;
    height: 100%;
}
```

* padding-bottom은 16:9 비율을 만들기 위해 9 ÷ 16을 계산해서 나온 값이다.
* 동영상의 비율이 4:3인 경우 75%이다.
<br>
