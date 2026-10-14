import os
import unittest

from app import sync


class Resp:
    def __init__(self, data=None):
        self._data = data

    def raise_for_status(self):
        pass

    def json(self):
        return self._data


class FakeSession:
    def __init__(self):
        self.posts = []

    def get(self, url, **kw):
        return Resp([{"id": "i1", "amount": 10, "currency": "EUR"}])

    def post(self, url, json=None, **kw):
        self.posts.append((url, json))
        return Resp()


class SyncTest(unittest.TestCase):
    def setUp(self):
        os.environ.update(
            INVOICE_API_URL="http://invoices.test",
            LEDGER_API_URL="http://ledger.test",
            API_TOKEN="placeholder",
        )

    def test_fetch_and_post(self):
        s = FakeSession()
        invoices = sync.fetch_invoices("2026-10-01", session=s)
        self.assertEqual(sync.post_to_ledger(invoices, session=s), 1)
        self.assertEqual(s.posts[0][1]["ref"], "i1")


if __name__ == "__main__":
    unittest.main()
