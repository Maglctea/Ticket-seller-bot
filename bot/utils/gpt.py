import openai
from bot.settings import GPT_TOKEN


async def send_to_gpt(text: str) -> str:
    """
    Sends a GPT connection and returns a response

    :param text: str:
    :return: str
    """
    openai.api_key = GPT_TOKEN

    response = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Вы - продавец авиабилетов."},
            {"role": "user", "content": text}
        ]
    )

    return response.choices[0].message["content"].strip()
