from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import JWTError, jwt
import os
from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserOut, Token
from dotenv import load_dotenv
load_dotenv()

router = APIRouter(prefix="/api/auth", tags=["auth"])
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)
oauth2 = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

def hash_password(password: str) -> str:
        return pwd_context.hash(password)

def verify_password(plain_password:str, hashed_password: str)-> bool:
        return pwd_context.verify(plain_password,hashed_password)

def create_access_token(data:dict,expires_delta: timedelta | None= None):
        to_encode = data.copy()
        expire = datetime.now() + (
                expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(
                token:str = Depends(oauth2),
                db:Session = Depends(get_db),
):
        credentials_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credebtials",
                headers={"WWW-Authenticate":"Bearer"},
                )
        try: 
            payload = jwt.decode(token,SECRET_KEY, algorithm=[ALGORITHM])
            user_id:str | None = payload.get("sub")
            if user_id is None:
                   raise credentials_exception
        except JWTError:
               raise credentials_exception
        
        user = db.query(User).filter(User.id == int(user_id)).first()
        if user is None:
               raise credentials_exception
        return user

@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db:Session = Depends(get_db)):
       existing = db.query(User).filter(
              (User.email == user.email) | (User.username == user.username)
       ).first()
       if existing:
              raise HTTPException(
                     status_code=400,
                     detail="Username or email already registered",
              )
       new_user = User(
              username=user.username,
              email=user.email,
hashed_password=hash_password(user.password),
       )

       db.add(new_user)
       db.commit()
       db.refresh(new_user)

       return new_user

@router.post("/login", response_model=Token)
def login(
       form_data: OAuth2PasswordRequestForm = Depends(),
       db:Session = Depends(get_db)
):
       user = db.query(User).filter(
              (User.email == form_data.username) | (User.username == form_data.username)
       ).first()
       if not user or not verify_password(form_data.password,user.hashed_password):
              raise HTTPException(
                     status_code=status.HTTP_401_UNAUTHORIZED,
                     detail="Incorrect email or password",
                     headers={"WWW-Authenticate":"Bearer"}
              )
       access_token = create_access_token(
              data={"sub": str(user.id)}
       )
       return{
              "access_token":access_token,
              "token_type":"bearer"
       }

@router.get("/me", response_model=UserOut)
def read_current_user(current_user:User = Depends(get_current_user)):
       return current_user