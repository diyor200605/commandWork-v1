from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


kb_mentor = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="👥 Мои студенты"), KeyboardButton(text="Статистика")],
        [KeyboardButton(text="📝Проверить задания")]
    ],
    resize_keyboard=True,
)

kb_role = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Ментор", callback_data="mentor")],
        [InlineKeyboardButton(text="Студент", callback_data="student")],
        [InlineKeyboardButton(text="Админ", callback_data="admin")]
    ]
)