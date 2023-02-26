import concurrent.futures
import uuid
from enum import Enum

import openai
from fastapi import APIRouter, Depends, File, HTTPException, Query, UploadFile

from app.app_paths import app_paths
from app.core.exceptions import DetailedHTTPException
from app.core.helpers import download_network_image
from app.dependencies import get_openai, openai_api_handle

router = APIRouter()


from fastapi import APIRouter, Depends, Query

router = APIRouter()


class ImageSize(str, Enum):
    HIGH = "1024x1024"
    MEDIUM = "512x512"
    LOW = "256x256"


@router.get("/v1")
async def generation_v1(
    query: str = Query(min_length=3),
    image_size: ImageSize = ImageSize.MEDIUM,
    number_of_images: int = Query(default=1, gt=1, le=10),
):
    try:
        response = get_openai().Image.create(
            prompt=query,
            n=number_of_images,
            size=image_size,
        )

        try:
            image_urls: list[str] = [item["url"] for item in response["data"]]  # type: ignore

            saved_images_file_names: list[str | None] = []

            with concurrent.futures.ThreadPoolExecutor() as executor:
                future_to_url = {
                    executor.submit(
                        download_network_image, url, f"{uuid.uuid4().hex}.jpg", app_paths.image_generation
                    ): url
                    for url in image_urls
                }
                for future in concurrent.futures.as_completed(future_to_url):
                    url = future_to_url[future]
                    try:
                        result = future.result()
                        saved_images_file_names.append(result)
                    except Exception as e:
                        print(f"Failed to download image from {url}: {e}")
            return saved_images_file_names

        except Exception as e:
            print(e)
            raise DetailedHTTPException()

    except openai.APIError as error:
        raise HTTPException(status_code=error.http_status, detail=error.json_body)  # type: ignore
