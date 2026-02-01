import requests
from modules.utils import clean_subdomains

def from_crtsh(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    subs = set()
    try:
        r = requests.get(url, timeout=10)
        for entry in r.json():
            name = entry.get("name_value", "")
            for sub in name.split("\\n"):
                if domain in sub:
                    subs.add(sub)
    except:
        pass
    return subs


def from_hackertarget(domain):
    url = f"https://api.hackertarget.com/hostsearch/?q={domain}"
    subs = set()
    try:
        r = requests.get(url, timeout=10).text
        for line in r.splitlines():
            sub = line.split(",")[0]
            subs.add(sub)
    except:
        pass
    return subs


def find_subdomains(domain):
    all_subs = set()

    all_subs.update(from_crtsh(domain))
    all_subs.update(from_hackertarget(domain))

    return clean_subdomains(all_subs)
