from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.core.config import settings
from app.core.logger import get_logger

logger=get_logger(__name__)

class DocumentService:
    def load_pdf(self):

        logger.info("Loading PDF path:%s",settings.PDF_PATH)
        loader=PyPDFLoader(settings.PDF_PATH)
        document=loader.load()
    
        logger.info("Loaded %s PDF Pages",len(document))
        return document
    
    def split_document(self,documents):
        logger.info("splitting documents into chunks")

        splitter=RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP
        )

        chunks= splitter.split_documents(documents)

        return chunks