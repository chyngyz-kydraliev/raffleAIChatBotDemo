import settings
from aiohttp import ClientSession


headers = {
    "Authorization": f"Bearer {settings.OPEN_AI_API_KEY}",
    "Content-Type": "application/json"
}


async def _send_request(url, method, data=None):
    async with ClientSession() as session:
        async with session.request(
            method, url, headers=headers, json=data
        ) as response:
            return await response.json()


async def send_message(prompt):
    response = await _send_request(
        "https://api.openai.com/v1/chat/completions",
        method="POST",
        data={
            "model": settings.OPEN_AI_MODEL,
            "messages": [
                {"role": "system", "content": prompt}
            ],
            "max_tokens": 3500,
        }
    )
    print(response)

    return response["choices"][0]["message"]["content"]
