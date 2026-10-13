from classify import classify_review

# 안전하게 csv 파일 읽기
def read_text_safely(path):
    for enc in ("utf-8", "cp949"):
        try:
            with open(path, "r", encoding=enc) as f:
                f.read()
                return enc
        except UnicodeDecodeError:
            continue
    raise ValueError(f"지원하지 않는 인코딩: {path}")

import pandas as pd

enc = read_text_safely("assignment2/reviews_sample.csv")
df = pd.read_csv("assignment2/reviews_sample.csv", encoding=enc)

stats = {"처리": 0, "실패": 0}
types = {}
for r in df["review_text"]:
    result, type = classify_review(r)
    types[type] = types.get(type,0) + 1
    if result is None:
        stats["실패"] += 1
        continue
    stats["처리"] += 1

print(f"처리 {stats["처리"]}건/ 실패 {stats["실패"]}건")
print(types)