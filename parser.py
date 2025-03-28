import re

academic_keywords = [
    "university", "college", "institute", "department", "hospital",
    "faculty", "school", "academy", "center", "centre"
]

def is_non_academic(affiliation: str) -> bool:
    if not affiliation:
        return False
    return not any(word in affiliation.lower() for word in academic_keywords)

def extract_email(affiliation: str) -> str:
    matches = re.findall(r"[\w\.-]+@[\w\.-]+", affiliation)
    return matches[0] if matches else ""

def extract_company_name(affiliation: str) -> str:
    if not affiliation:
        return ""
    return re.sub(r"(Inc\.?|Ltd\.?|LLC|Corp\.?|Co\.?)", "", affiliation).strip()
