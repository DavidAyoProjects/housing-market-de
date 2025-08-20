import requests
from pathlib import Path

def run():
    url = "https://www.ons.gov.uk/generator?format=csv&uri=/economy/inflationandpriceindices/datasets/ukhousepriceindexdata/current"
    raw_dir = Path("data/raw/ons_hpi")
    raw_dir.mkdir(parents=True, exist_ok=True)

    output_file = raw_dir / "ons_hpi.csv"
    print(f"Downloading ONS HPI data to {output_file}...")

    r = requests.get(url)
    r.raise_for_status()  # fail if bad response

    with open(output_file, "wb") as f:
        f.write(r.content)

    print("Download complete.")

if __name__ == "__main__":
    run()