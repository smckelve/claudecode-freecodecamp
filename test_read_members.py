from pathlib import Path

import pytest

from read_members import format_members_table, read_members, search_members

CSV_CONTENT = """first_name,last_name,email
Ada,Lovelace,ada@example.com
Grace,Hopper,grace@example.com
Alan,Turing,alan@example.com
"""


@pytest.fixture
def csv_path(tmp_path: Path) -> str:
    path = tmp_path / "members.csv"
    path.write_text(CSV_CONTENT)
    return str(path)


def test_read_members_returns_dicts_with_csv_columns(csv_path: str) -> None:
    members = read_members(csv_path)
    assert members[0] == {"first_name": "Ada", "last_name": "Lovelace", "email": "ada@example.com"}


def test_read_members_respects_limit(csv_path: str) -> None:
    members = read_members(csv_path, limit=2)
    assert len(members) == 2


def test_read_members_raises_for_missing_file() -> None:
    with pytest.raises(FileNotFoundError):
        read_members("does-not-exist.csv")


def test_search_members_matches_name_case_insensitively(csv_path: str) -> None:
    members = read_members(csv_path)
    results = search_members(members, "ada")
    assert [member["first_name"] for member in results] == ["Ada"]


def test_search_members_matches_email(csv_path: str) -> None:
    members = read_members(csv_path)
    results = search_members(members, "grace@example")
    assert [member["first_name"] for member in results] == ["Grace"]


def test_search_members_returns_empty_for_no_match(csv_path: str) -> None:
    members = read_members(csv_path)
    assert search_members(members, "nonexistent") == []


def test_format_members_table_aligns_columns_to_widest_value(csv_path: str) -> None:
    members = read_members(csv_path)
    table = format_members_table(members)
    lines = table.splitlines()

    assert lines[0] == "First Name  Last Name  Email"
    assert lines[1] == "----------  ---------  -----------------"
    assert lines[2] == "Ada         Lovelace   ada@example.com"
    assert lines[3] == "Grace       Hopper     grace@example.com"
    assert lines[4] == "Alan        Turing     alan@example.com"


def test_format_members_table_respects_field_selection(csv_path: str) -> None:
    members = read_members(csv_path)
    table = format_members_table(members, fields=("first_name",))

    assert table.splitlines() == ["First Name", "----------", "Ada", "Grace", "Alan"]
