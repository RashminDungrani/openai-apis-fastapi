from fastapi import APIRouter, Depends, File, HTTPException, Query, UploadFile

from app.core.exceptions import DetailedHTTPException
from app.dependencies import get_openai, openai_api_handle

router = APIRouter()


from fastapi import APIRouter, Depends, Query

router = APIRouter()


@router.get("/v1")
async def summarize_v1(query: str = Query(min_length=3)):

    response = openai_api_handle(
        model="text-davinci-003",
        prompt=f"Summarize this for a second-grade student:\n\n{query}",
        api_end_point="/api/text_completion/summarize/v1",
        temperature=0.7,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    if response.openai_response:
        answer = response.openai_response.choices[0].text.strip()
        return {"answer": answer}

    raise DetailedHTTPException()
