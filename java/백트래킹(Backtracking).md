## 백트래킹(Backtracking)

모든 경우의 수를 확인하여 답을 찾는 알고리즘이다.

깊이우선탐색(Depth First Search, DFS)과 너비우선탐색(Breadth First Search, BFS), 최선 우선 탐색(Best First Search/Heuristic Search)

<br>


__예시 : 프로그래머스 Level2 : 소수 찾기__

```java
    public int solution(String numbers) {
        recursive("",numbers); //재귀함수 , 모든 조합의 숫자 찾기
        .
        .
        
        return answer;
    }
    
    public void recursive(String comb, String others){
        //현재 조합 넣기
        if(!comb.equals("")) numberSet.add(Integer.valueOf(comb));
        
        //남은 숫자 중 하나 더하기
        for(int i = 0; i < others.length(); i++){
            recursive(comb + others.charAt(i), others.substring(0,i)+others.substring(i+1));
        }
        
    }
```

recursive 함수 안에서 recursive를 불러오며 여러 가지 숫자 조합을 찾을 수 있다.
