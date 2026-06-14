from fastapi import APIRouter

router = APIRouter(prefix="/categories", tags=["Categories"])

fake_categories = ["local", "italian", "indian", "chinese"]

@router.get("/")
def get_categories():
    return fake_categories