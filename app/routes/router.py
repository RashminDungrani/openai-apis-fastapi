from fastapi.routing import APIRouter

from app.routes import q_and_a

api_router = APIRouter(prefix="/api")

# api_router.include_router(token.router, tags=["Token"], include_in_schema=True)

api_router.include_router(q_and_a.router, prefix="/q_and_a", tags=["Question & Answers"])
