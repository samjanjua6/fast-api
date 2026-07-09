from fastapi import FastAPI, HTTPException

from schemas import (
    LoginRequest,
    TokenResponse,
    UserCreate,
    UserResponse,
)

from storage import (
    authenticate,
    create_user,
    get_user,
)

app = FastAPI()


@app.post("/signup", response_model=UserResponse)
def signup(user: UserCreate):
    try:
        created = create_user(
            user.username,
            user.email,
            user.password,
        )
        return UserResponse(**created.model_dump())

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/login", response_model=TokenResponse)
def login(data: LoginRequest):
    user = authenticate(
        data.username_or_email,
        data.password,
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
        )

    return TokenResponse(
        access_token="dummy-token-12345"
    )


@app.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int):
    user = get_user(user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return UserResponse(**user.model_dump())