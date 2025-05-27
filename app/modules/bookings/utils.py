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

def make_html_body(customer_name: str, customer_phone:str, customer_email:str, service_id : int):
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
       <p style="font-size: 12px; color: #999; text-align: center;">
            &copy; 2025 Sheba.xyz. All rights reserved.
        </p>
    </div>
    """
    return html_body


def make_html_body_for_changing_status(customer_name: str, customer_phone:str, customer_email:str, booking_id: int, status: str):
    html_body = f"""
    <div style="font-family: Arial, sans-serif; max-width: 600px; margin: auto; padding: 20px; background-color: #f4f8fb; border-radius: 8px; border: 1px solid #dce3e8;">
        <h2 style="text-align: center; color: #2b3e50;">🔄 Booking Status Updated</h2>
        
        <p style="font-size: 16px; color: #333;">Hello <strong>{customer_name}</strong>,</p>
        
        <p style="font-size: 15px; color: #555;">
            We wanted to let you know that the status of your booking has been updated. Below are the updated details:
        </p>
        
        <div style="background-color: #ffffff; padding: 15px; border-radius: 6px; border: 1px solid #ccc; margin-top: 15px;">
            <p><strong>📞 Phone:</strong> {customer_phone}</p>
            <p><strong>📧 Email:</strong> {customer_email}</p>
            <p><strong>🛠️ Booking ID:</strong> {booking_id}</p>
            <p><strong>📌 New Status:</strong> {status}</p>
        </div>

        <p style="font-size: 14px; color: #666; margin-top: 20px;">
            If you have any questions or need further assistance, feel free to contact us anytime.
        </p>

        <hr style="margin-top: 30px; border: none; border-top: 1px solid #e0e0e0;" />
        <p style="font-size: 12px; color: #999; text-align: center;">
            &copy; 2025 Sheba.xyz. All rights reserved.
        </p>
    </div>
    """
    return html_body
