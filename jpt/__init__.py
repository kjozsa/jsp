import json
import sys

import argparse
from jsonpath_ng.ext import parse
from loguru import logger
from pygments import highlight, lexers, formatters


def get_jsonpath():
    parser = argparse.ArgumentParser(description='Process a jsonpath over stdin.')
    parser.add_argument('jsonpath', help='valid jsonpath expression')

    args = parser.parse_args()
    logger.trace(f'using jsonpath: {args.jsonpath}')
    return args.jsonpath


def get_data():
    if not sys.stdin.isatty():
        data = ''.join(sys.stdin.readlines())
        logger.trace(f'input: {data}')
        return json.loads(data)
    else:
        logger.error("Could not read json from <stdin>")
        sys.exit(1)


def colorize(json_data):
    return highlight(json_data, lexers.JsonLexer(), formatters.TerminalFormatter()).strip()


def print_results(results):
    for result in results:
        logger.trace(f'json parsing result: {result} {type(result)}')
        print(colorize(json.dumps(result)))


def main():
    try:
        print_results([x.value for x in parse(get_jsonpath()).find(get_data())])
    except Exception as e:
        print(e, file=sys.stderr)


if __name__ == '__main__':
    main()
