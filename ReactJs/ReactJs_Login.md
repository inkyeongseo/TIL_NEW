## Login 과정
<br>

목표 
* Redux를 이용해 로그인 하는 과정을 정리한다.
* 이 과정을 통해 회원가입, 로그아웃 페이지도 만들 수 있다.

1. LoginPage.js
```js
<form style={{display:'flex', flexDirection:'column'}}
            onSubmit={onSubmitHandler}
        >
            <label>Email</label>
            <input type="email" value={Email} onChange={onEmailHandler}/>
            <label>Password</label>
            <input type="password" value={Password} onChange={onPasswordHandler}/>
            
            <br/>
            <button type="submit">
                Login
            </button>
        </form>
```
로그인을 할 __form__ 을 생성한다.


```js
const dispatch = useDispatch();

const [Email, setEmail] = useState("")

const onEmailHandler = (event) =>{
    setEmail(event.currentTarget.value)
}
```
useState을 이용해 input에 값을 입력하도록 작성한다.

(password도 동일한 방식)

```js
const onSubmitHandler = (event)=>{
        //페이지가 리프레시되는 걸 방지
        event.preventDefault();
        
        let body = {
            email : Email,
            password : Password
        }

        //loginUser는 aciton
        dispatch(loginUser(body))
        .then(response=>{
            if(response.payload.loginSuccess){
                props.history.push('/') 
            } else{
                alert('Error')
            }                
        }) 
```
submit을 하면 eamil과 pass가 action으로 이동한다.

로그인 성공 시 push를 이용해 랜딩페이지인 root page 로 이동

<br>
<br>

2.user_action.js
```js
export function loginUser(dataTosubmit){
    const request = axios.post('/api/users/login',dataTosubmit)
            .then(response => response.data)

    return{
        type: LOGIN_USER,
        payload: request
    }
}
```
axios.post에서 보내는 url은 server단에 미리 만들어 놓은 것

return은 위에 있는 변수 request를 reducer에 보내는 작업

<br>
<br>
3.user_reducer.js

```js
export default function(state ={}, action){
    switch (action.type) {
        case LOGIN_USER:
            return {...state, loginSuccess: action.payload}
            break;     
        default:
            return state;
    }
}
```
reducer는 이전state와 action을 사용해 다음state을 return하는 것

...state : spread operator를 이용해 빈 상태를 그대로 가져옴

로그인이 성공하면 user_action에서 보낸 payload를 보여줌


<br>
<br>
<br>

__출처__

* 인프런 [따라하며 배우는 노드, 리액트 시리즈 - 기본 강의]
* https://www.inflearn.com/course/따라하며-배우는-노드-리액트-기본/dashboard