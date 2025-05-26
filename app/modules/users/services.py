
from sqlalchemy.ext.asyncio import AsyncSession
from modules.users.models import User
from exceptions.models import CustomError
from exceptions.models import CustomError
from utils.manage_auth import generate_passwd_hash
from utils.send_mail import send_email, EmailSchema
from modules.users.utils import make_html_body



async def create_user(db: AsyncSession, email :str, name :str, password :str):
    password_hash= generate_passwd_hash(password)
    new_user = User(email =email,name =name,password =password_hash)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    if not new_user:
        raise CustomError(status_code=401, message="Something Went Wrong")
    
    # sending mail to the user
    # is_sent=await send_email(EmailSchema(
    #     receiver_email=email,
    #     subject="Welcome to Sheba.xyz – user Registration Successful",
    #     html_body = make_html_body(name, email,  password, role=new_user.role)
    # )) 
    # print("email has sent successfully" if is_sent else "email has not sent somehow")
    return new_user
