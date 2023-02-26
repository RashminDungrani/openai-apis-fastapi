import os


class AppPaths:
    base: str = os.path.dirname(__file__)
    static: str = os.path.join(base, "static")
    media: str = os.path.join(static, "media")

    # * app specific
    results: str = os.path.join(media, "results")


app_paths = AppPaths()
