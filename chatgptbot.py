import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


token = '6295550677:AAF5O-jfuFJGyh18JfqOHGIDq5dn4Jpq5AY'
openai.api_key = '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'

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler()
async def send(message: types.Message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.9,
        max_tokens=4000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    await message.answer(response['choices'][0]['text'])

executor.start_polling(dp, skip_updates=True)