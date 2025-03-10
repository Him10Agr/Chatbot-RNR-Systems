from enum import StrEnum


class DataCategory(StrEnum):
    PROMPT = "prompt"
    QUERIES = "queries"

    HOME = "home"
    ABOUT = "about"
    SERVICES = "services"
    PROJECTIONSYSTEMS = "projectionsystems"
    CONTACT = "contact"
    PRIVACYPOLICY = "privacypolicy"
    DISCLAIMER = "disclaimer"
    TERMSCONDITIONS = "termconditions"
    OUTDOORLEDDISPLAYS = "outdoorleddisplays"
    INDOORLEDDISPLAYS = "indoorleddisplays"
    TRANSPARENTFLEXIBLELEDDISPLAYS = "transparentflexibleleddisplays"
    MOBILELEDDISPLAYS = "mobileleddisplays"
    LEDSTANDEES = "ledstandees"
    LEDSCREENRENTALS = "ledscreenrentals"
    ARTICLES = "articles"
    REPOSITORIES = "repositories"