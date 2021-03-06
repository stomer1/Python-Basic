def bool_ex(): # bool 자료형
    print("===== bool 연습")
    # 참(True), 거짓(False)
    # 내부적으로 거짓은 0, 나머지는 모두 참으로 판단
    # bool의 판별 방법

    print(bool(0), bool(1))
    a = 1
    print(a > 10) # 논리 연산 or 비교 연산의 결과

    b = a == 1
    print(b, type(b))

    print(b + 10)

    # bool은 bool의 객체인가?
    print(isinstance(True, bool))
    print(isinstance(True, int))

    # bool 캐스팅
    print("정수형:", bool(10), bool(0))
    print("실수형:", bool(3.14), bool(0.0))
    print("문자열:", bool("python"), bool(""))
    print("순차형:", bool([1, 2, 3]), bool([]))
    print("Map:", bool({"a": 2}), bool({}))
    print("None:", bool(None)) # None : Java의 null과 비슷 -> 아무 것도 할당되지 않은 상태
    
    # Circuit Break
    print("CB or 1:", [1, 2, 3] or []) # or는 먼저 나온 True 객체를 선택
    print("CB or 2:", [] or [1, 2, 3])
    print("CB and 1:", [1, 2, 3] and [4, 5, 6]) # and의 경우, 논리식이 참 -> 뒤쪽 객체를 선택
    print("CB and 2:", [1, 2, 3] and []) # and의 경우, 전체의 논리값이 False -> None


def integer_ex(): # 정수형
    print("======== 정수형 연습")
    a = 23 #Literal
    b = int(23) # 타입함수를 이용
    print(a, "is", type(a))
    print(b, "is", isinstance(b, int))

    # 2진, 8진, 16진 정수 표현 가능
    b = 0b1101 #2진수 0b 접두사
    o = 0o23 # 8진수 0o 접두사
    x = 0xFF #16진수 0x 접두사

    print(b, o, x)

    # 3.x에서는 int, long 구분하지 않는다
    #Long 형의 저장크기인 64bit를 초과 하는 정수도 입력 가능
    i = 2 ** 2048
    print(i)
    print(i.bit_length()) # i 객체의 비트 수 확인

    # 진법 변환 함수
    print(bin(2021))
    print(oct(2021))
    print(hex(2021))

def float_ex():
    # 실수형은 모두 float로 표기
    print("========= 실수형 연습")
    a = 3.14159 # 리터럴로 선언
    print(a, "is", type(a))
    b = float(3.0) # 타입 함수를  이용해 생성
    print(b, "는 float의 객체인가?", isinstance(b, float))
    # is_integer : 타입 판별이 아니라 값의 형태가 정수형(소숫점 아래 값이 없는지) 인지 판별
    print(a.is_integer(), b.is_integer())

    # 소수점 포함, e E 지수형태로 표현 가능
    c = 3e3 # 3* 10 ** 3 == 3000.0
    d = -2E-5 #-2 * 10 ** -5 == -0.00002
    print(c, d)
    print(-2E-5 == -0.00002)


def complex_ex(): # 복소수
    print("======== 복소수 연습")
    # 복소수 : 실수부 + 허수부 형태
    a= 4+ 5j  # 실수부 4, 허수부 5인 복소수
    print(a, "is", type(a))
    b = 7-2J # 실수부 7, 허수부 -2인 복소수
    print(b, "complex의 객체?", isinstance(b, complex))

    #복소수 -> 수치형 -> 산술연산
    print(a, b)

    print(a, "실수부?", a.real)
    print(a, "허수부?", a.imag)
    print(a, "의 켤레 복소수?", a.conjugate())

    # 타입 함수를 이용한 복소수의 생성
    c = 7
    d = 3
    e = complex(7, 3) # 실수부 = 7 허수부 = 3 복소수 생성
    print(e, "is", type(e))

def builtin_math_function():    # 내장 수치 함수
    print(abs(-1)) # 절댓값
    print(int(3.14159)) # 타입함수를 이용한 타입의 변환
    print(float(3))     # 타입 변환
    print(complex(1))   # 타입 변환
    print(divmod(5, 3)) # 정수 나눗셈의 몫과 나머지 일괄 계산
    print(pow(2, 10))   # == 2 ** 10



if __name__ == "__main__":
    bool_ex()
    integer_ex()
    float_ex()
    complex_ex()
    builtin_math_function()