import argparse

from app.sync import fetch_invoices, post_to_ledger


def main(argv=None):
    p = argparse.ArgumentParser(description="Sync invoices to the ledger")
    p.add_argument("--since", required=True, help="start date, YYYY-MM-DD")
    args = p.parse_args(argv)
    count = post_to_ledger(fetch_invoices(args.since))
    print(f"synced {count} invoices")


if __name__ == "__main__":
    main()
