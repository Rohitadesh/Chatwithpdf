from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from app.core.config import Settings
from app.core.logger import get_logger
from app.services.vector_service import VectorService

logger=get_logger(__name__)

class RagService:
    def __int__(self):
        self.vector_service=VectorService()
        self.vector_db=self.vector_service.get_vector_db()

        self.llm=ChatOpenAI(
            model=settings.OPEN_CHAT_MODEL,
            temperature=0
        )

        self.rag_chain=self._create_rag_chain()
    
    def _format_docs(self,docs):
        return "\n\n".join(doc.page_content for doc in docs)
    
    def _create_rag_chain(self):
        retriver=self.vector_db.as_retriver(
           search_kwargs={"k": settings.RETRIEVER_K}
        )
        prompt=ChatPromptTemplate.from_template(
                      """
You are a helpful PDF assistant.

Use only the given context to answer the question.
Do not make up answers.

If the answer is not available in the context, say:
"I don't know based on the uploaded PDF."

Context:
{context}

Question:
{question}

Answer:"""
        )
        chain=(
            {
                "context":retriver|self._format_docs,
                "question":RunnablePassthrough()
            }
            | prompt
            | self.llm
            | StroutParser()
        )
        return chain
    
    def ask(self,question:str)->str:

        logger.info("Recevied question:%s",question)
        return answer