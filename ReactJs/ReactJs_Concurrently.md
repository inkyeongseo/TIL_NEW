## Concurrently 설정

<br>

프론트, 백 서버를 한번에 키기 위해 사용

<br>

__설치__

```js
npm install concurrently --save
```
<br>

__사용법__
```js
"start" : "concurrently \"command1 arg\" \"command2 arg\""
```
concurrently 뒤에 실행해야하는 것들을 적는다.

<br>

__적용__

```js
"dev" : "concurrently \"npm run backend\" \"npm run start --prefix client\""
```
현재 server와 client 폴더로 프론트와 백을 구분하고 있다.

프론트 서버는 client폴더 안에서 실행되어야 하므로 --prefix client를 뒤여 붙여준다.

<br>
<br>

__문제점__

프론트 서버는 정상적으로 동작이 되었지만 백엔드 서버에 에러가 발생했다.

<br>

백엔드와 관련된 파일들을 모두 server폴더에 옮기는 과정에서 새롭게 경로지정을 해주지 않아 발생했다는 것을 알았다.

```js
"backend": "nodemon server/index.js",
```

<br>
<br>
<br>

__출처__

* 인프런 [따라하며 배우는 노드, 리액트 시리즈 - 기본 강의]
* https://www.inflearn.com/course/따라하며-배우는-노드-리액트-기본/dashboard
