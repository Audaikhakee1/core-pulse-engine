from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"status": "Core-Pulse Engine Running"}

# تغيير POST إلى GET لجعل الاختبار من المتصفح سهلاً جداً
@app.get("/deploy")
async def deploy_resource(type: str = "Default", provider: str = "Admin"):
    return {
        "message": f"تم استقبال أمر: {type} بنجاح",
        "status": "Online",
        "executor": provider
    }

# سنبقي الـ POST أيضاً ليعمل الزر في الواجهة
@app.post("/deploy")
async def deploy_post(type: str = "Default", provider: str = "Admin"):
    return {"message": f"تم استقبال أمر POST: {type}", "status": "Success"}
