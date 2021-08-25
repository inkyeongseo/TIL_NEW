## Redux

<br>

상태 관리 라이브러리

react에는 props와 state가 있으며 Redux은 State를 관리하는 것

<br>

__1.Props__
* properties의 약자

* 컴포넌트 간 무언가를 주고받을 때 사용

* 부모컴포넌트에서 자식컴포넌트로만 보낼 수 있다

* 부모 컴포넌트에서 자식컴포넌트로 보낸 데이터는 자식컴포넌트에서 바꿀 수 없고 값을 바꾸기 위에서는 부모 컴포넌트에서 새로 보내야 한다.

<br>

__2.State__

* 부모-자식 컴포넌트 간이 아닌 그 컴포넌트 안에서 데이터를 전달할때 사용

* 이 안에서 값을 변경할 수 있다.
* 값이 바뀌면 re-render 된다.

<br>

----

<br>

__Redux 데이터 흐름__

react component -> ACTION -> REDUCER -> STORE -> react component

한방향으로만 흐른다

<br>

1)ACTION

무엇이 일났는지 설명하는 객체

type 필드를 무조건 가지고 있어야 한다.

예
```js
{type : 'LIKE_ARTICLE', articleId : 42}
```
<br>

2)REDUCER

aciton으로 인해 바뀐 내용을 알려준다
```js
(previousState, action) => nextState
```
이전 State과 action object를 받은 후 next state을 return한다.

<br>

3)STORE

state을 감싸주는 역할

여러 메소드들을 이용해 state관리

<br>
<br>


### 사용법

<br>


__설치__

```js
npm install redux react-redux redux-promise redux-thunk --save
```
redux-promise, redux-thunk는 redux 미들웨어

STORE는 객체 형식으로 받는데 객체형식말고 promise, function형식으로 올 때가 있다.

그래서 redux-thunk : dispatch에게 어떻게 function을 받는지 알려주고 

redux-promise : dispatch에게 promise가 왔을 때 어떻게 대처해야하는지 알려준다.

<br>
<Br>

__예시__

index.js
```js
import{Provider} from 'react-redux';
import { applyMiddleware, createStore } from 'redux';
import promiseMiddleware from 'redux-promise';
import ReduxThunk from 'redux-thunk';
import Reducer from './_reducer'

const createStoreWithMiddleware = applyMiddleware(promiseMiddleware, ReduxThunk)(createStore)

ReactDOM.render(
  <Provider
    store={createStoreWithMiddleware(Reducer,
        window.__REDUX_DEVTOOLS_EXTENSION__ &&
        window.__REDUX_DEVTOOLS_EXTENSION__()
      )}
  >
    <App />
  </Provider>,
  document.getElementById('root')
);
```


<br>

```js
const createStoreWithMiddleware = applyMiddleware(promiseMiddleware, ReduxThunk)(createStore)
```
createStore를 사용해 STORE를 Redux에 생성하는데 위에 정리한 이유로 promise와 function도 받기 위해 미들웨어와 함께 생성한다.

```js
window.__REDUX_DEVTOOLS_EXTENSION__ &&
window.__REDUX_DEVTOOLS_EXTENSION__()
```
REDUX Extension 사용을 위해 작성함

다운링크

https://chrome.google.com/webstore/detail/redux-devtools/lmhkpmbekcpmknklioeibfkpmmfibljd/related

<br>
<br>
<br>

__출처__

* 인프런 [따라하며 배우는 노드, 리액트 시리즈 - 기본 강의]
* https://www.inflearn.com/course/따라하며-배우는-노드-리액트-기본/dashboard