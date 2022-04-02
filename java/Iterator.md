## Iterator<E> : 반복자

컬렉션 프레임워크

리스트에 들어있는 값을 순차적으로 출력

```java
Iterator<Integer> it = numberSet.iterator();

    while (it.hasNext()){
        int number = it.next();

        it.remove();
    }
```

* boolean hasNext() : 다음에 읽어올 값이 있다면 true, 없다면 false를 반환한다.

* Object next() : 다음 요소 값을 가져온다.

* void remove() : 현재 요소 값을 삭제한다.
