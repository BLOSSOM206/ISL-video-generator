from fastapi import FastAPI, UploadFile, File
from tasks import process_pdf
import threading
import uuid

app = FastAPI()
job_store = {}

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())
    
    job_id = str(uuid.uuid4())
    job_store[job_id] = "PENDING"
    
    thread = threading.Thread(target=process_pdf, args=(file_path, job_id, job_store))
    thread.start()
    
    return {"job_id": job_id}

@app.get("/status/{job_id}")
def get_status(job_id: str):
    if job_id not in job_store:
        return {"error": "Job not found"}
    return {"job_id": job_id, "status": job_store[job_id]}

@app.get("/download/{job_id}")
def download_video(job_id: str):
    if job_id not in job_store:
        return {"error": "Job not found"}
    job = job_store[job_id]
    if isinstance(job, dict) and job["status"] == "SUCCESS":
        return {"video_path": job["video_path"]}
    return {"error": f"Not ready. Status: {job_store[job_id]}"}