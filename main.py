from fastapi import FastAPI, HTTPException
from fastapi.logger import logger
import logging

from fast import process_matches

app = FastAPI()

# set up logging
gunicorn_logger = logging.getLogger("gunicorn.error")
logger.handlers = gunicorn_logger.handlers
logger.setLevel(logging.INFO)


@app.get("/fast/{letters}/{center_letter}", response_model=list[str])
def fast_solver(letters: str, center_letter: str):
    if len(letters) != 7:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid number of supplied letters: {len(letters)}",
        )

    if len(center_letter) != 1:
        raise HTTPException(
            status_code=400,
            detail=f"Need one and only one center letter, got: {center_letter}",
        )

    if center_letter not in letters:
        raise HTTPException(
            status_code=400, detail=f"Center letter must be in letter set."
        )

    return process_matches(letters=letters, center_letter=center_letter)
