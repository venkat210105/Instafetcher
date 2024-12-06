import whisper

def transcribe_audio_to_text(audio_file, output_file):
    # Load the Whisper model (choose from "tiny", "base", "small", "medium", or "large")
    model = whisper.load_model("small")

    # Transcribe the audio file
    result = model.transcribe(audio_file)

    # Extract text from the result
    transcribed_text = result["text"]
    
    # Split the transcribed text into multiple lines (assuming each sentence ends with a period)
    lines = transcribed_text.split('. ')
    
    # Write the lines to the output text file
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line.strip() + '\n')  # Write each line to the file

# Example usage
audio_file_path = r"D:\hackathon\video_audio_files\instagram_audio.mp3"
output_file_path = r"D:\hackathon\insta-fetcher\video_audio_files\audio_extract.txt"
transcribe_audio_to_text(audio_file_path, output_file_path)
