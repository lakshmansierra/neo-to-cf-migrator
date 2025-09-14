from models.response_model import APIResponse

def make_response(status: str, status_code: int, message: str, data: dict | None = None) -> APIResponse:
    return APIResponse(
        status=status,
        status_code=status_code,
        message=message,
        data=data
    )
