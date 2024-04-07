import os
import csv
import anthropic

api_key = os.getenv('ANTHROPIC_API_KEY')

client = anthropic.Anthropic(
    api_key=api_key,
)

mood = "I am stressed"
past_history = "photos_claude_description.csv"

file_history = []
with open(past_history, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        file_history.append(row)


message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0,
    tools=[
        {
            "name": "get_weather",
            "description": "Get the weather at a given location and time",
            "input_schema": {
                "type": "object",
                "properties": {
                    "gps_location": {
                        "type": "string",
                        "description": "GPS location: latitutde and longitude"
                    },
                    "date_photo_taken": {
                        "type": "string",
                        "description": "Date and time of the photo in %Y:%m:%d %H:%M:%S format"
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "The unit of temperature, either \"celsius\" or \"fahrenheit\""
                    }
                },
                "required": ["gps_location", "date_photo_taken", "unit"]
            }
        }
    ],
    system="You are a mood companion to help suggest activities based on user's current location, mood and past location history. ",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/jpeg",
                        "data": "<base64_encoded_image>"
                    }
                },
                {
                    "type": "text",
                    "text": f"This photo was taken at the following GPS location: <latitude>{latitude}</latitude> and <longitude>{longitude}</longitude> on <date_photo_taken>{date_photo_taken}</date_photo_taken>.\n\nBased on GPS location and data/time information, describe the photo in detail to answer the questions listed below. Provide your answers in the corresponding tags noted for each question.\n\n1. Where was this photo taken? <photo_likely_location>\n2. What was the weather like? <weather>\n3. Get the weather given GPS location and date photo taken using get_weather tool. <weather_tool>  \n4. Describe the photo in detail. <photo_description>\n5. How would you describe this photo considering the mood of the person who took it? Answer using 5 adjectives that describe someone's feelings. Use numbered list. Return only the numbered list and no additional text. <feelings>"
                }
            ]
        }
    ]
)
print(message.content)



