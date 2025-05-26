from sqlalchemy.ext.asyncio import AsyncSession
from modules.services.models import Service
from utils.query_builder import query_builder
from sqlalchemy.future import select
from exceptions.models import CustomError
from modules.bookings.models import Booking

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


async def get_services(db: AsyncSession, page:int, limit:int, category:str):
    filters= {"category": category} # Dynamic filters
    return await query_builder(
        db=db,
        model=Service,
        filters=filters,
        page=page,
        limit=limit
    )

async def delete_service(db: AsyncSession, id: str):
    result = await db.execute(select(Service).filter(Service.id == id))
    service = result.scalars().first()
    if not service:
        raise CustomError(
            status_code=404, 
            message="No service found with this ID",
            resolution="Please provide a valid service ID"
        )
    # Fetch related entity
    bookings = await db.execute(select(Booking).filter(Booking.service_id == id))

    # Convert scalars to lists
    bookings = bookings.scalars().all()

    # Delete all related entities
    for entity in bookings:
        await db.delete(entity)

    # Delete the Service itself
    await db.delete(service)
    await db.commit()
    return None