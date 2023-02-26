from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TextCompletionChoice(BaseModel):
    finish_reason: str
    index: int
    logprobs: Optional[dict]
    text: str


class TextCompletion(BaseModel):
    choices: list[TextCompletionChoice]
    created: int
    id: str
    model: str
    object: str
    usage: dict


class APIResult(BaseModel):
    api_end_point: str
    called_at: datetime
    input: str
    openai_response: TextCompletion | None
