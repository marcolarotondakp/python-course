from pathlib import Path
from typing import Any, Literal, overload
from urllib.parse import quote_plus

import yaml
from sqlalchemy import create_engine, text
from sqlalchemy.engine.cursor import CursorResult
from sshtunnel import SSHTunnelForwarder

path = Path(__file__).parent.joinpath("db_config.yaml")
with open(path, "r") as file:
    config = yaml.safe_load(file)
print(config)


@overload
def _execute_query(
    query: str,
    params: dict[str, Any] | list[dict[str, Any]] | None = None,
    *,
    commit: Literal[False] = False,
    schema: str | None,
) -> CursorResult[Any]: ...


@overload
def _execute_query(
    query: str,
    params: dict[str, Any] | list[dict[str, Any]] | None = None,
    *,
    commit: Literal[True],
    schema: str | None = None,
) -> int: ...


def _execute_query(
    query: str,
    params: dict | list[dict] | None = None,
    commit: bool = False,
    schema: str | None = None,
) -> CursorResult[Any] | int:
    ssh_config = config["ssh-tunnel"]
    db_config = config["db"]
    remote_host = ssh_config.get("remote-host", "127.0.0.1")
    remote_port = ssh_config.get("remote-port", 3306)
    local_host = ssh_config.get("local-host", "127.0.0.1")
    local_port = ssh_config.get("local-port", 0)
    ssh_port = ssh_config.get("port", 22)
    with SSHTunnelForwarder(
        ssh_address_or_host=(ssh_config["url"], ssh_port),
        ssh_username=ssh_config["admin"],
        ssh_pkey=ssh_config["path-pem"],
        remote_bind_address=(remote_host, remote_port),
        local_bind_address=(local_host, local_port),
    ) as tunnel:
        assert isinstance(tunnel, SSHTunnelForwarder)
        assigned_local_port = tunnel.local_bind_port
        connection_string = f"mysql+pymysql://{db_config['user']}:{quote_plus(db_config['password'])}@{local_host}:{assigned_local_port}"
        if schema is None:
            schema = db_config["schema"]
        connection_string += f"/{schema}"
        with create_engine(connection_string).connect() as connection:
            result = connection.execute(text(query), params)
            if commit:
                connection.commit()

                return result.rowcount
            return result


def fetch(
    query: str, params: dict | None = None, schema: str | None = None
) -> CursorResult[Any]:
    return _execute_query(query=query, params=params, schema=schema)


def modify(
    query: str, params: dict | list[dict] | None = None, schema: str | None = None
) -> int:
    return _execute_query(query=query, params=params, commit=True, schema=schema)
