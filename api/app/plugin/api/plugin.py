from fastapi import APIRouter, Request

router = APIRouter(
    prefix='/plugin',
    tags=['插件服务'],
    responses={404: {'description': 'Not found'}},
)


@router.post("/upload")
async def fetch(request: Request):
    """
    插件上传
    """
    pass


@router.get("/download")
async def config(request: Request):
    """
    插件下载
    """
