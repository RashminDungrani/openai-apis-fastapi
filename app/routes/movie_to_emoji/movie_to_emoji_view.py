from fastapi import APIRouter, Depends, File, HTTPException, Query, UploadFile

from app.core.exceptions import DetailedHTTPException
from app.dependencies import get_openai, openai_api_handle

router = APIRouter()


from fastapi import APIRouter, Depends, Query

router = APIRouter()


@router.get("/v1")
async def movie_to_emoji_v1(movie_name: str = Query(min_length=3)):

    response = openai_api_handle(
        model="code-davinci-002",
        prompt=f"Convert movie titles into emoji.\n\nBack to the Future: 👨👴🚗🕒 \nBatman: 🤵🦇 \nTransformers: 🚗🤖 \n{movie_name}: ",
        api_end_point="/api/movie_to_emoji/v1",
        temperature=0.8,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"],
    )
    if response.openai_response:
        answer = response.openai_response.choices[0].text.strip()
        return {"answer": answer}

    raise DetailedHTTPException()
