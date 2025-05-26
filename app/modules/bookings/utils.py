from modules.services.schemas import ServiceReferenceResponseForBookingService

def transform_service_data(booking):
    """Transforms a Booking ORM object into a dictionary format with nested schema."""
    return {
        "id": booking.id,
        "customer_name": booking.customer_name,
        "customer_phone": booking.customer_phone,
        "status": booking.status,
        "service": ServiceReferenceResponseForBookingService(**booking.service.__dict__) if booking.service else None,
        "created_at": booking.created_at,
        "updated_at": booking.updated_at

    }