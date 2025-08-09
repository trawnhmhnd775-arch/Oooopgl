from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def create_button(text, callback_data):
    return InlineKeyboardButton(text, callback_data=callback_data)

def create_keyboard(buttons):
    return InlineKeyboardMarkup(buttons)
  
