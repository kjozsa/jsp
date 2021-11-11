import io

from jsp import read_input
from loguru import logger


def test_single_json_input(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('{"a": "b"}'))
    data = read_input()
    logger.debug(data)
    logger.debug(type(data))


def test_single_multiline_json_input(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('{\n"a": "b"\n}'))
    data = read_input()
    logger.debug(data)


def test_multi_json_input(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('{"a": "b"}\n{"c": "d"}'))
    data = read_input()
    logger.debug(data)
