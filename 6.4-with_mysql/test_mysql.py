from __future__ import annotations

import os
import time
from collections.abc import Iterator
from contextlib import closing
from typing import TypedDict

import pymysql
import pytest


class MySQLConfig(TypedDict):
	host: str
	port: int
	user: str
	password: str
	database: str
	charset: str
	cursorclass: type[pymysql.cursors.Cursor]


def _get_mysql_config() -> MySQLConfig:
	"""Pull connection settings from the environment with sensible defaults."""

	return {
		"host": os.getenv("MYSQL_HOST", "mysql"),
		"port": int(os.getenv("MYSQL_PORT", "3306")),
		"user": os.getenv("MYSQL_USER", "mysql_user"),
		"password": os.getenv("MYSQL_PASSWORD", "mysql_password"),
		"database": os.getenv("MYSQL_DATABASE", "app"),
		"charset": "utf8mb4",
		"cursorclass": pymysql.cursors.Cursor,
	}


def _connect_once() -> pymysql.Connection:
	return pymysql.connect(connect_timeout=3, **_get_mysql_config())


# Retry the connection until the database in the sibling container finishes booting.
def _wait_for_connection(timeout_seconds: int = 45, backoff_seconds: float = 1.5) -> pymysql.Connection:
	deadline = time.monotonic() + timeout_seconds
	attempt = 0
	last_error: BaseException | None = None

	while time.monotonic() < deadline:
		attempt += 1
		try:
			return _connect_once()
		except pymysql.MySQLError as exc:  # pragma: no cover - only hit when server not ready
			last_error = exc
			sleep_for = min(backoff_seconds * attempt, 5)
			time.sleep(sleep_for)

	raise AssertionError(f"MySQL not reachable after {timeout_seconds}s: {last_error}")


@pytest.fixture(scope="module")
def mysql_connection() -> Iterator[pymysql.Connection]:
	conn = _wait_for_connection()
	try:
		yield conn
	finally:
		conn.close()


def test_mysql_connection(mysql_connection: pymysql.Connection) -> None:
	with closing(mysql_connection.cursor()) as cursor:
		cursor.execute("SELECT 1")
		row = cursor.fetchone()

	assert row is not None, "SELECT 1 returned no rows"
	assert row[0] == 1, f"Unexpected value returned from MySQL: {row[0]}"
