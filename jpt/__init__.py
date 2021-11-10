import json
import sys

import argparse
from jsonpath_ng.ext import parse
from loguru import logger
from pygments import highlight, lexers, formatters


def get_args():
    parser = argparse.ArgumentParser(description='Process a JSONPath expression over a JSON read from <stdin>.')
    parser.add_argument('jsonpath', help='valid jsonpath expression')
    parser.add_argument('--color', help='enable/disable colored highlights', action=argparse.BooleanOptionalAction, default=True)

    args = parser.parse_args()
    logger.trace(f'using parsed arguments: {args}')
    return args


def get_data():
    if not sys.stdin.isatty():
        return json.loads(''.join(sys.stdin.readlines()))
    else:
        logger.error("Could not read json from <stdin>")
        sys.exit(1)


def colorize(json_data):
    return highlight(json_data, lexers.JsonLexer(), formatters.TerminalFormatter()).strip()


def print_results(results, color):
    for result in results:
        logger.trace(f'json parsing result: {result} {type(result)}')
        output = json.dumps(result)
        print(colorize(output)if color else output)


def main():
    try:
        args = get_args()
        print_results([x.value for x in parse(args.jsonpath).find(get_data())], args.color)
    except Exception as e:
        print(e, file=sys.stderr)


if __name__ == '__main__':
    main()
