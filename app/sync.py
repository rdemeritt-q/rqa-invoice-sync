import os

import requests


def fetch_invoices(since, session=None):
    s = session or requests.Session()
    r = s.get(
        f"{os.environ['INVOICE_API_URL']}/invoices",
        params={"since": since},
        headers={"Authorization": f"Bearer {os.environ['API_TOKEN']}"},
        timeout=10,
    )
    r.raise_for_status()
    return r.json()


def post_to_ledger(invoices, session=None):
    s = session or requests.Session()
    posted = 0
    for inv in invoices:
        entry = {"ref": inv["id"], "amount": inv["amount"], "currency": inv["currency"]}
        r = s.post(
            f"{os.environ['LEDGER_API_URL']}/entries",
            json=entry,
            headers={"Authorization": f"Bearer {os.environ['API_TOKEN']}"},
            timeout=10,
        )
        r.raise_for_status()
        posted += 1
    return posted
