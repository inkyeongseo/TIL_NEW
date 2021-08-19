## Bcrypt 암호화

 Bcrypt를 이용해 비밀번호를 암호화 하며 보안성을 높여주기 위해 필요하다

<br>

__Bcrypt 란?__

* 패스워드 암호화 알고리즘
* salt를 추가하여 해싱하기 때문에 보안성이 높다
* bcrypt를 사용하려면 라이브러 필요하다

```js
npm install bcrypt --save
```

<br>
<br>

__암호화 방법/순서__

1. 유저 정보들을 db에 저장하기 전에 암호화를 진행해야 한다.
2. salt를 이용해서 암호화 -> 따라서 salt를 먼저 생성해야 한다.
```js
bycrpt.hash(myPlaintextPassword, salt, function(err,hash){

        });

```
(saltRounds를 설정해야 하는데 이는 salt를 몇자리로 설정할 것인지 정하는 것)
3. 코드 작성

```js
userSchema.pre('save',function(next){
    //비밀번호를 암호화 시키는 과정
    var user = this;
    //비밀번호가 수정되었을 때만 이 과정을 수행
    if(user.isModified('password')){
        //salt생성
        bcrypt.genSalt(saltRounds, function(err,salt){
            if(err) return next(err)

            bcrypt.hash(user.password, salt, function(err, hash){
                if(err) return next(err)
                user.password = hash
                next()
            })
        })
    }else{
        next()
        //비밀번호가 아니 다른 것을 바꿀 때 
    }
})

```
index.js에서 save가 이루어 지기 전(pre)에 수행한다.


<br>
<br>
<br>

__출처__

* 인프런 [따라하며 배우는 노드, 리액트 시리즈 - 기본 강의]
* https://www.inflearn.com/course/따라하며-배우는-노드-리액트-기본/dashboard
