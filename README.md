# FastAPI User API

Small FastAPI app for creating users, logging in, and fetching users from a local JSON file.

## Requirements

- Python 3.13+
- FastAPI
- Uvicorn

## Run the app

From the project root:

```powershell
uvicorn main:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

## Endpoints

### POST /signup

Creates a new user.

Example body:

```json
{
	"username": "sam",
	"email": "sam@example.com",
	"password": "secret123"
}
```

### POST /login

Authenticates with username or email and password.

Example body:

```json
{
	"username_or_email": "sam",
	"password": "secret123"
}
```

### GET /users/{user_id}

Returns a user by numeric id.

Example:

```text
/users/1
```

## Data storage

User data is stored in [users.json](users.json) in the project root.

## Notes

- The login endpoint returns a dummy token for now.
- Passwords are stored as SHA-256 hashes in the JSON file.
