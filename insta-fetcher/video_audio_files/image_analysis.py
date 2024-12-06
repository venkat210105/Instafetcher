import os
import pandas as pd

# Load the CSV with product details
csv_file_path = 'D:\\hackathon\\insta-fetcher\\electronics_product.csv'
df = pd.read_csv(csv_file_path)

# Directory containing images
images_directory = 'D:\\hackathon\\insta-fetcher\\output_images'

# Process each image in the directory
for image_file in os.listdir(images_directory):
    if image_file.endswith('.jpg'):
        image_path = os.path.join(images_directory, image_file)

        # Extract predicted category from image filename
        try:
            predicted_category = int(image_file.split('_')[-1].split('.')[0])
        except ValueError:
            print(f"Skipping file {image_file} due to unexpected filename format.")
            continue

        # Attempt to match the predicted category with the CSV data
        matched_product = df[df['Category'] == predicted_category]
        
        if not matched_product.empty:
            # Extract and display product details if a match is found
            for _, product_row in matched_product.iterrows():
                print(f"\nImage: {image_file}")
                print(f"Product Name: {product_row['Product Name']}")
                print(f"Main Category: {product_row['Main Category']}")
                print(f"Sub-category: {product_row['Sub-category']}")
                print(f"Predicted Category: {predicted_category}")
                print(f"Ratings: {product_row['Ratings']}")
                print(f"Discount Price: {product_row['Discount Price']}")
                print(f"Actual Price: {product_row['Actual Price']}")
        else:
            # If no match is found, print 'Unknown Product' with available details
            print(f"\nImage: {image_file}")
            print("Product Name: Unknown Product")
            print("Main Category: Unknown Category")
            print("Sub-category: Unknown Sub-category")
            print(f"Predicted Category: {predicted_category}")
            print("Ratings: N/A")
            print("Discount Price: N/A")
            print("Actual Price: N/A")
