## 로그인 기능

<br>

내용 : 이메일과 패스워드가 DB에 저장된 값과 같다면 토근 생성

<br>

__순서__

1. 요청된 이메일을 데이터베이스에서 있는지 찾는다.
```js
User.findOne({email: req.body.email}, (err,user)=>{
    if(!user){
      return res.json({
        loginSuccess: false,
        message: "제공된 이메일에 해당하는 유저가 없습니다."
      })
    }
```

2. 요청된 이메일이 있다면 비밀번호가 맞는지 확인한다.
```js
user.comparePassword(req.body.password, (err,isMatch)=>{
      if(!isMatch)
        return res.json({loginSuccess : false, message : "비밀번호가 틀렸습니다"})
```
comparePassword 메소드를 생성한다.
```js
userSchema.methods.comparePassword = function(plainPassword, cb){
       bcrypt.compare(plainPassword, this.password, function(err, isMatch){
        if(err) return cb(err);
        cb(null, isMatch)
    })
}
```
plainPassword가 진짜 비밀번호, 암호화된 비밀번호와 같은지 확인

plainPassword을 암호화해서 db에 있는 것과 같은지 확인해야 함

cb에 에러는 없고 Match가 됨을 뜻함 

3. 비밀번호가 같다면 token을 생성한다.

```js
user.generateToken((err,user)=>{
      if(err) return res.status(400).send(err);
      
        res.cookie("x_auth",user.token)
        .status(200)
        .json({loginSuccess: true,userId: user._id})

    })
```
staus(400)은 에러

token 저장은 쿠키, 로컬스토리지 등에 할 수 있다 

지금은 쿠키에 저장하는 과정이다.

쿠키에 토큰을 저장하기 위해서는 cookie-parser라이브러리가 필요하다.

```js
userSchema.methods.generateToken =function(cb){

    var user = this;
    //jsonwebtoken을 이용해 token을 생성하기
    var token = jwt.sign(user._id.toHexString(),'secretToken')

    user.token = token
    user.save(function(err,user){
        if(err) return cb(err)
        cb(null,user)
    })
}
```
토큰 생성을 위해 JSONWEBTOKEN라이브러리 설치가 필요하다.

참고 https://www.npmjs.com/package/jsonwebtoken

token은 uer_id와 'secretToeken'을 합쳐서 만든다

그렇기 때문에 뒤에 문자 'secretToken'도 기억하고 있어야 한다.

<br>
<br>
<br>

__출처__

* 인프런 [따라하며 배우는 노드, 리액트 시리즈 - 기본 강의]
* https://www.inflearn.com/course/따라하며-배우는-노드-리액트-기본/dashboard