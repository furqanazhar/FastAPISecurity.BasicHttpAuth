from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from utils.common import convert_response_to_json, validate_credentials



router = APIRouter()
security = HTTPBasic() # Simple HTTP Basic Auth


def validate(credentials: HTTPBasicCredentials = Depends(security)):
    is_valid = validate_credentials(credentials.username, credentials.password)
    if is_valid:
        return True
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )


@router.get('/sample', response_description='Get sample')
async def check_api_security(valid: bool = Depends(validate)):
    try:
        payload = {
            'message': 'Successfully retrieved resource',
            'data': convert_response_to_json('dummy data')
        }
        return JSONResponse(status_code=status.HTTP_200_OK, content=payload)
    except Exception as ex:
        payload = {
            'message': 'Failed to retrieve resource',
            'error': convert_response_to_json(ex)
        }
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=payload)
