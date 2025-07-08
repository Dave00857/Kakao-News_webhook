import schedule
import time
import requests
from datetime import datetime

WEBHOOK_URL = "https://jungdaily-news.onrender.com/kakao-webhook"  # ← 실제 Render 주소로 교체

def generate_summary():
    return (
        f"🗓️ {datetime.now().strftime('%m월 %d일')} 뉴스 요약\n"
        "📌 국내: 한은, 기준금리 동결\n"
        "📌 국제: 나토 회의, 우크라 지원 확대\n"
        "💡 시사점: 방산·금리 민감주 영향 예상"
    )

def send_news():
    summary = generate_summary()
    payload = { "summary": summary }
    res = requests.post(WEBHOOK_URL, json=payload)
    print(f"[{datetime.now()}] 뉴스 발송 결과: {res.status_code}")

schedule.every().day.at("06:30").do(send_news)

if __name__ == "__main__":
    print("뉴스 발송 스케줄러 실행 중...")
    while True:
        schedule.run_pending()
        time.sleep(60)
