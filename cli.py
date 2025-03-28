import argparse
from pubmed_extractor.main import get_papers

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with pharma affiliations.")
    parser.add_argument("query", type=str, help="PubMed query string")
    parser.add_argument("-f", "--file", type=str, help="Output CSV file name")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug output")

    args = parser.parse_args()
    df = get_papers(args.query)

    if args.file:
        df.to_csv(args.file, index=False)
        print(f"Saved to {args.file}")
    else:
        print(df.to_string(index=False))

if __name__ == "__main__":
    main()
