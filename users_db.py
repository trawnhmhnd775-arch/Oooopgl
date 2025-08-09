# قاعدة بيانات مؤقتة لتخزين معلومات المستخدمين
users_db = {}

def add_user(user_id, username, balance=0):
    users_db[user_id] = {"username": username, "balance": balance}

def get_user(user_id):
    return users_db.get(user_id)

def update_balance(user_id, amount):
    if user_id in users_db:
        users_db[user_id]["balance"] += amount
