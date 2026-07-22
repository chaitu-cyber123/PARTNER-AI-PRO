import base64
import requests

from config import API_KEY, BASE_URL, MODEL


def encode_image(image_path):
    with open(image_path, "rb") as image:
        return base64.b64encode(image.read()).decode("utf-8")


def analyze_image(image_path, question="Describe this image"):

    try:
        image_data = encode_image(image_path)

        payload = {
            "model": MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": question
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{image_data}"
                            }
                        }
                    ]
                }
            ],
            "max_tokens": 500
        }

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:5000",
            "X-Title": "Partner AI"
        }


        for attempt in range(3):

            try:
                response = requests.post(
                    BASE_URL,
                    headers=headers,
                    json=payload,
                    timeout=120
                )

                break

            except requests.exceptions.SSLError:

                if attempt == 2:
                    return "Vision connection failed. Please try again."


        data = response.json()


        if "error" in data:
            return f"Vision error: {data['error']}"


        return data["choices"][0]["message"]["content"]


    except FileNotFoundError:
        return "Image file not found."


    except Exception as e:
        return f"Vision error: {str(e)}"
