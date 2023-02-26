import os


class AppPaths:
    base: str = os.path.dirname(__file__)
    static: str = os.path.join(base, "static")
    media: str = os.path.join(static, "media")

    # * app specific
    results: str = os.path.join(media, "results")
    openai_responses_json: str = os.path.join(static, "json", "openai_responses.json")
    image_generation: str = os.path.join(media, "image_generation")


app_paths = AppPaths()
