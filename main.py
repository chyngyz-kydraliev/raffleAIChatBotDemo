from wit_ai_interface.views import get_user_intents, get_according_response
from open_ai_interface.views import send_message
from open_ai_interface.prompts import GET_RESPONSE_PROMPT
import asyncio
from aiohttp import web
import settings


app = web.Application()


async def handle_message(request):
    response_headers = {}

    response_headers['Access-Control-Allow-Origin'] = '*'
    response_headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    response_headers['Access-Control-Allow-Headers'] = 'Content-Type'

    if request.method == "OPTIONS":
        return web.Response(headers=response_headers)

    payload = await request.json()
    message_text = payload.get("message_text")
    intents = await get_user_intents(message_text)
    response_to_intent = await get_according_response(intents)
    prompt = GET_RESPONSE_PROMPT.format(message_text, response_to_intent)
    generate_final_response = await send_message(prompt)
    
    return web.json_response({"response": generate_final_response}, headers=response_headers)


async def render_index(request):
    return web.FileResponse('frontend/index.html')


app.router.add_post("/chat", handle_message)
app.router.add_options('/chat', handle_message)
app.router.add_get('/', render_index)


if __name__ == "__main__":
    web.run_app(app, host=settings.HOST, port=settings.PORT)