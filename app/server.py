from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "healthy 👀"}

@app.post("/upload")
def upload_file(file: UploadFile = File(...)):

    print(f"Received file: {file}")
    return {"message": "Upload endpoint"}

