import user_info_evening as user
from bot import Bot

instance = Bot(user.email, user.password, user.attendance_link)
instance.mark_attendance()
