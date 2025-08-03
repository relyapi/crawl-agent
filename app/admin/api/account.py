from fastapi import APIRouter, Request

from app.task.server import sio

router = APIRouter(
    prefix='/account',
    tags=['账户服务'],
    responses={404: {'description': 'Not found'}},
)


@router.get("/dispatch")
async def dispatch(request: Request):
    """
    登录账户  下发到client 设备管理
    """
    # 需要知道是那个 sid  account和sid 对应关系
    # to=sid 不指定全部
    await sio.emit('task', {})
    return 'ok'
