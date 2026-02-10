from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # تأكد من وجود هذا السطر

app = FastAPI()

# هذه هي الأسطر السحرية التي تحل مشكلة الاتصال
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # يسمح لأي موقع بالحديث مع المحرك
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"status": "Core-Pulse Engine Running"}

@app.post("/deploy")
async def deploy_resource(type: str, provider: str):
    return {"message": f"تم استقبال أمر: {type}", "status": "Success"}
