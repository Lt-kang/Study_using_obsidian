# ts의 기본 타입

# ts에서의 타입 선언(const / type / interface)
## const
실제 데이터를 만드는 것
```
const user = {
  id: 1,
  name: "Kim",
}
```
- user라는 실제 객체를 선언하는 것


## type
type(설계도) 선언한다.
```
type User = {
  id: number
  name: string
}
```
- user라는 타입 설계도를 선언하는 것
- 컴파일되면 사라짐.


## interface
객체 구조를 정의하기 위한 전용 문법
```
interface User {
  id: number
  name: string
}
```
- 객체 형태만 정의 가능
- 확장(extends)이 매우 강력
- 선언 병합 가능
```
interface User {
  id: number
}

interface User {
  name: string
}

// 결과적으로
// User = { id: number; name: string }
```


## type vs interface
- 



# 함수에서의 사용


# ETC
- React는 component를 조합하는 게임이며 TypeScript는 그 조합을 안전하게 만들어 준다.
- `label?: string;` > ts에서 `?`의 의미는 "이 프로퍼티는 있어도 되고, 없어도 된다"의 의미
	- `label?: string;` 이 부분은 `label: string | undefined` 이렇게 치환할 수 있음.
	- 초기에는 없으나 나중에 채워질 값에서 주로 사용
	- api 응답에서 optional field에 주로 사용
- `?.`(optional chaining)
	- 값이 없을 수도 있을 때, 런타임 에러 없이 안전하게 접근하기 위한 js/ts 문법
	- `return dog?.tail`에서 
	  만약 dog가 null 혹은 undifiend일 경우 optional chaining으로 인해 
	  undifiend를 return하게 된다.

