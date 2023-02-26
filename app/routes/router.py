from fastapi.routing import APIRouter

from app.routes import (
    grammer,
    natural_language_to_code,
    q_and_a,
    sql_translate,
    summarize,
    text_to_command,
    translate,
)

api_router = APIRouter(prefix="/api")

# api_router.include_router(token.router, tags=["Token"], include_in_schema=True)

api_router.include_router(q_and_a.router, prefix="/q_and_a", tags=["Question & Answers"])
api_router.include_router(grammer.router, prefix="/grammer", tags=["Grammer"])
api_router.include_router(summarize.router, prefix="/summarize", tags=["Summarize"])
api_router.include_router(
    natural_language_to_code.router, prefix="/natural_language_to_code", tags=["Natural language to code"]
)
api_router.include_router(text_to_command.router, prefix="/text_to_command", tags=["Text to Command"])
api_router.include_router(translate.router, prefix="/translate", tags=["Translate"])
api_router.include_router(sql_translate.router, prefix="/sql_translate", tags=["SQL Translate"])
