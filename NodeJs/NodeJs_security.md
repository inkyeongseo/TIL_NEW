## 보안 설정

<br>

파일에 있는 모든 정보를 깃허브에 업로드 하거나 공유하면 코드 속 비밀번호나 중요한 정보를 도출할 수 있다.

이를 위해 중요한 정보늘 따로 빼두는 작업을 진행해야 한다.

<br>

__방법__

1. 비밀번호 코드를 새로운 파일에 옮긴다.

2. 필요한 곳에서 그 파일을 불러와 사용한다.

```js
const config = require('./config/key')

mongoose.connect(config)
```

3. .gitignore파일을 생성한다.

4. 깃허브에 업로드 되지 않아야하는 파일 명을 .gitignore파일에 적는다.

5. 깃허브에 업로드시 .gitignore에 작성된 파일은 업로드 되지 않는다.

<br>
<br>

__환경 설정__

process.env.NODE_ENV

: development또는  production로 환경변수 설정 


1) Local 환경에서 개발하는  development 환경

2) Deploy(배포) 한 후 production 환경

```js
if(process.env.NODE_ENV == 'production'){
    module.exports = require('./prod');
}else{
    module.exports = require('./dev');
}
```

<br>
<br>
<br>

__출처__

* 인프런 [따라하며 배우는 노드, 리액트 시리즈 - 기본 강의]
* https://www.inflearn.com/course/따라하며-배우는-노드-리액트-기본/dashboard

