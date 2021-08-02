## __Comparator__
특정한 정렬이 필요할 때 사용한다.

<br>

배열에 있는 값을 오름차순으로 정렬하는 방법
<br>

1.첫 번째
```java
public List<Interval> merge(List<Interval> intervals){
    Collections.sort(intervals, (a,b)->a.start-b.start);
}
```
<br>

2.두 번째
```java
public List<Interval> merge(List<Interval> intervals){
    Collection.sort(intervals, comp);
}

Comparator comp = new Comparator<Interval>(){
    @Override
    public int compare(Interval a, Interval b){
        return a.start-b.start;
    }
};
```

<br>

2.세 번째
```java
public List<Interval> merge(List<Interval> intervals){
    Collection.sort(intervals, comp);
}

Comparator comp = new Comparator<Interval>(){
    @Override
    public int compare(Interval a, Interval b){
        if(a.start < b.start){
            return -1;
        }else if(a.start > b.start{
            return 1;
        }else{
            return 0;
        }
    }
};
```

<br>

<br><br>

출처

* 인프런 - 코딩테스트 전 꼭 알아야 할 개념과 문제(with 자바)