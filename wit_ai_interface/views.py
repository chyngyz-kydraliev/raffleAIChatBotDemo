import settings
from actions_on_user_intents.text_responses import TEXT_RESPONSES
from actions_on_user_intents.actions import ACTIONS
import aiohttp

headers = {
    "Authorization": f"Bearer {settings.WIT_AI_ACCESS_TOKEN}"
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

async def get_according_response(intent):
    if not intent:
        return "Chat bot was not able to understand the message"

    return TEXT_RESPONSES.get(intent, "The bot is not trained to respond to that")


async def perform_according_action(intent):
    if not intent:
        return None
    action = ACTIONS.get(intent)
    
    if callable(action):
        return action()
    else:
        return action or None




