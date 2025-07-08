
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/kakao-webhook")
async def kakao_webhook(request: Request):
    body = await request.json()
    summary = body.get("summary", "요약된 뉴스가 없습니다.")

    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": f"📢 오늘의 뉴스 요약\n\n{summary}"
                    }
                }
            ]
        }
    }
    return JSONResponse(content=response)
