import os
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

from app.core.config import settings
from app.core.logger import get_logger
from app.services.document_service import DocumentService

logger=get_logger(__name__)


class VectorService:
    def __init__(self):
        self.embeddings=OpenAIEmbeddings(
            model=settings.OPENAI_EMBEDDING_MODEL
        )
    
    def vector_db_exists(self):
        return os.path.exists(settings.CHROMA_DB_PATH)
    
    def create_vector_db(self):
        logger.info("Creating new Vector DB")
        document_service=DocumentService()

        documents=document_service.load_pdf()
        chunks=document_service.split_document(documents)

        vector_db=Chroma.from_documents(
            documents=chunks,
            embedding=self.embeddings,
            presist_directory=settings.CHROMA_DB_PATH
        )
        logger.info("Vector DB created successfully")
        return vector_db

    def load_vector_db(self):
        logger.info("Loading exiting vector DB")
        vector_db=Chroma(
            persist_directory=settings.CHROMA_DB_PATH,
            embedding_function=self.embeddings
        )
        return vector_db
    def get_vector_db(self):
        """
        If vector DB exists, load it.
        Otherwise create it.
        """
        if self.vector_db_exists():
            return self.load_vector_db()

        return self.create_vector_db()