from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME:str = "PDF RAG Chatbot"
    APP_ENV:str ="development"
    OPENAI_API_KEY: str
    PDF_PATH: str = "data/sample.pdf"
    CHROMA_DB_PATH: str = "chroma_db"

    OPENAI_CHAT_MODEL: str = "gpt-4o-mini"
    OPENAI_EMBEDDING_MODEL: str = "text-embedding-3-small"

    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 200
    RETRIEVER_K: int = 4

    class Config:
        env_file = ".env"

settings=Settings()