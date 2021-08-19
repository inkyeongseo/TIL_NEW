## Auth 기능

* 페이지 이동시마다 로그인이 되어 있는지 관리자/유저인지 등을 체크

* 글을 쓰거나 지울 때 권한이 있는지 체크

<br>

__방법__

클라이언트는 쿠키에 있는 토큰(인코드 되어 있는)를 디코드하면 user_id가 나온다

데이터베이스안에 user_id가 있고 그 아이디가 토큰이 있다면 인증이 가능

<br>
<br>

1. 미들웨어에 auth를 생성한다.

```js
let auth =(req, res, next) => {
    //1.클라이언트 쿠키에서 토큰을 가져온다
    
    let token = req.cookies.x_auth;

    //2.토큰을 복호화 한 후 유저를 찾는다

    User.findByToken(token, (err,user)=>{
        if(err) throw err;
        //유저가 없으면 인증되지 않음
        if(!user) return res.json({isAuth:false, err: true})

        //4.유저가 있으면 인증 완료
        req.token = token;
        req.user = user;
        
        next();
    })
}

```
auth는 인증처리를 수행하는 곳

각 정보를 req하는 이유는 index.js에서 user,token 정보를 가질 수 있다.

작업이 모두 끝나면 다음으로 넘어갈 수 있도록 하기 위해 next()

<br>
<br>

2. 중간에 findByToken을 User.js에 생성한다.
```js
    jwt.verify(token,'secretToken',function(err,decoded){

       user.findOne({"_id":decoded, "token": token},function(err,user){
           if(err) return cb(err);
           cb(null, user)
       })
    })
```
이 과정에서 토큰을 decode(복화화)한다

암호화 할때 사용한 'secretToken'으로 복호화 한다.

복호화 한 유저 아이디를 이용해 DB 유저를 찾음

클라이언트에서 가져온 토큰과 DB에 저장된 토큰이 일치하는지 확인한다.

<br>
<br>

3.auth route 만들기

```js
app.get('/api/users/auth',auth,(req,res)=>{

    res.status(200).json({
      _id : req.user._id,
      isAdmin : req.user.role === 0 ? false : true,
      isAuth: ture,
      email : req.user.email,
      name : req.user.name,
      lastname : req.user.lastname,
      role : req.user.role,
      image : req.user.image
    })

})
```
auth은 endpoint와 cb사이 중간에 실행(middleware)

미들웨어를 통과해 여기 부분을 실행하고 있다는 것은 Authentication이 True라는 뜻

유저의 다양한 데이터를 전달해 그 페이지에서 사용하게 한다.


<br>
<br>

__기타__

이 과정은 하나의 완전한 함수를 만들고 다음으로 넘어 가는 것이 아닌 중간중간 필요한 메소드를 선언하면서 만들어야 한다.

<br>
<br>
<br>

__출처__

* 인프런 [따라하며 배우는 노드, 리액트 시리즈 - 기본 강의]
* https://www.inflearn.com/course/따라하며-배우는-노드-리액트-기본/dashboard



