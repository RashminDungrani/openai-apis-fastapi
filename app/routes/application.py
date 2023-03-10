"""FastAPI application
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import UJSONResponse
from fastapi.staticfiles import StaticFiles

from app.app_paths import app_paths
from app.core.settings import settings

# from app.app_paths import app_paths
# from app.routes.lifetime import register_shutdown_event, register_startup_event
from app.routes.router import image_generation_api_router, text_completion_api_router

# from fastapi.staticfiles import StaticFiles


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """

    app = FastAPI(
        title=settings.fastapi_title,
        description=settings.fastapi_desc,
        version=settings.fastapi_version,
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url="/api/openapi.json",
        default_response_class=UJSONResponse,
    )

    # origins = [
    #     "http://192.168.1.237",
    #     "http://192.168.1.237:8000",
    # ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Adds startup and shutdown events.
    # register_startup_event(app)
    # register_shutdown_event(app)

    # # Add Icon
    # @app.get("/favicon.ico", include_in_schema=False)
    # async def _() -> FileResponse:
    #     return FileResponse(join(app_paths.static, "favicon.ico"))

    # Main router for the API.
    app.include_router(router=text_completion_api_router)
    app.include_router(router=image_generation_api_router)

    # mount static posts
    app.mount("/static", StaticFiles(directory=app_paths.static), name="static")

    return app
