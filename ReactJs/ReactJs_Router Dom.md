## React Router Dom

페이지 이동을 할 때 사용

페이지를 이동하여 보여주는 것이 아닌 각 페이지의 컴포넌트를 가져와 보여줌

<br>

설치
```js
npm install react-router-dom
```
<br>

__순서__

먼저 보여 줄 페이지를 만들어 놓는 것을 전제로 한다.

예를 들어 login.js, about.js 등

<br>

보여줄 페이지를 import 해온다.
```js
import LandingPage from './components/views/LandingPage/LandingPage'
```

각 페이지의 path와 componet를 지정한다.
```js
<Route exact path="/" component={LandingPage}/>
```

<br>
<br>

__전체__

```js
import LandingPage from './components/views/LandingPage/LandingPage'

function App() {
  return (
    <Router>
      <div>
        <Switch>
          <Route exact path="/" component={LandingPage}/>
        </Switch>
      </div>
    </Router>
  );
}

```
Route : 컴포넌트에 설정한 경로로 가면 해당 컴포넌트를 렌더링

Switch : 자식 컴포넌트 Route또는 Redirect중 제일 처음 매칭되는 요소를 렌더링하여 충돌 방지

<br>

참고 

https://reactrouter.com/web/example/basic


<br>
<br>
<br>

__출처__

* 인프런 [따라하며 배우는 노드, 리액트 시리즈 - 기본 강의]
* https://www.inflearn.com/course/따라하며-배우는-노드-리액트-기본/dashboard