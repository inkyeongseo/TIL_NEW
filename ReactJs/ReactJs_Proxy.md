## Proxy설정

<br>

__문제__

두 개의 다른 포트를 가지고 있는 서버는 아무 설정없이 Request 보낼 수 없다

예를 들어 서버는 localhost:5000이고 client는 localhost:3000인 경우를 말한다.


-> CORS정책 때문이며 보안을 위해서이다

<br>

__CORS(Cross-Origin Resource Sharing)__

* 서로 다른 origin에서 리소스를 교환할 수 있도록 만든 정책<br>여기서 origin은 각 프로토콜(http)+호스트(localhost)+포트(3000)을 말한다 

*  추가 http헤더를 사용해 하나의 origin에서 실행중인 웹 애플리케이션이 다른 origin의 자원에 접근할 수 있도록 권한을 부여하여 브라우저에 알려준다.

<br>

__해결방법__

해결하는 방법은 여러가지가 있지만 이번에는 Proxy사용하는 방법으로 해결 할 것이다.

<br>

```js
npm install http-proxy-middleware --save
```
먼저 위 패키지를 설치한다.

<br>


setupProxy.js
```js
const { createProxyMiddleware } = require('http-proxy-middleware');

module.exports = function(app) {
  app.use(
    '/api',
    createProxyMiddleware({
      target: 'http://localhost:5000',
      changeOrigin: true,
    })
  );
};
```
src퐅더에 setupProxy.js 파일을 만들어준다.

서버의 포트가 5000번이므로 target을 5000번으로 설정한다.

<br>

참고

https://create-react-app.dev/docs/proxying-api-requests-in-development/

<br>

__Proxy Server 역할__

<br>

1. 데이터를 보내는 유저의 IP를 임의로 바꿔 인터넷에 접근하는 유저의 IP를 모르게 할 수 있다.
2. 보내는 데이터를 임의로 바꿀 수 있다.
3. 방화벽 기능
4. 웹 필터 기능
5. 캐쉬 데이터, 공유 데이터 제공 기능

<br>

__Proxy Server 사용 이유__

* 특정 사이트에 접근하지 못하도록 제어 
* 캐쉬를 이용해 더 빠른 인터넷 제공
* 유저 IP를 임의로 변경해 더 나으 보안 제공


<br>
<br>
<br>

__출처__

* 인프런 [따라하며 배우는 노드, 리액트 시리즈 - 기본 강의]
* https://www.inflearn.com/course/따라하며-배우는-노드-리액트-기본/dashboard

 
