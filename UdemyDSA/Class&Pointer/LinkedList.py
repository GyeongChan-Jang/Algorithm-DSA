head = {
    "value": 11,
    "next": {
        "value": 3,
        "next": {
            "value": 23,
            "next": {
                "value": 7,
                "next": None
            }
        }
    }
}

print(head['next']['next']['value'])

# under the hood
# 자동차 후드 아래에서 벌어지는 일이라는 의미였네요. 그거 몰라도 운전하는데 지장 없지만, 제대로 할려면 원리를 알 필요가 있는. 첨부된 링크에 있는 위 답변이 가장 직관적이고 이해가 잘 되네요.
