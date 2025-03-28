# PubMed Extractor

This is a CLI tool and module for fetching PubMed papers with non-academic pharma/biotech authors.

PubMed Pharma Paper Extractor
This project fetches research papers from PubMed using a user-specified query and returns only those with
at least one non-academic author specifically authors affiliated with pharmaceutical or biotech companies.

It is built to support:
- Google Colab for interactive analysis
- Command-line usage via Poetry packaging
- Publishing to TestPyPI for distribution
- 
Features
- Queries PubMed using Biopythons Entrez API
- Detects non-academic affiliations using rule-based heuristics
- Extracts structured information:
 - PubmedID
 - Title
 - Publication Date
 - Non-academic Author(s)
 - Company Affiliation(s)
 - Corresponding Author Email
- Filters out papers with only academic authors
- Supports both CSV output and CLI-based queries

- 
Getting Started (Colab / Local)
Google Colab
Open PubMed_Extractor_UPDATED.ipynb and run all cells.
Install dependencies (if running locally):
pip install biopython pandas tqdm

Heuristics for Filtering
An author is considered non-academic if their affiliation does NOT contain any of these academic keywords:
university, college, institute, school, faculty,
hospital, department, center, centre, academy
Company names are extracted from affiliation strings by removing suffixes like:
Inc., Ltd., Corp., LLC, Co.

Sample Usage (Notebook)
query = "cancer AND biotech"
df = get_papers(query, max_results=25)
df.to_csv("papers_output.csv", index=False)

Output format includes:

PubmedID | Title | Publication Date | Non-academic Author(s) | Company Affiliation(s) | Corresponding Author
Email

Command-Line Version (Bonus)
This project is also structured as a modular package with CLI access:
poetry install
poetry run get-papers-list "cancer AND biotech" -f output.csv

Command-line options:
 get-papers-list "query string"
 -f, --file Save results to CSV
 -d, --debug Enable debug output
 
Project Structure
pubmed_extractor/
 pubmed_extractor/
 fetch.py
 parser.py
 main.py
 cli.py
 pyproject.toml
 README.md

 




Tools Used
- biopython PubMed API (Entrez)
- pandas CSV/DataFrame handling
- tqdm Progress tracking
- ChatGPT Used for code design and documentation support
Author
  [Akshay Ambaprasad]
  [akshay21444@iiitd.ac.in]
Note
All output has been validated to ensure only papers with non-academic authors are included strictly as
required.
