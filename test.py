def define_str():
    str = "Life is too short, You need Python"
    str1 = "Life is too short, You need Python".strip()
    str2 = str1.strip()
    # 문자열 내의 공백과 (,)를 제거
    print("공백, 콤마제거:", str.replace(" ", "", ).replace(",", ""))
    # 문자열 모두 대문자
    print("대문자:", str.upper())
    # 문자열 모두 소문자
    print("소문자:", str.lower())

    lst = list(str)
    print(lst, type(lst))
    # 사용된 알파벳 수
    chars = set(lst)
    print(chars, type(chars))

    lst = list(chars)
    print(lst, type(lst))

    lst.sort()
    print(lst, len(lst))

def define_set():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    slice = lst[3:7]
    slice = slice[::-1]
    lst[3:7] = slice

    print(lst)
    print(slice, type(slice))

    #lst.insert(3, slice)
    print(lst)
    #lst[3] = slice
    #print(lst)



def define_quiz():

    students = [
        {
            "name": "Kim",
            "kor": 80,
            "eng": 90,
            "math": 80
        },
        {
            "name": "Lee",
            "kor": 90,
            "eng": 85,
            "math": 85
        }
    ]
    print("합계:", sum(students))
def quiz():
    # 연습문제 1. 2단 ~ 9단까지 구구표 출력
    for i in range(2, 10):
        for x in range(1, 10):
            print(i, "X", x, "=", i * x)
    # 연습문제 2. 삼각형 그리기
    """
    *
    **
    ***
    ****
    *****
    """
    for i in range(0, 5):
        i += 1
        print("*"*i)

    sum = 0
    num = int(input("수를 입력하세요"))

    message = "1부터 100까지 3의 배수의 합"
    for n in range(0, 100):
        if n % 3 == 0:
            sum += n
            print(sum)
        else:
            print("정수가 아닙니다. 다시 입력하세요")

def quiz1():
    lst = (80, 75, 90, 95, 85)
    print("SUM:", sum(lst))
    print("MIN:", min(lst))
    print("MAX:", max(lst))
    print("AVERAGE:", sum(lst) / len(lst))
    print("SUM:", sum(lst),"MIN:", min(lst), "MAX:", max(lst), "AVERAGE:", sum(lst) / len(lst))

def quiz2():
    s = """We encourage everyone to contribute to Python. 
    If you still have questions after reviewing the material
    in this guide, then the Python Mentors 
    group is available to help guide new contributors through the process."""

    print("제거:", s.replace(",", ""), s.replace(".", ""), s.replace(" ", ""), s.upper())
    #print("대문자:", s.upper())


if __name__ == "__main__":
    #define_str()
    define_set()
    #define_quiz()
    #quiz()
    #quiz1()
    #quiz2()