"""Tests de l'infrastructure SQLite partagée."""

import sqlite3
import tempfile
import unittest
from pathlib import Path

from filrouge.adapters.sqlite_connection import open_connection
from filrouge.domain.exceptions import StorageError


class TestOpenConnection(unittest.TestCase):
    def test_creates_parent_directory_and_commits(self):
        with tempfile.TemporaryDirectory() as tmp:
            db_path = Path(tmp) / "nested" / "app.sqlite3"

            with open_connection(db_path) as conn:
                conn.execute("CREATE TABLE t (x INTEGER)")
                conn.execute("INSERT INTO t VALUES (1)")

            self.assertTrue(db_path.exists())
            with open_connection(db_path) as conn:
                self.assertEqual(conn.execute("SELECT x FROM t").fetchall(), [(1,)])

    def test_connection_is_closed_after_use(self):
        with tempfile.TemporaryDirectory() as tmp:
            with open_connection(Path(tmp) / "app.sqlite3") as conn:
                pass

            with self.assertRaises(sqlite3.ProgrammingError):
                conn.execute("SELECT 1")

    def test_sql_error_is_wrapped_in_storage_error(self):
        with (
            tempfile.TemporaryDirectory() as tmp,
            self.assertRaises(StorageError),
            open_connection(Path(tmp) / "app.sqlite3") as conn,
        ):
            conn.execute("SELECT * FROM table_inexistante")


if __name__ == "__main__":
    unittest.main()
