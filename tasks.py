from utils.extractor import extract_text_from_pdf
from utils.simplifier import simplify_text
from utils.glosser import gloss_text
from utils.stitcher import stitch_video

def process_pdf(file_path, job_id, job_store):
    try:
        job_store[job_id] = "PROCESSING"
        text = extract_text_from_pdf(file_path)
        simple_text = simplify_text(text)
        gloss = gloss_text(simple_text)
        gloss = gloss_text(simple_text)
        print("GLOSS OUTPUT:", gloss)  # ← add this
        video_path = stitch_video(gloss)
        video_path = stitch_video(gloss)
        job_store[job_id] = {"status": "SUCCESS", "video_path": video_path}
    except Exception as e:
        job_store[job_id] = {"status": "FAILED", "error": str(e)}