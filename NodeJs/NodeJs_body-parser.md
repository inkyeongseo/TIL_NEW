## body-parser
* node js 모듈
* 클라이언트 post request data의 body로부터 파라미터를 편리하게 추출

<br>

```js
app.use(bodyParser.urlencoded({extended: true}));
```
urlencoded는 주소 형식으로 데이터를 보내는 방식

extended : true는 qs모듈을 사용하여 쿼리스트링을 해석, false는 querystring 모듈을 사용하여 쿼리스트링을 해석한다.

qs모듈은 querystring모듈을 확장한 모듈이며 내장모듈이 아닌 npm 패키지로 설치가 필요하다.

<br>
<br>

## 회원가입 구현
<br>
express 프레임워크에서 사용할 수 있는 중간 처리 목적의 소프트웨어인 미들웨어를 생성한다.

코드 실행, 요청-응답 주기 종료, 오브젝트 변경 실행 등을 수행한다.

<br>


```js
app.post('/register',(req,res) =>{
  
  //회원가입 할 때 필요한 정보들을 client에서 가져오면
  //그것들을 데이터 베이스에 넣는다.
  
  const user = new User(req.body)
  //body-parser가 있어서 request body로 받을 수 있다.

  user.save((err,userInfo)=>{
    if(err) return res.json({success: false,err})
    return res.status(200).json({
      success: true
    })
  })
})
```
1. post : 미들웨어 함수가 적용되는 http 메소드
2. './register' : 미들웨어 함수가 적용되는 경로
3. req : 미들웨어 함수에 대한 http의 요청 인수
4. res : 미들웨어 함수에 대한 http의 응답 인수

<br>
<br>
<br>

__Node Mon__
* 노드 서버 킨 다음 사용하고 변경 사항이 있으면 노드 서버를 끈다음 다시 시작해야 바뀐 소스가 적용됨
* node mon을 이용하면 서버를 내리고 올리지 않아도 소스 변경을 감지한다

<br>
<br>

__기타__


1)__require__
외부 모듈을 불러오기 위해 사용하는 함수
```js
const ex = requre('파일 경로');
```

위와 같이 가져올 모듈의 파일 경로 값을 받는다.

<br>

2)__const__

상수를 선언하는 키워드

선언과 동시에 값을 할당해야 한다

<br>
<br>
<br>

__출처__

* 인프런 [따라하며 배우는 노드, 리액트 시리즈 - 기본 강의]
* https://www.inflearn.com/course/따라하며-배우는-노드-리액트-기본/dashboard
