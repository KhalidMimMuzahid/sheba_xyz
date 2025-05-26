
def make_html_body(name: str, email:str,  password:str, role: str):
    html_body = f"""
    <div style="font-family: Arial, sans-serif; max-width: 600px; margin: auto; padding: 20px; background-color: #f4f4f4; border-radius: 8px; border: 1px solid #ddd;">
        <h2 style="text-align: center; color: #2d2d2d;">👮 Welcome to Sheba.xyz</h2>

        <p style="font-size: 16px; color: #333;">
            Hello <strong>{name}</strong>,
        </p>

        <p style="font-size: 15px; color: #444;">
            Your account has been successfully registered in the <strong>AI Policing System</strong>.
        </p>

        <div style="background-color: #ffffff; padding: 15px; border-radius: 6px; border: 1px solid #ccc; margin-top: 15px;">
            <p><strong>📧 Email:</strong> {email}</p>
            <p><strong>🔒 Password:</strong> {password}</p>
            <p><strong>🧑‍💼 Role:</strong> {role}</p>
        </div>

        <p style="font-size: 14px; color: #555; margin-top: 20px;">
            Please keep this information secure. You can now log in and begin using the system.
        </p>



        <hr style="margin-top: 30px; border: none; border-top: 1px solid #e0e0e0;" />
        <p style="font-size: 12px; color: #999; text-align: center;">
            &copy; 2025 Sheba.xyz. All rights reserved.
        </p>
    </div>
    """