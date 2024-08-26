"""Test jinja parenthesis.

poetry run pytest tests/test_jinja/test_parenthesis.py
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from src.djlint.reformat import formatter
from tests.conftest import printer

if TYPE_CHECKING:
    from src.djlint.settings import Config

test_data = [pytest.param(("{{ url('foo')}}"), ('{{ url("foo") }}\n'), id="parenthesis_tag")]


@pytest.mark.parametrize(("source", "expected"), test_data)
def test_base(source: str, expected: str, jinja_config: Config) -> None:
    output = formatter(jinja_config, source)

    printer(expected, source, output)
    assert expected == output
