import openai

# Set your OpenAI API key
#openai.api_key = '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'  # Replace with your actual API key

# Function to extract specifications using OpenAI API
def extract_specs(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Choose your model
        messages=[
            {"role": "user", "content": f"Extract the device specifications from the following text: {text}"}
        ]
    )
    return response['choices'][0]['message']['content']

# Read the transcription from the file
with open("D:\\hackathon\\insta-fetcher\\video_audio_files\\transcription.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Call the function to extract specifications
specs = extract_specs(text)

# Print the extracted specifications
print(specs)
