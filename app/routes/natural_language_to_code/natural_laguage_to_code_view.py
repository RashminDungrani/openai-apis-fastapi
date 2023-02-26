from fastapi import APIRouter, Depends, File, HTTPException, Query, UploadFile

from app.core.exceptions import DetailedHTTPException
from app.dependencies import get_openai, openai_api_handle

router = APIRouter()


from fastapi import APIRouter, Depends, Query

router = APIRouter()


@router.get("/v1")
# TODO: need to explore more
async def natural_laguage_to_code_v1(query: str = Query(min_length=3)):

    response = openai_api_handle(
        model="code-davinci-002",
        prompt="""
Util exposes the following:
util.openai() -> authenticates & returns the openai module, which has the following functions:
openai.Completion.create(
    prompt="<my prompt>", # The prompt to start completing from
    max_tokens=123, # The max number of tokens to generate
    temperature=1.0 # A measure of randomness
    echo=True, # Whether to return the prompt in addition to the generated completion
)

import util

Create an OpenAI completion starting from the prompt "Once upon an AI", no more than 5 tokens. Does not include the prompt.
""",
        api_end_point="/api/natural_language_to_code/v1",
        temperature=0,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=['"""'],
    )
    if response.openai_response:
        answer = response.openai_response.choices[0].text.strip()
        return {"answer": answer}

    raise DetailedHTTPException()
