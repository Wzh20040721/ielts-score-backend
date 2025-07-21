from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from utils.youdao_api import correct_writing

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ScoreRequest(BaseModel):
    text: str
    grade: str = "ielts_task2"
    title: str = ""
    modelContent: str = ""
    isNeedSynonyms: str = "false"
    correctVersion: str = "advanced"
    isNeedEssayReport: str = "true"

@app.post("/score")
def score_essay(req: ScoreRequest):
    result = correct_writing(
        text=req.text,
        grade=req.grade,
        title=req.title,
        modelContent=req.modelContent,
        isNeedSynonyms=req.isNeedSynonyms,
        correctVersion=req.correctVersion,
        isNeedEssayReport=req.isNeedEssayReport
    )
    if result.get("errorCode") == "0":
        res = result.get("Result", {})
        return {
            "score": res.get("totalScore", 0),
            "majorScore": res.get("majorScore", {}),
            "advice": res.get("essayAdvice", ""),
            "essayFeedback": res.get("essayFeedback", {}),
            "essayReport": res.get("essayReport", {}),
            "allFeatureScore": res.get("allFeatureScore", {}),
            "raw": res
        }
    else:
        return {"error": result.get("errorMsg", "API调用失败"), "raw": result}