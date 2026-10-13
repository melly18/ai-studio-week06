import random

def mock_llm_call(system, user_message, temperature=0.2, max_tokens=500):
    reviews_keywords = {
        "배송" : '{"category": "배송", "sentiment": "긍정", "score": 4}',
        "환불" : '{"category": "환불", "sentiment": "부정", "score": 2}',
        "품질" : '{"category": "품질", "sentiment": "긍정", "score": 5}'
    }
    present = 0  # keyword의 존재를 알려주는 변수. 분류를 위해 쓰인다.
    for keyword, canned in reviews_keywords.items():
        if keyword in user_message and present == 0:  # 이전에 분류되지 않았고 키워드가 등장했다면
            result =  {"text": canned, "stop_reason": "end_turn",
                    "usage": {"input_tokens": 120, "output_tokens": 35}}
            present = 1  # 분류되었음을 표시
    if present == 0:
        result = {"text": '{"category": "기타", "sentiment": "중립", "score": 3}',
                    "stop_reason": "end_turn",
                    "usage": {"input_tokens": 120, "output_tokens": 35}}
    
    # 20%확률로 3가지 답변 중 무작위로 불량 응답을 만든다.
    rand = random.random()
    type = "normal"  # 응답의 유형도 저장한다.
    prob = 0.2/3
    if rand < prob:
        result["text"] = "```json\n" + result["text"] + "\n```"  # 코드펜스 포함
        type = "codefence"
    elif rand < prob * 2:
        result["text"] = "물론입니다! 분석 결과는 다음과 같습니다.\n" + result["text"]  # 사족 포함
        type = "comment"
    elif rand < prob * 3:
        result["text"] = result["text"][:-20]  # 잘린 JSON
        type = "split"
    return result, type