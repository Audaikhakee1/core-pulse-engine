from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# تفعيل تصريح العبور العالمي لفك حظر المتصفح
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

# تعديل بسيط ليتوافق مع طلب الواجهة
@app.post("/deploy")
async def deploy_resource(type: str = "Unknown", provider: str = "Demo"):
    return {
        "message": f"تم استقبال أمر: {type} بنجاح من القائد",
        "status": "Success"
    }
