# pip install pymongo
import pymongo
from pymongo import MongoClient

# 접속 함수
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
        {"name": "고길동", "hp": "010-10**-23**", "tel": "02-43**-90**"},
        {"name": "도우너", "hp": "010-55**-55**", "tel": "02-43**-90**"},
        {"name": "마이콜", "hp": "010-99**-77**", "tel": "02-43**-90**"},
        {"name": "또치", "hp": "010-88**-90**", "tel": "02-43**-90**"},
        {"name": "남승균", "hp": "010-98**-14**", "tel": "02-9**-98**"}
    ])

    print(xs.inserted_ids)
    print(len(xs.inserted_ids), "개 레코드 삽입되었음")

def test_project():
    print("****************************")
    print("*    전화번호 관리 프로그램    *")
    print("****************************")
    print("1.리스트 2.등록 3.삭제 4.검색 5.종료")
    print("-------------------------------")
    print(">메뉴번호:")

from datetime import datetime
def test_update():
    # address == "서울"인 문서
    # method -> update, modified_at -> 현재 시간
    coll = test_collection()

    xs = coll.update_many({ "address": "서울"}, # 조건)
                          { '$set': {
                              "method": "update",
                              "modified_at": datetime.now()
                          }}
                          )
    print(xs.matched_count, "개가 매칭 되었습니다") # 조건에 맞는 문서의 개수
    print(xs.modified_count, "개가 갱신 되었습니다") # 실제 변경된 문서 개수


def test_select_by_filter(filter={}, projection={}):
    """
    db.collection.find({ 조건 }, { projection })
        프로젝션은 값 1: 표시, 값 0, 표시 X
    """
    coll = test_collection()
    docs = coll.find(filter, projection)

    for doc in docs:
        print(doc)
def test_delete_by_filter(filter = {}):
    coll = test_collection()
    xs = coll.delete_many(filter)
    print(xs.deleted_count, "개의 레코드가 삭제!")
import re # 정규표현식 객체
if __name__ == "__main__":
#    test_connect()
#    test_insert()
#    test_insert_many()
#    test_update()
#   test_select_by_filter(projection={
#       "name": 1, "address": 1, "_id": 0
#   }) # filter={}, projection={}
    # SELECT * FROM 테이블 WHERE 컬럼 LIKE ->
    # 정규식을 이용, 패턴 전달
#    filter = re.compile(r"길동")
#    """
#    db.pymongo.find({"name": /길동/}, { "name": 1, "_id": 0})
#   """
#   test_select_by_filter({ "name": filter},
#                          { "name": 1}, {"_id": 0})
    # address == "서울"인 문서들 삭제
    #test_delete_by_filter({"address": "서울"})
    # db.pymongo.delete({"address": "서울"})
    # 전체 문서 삭제
    #db.pymongo.delete({})
#    test_delete_by_filter()
    test_project()


