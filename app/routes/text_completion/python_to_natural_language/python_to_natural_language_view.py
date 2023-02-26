from fastapi import APIRouter, Depends, File, HTTPException, Query, UploadFile

from app.core.exceptions import DetailedHTTPException
from app.dependencies import get_openai, openai_api_handle

router = APIRouter()


from fastapi import APIRouter, Depends, Query

router = APIRouter()


@router.get("/v1")
async def python_to_natural_language_v1(python_code: str = Query(min_length=3)):

    response = openai_api_handle(
        model="code-davinci-002",
        prompt=f"# Python 3\n{python_code}\n\n# Explanation of what the code does\n\n#",
        api_end_point="/api/text_completion/python_to_natural_language/v1",
        temperature=0,
        max_tokens=64,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    if response.openai_response:
        answer = response.openai_response.choices[0].text.strip()
        return {"answer": answer}

    raise DetailedHTTPException()
