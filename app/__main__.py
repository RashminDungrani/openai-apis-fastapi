import uvicorn

from app.core.settings import settings


def main() -> None:
    """Entrypoint of the application."""

    uvicorn.run(
        "app.routes.application:get_app",
        workers=settings.workers_count,
        host=settings.host,
        port=settings.port,
        # TODO: if only show open api docs if env is in these from three
        # SHOW_DOCS_ENVIRONMENT = (
        # "local",
        # "staging",
        # "dev",
        # )  # explicit list of allowed envs
        reload=settings.reload,
        log_level=settings.log_level.value.lower(),
        factory=True,
    )


if __name__ == "__main__":
    main()
