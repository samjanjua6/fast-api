import json
from datetime import datetime
from hashlib import sha256
from pathlib import Path

from schemas import User

DATA_FILE = Path(__file__).with_name("users.json")


def load_users():
    if not DATA_FILE.exists():
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        DATA_FILE.write_text("[]")

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    return [User(**user) for user in data]


def save_users(users):
    with open(DATA_FILE, "w") as f:
        json.dump(
            [user.model_dump(mode="json") for user in users],
            f,
            indent=4,
        )


def hash_password(password: str):
    return sha256(password.encode()).hexdigest()


def create_user(username, email, password):
    users = load_users()

    for user in users:
        if user.username == username:
            raise ValueError("Username already exists")
        if user.email == email:
            raise ValueError("Email already exists")

    new_user = User(
        id=len(users) + 1,
        username=username,
        email=email,
        hashed_password=hash_password(password),
        created_at=datetime.utcnow(),
    )

    users.append(new_user)
    save_users(users)

    return new_user


def authenticate(username_or_email, password):
    users = load_users()
    hashed = hash_password(password)

    for user in users:
        if (
            user.username == username_or_email
            or user.email == username_or_email
        ):
            if user.hashed_password == hashed:
                return user

    return None


def get_user(user_id):
    users = load_users()

    for user in users:
        if user.id == user_id:
            return user

    return None