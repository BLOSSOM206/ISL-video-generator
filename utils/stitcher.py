from moviepy import VideoFileClip, concatenate_videoclips
import config
def stitch_video(gloss):
    words = gloss.split()  # "CAT SIT MAT" → ["CAT", "SIT", "MAT"]
    clips = []

    for word in words:
        try:
            # build path like "clips/CAT.mp4"
            clip_path = clip_path = f"clips/{word.lower().capitalize()}.mp4"
            # load video clip
            clip = VideoFileClip(clip_path)
            # append to clips list
            clips.append(clip)
            print(f"Loaded clip for word '{word}' from '{clip_path}'")
        except Exception as e:
            print(f"Error loading clip for word '{word}': {e}")
            continue
    
    # concatenate all clips
    final_clip = concatenate_videoclips(clips)
    # write to outputs/
    output_path = "outputs/final_video.mp4"
    final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
    # return output path    
    return output_path