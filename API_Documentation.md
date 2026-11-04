# HomeServe API Documentation (MVP inventory)

Base URL (local): `http://127.0.0.1:8000`

Interactive OpenAPI/Swagger: `http://127.0.0.1:8000/docs`

Authentication: protected endpoints use `Authorization: Bearer <access_token>`.

| Method | Endpoint | Purpose | Access |
|---|---|---|---|
| GET | `/` | API welcome/status | Public |
| GET | `/health` | Health check | Public |
| POST | `/auth/register` | Register customer/provider | Public |
| POST | `/auth/login` | Login and receive JWT | Public |
| GET | `/users/me` | Current user profile | Authenticated |
| GET | `/admin/dashboard` | Basic counts and revenue summary | Admin |
| GET | `/categories` | List active categories | Public |
| POST | `/categories` | Create category | Admin |
| PUT | `/categories/{category_id}` | Update category | Admin |
| DELETE | `/categories/{category_id}` | Delete category if unused | Admin |
| GET | `/services` | List active services | Public |
| POST | `/services` | Create service | Admin |
| PUT | `/services/{service_id}` | Update service | Admin |
| POST | `/addresses` | Add customer address | Customer |
| GET | `/addresses` | List customer addresses | Customer |
| DELETE | `/addresses/{address_id}` | Delete customer address | Customer |
| POST | `/providers/services` | Provider offers a service | Approved provider |
| GET | `/providers/services` | List provider services | Provider |
| POST | `/availability` | Add provider availability | Approved provider |
| GET | `/availability` | List available slots | Public |
| POST | `/bookings` | Create booking | Customer |
| GET | `/bookings` | List bookings visible to current user | Authenticated |
| PATCH | `/bookings/{booking_id}/status` | Update booking status | Owner/admin/provider rules |
| POST | `/payments/test` | Create a non-charge test payment record | Customer |
| POST | `/reviews` | Review own completed booking | Customer |
| POST | `/coupons` | Create coupon | Admin |
| GET | `/coupons/{code}` | Validate coupon | Public |
| POST | `/complaints` | Create complaint | Customer |
| GET | `/complaints` | List complaints visible to user | Customer/Admin |
| POST | `/notifications` | Create notification | Admin |
| GET | `/notifications` | List own notifications | Authenticated |
| PATCH | `/notifications/{notification_id}/read` | Mark own notification read | Authenticated |
| GET | `/invoices` | List invoices visible to user | Authenticated |
| POST | `/invoices` | Create invoice for completed booking | Admin |

## Example registration
```json
{
  "full_name": "Demo Customer",
  "email": "customer@example.com",
  "mobile": "9876543210",
  "password": "ChangeThis123",
  "role": "customer"
}
```

## Example login
```json
{
  "email": "customer@example.com",
  "password": "ChangeThis123"
}
```

## Example booking
```json
{
  "address_id": 1,
  "service_id": 1,
  "scheduled_date": "2026-12-01",
  "scheduled_time": "10:00:00",
  "description": "Kitchen tap is leaking",
  "slot_id": null
}
```

Note: The endpoint inventory describes the starter implementation. Always use the running Swagger UI as the source of truth and test role permissions, validation, ownership, and error cases before submission.
