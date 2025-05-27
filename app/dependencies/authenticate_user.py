from fastapi import Request, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from app.utils.manage_auth import decode_access_token
from app.exceptions.models import CustomError
from urllib.parse import urlparse

# Define security scheme
security = HTTPBearer(auto_error=False)

# Define included routes that require authentication
PRIVATE_ROUTES = {
    "/api/v1/services/add-service",
    "/api/v1/services/delete-service",
    "/api/v1/services/update-service", 
    "/api/v1/services/get-bookings",
    "/api/v1/bookings/update-booking-status"
    # Add more private routes here
}

# Define the user payload structure
class TokenData(BaseModel):
    email: str
    id: str
    role: str

async def authenticate_user(
    request: Request, credentials: HTTPAuthorizationCredentials = Security(security)
):
    """Middleware-style function for authenticating users before hitting the router."""
    # path = request.url.path 

    path = urlparse(request.url.path).path  # Extract path without query parameters
    # print("path: ", path)
    # Only allow access if the path is in private routes
    if path not in PRIVATE_ROUTES:
        return  # Return early or skip auth if the path is NOT private

    # Extract JWT from the Authorization header
    token = credentials.credentials if credentials else None
    if not token:
        raise CustomError(message= "access_token is required", status_code=403, resolution="please provide a token")

    # Decode and validate the token
    token_data = decode_access_token(token)

    auth=token_data["auth"]
    if not auth:
        raise CustomError(message= "no enough data has provided in this token", status_code=401)
    # Validate required claims
    if not all(k in auth for k in ["email", "id", "role"]):
        raise CustomError(message= "no enough data has provided in this token", status_code=401)

    # Attach user data to the request for further use
    request.state.user = auth
