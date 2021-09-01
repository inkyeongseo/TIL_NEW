## ReactJs

<br>

* 웹 프레임워크로, 자바스크립트 라이브러리
* 사용자 인터페이스를 만들기 위해 사용
* 컴포넌트로 이루어져 있어 재사용성이 용이함

<br>

__virtual DOM__

React는 virtual DOM 기반으로 가볍다는 특징이 있다.

여러 리스트 중 업데이트 되것만 DOM에서 바꾼다.

가상 돔으로 페이지가 변경될 때마다 랜더링 되어 보이지만 하위 컴포넌트만 렌더링 된다.

<br>



__문제__

리액트 앱을 실행하기 위해서는 webpack이나 babel같은 것을 설정해야하는데 시간이 오래걸린다.

아래의 패키지를 이용하여 해결한다.

```js
create-react-app Command
```

<br>


__JSX(Javascript Extension)__

Javascript에서 확장된 문법

자바스크립트 안에서 html을 문법을 사용하여 보여주는 것

빌드 시 Babel에 의해 자바스크립트로 변환

<br>

__babel__

최신 자바스크립트 문법을 지원하지 않는 브라우저를 위해 문법을 구형 브라우저에 맞게 변환

<br>

__webpack__

많은 모듈을 하나의 파일로 모아 모듈 번들을 만든다

<br>

```js
npx create-react-app .
```
띄어쓰기 .필요!! -> .은 선언


<br>
<br>
<br>

__출처__

* 인프런 [따라하며 배우는 노드, 리액트 시리즈 - 기본 강의]
* https://www.inflearn.com/course/따라하며-배우는-노드-리액트-기본/dashboard
