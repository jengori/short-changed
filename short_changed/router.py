from fastapi import APIRouter
import secrets
import string

from short_changed.database import Database
from short_changed.models import CreateShortUrlResponse
from starlette.responses import RedirectResponse

db = Database()

router = APIRouter()


@router.get("/create/{long_url:path}")
async def create(long_url: str) -> CreateShortUrlResponse:
    # Generate a 7 character string
    short_url_length = 7
    short_url = ''.join(secrets.choice(string.ascii_lowercase + string.digits)
                        for i in range(short_url_length))

    if db.add_data(long_url, short_url):
        return CreateShortUrlResponse(longurl=long_url, shorturl=short_url)
    else:
        short_url = db.get_short_url(long_url)
        return CreateShortUrlResponse(longurl=long_url, shorturl=short_url)


@router.get("/{short_url}")
async def redirect(short_url: str):

    if db.short_url_exists(short_url):

        url = db.get_long_url(short_url)

        # Return redirect response
        response = RedirectResponse(url=url)
        return response

    else:
        # Return error message
        return {"message": "unable to reach"}
