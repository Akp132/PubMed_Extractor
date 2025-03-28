from .fetch import fetch_pubmed_ids, fetch_paper_xml
from .parser import is_non_academic, extract_email, extract_company_name
import pandas as pd
import time
from tqdm import tqdm

def get_papers(query: str, max_results: int = 20) -> pd.DataFrame:
    ids = fetch_pubmed_ids(query, max_results)
    papers = []

    for pubmed_id in tqdm(ids, desc="Fetching paper details"):
        try:
            xml = fetch_paper_xml(pubmed_id)
            article = xml['PubmedArticle'][0]
            info = article['MedlineCitation']['Article']
            title = info['ArticleTitle']
            year = info.get("Journal", {}).get("JournalIssue", {}).get("PubDate", {}).get("Year", "Unknown")

            authors_info = info.get("AuthorList", [])
            non_acad_authors = []
            companies = []
            email = ""

            for author in authors_info:
                aff = author.get("AffiliationInfo", [{}])[0].get("Affiliation", "")
                if is_non_academic(aff):
                    name = " ".join(filter(None, [author.get("ForeName", ""), author.get("LastName", "")]))
                    non_acad_authors.append(name)
                    companies.append(extract_company_name(aff))
                if "@" in aff and not email:
                    email = extract_email(aff)

            if non_acad_authors:
                papers.append({
                    "PubmedID": pubmed_id,
                    "Title": title,
                    "Publication Date": year,
                    "Non-academic Author(s)": "; ".join(non_acad_authors),
                    "Company Affiliation(s)": "; ".join(set(companies)),
                    "Corresponding Author Email": email
                })

        except Exception as e:
            print(f"Error processing {pubmed_id}: {e}")
        time.sleep(0.34)

    return pd.DataFrame(papers)
