import openai

from app.core.settings import settings


def get_openai():
    # sets open API API KEY
    openai.api_key = settings.OPENAI_API_KEY
    return openai
