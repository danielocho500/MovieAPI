import json
import logging
from fastapi import Response


def response_message(code: int, message: str, data: object = {}, headers: object = {}) -> Response:
    try:
        return Response(content= json.dumps({"message": message, "data":data}), status_code=code, media_type="application/json",headers=headers)
    except Exception as e:
        logging.error(f'response_message: {e}')
        return "Error in the response", 500