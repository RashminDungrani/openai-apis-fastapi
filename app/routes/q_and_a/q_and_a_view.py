from fastapi import APIRouter, Depends, File, HTTPException, Query, UploadFile

from app.core.exceptions import DetailedHTTPException
from app.dependencies import get_openai, openai_api_handle

router = APIRouter()


from fastapi import APIRouter, Depends, Query

router = APIRouter()


@router.get("/v1")
async def question_and_answer_v1(question: str = Query(min_length=3)):

    response = openai_api_handle(
        model="text-davinci-003",
        prompt=f'I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with "Unknown".\n\nQ: What is human life expectancy in the United States?\nA: Human life expectancy in the United States is 78 years.\n\nQ: Who was president of the United States in 1955?\nA: Dwight D. Eisenhower was president of the United States in 1955.\n\nQ: Which party did he belong to?\nA: He belonged to the Republican Party.\n\nQ: What is the square root of banana?\nA: Unknown\n\nQ: How does a telescope work?\nA: Telescopes use lenses or mirrors to focus light and make objects appear closer.\n\nQ: Where were the 1992 Olympics held?\nA: The 1992 Olympics were held in Barcelona, Spain.\n\nQ: How many squigs are in a bonk?\nA: Unknown\n\nQ: {question}\nA: ',
        api_end_point="/api/q_and_a/v1",
        stop=["\n"],
    )
    if response.openai_response:
        answer = response.openai_response.choices[0].text
        return {"answer": answer}
    raise DetailedHTTPException()


@router.get("/v2")
async def question_and_answer_v2(question: str = Query(min_length=3)):
    response = openai_api_handle(
        model="text-davinci-003",
        prompt=f"Q: {question}\nA: ",
        api_end_point="/api/q_and_a/v2",
    )
    if response.openai_response:
        answer = response.openai_response.choices[0].text.strip()
        return {"answer": answer}
    raise DetailedHTTPException()
