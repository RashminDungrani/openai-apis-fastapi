from fastapi import APIRouter, Depends, File, HTTPException, Query, UploadFile

from app.core.exceptions import DetailedHTTPException
from app.dependencies import openai_api_handle

router = APIRouter()


from fastapi import APIRouter, Depends, Query

router = APIRouter()


@router.get("/v1")
async def translate_v1(
    langauge: str = Query(min_length=2),
    input: str = Query(min_length=3),
):
    #     completions = openai.Completion.create(
    #     engine="davinci",
    #     prompt=prompt,
    #     max_tokens=60,
    #     n=1,
    #     stop=None,
    #     temperature=0.5,
    # )
    response = openai_api_handle(
        model="text-davinci-003",
        prompt=f"Translate this into {langauge}: \n\n{input}",
        api_end_point="/api/translate/v1",
        temperature=0.3,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        # stop=["\n"],
    )
    if response.openai_response:
        answer = response.openai_response.choices[0].text.strip()
        return {"answer": answer}

    raise DetailedHTTPException()
