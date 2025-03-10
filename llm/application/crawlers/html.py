from urllib.parse import urlparse
from typing import Generic, Type, TypeVar

from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_community.document_transformers.html2text import Html2TextTransformer
from loguru import logger

from llm.data.document import Document

from .base import BaseCrawler

T = TypeVar("T", bound="Document")

class HTMLCrawler(BaseCrawler):

    model: Type[Document]

    def __init__(self, model: Type[Document]) -> None:
        super().__init__()
        self.model = model

    def extract(self, link: str, **kwargs) -> None:
        old_model = self.model.find(link=link)
        if old_model is not None:
            logger.info(f"Article already exists in the database: {link}")

            return

        logger.info(f"Starting scrapping html: {link}")

        loader = AsyncHtmlLoader([link])
        docs = loader.load()

        html2text = Html2TextTransformer()
        docs_transformed = html2text.transform_documents(docs)
        doc_transformed = docs_transformed[0]

        content = {
            "Title": doc_transformed.metadata.get("title"),
            "Subtitle": doc_transformed.metadata.get("description"),
            "Content": doc_transformed.page_content,
            "language": doc_transformed.metadata.get("language"),
        }

        parsed_url = urlparse(link)
        platform = parsed_url.path

        instance = self.model(
            content=content,
            link=link,
            platform=platform
        )
        instance.save()

        logger.info(f"Finished scrapping html: {link}")