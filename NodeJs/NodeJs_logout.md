## 로그아웃 기능

<br>

__순서__

1. 로그아웃 하려는 유저를 데이터베이스에서 찾는다.
2. 그 유저의 토큰을 지워준다<br>(로그인 인증을 할 때 토큰으로 인증했기 때문에)

<br>

```js
app.get('/api/users/logout',auth,(req,res)=>{

  User.findOneAndUpdate({_id: req.user._id},
    {token : ""},(err,user)=>{
      if(err) return res.json({success:false, err});
      return res.status(200).send({
        success: true
      })
    })

})
```
<br>
findOneAndUpdate은 컬렉션에 있는 스키마의 데이터를 업데이트한다.

<br>
<br>
<br>

__출처__

* 인프런 [따라하며 배우는 노드, 리액트 시리즈 - 기본 강의]
* https://www.inflearn.com/course/따라하며-배우는-노드-리액트-기본/dashboard