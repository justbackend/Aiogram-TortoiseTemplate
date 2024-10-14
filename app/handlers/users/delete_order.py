from pyexpat.errors import messages

from aiogram import F, Router, Bot
from aiogram.types import CallbackQuery

from app.config import settings

user_router = Router()



@user_router.callback_query(F.data.startswith('delete'))
async def send_message_to_group(call: CallbackQuery, bot: Bot):
    data = call.data.split('-')
    message_id = data[1]
    await bot.delete_message(chat_id=settings.LORRY_CHAT_ID, message_id=int(message_id))
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("Muvaffaqiyatli o'chirildi")


