## npm vs npx

<br>

__npm(node package manager)__

* 패키지 관리를 위한 패키지 매니저
* 라이브러리를 담고 있는 레지스트리 역할을 함
* 설치, 시작이나 빌드할 때 사용
* package.json에 정리되어 있음

<br>

__npm local과 global 저장__

<npm install ~ 로 다운받으면 local 저장> 

Local에 다운받아져서  ./node_modules/.bin 디렉토리에 생성

<br>

<npm install -g ~ 다운받으면 global 저장>

컴퓨터 내부 bin/디렉토리에 저장 

글로벌 공간에 저장되어 공유할 수 있음


<br>
<br>

__npx__

*  node.js 패키지를 실행시키는 하나의 도구
* 모듈을 저장하지 않고 최신버전을 임시로 가져와 사용 수 삭제
* 예로 npx가 npm registry에서 create-reat-app을 찾아서 다운로드 없이 실행
* disk space 낭비를 하지 않음
* 항상 최신버전을 사용할 수 있음

<br>
<br>
<br>

__출처__

* 인프런 [따라하며 배우는 노드, 리액트 시리즈 - 기본 강의]
* https://www.inflearn.com/course/따라하며-배우는-노드-리액트-기본/dashboard
