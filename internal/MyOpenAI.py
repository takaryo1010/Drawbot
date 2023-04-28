import openai
import requests

def organizingAI(api_key, organization, inputs_translated):
    openai.api_key = api_key
    openai.organization = organization
    text = "You are a professional painter. Please output only the best picture image statement in a short sentence from the following words"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "assistant", "content": text},
            {"role": "assistant", "content": inputs_translated}

        ]
    )
    return response.choices[0]["message"]["content"].strip()

def drawAI(api_key, organization,response_AI):
    openai.api_key = api_key
    openai.organization = organization
    response = openai.Image.create(
        prompt = response_AI,
        n = 1,
        size = "1024x1024"
    )
    image_url = response['data'][0]['url']
    image_data = requests.get(image_url).content
    
    with open("Drawbot.jpg","wb")as f:
        f.write(image_data)