from Bio import Entrez

Entrez.email = "your-email@example.com"
Entrez.api_key = "your-api-key-here"

def fetch_pubmed_ids(query: str, max_results: int = 50):
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    record = Entrez.read(handle)
    return record["IdList"]

def fetch_paper_xml(pubmed_id: str):
    handle = Entrez.efetch(db="pubmed", id=pubmed_id, retmode="xml")
    return Entrez.read(handle)
