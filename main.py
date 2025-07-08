from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

@app.post("/kakao-webhook")
async def kakao_webhook(req: Request):
    data = await req.json()
    summary = data.get("summary", "요약 정보가 없습니다.")

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

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=10000)
