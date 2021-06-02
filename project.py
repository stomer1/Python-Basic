
from pymongo import MongoClient



def connect():
    client = MongoClient("mongodb://localhost:27017")
    return client

def test_connect():
    conn = connect()
    #print(dir(conn))
    print("데이터베이스:")
    for db in conn.list_database_names():
        print(db)


def test_collection():
    # 접속
    conn = connect()
    # 사용할 데이터베이스 선택
    db = conn['mydb'] # use mydb
    # 컬렉션 선택
    coll = db['pymongo']
    return coll

def test_insert():
    # 컬렉션 확보
    coll = test_collection()

    # 한개 문서 삽입
    x = coll.insert_one({
        "name": "홍길동",
        "address": "서울"
    }) # 새로 생성된 Document의 _id를 반환

    # 결과 확인
    print(x.inserted_id)



def test_insert_many():
    coll = test_collection()

    xs = coll.insert_many([
        {"name": "고길동", "hp": "010-10**-23**", "tel": "02-43**-90**", "method": "insert_many"},
        {"name": "도우너", "hp": "010-55**-55**", "tel": "02-43**-90**", "method": "insert_many"},
        {"name": "마이콜", "hp": "010-99**-77**", "tel": "02-43**-90**", "method": "insert_many"},
        {"name": "또치", "hp": "010-88**-90**", "tel": "02-43**-90**", "method": "insert_many"},
        {"name": "남승균", "hp": "010-98**-14**", "tel": "02-9**-98**"}
    ])

    print(xs.inserted_ids)
    print(len(xs.inserted_ids), "개 레코드 삽입되었음")


if __name__ == "__main__":
#    connect()
#    test_connect()
#    test_collection()
#    test_insert()
#    test_insert_many()