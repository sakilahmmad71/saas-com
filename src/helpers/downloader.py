import requests
from pathlib import Path


def download_file(url: str, output_path: Path, parent_mkdir: bool = True):
    if not isinstance(output_path, Path):
        raise ValueError("output_path must be a Path object")
    if parent_mkdir:
        output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        response = requests.get(url)
        response.raise_for_status()
        # Write the file output in the binary mode to prevent any newline conversions
        output_path.write_bytes(response.content)
        return True
    except requests.RequestException as e:
        print(f"Error downloading {url}: {e}")
        return False
