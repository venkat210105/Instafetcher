from moviepy.editor import VideoFileClip
import yt_dlp
import os

def download_instagram_audio(post_url):
    # Directory for audio and video files
    output_dir = "video_audio_files"
    os.makedirs(output_dir, exist_ok=True)

    # Define file paths in output directory
    video_filename = os.path.join(output_dir, "instagram_video.mp4")
    audio_filename = os.path.join(output_dir, "instagram_audio.mp3")
    
    # yt-dlp options for downloading video
    ydl_opts = {
        'format': 'best',
        'outtmpl': video_filename,  # Download video to output directory
    }

    # Download video using yt-dlp
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([post_url])
    
    # Extract audio from video
    try:
        video_clip = VideoFileClip(video_filename)
        video_clip.audio.write_audiofile(audio_filename)
        video_clip.close()
        print(f"Audio downloaded and saved as {audio_filename}")
    except Exception as e:
        print(f"Error extracting audio: {e}")

# Example usage
post_url = "https://www.instagram.com/p/C-ZgW-GiRok/"
download_instagram_audio(post_url)
