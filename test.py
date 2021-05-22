def define_str():
    str = "Life is too short, You need Python"
    str1 = "Life is too short, You need Python".strip()
    str2 = str1.strip()
    lst = list(str1)
    print(lst, len(lst))
    # 사용된 알파벳 수
    chars = set(str1)
    print(chars, len(chars))
    # 문자열 모두 대문자
    print("대문자:", str.upper())
    # 문자열 내의 공백과 (,)를 제거
    #lst = list(chars)
    #print(lst, len(lst))

    result = sorted(str)
    print(result, len(result))

if __name__ == "__main__":
    define_str()