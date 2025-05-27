import pytest

# Module‐level variables to carry state between tests
auth_token = None
service_id = None
booking_id = None

@pytest.mark.asyncio
async def test_1_register_user(client):
    global auth_token
    payload = {
        "name": "Test User",
        "email": "testuser@example.com",
        "password": "password123"
    }
    resp = await client.post("/api/v1/users/register-user", json=payload)
    assert resp.status_code == 200, resp.text
    body = resp.json()
    assert body["is_success"] is True

@pytest.mark.asyncio
async def test_2_login_user(client):
    global auth_token
    params = {
        "email": "testuser@example.com",
        "password": "password123"
    }
    resp = await client.get("/api/v1/users/login", params=params)
    assert resp.status_code == 200, resp.text
    body = resp.json()
    assert body["is_success"] is True
    auth_token = body["data"]["access_token"]
    assert isinstance(auth_token, str) and len(auth_token) > 0

@pytest.mark.asyncio
async def test_3_add_service(client):
    global service_id
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {
        "name": "Test Service",
        "category": "testing",
        "description": "Used for unit tests",
        "price": 100
    }
    resp = await client.post("/api/v1/services/add-service", json=payload, headers=headers)
    assert resp.status_code == 200, resp.text
    body = resp.json()
    assert body["is_success"] is True
    service_id = body["data"]["id"]
    assert isinstance(service_id, int)

@pytest.mark.asyncio
async def test_4_list_services(client):
    # No Authorization header required
    resp = await client.get("/api/v1/services/get-services", params={"page": 1, "limit": 10})
    assert resp.status_code == 200, resp.text

    body = resp.json()
    assert body["is_success"] is True

    data = body["data"]
    assert isinstance(data, list)

    # Our service should be present
    ids = [s["id"] for s in data]
    assert service_id in ids

    # Check pagination meta_data
    meta = body["meta_data"]
    assert "current_page" in meta and "total_page" in meta


@pytest.mark.asyncio
async def test_5_create_booking(client):
    global booking_id
    # No Authorization header required
    payload = {
        "customer_name": "Jane Doe",
        "customer_phone": "+1234567890",
        "customer_email": "jane@example.com",
        "service_id": service_id
    }
    resp = await client.post("/api/v1/bookings/booking-service", json=payload)
    assert resp.status_code == 200, resp.text

    body = resp.json()
    assert body["is_success"] is True
    booking_id = body["data"]["id"]
    assert isinstance(booking_id, int)


@pytest.mark.asyncio
async def test_6_check_booking_status(client):
    # No Authorization header required
    resp = await client.get(
        "/api/v1/bookings/check-booking-status",
        params={"booking_id": booking_id}
    )
    assert resp.status_code == 200, resp.text

    body = resp.json()
    assert body["is_success"] is True

    data = body["data"]
    assert data["id"] == booking_id
    assert data["status"] == "pending"
