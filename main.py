from open_ai_interface.views import send_message
from open_ai_interface.prompts import GET_RESPONSE_PROMPT, ADDITIONAL_PARTS_PROMPT
from wit_ai_interface.views import get_user_intents, get_according_response, perform_according_action
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
    previous_message_bot = payload.get("previous_message_bot")
    previous_message_user = payload.get("previous_message_user")


    intents = await get_user_intents(message_text)

    most_probable_intent = intents[0]["name"] if intents else None

    response_to_intent = await get_according_response(most_probable_intent)
    action_to_intent = await perform_according_action(most_probable_intent)

    prompt = GET_RESPONSE_PROMPT.format(message_text, response_to_intent)

    if previous_message_bot and previous_message_user:
        prompt += ADDITIONAL_PARTS_PROMPT.format(previous_message_user, previous_message_bot)

    generate_final_response = await send_message(prompt)
    
    return web.json_response({"response": generate_final_response,
                              "action_performed_result": action_to_intent,
                              "intent": most_probable_intent}, headers=response_headers)


async def render_index(request):
    return web.FileResponse('frontend/index.html')

async def get_image(request):
    if image_name := request.match_info.get('image'):
        return web.FileResponse(f'frontend/image/{image_name}')
    else:
        return web.Response(text='Image not found', status=404)
    

async def get_file(request):
    if file_name := request.match_info.get('frontend'):
        return web.FileResponse(f'frontend/{file_name}')
    else:
        return web.Response(text='File not found', status=404)


app.router.add_post("/chat", handle_message)
app.router.add_options('/chat', handle_message)
app.router.add_get('/frontend/image/{image}', get_image)
app.router.add_get('/app', render_index)
app.router.add_get('/frontend/{frontend}', get_file)



if __name__ == "__main__":
    web.run_app(app, host=settings.HOST, port=settings.PORT)