
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from modules.users.models import User
from exceptions.models import CustomError
from exceptions.models import CustomError
from utils.manage_auth import generate_passwd_hash, verify_password, create_access_token
from utils.send_mail import send_email, EmailSchema
from utils.model_to_dict import model_to_dict
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
    is_sent=await send_email(EmailSchema(
        receiver_email=email,
        subject="Welcome to Sheba.xyz, user Registration Successful",
        html_body = make_html_body(name=name, email=email,  password=password, role=new_user.role.value)
    )) 
    # print("email has sent successfully" if is_sent else "email has not sent somehow")
    access_token = create_access_token(
        user_data= {
            "id": new_user.id,
            "email": new_user.email,
            "role": new_user.role.value
        }
    )
    new_user = model_to_dict(new_user)
    new_user["access_token"] = access_token
    return new_user



async def login_user_service(db: AsyncSession, email:str, password:str):
    result = await db.execute(select(User).where(User.email== email))
    user_data = result.scalars().first()
    if user_data is None:
        raise CustomError(status_code=401, message="no user found with this email", resolution= "enter a new email")
    password_is_valid = verify_password(password= password, hash= user_data.password)
    if not password_is_valid:
        raise CustomError(status_code=401, message="Invalid Password", resolution= "enter a correct password")
    access_token = create_access_token(
        user_data= {
            "id": user_data.id,
            "email": user_data.email,
            "role": user_data.role.value
        }
    )
    login_data = model_to_dict(user_data)
    login_data["access_token"] = access_token
    return login_data