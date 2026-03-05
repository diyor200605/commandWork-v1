from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from keyboards.mentor_kb import kb_mentor, kb_role

router = Router()

admin_ids = [459976003]

@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет сучка!💋", reply_markup=kb_role)


@router.message(lambda message: message.text == "Ментор")
async def mentor(message: Message):
    if message.from_user.id in admin_ids:
        await message.answer("Вы ментор", reply_markup=kb_mentor)
    else:
        await message.answer("Вы не ментор\n\n\nДура используй свою роль🖕🏻")



