from app.api.routers import router
from app.core.config import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def create_app():
    app=FastAPI(
        title=settings.APP_NAME
        ,version="1.0.0"
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credential=True,
          allow_methods=["*"],
        allow_headers=["*"],
    )
    
    app.include_router(router)

    return app

app=create_app()