from urllib.parse import urlparse

from loguru import logger
from tqdm import tqdm
from typing_extensions import Annotated
from zenml import get_step_context, step

from llm.application.crawlers import HTMLCrawler
from llm.data.document import *


@step
def crawl_links(links: list[str]) -> Annotated[list[str], "crawled_links"]:

    logger.info(f"Starting to crawl {len(links)} link(s).")

    metadata = {}
    successfull_crawls = 0
    for link in tqdm(links):
        successfull_crawl, crawled_path = _crawl_link(HTMLCrawler(model=_get_document_type(link)), link)
        successfull_crawls += successfull_crawl

        metadata = _add_to_metadata(metadata, crawled_path, successfull_crawl)

    step_context = get_step_context()
    step_context.add_output_metadata(output_name="crawled_links", metadata=metadata)

    logger.info(f"Successfully crawled {successfull_crawls} / {len(links)} links.")

    return links


def _crawl_link(crawler: HTMLCrawler, link: str) -> tuple[bool, str]:
    crawler_path = urlparse(link).path

    try:
        crawler.extract(link=link)

        return (True, crawler_path)
    except Exception as e:
        logger.error(f"An error occurred while crawling: {e!s}")

        return (False, crawler_path)


def _add_to_metadata(metadata: dict, path: str, successfull_crawl: bool) -> dict:
    if path not in metadata:
        metadata[path] = {}
    metadata[path]["successful"] = metadata[path].get("successful", 0) + successfull_crawl
    metadata[path]["total"] = metadata[path].get("total", 0) + 1

    return metadata

def _get_document_type(link: str) -> type[Document]:
     
    parsed_url = urlparse(link)
    path = parsed_url.path

    if "/" in path:
        return HOMEDocument
    elif "/about/" in path:
        return ABOUTDocument
    elif "/services/" in path:
        return SERVICESDocument
    elif "/projection-systems/" in path:
        return PROJECTIONSYSTEMSDocument
    elif "/contact/" in path:
        return CONTACTDocument
    elif "/privacy-policy-2/" in path:
        return PRIVACYPOLICYDocument
    elif "/disclaimer/" in path:
        return DISCLAIMERDocument
    elif "/terms-conditions/" in path:
        return TERMSCONDITIONSDocument
    elif "/outdoor-led-displays/" in path:
        return OUTDOORLEDDISPLAYSDocument
    elif "/indoor-led-displays/" in path:
        return INDOORLEDDISPLAYSDocument
    elif "/transparent-flexible-led-displays/" in path:
        return TRANSPARENTFLEXIBLELEDDISPLAYSDocument
    elif "/mobile-led-displays/" in path:
        return MOBILELEDDISPLAYSDocument
    elif "/led-standees/" in path:
        return LEDSTANDEESDocument
    elif "/led-screen-rentals/" in path:
        return LEDSCREENRENTALSDocument
    elif "/articles/" in path:
        return ARTICLESDocument
    elif "/repositories/" in path:
        return REPOSITORIESDocument
    else:
        raise ValueError(f"Unable to determine document type for link: {link}")