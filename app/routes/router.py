from fastapi.routing import APIRouter

from app.routes.image_generation import generation
from app.routes.text_completion import (
    grammar,
    movie_to_emoji,
    natural_language_to_code,
    python_to_natural_language,
    q_and_a,
    sql_translate,
    summarize,
    text_to_command,
    translate,
)

text_completion_api_router = APIRouter(prefix="/api/text_completion", tags=["Text Completion"])

# api_router.include_router(token.router, tags=["Token"], include_in_schema=True)

text_completion_api_router.include_router(q_and_a.router, prefix="/q_and_a")
text_completion_api_router.include_router(grammar.router, prefix="/grammar")
text_completion_api_router.include_router(summarize.router, prefix="/summarize")
text_completion_api_router.include_router(natural_language_to_code.router, prefix="/natural_language_to_code")
text_completion_api_router.include_router(text_to_command.router, prefix="/text_to_command")
text_completion_api_router.include_router(translate.router, prefix="/translate")
text_completion_api_router.include_router(sql_translate.router, prefix="/sql_translate")
text_completion_api_router.include_router(python_to_natural_language.router, prefix="/python_to_natural_language")
text_completion_api_router.include_router(movie_to_emoji.router, prefix="/movie_to_emoji")

image_generation_api_router = APIRouter(prefix="/api/image_generation", tags=["Image Generation"])

image_generation_api_router.include_router(generation.router, prefix="/generation")
