## MongoDB 연결

<br>

__Cluster 생성 방법__

1. 새로운 프로젝트를 생성한다.

2. cluster 생성을 누룬 뒤 무료버전을 선택한다.(일단 FREE버전)

3. Region 선택에서 가장 가까운 나라를 선택한다(한국은 선택지에 없으며 가장 가까운 나라는 현재 싱가포르이다)

4. 생성까지 1-2분의 시간이 소요된다.

<br>
<br>

__연결방법__

1. 생성된 클러스터에서 connect버튼을 누룬 뒤 단계를 수행한다.

2. 마지막 단계에서 'Add your connection string into your application code'를 복사한다.

3. 아래의 코드로 연결을 확인한다.
```js
const mongoose = require('mongoose')
mongoose.connect('mongodb+srv://inkyeong:<password>@cluster0.msxuf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority',{
  useNewUrlParser: true, useUnifiedTopology: true, useCreateIndex: true, useFindAndModify:false
}).then(() => console.log('MongoDB Connected...'))
  .catch(err => console.log(err))

```
<br>

--------

<br>
<br>

## Model과 Schema
<br>


__Schema__

하나하나의 역할과 타입을 지정해주는 것

```js
const mongoose = require('mongoose');

const userSchema = mongoose.Schema({
    name:{
        type: String,
         maxlength: 50
    },
    email:{
        type: String,
        trim: true,
        unique: 1
    }
})

```
각각의 필드명을 적고 각 필드에 해당하는 타입, 속성 등을 선언한다.

<br>
<br>

__Model__

스키마를 감싸주는 역할 

스키마를 통해 만드는 인스턴스
```js

const User = mongoose.model('User',userSchema)

```

mongoose.model('모델 이름', 스키마) 형식으로 모델을 생성한다.

<br>
<br>
<br>

__출처__

* 인프런 [따라하며 배우는 노드, 리액트 시리즈 - 기본 강의]
* https://www.inflearn.com/course/따라하며-배우는-노드-리액트-기본/dashboard