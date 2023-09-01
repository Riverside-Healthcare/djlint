"""Test jinja parenthesis.

poetry run pytest tests/test_jinja/test_parenthesis.py
"""
import pytest

from src.djlint.reformat import formatter
from tests.conftest import printer

test_data = [
    pytest.param(
        "{{ url('foo') }}",
        '{{ url("foo") }}\n',
        id="single_parenthesis_tag",
    ),
    pytest.param(
        '<a href="{{ url(\'fo"o\') }}"\n'
        '   href="{{ url(\'fo\\"o\') }}"\n'
        '   href="{{ url("fo\'o") }}"\n'
        '   href="{{ url("fo\\\'o") }}"\n'
        "   href=\"{{ url('foo') }}\"\n"
        '   href="{{ url("foo") }}"></a>',
        '<a href="{{ url(\'fo"o\') }}"\n'
        '   href="{{ url(\'fo\\"o\') }}"\n'
        "   href=\"{{ url('fo\\'o') }}\"\n"
        "   href=\"{{ url('fo\\\\'o') }}\"\n"
        "   href=\"{{ url('foo') }}\"\n"
        "   href=\"{{ url('foo') }}\"></a>",
        id="single_escaped quote",
    ),
    pytest.param(
        '<a href="{{ url_for(\'test_reminders\') }}" class="btn clr sm">Test reminders</a>',
        '<a href="{{ url_for(\'test_reminders\') }}" class="btn clr sm">Test reminders</a>\n',
        id="single_url_for",
    ),
    pytest.param(
        '{{ url("foo") }}',
        '{{ url("foo") }}\n',
        id="double_parenthesis_tag",
    ),
    pytest.param(
        '<a href="{{ url_for("test_reminders") }}" class="btn clr sm">Test reminders</a>',
        '<a href="{{ url_for(\'test_reminders\') }}" class="btn clr sm">Test reminders</a>\n',
        id="double_url_for",
    ),
]


@pytest.mark.parametrize(("source", "expected"), test_data)
def test_base(source, expected, jinja_config):
    output = formatter(jinja_config, source)

    printer(expected, source, output)
    assert expected == output
