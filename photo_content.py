import os
import anthropic

api_key = os.getenv('ANTHROPIC_API_KEY')

client = anthropic.Anthropic(
    api_key=api_key,
)

latitude, longitude, date_photo_taken = 37.7600027777778, -122.426941666667, "2023:11:11 16:55:35"


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
    system="You are an excellent visual assistant to describe photos in detail. You make note of people, animals, objects, landmarks etc in the photo. GPS location for the photo taken is provided in <latitude> and <longitude> tags. Date and time of the photo are provided in <date_photo_taken> tag. Make best effort to infer the most likely semantic location given the coordinates. Semantic location may refer to a business premise such as coffee shop, bookstore, movie theater, touristic spot etc.If there are multiple options, pick the option that matches a specific place (e.g., Blue Bottle Coffee) instead of generic location (e.g., a coffee shop).",
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



