
from aiogram.filters import Filter
from aiogram.types import Message


class IsSpecificTopicGroup(Filter):
    def __init__(self, chat_id: int, topic_id) -> None:
        self.chat_id = chat_id
        self.topic_id = topic_id
    async def __call__(self, message: Message) -> bool:
        if message.message_thread_id:
            return message.message_thread_id == self.topic_id
        return True
        # return message.chat.id == self.chat_id and self.topic_id is message.message_thread_id


class ChatIdFilter(Filter):
    def __init__(self, chat_id: int) -> None:
        self.chat_id = chat_id
    async def __call__(self, message: Message) -> bool:
        return self.chat_id == message.chat.id
