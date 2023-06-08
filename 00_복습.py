"""# Hello World!"""

# Hello, world! 를 출력

"""* ' '(작은따옴표)로 묶은 부분 = 문자열
* `print`는 값을 화면에 출력

* `print`처럼 단어 뒤에 ( )(괄호)가 붙은 것 = 함수(function) : 정해진 일을 수행하는 단위
* 함수는 `print('Hello, world!')`와 같이 함수 이름 `print`를 써주고, 괄호 안에 출력할 내용을 넣으면 함수가 실행
* 함수 실행을 다른 말로는 함수를 호출(call)한다고 말하기도 함

# 기본 문법

## 세미콜론 (;)
* 많은 프로그래밍 언어들은 구문이 끝날 때 ;(세미콜론)을 붙여야 함 (JAVA, C...)
* 하지만 파이썬은 세미콜론을 붙이지 않음
"""



"""* 단, 세미콜론을 붙여도 문법 에러는 발생하지 않음
* 보통 한 줄에 여러 구문을 사용할 때 세미콜론으로 구분

"""



"""## 주석
* 파이썬에서 사람만 알아볼 수 있도록 작성하는 부분을 *주석(comment)*라고 함
* 즉, 주석은 파이썬 인터프리터(실행기)가 처리하지 않으므로 프로그램의 실행에는 영향을 주지 않음
* 보통 주석은 코드에 대한 자세한 설명을 작성하거나, 특정 코드를 임시로 사용하지 않도록 만들 때 사용
* 주석은 **한 줄 주석**과 **블록 주석** 두 가지가 있음

### 한 줄 주석
"""

# Hello, world! 출력

"""* 코드 맨 앞에 #을 사용하면 해당 줄은 모두 주석이 됨
* 따라서 다음 `print` 함수는 동작하지 않음
"""



"""* 코드 뒤에 #으로 주석을 작성할 수도 있음
* 이때는 앞에 있는 코드만 정상적으로 동작하며 # 뒤에 있는 코드는 동작하지 않음
"""



"""* Colab에서의 주석 단축키 : `Ctrl + /`

### 블록 주석
"""

# 작은따옴표

# 큰따옴표

"""## 들여쓰기
* 들여쓰기는 코드를 읽기 쉽도록 일정한 간격을 띄워서 작성하는 방법, 특히 파이썬은 들여쓰기 자체가 문법
* 예를 들어 if의 다음 줄은 항상 들여쓰기를 해야 함
* 만약 들여쓰기를 하지 않으면 문법 에러이므로 코드가 실행되지 않음
"""





"""* 파이썬에서 들여쓰기 방법은 공백(스페이스) 2칸, 4칸, 탭(tab) 등 여러 가지 방법이 있음

## 코드 블록
* 코드 블록은 특정한 동작을 위해서 코드가 모여 있는 상태를 뜻하며 파이썬은 들여쓰기를 기준으로 코드 블록을 구성
"""



"""* 단, 같은 블록은 들여쓰기 칸 수가 같아야 함"""

print("hi")

print("hi")
print("hi")
print("hi")
