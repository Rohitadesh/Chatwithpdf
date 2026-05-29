from fastapi import APIRouter, HTTPException

from app.schemas.chat_schema import ChatRequest, ChatResponse
from app.services.rag_service import RagService
from app.core.logger import get_logger


logger = get_logger(__name__)

router = APIRouter(prefix="/api/v1", tags=["PDF RAG"])

rag_service = RagService()


@router.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "PDF RAG API is running"
    }


@router.post("/chat", response_model=ChatResponse)
def chat_with_pdf(payload: ChatRequest):
    try:
        answer = rag_service.ask(payload.question)

        return ChatResponse(answer=answer)

    except Exception as error:
        logger.exception("Error while processing chat request")

        raise HTTPException(
            status_code=500,
            detail="Something went wrong while processing your question."
        )