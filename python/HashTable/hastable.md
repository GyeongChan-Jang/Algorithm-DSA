# Hash Table은 효율적인 탐색(빠른 탐색)을 위한 자료구조로써 key-value 쌍의 데이터를 입력 받음

# hash function h에 key값을 입력으로 넣어 얻은 해시값 h(k)를 위치로 지정하여 key-value 데이터 쌍을 저장

# 저장, 삭제, 검색의 시간복잡도는 모두 O(1)

# 충돌 해결 방법

# 1. Open Addressing

# 바로 다음 인덱스에 저장

# 2. Separate Chaining

# 파이썬에서는 Hash Table이 Dictionary로 구현되어 있음
