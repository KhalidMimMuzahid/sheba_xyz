
from sqlalchemy.ext.asyncio import AsyncSession
from modules.services.models import Service

async def create_service(db: AsyncSession, name: str, category:str, description:str, price:int ):
     #  making an instance of the Service object that inherits from Service Class (Models class)
    new_service = Service(name=name, category=category, description=description, price=price )
    db.add(new_service)
    await db.commit()
    await db.refresh(new_service)

    return {
          "id" : new_service.id,
          "name" :new_service.name,
          "category" :new_service.category,
          "description" :new_service.description,
          "price" :new_service.price,
    }


