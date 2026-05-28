from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("/live")
async def live() -> dict[str, str]:
    return {
        "status": "healthy",
        "service": "backend",
    }


@router.get("/ready")
async def ready() -> dict[str, str]:
    return {
        "status": "ready",
        "service": "backend",
    }