import sys
import requests
import re


def download_url_and_get_all_hrefs(url):
    response = requests.get(url)
    hrefs = []

    if response.status_code == 200:
        hrefs = re.findall(r'<a\s+href="(.*?)"', response.text)

    return hrefs



if __name__ == "__main__":
    try:
        url = sys.argv[1]
        download_url_and_get_all_hrefs(url)
    # osetrete potencialni chyby pomoci vetve except
    except Exception as e:
        print(f"Program skoncil chybou: {e}")
