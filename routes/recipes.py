from fastapi import APIRouter

router = APIRouter(
    prefix = "/recipes",
    tags = ["Recipes"]
)

@router.get("/")
def get_recipes():
    return {"recipes": []}