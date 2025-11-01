import os
import socket
from typing import Any, Tuple

import psycopg
import pytest


def _connection_args() -> Tuple[tuple[object, ...], dict[str, Any]]:
	"""Build positional and keyword args for psycopg.connect."""
	conninfo = os.getenv("POSTGRES_DSN")
	if conninfo:
		return (conninfo,), {"connect_timeout": 5}

	host = os.getenv("POSTGRES_HOST", "postgres")
	port = int(os.getenv("POSTGRES_PORT", 5432))
	user = os.getenv("POSTGRES_USER", "postgres")
	password = os.getenv("POSTGRES_PASSWORD")
	dbname = os.getenv("POSTGRES_DB", "postgres")

	kwargs: dict[str, object] = {
		"host": host,
		"port": port,
		"user": user,
		"dbname": dbname,
		"connect_timeout": 5,
	}
	if password:
		kwargs["password"] = password

	return (), kwargs


def _is_host_reachable(host: str, port: int, timeout: float = 3.0) -> bool:
	"""Return True if a TCP connection to host/port succeeds."""
	try:
		with socket.create_connection((host, port), timeout=timeout):
			return True
	except OSError:
		return False


def test_postgresql_connection() -> None:
	args, kwargs = _connection_args()
	target = kwargs.get("host", "POSTGRES_DSN")

	if not args:
		host = str(target)
		port = int(kwargs.get("port", 5432))
		if not _is_host_reachable(host, port):
			pytest.skip(f"PostgreSQL host {host}:{port} is not reachable.")

	try:
		with psycopg.connect(*args, **kwargs) as conn:
			with conn.cursor() as cur:
				cur.execute("SELECT 1")
				result = cur.fetchone()
	except Exception as exc:  # pragma: no cover - defensive failure path
		pytest.fail(f"Failed to connect to PostgreSQL at {target}: {exc}")

	assert result == (1,), f"Unexpected query result from PostgreSQL: {result}"
