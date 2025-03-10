from abc import ABC
from typing import Optional

from pydantic import UUID4, Field

from .base_document import NoSQLBaseDocument
from .types import DataCategory


class Document(NoSQLBaseDocument, ABC):
    content: dict

class HOMEDocument(Document):
    link: str
    platform: str
    class Settings:
        name = DataCategory.HOME

class ABOUTDocument(Document):
    link: str
    platform: str
    class Settings:
        name = DataCategory.ABOUT

class SERVICESDocument(Document):
    link: str
    platform: str
    class Settings:
        name = DataCategory.SERVICES

class PROJECTIONSYSTEMSDocument(Document):
    link: str
    platform: str
    class Settings:
        name = DataCategory.PROJECTIONSYSTEMS

class CONTACTDocument(Document):
    link: str
    platform: str
    class Settings:
        name = DataCategory.CONTACT

class PRIVACYPOLICYDocument(Document):
    link: str
    platform: str
    class Settings:
        name = DataCategory.PRIVACYPOLICY

class DISCLAIMERDocument(Document):
    link: str
    platform: str
    class Settings:
        name = DataCategory.DISCLAIMER

class TERMSCONDITIONSDocument(Document):
    link: str
    platform: str
    class Settings:
        name = DataCategory.TERMSCONDITIONS

class OUTDOORLEDDISPLAYSDocument(Document):
    link: str
    platform: str
    class Settings:
        name = DataCategory.OUTDOORLEDDISPLAYS

class INDOORLEDDISPLAYSDocument(Document):
    link: str
    platform: str
    class Settings:
        name = DataCategory.INDOORLEDDISPLAYS

class TRANSPARENTFLEXIBLELEDDISPLAYSDocument(Document):
    link: str
    platform: str
    class Settings:
        name = DataCategory.TRANSPARENTFLEXIBLELEDDISPLAYS

class MOBILELEDDISPLAYSDocument(Document):
    link: str
    platform: str
    class Settings:
        name = DataCategory.MOBILELEDDISPLAYS

class LEDSTANDEESDocument(Document):
    link: str
    platform: str
    class Settings:
        name = DataCategory.LEDSTANDEES

class LEDSCREENRENTALSDocument(Document):
    link: str
    platform: str
    class Settings:
        name = DataCategory.LEDSCREENRENTALS

class ARTICLESDocument(Document):
    link: str
    platform: str
    class Settings:
        name = DataCategory.ARTICLES

class REPOSITORIESDocument(Document):
    link: str
    platform: str
    class Settings:
        name = DataCategory.REPOSITORIES