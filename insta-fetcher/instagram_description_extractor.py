import re
import requests
import csv
import nltk
from nltk.tokenize import word_tokenize

# Ensure NLTK data is downloaded
nltk.download('punkt')

# Function to fetch media IDs
def fetch_media_ids(access_token):
    url = f"https://graph.instagram.com/me/media?fields=id&access_token={access_token}"
    response = requests.get(url)
    if response.status_code == 200:
        return [item['id'] for item in response.json().get('data', [])]
    else:
        print(f"Failed to fetch media IDs: {response.status_code}")
        return []

# Function to fetch media description
def fetch_media_description(media_id, access_token):
    url = f"https://graph.instagram.com/{media_id}?fields=caption&access_token={access_token}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data.get('caption', '')  # Get the caption from the response
    else:
        print(f"Failed to fetch media description: {response.status_code}")
        return None

# Function to extract product information
def extract_product_info(description):
    # Define keywords for extraction
    keywords = {
        'brand': r'(?i)\b(Titan|Rolex|Casio|Seiko|Fossil)\b',
        'model': r'(?i)\bmodel\b:?\s*(\w+)',
        'price': r'(?i)\bprice\b:?\s*(\d+)',
        'features': r'(?i)\bfeatures\b:?\s*(.*?)(?:\n|$)',
        'tags': r'(?i)#\w+',
    }

    extracted_info = {
        'brand': None,
        'model': None,
        'price': None,
        'features': None,
        'tags': []
    }

    for key, pattern in keywords.items():
        if key == 'tags':
            extracted_info[key] = re.findall(pattern, description)
        else:
            match = re.search(pattern, description)
            if match:
                extracted_info[key] = match.group(0)

    return extracted_info

# Function to save product info to a CSV file
def save_to_csv(product_info):
    with open('product_info.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([product_info['brand'], product_info['model'], product_info['price'], ', '.join(product_info['tags'])])

# Replace with your actual media ID and access token
access_token = 'IGQWRQM204NlpLdWpnS2tTOFlrdWx3a0I0ZAF9oM3U1X19sTlRTb2VPTmdQaGNZAUTJyeTRKTlpPSE45eENMMVNLR2xUWl9Lcy1uNHVsZAlRmWGtIT0haR0kteW5HLW93MGgxV2hXOFI5LW1NdHF0dGRVOXJpLVNSUzQZD'

# Fetch media IDs
media_ids = fetch_media_ids(access_token)

# Loop through each media ID to fetch descriptions and extract information
for media_id in media_ids:
    description = fetch_media_description(media_id, access_token)
    if description:
        # Extract product info from the fetched description
        product_info = extract_product_info(description)
        print(product_info)  # Print for debugging
        # Save the extracted product info
        save_to_csv(product_info)
    else:
        print("No description available to extract product info.")