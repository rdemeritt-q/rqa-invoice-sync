# rqa-invoice-sync

Syncs invoices from the billing API to the ledger.

## Configuration

Copy `.env.template` to `.env` and set:

- `INVOICE_API_URL`: base URL of the billing API
- `LEDGER_API_URL`: base URL of the ledger API
- `API_TOKEN`: bearer token for both

## Run

    pip install -r requirements.txt
    python -m app.main --since 2026-10-01

## Test

    python -m unittest discover -s tests

## Docker

The base image is a build argument:

    docker build --build-arg BASE_IMAGE=<image> -t rqa-invoice-sync .
    docker run --rm --env-file .env rqa-invoice-sync --since 2026-10-01
