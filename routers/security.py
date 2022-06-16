from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from utils.common import convert_response_to_json


router = APIRouter()


@router.get('/sample', response_description='Get sample')
async def get_all_notes():
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