from wit_ai_interface import settings
from actions_on_user_intents.text_responses import TEXT_RESPONSES
import aiohttp

headers = {
    "Authorization": f"Bearer {settings.ACCESS_TOKEN}"
}

async def get_user_intents(message_text):
    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"https://api.wit.ai/message?q={message_text}",
            headers=headers
        ) as response:
            data = await response.json()
            print(data)
            intents = data.get("intents")
            return intents

async def get_according_response(intents):
    if not intents:
        return "Chat bot was not able to understand the message"
    
    most_probable_intent = intents[0]["name"]

    return TEXT_RESPONSES.get(most_probable_intent, "The bot is not trained to respond to that")




