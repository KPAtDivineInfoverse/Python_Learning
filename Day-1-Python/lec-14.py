import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyDDDX39h_9tNE3o5Mv3Awj8ZluRrqckhJI")

# Use the correct model
model = genai.GenerativeModel("gemini-1.5-flash")

# Generate content
response = model.generate_content("how to make add to cart in laravel mysql")

# Print response
print(response.text)
