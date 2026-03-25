from fastapi import APIRouter

router = APIRouter(prefix='/payment', tags= ['Payment'])

@router.get('/')
def hello():
    return {'messege' : "Hello"}