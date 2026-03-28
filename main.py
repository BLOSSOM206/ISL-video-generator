from typing import Any
import pdfplumber
from io import BytesIO
from fastapi import Body, FastAPI, File, HTTPException, UploadFile
from google import genai
import os
from dotenv import load_dotenv
from pydantic import BaseModel
app = FastAPI()

@app.get("/Hello")
async def hello():
    return {"message": "Hello, World!"}


@app.post("/echo")
async def echo(payload: Any = Body(...)):
    return {"echo": payload}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return { "filename":file.filename,
            "content_type": file.content_type,}


#extract text from pdf file
@app.post("/extract_text")
async def extract_text(file: UploadFile = File(...)):
    content = await file.read()
    with pdfplumber.open(BytesIO(content)) as pdf:
        texts = []
        for page in pdf.pages:
            texts.append(page.extract_text() or "")
        text = "".join(texts)
    return {"text": text}


load_dotenv()
genai_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class SimplifyRequest(BaseModel):
    text: str

@app.post("/simplify")
async def simplify(payload: SimplifyRequest):
    try:
        text = payload.text.strip()
        if not text:
            raise HTTPException(status_code=400, detail="Text must not be empty.")

        response = genai_client.models.generate_content(
            model="gemini-2.0-flash",
            contents=text,
            config=genai.types.GenerateContentConfig(
                system_instruction=(
                    "You are a tutor simplifying any document for deaf students "
                    "of any academic background. Use short, simple sentences. Keep technical "
                    "terms but explain them briefly in simple words. Remove jargon. Do not use "
                    "passive voice or complex grammar."
                )
            ),
        )
        return {"simplified_text": response.text}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))