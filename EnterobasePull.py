import os
import json
import base64
import shutil
import urllib.request

from pathlib import Path
from config import API_TOKEN, OUTDIR, SERVER_ADDRESS, DATABASE, SCHEME_LIST

__version__ = "0.0.1"
__author__ = "Forest Dussault"
__email__ = "forest.dussault@canada.ca"


def create_request(url: str):
    """Create request for URL using API token"""
    credentials = f"{API_TOKEN}:"
    bytes_base64_encoded_credentials = base64.encodebytes(credentials.encode('utf-8')).decode('utf-8').replace('\n', '')
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Basic {0}'.format(bytes_base64_encoded_credentials)}
    request = urllib.request.Request(url, headers=headers)
    return request


def retrieve_json(url: str):
    """Open URL and load the JSON"""
    response = urllib.request.urlopen(create_request(url))
    data = json.load(response)
    return data


def download_loci(data: dict, outdir: Path):
    """Download all loci from data object to output directory"""
    for scheme_record in data['loci']:
        profile_link = scheme_record['download_alleles_link']
        locus = scheme_record['locus']
        file_name = outdir / Path(locus).with_suffix(".gz").name
        if not file_name.exists():
            if profile_link:
                print(f"Retrieving {profile_link}...")
                with urllib.request.urlopen(profile_link) as response, open(str(file_name), 'wb') as out_file:
                    shutil.copyfileobj(response, out_file)
        else:
            print(f"{file_name} already exists, skipping")


def download_schemes(data: dict, outdir: Path):
    for scheme_record in data['Schemes']:
        profile_link = scheme_record['download_sts_link']
        file_name = outdir / "MLST-profiles.gz"
        if profile_link:
            print(f"Retrieving {profile_link}")
            with urllib.request.urlopen(profile_link) as response, open(str(file_name), 'wb') as out_file:
                shutil.copyfileobj(response, out_file)


def main():
    for scheme in SCHEME_LIST:
        print(f"Starting download for {scheme}")
        address = f"http://enterobase.warwick.ac.uk/api/v2.0/senterica/{scheme}/loci?limit=4000"
        data = retrieve_json(url=address)
        outdir = OUTDIR / scheme
        os.makedirs(outdir, exist_ok=True)
        download_loci(data=data, outdir=outdir)


if __name__ == "__main__":
    main()
