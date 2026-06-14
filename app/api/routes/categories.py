from fastapi import APIRouter

router = APIRouter(prefix="/categories", tags=["Categories"])

fake_categories = ["local", "italian", "indian", "chinese"]

@router.get("/")
def get_categories():
    return fake_categories


@router.get("/{category}")
def filter_by_category(category: str):
    return {
        "category": category,
        "message": f"Filter logic will go here for {category}"
    }