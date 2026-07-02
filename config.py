from dotenv import load_dotenv
import os
import imageio_ffmpeg
import os

os.environ["FFMPEG_BINARY"] = imageio_ffmpeg.get_ffmpeg_exe()

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")