from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# تصريح المرور العالمي (إصلاح مشكلة الـ CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # يسمح لأي واجهة بالاتصال
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"status": "Core-Pulse Engine Running", "version": "1.0.0-Alpha"}

@app.post("/deploy")
async def deploy_resource(type: str, provider: str):
    return {
        "message": f"تم استقبال أمر: {type} عبر مزود: {provider}",
        "status": "Success"
    }
