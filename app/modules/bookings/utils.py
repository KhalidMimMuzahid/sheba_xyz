from modules.services.schemas import ServiceReferenceResponseForBookingService

def transform_service_data(booking):
    """Transforms a Booking ORM object into a dictionary format with nested schema."""
    return {
        "id": booking.id,
        "customer_name": booking.customer_name,
        "customer_phone": booking.customer_phone,
        "customer_email": booking.customer_email,
        "status": booking.status,
        "service": ServiceReferenceResponseForBookingService(**booking.service.__dict__) if booking.service else None,
        "created_at": booking.created_at,
        "updated_at": booking.updated_at

    }

def make_html_body(customer_name: str, customer_phone:str, customer_email:str, service_id = int):
    html_body = f"""
    <div style="font-family: Arial, sans-serif; max-width: 600px; margin: auto; padding: 20px; background-color: #f9f9f9; border-radius: 8px; border: 1px solid #e0e0e0;">
        <h2 style="text-align: center; color: #333;">🎉 Booking Confirmed!</h2>
        
        <p style="font-size: 16px; color: #444;">Hi <strong>{customer_name}</strong>,</p>
        
        <p style="font-size: 15px; color: #555;">
            Your service booking has been successfully confirmed. Here are the details:
        </p>
        
        <div style="background-color: #ffffff; padding: 15px; border-radius: 6px; border: 1px solid #ddd; margin-top: 15px;">
            <p><strong>📞 Phone:</strong> {customer_phone}</p>
            <p><strong>📧 Email:</strong> {customer_email}</p>
            <p><strong>🛠️ Service ID:</strong> {service_id}</p>
        </div>

        <p style="font-size: 14px; color: #777; margin-top: 20px;">
            Thank you for choosing our services. We look forward to serving you!
        </p>


        <hr style="margin-top: 30px; border: none; border-top: 1px solid #eee;" />
        <p style="font-size: 12px; color: #aaa; text-align: center;">
            &copy; 2025 Your Company. All rights reserved.
        </p>
    </div>
    """
    return html_body