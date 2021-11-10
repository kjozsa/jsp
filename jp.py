import json
import sys

import argparse
from jsonpath_ng.ext import parse
from loguru import logger
from pygments import highlight, lexers, formatters


def colorize(json_data):
    return highlight(json_data, lexers.JsonLexer(), formatters.TerminalFormatter()).strip()


def print_results(results):
    for result in results:
        logger.trace(f'json parsing result: {result} {type(result)}')
        print(colorize(json.dumps(result)))


def main():
    parser = argparse.ArgumentParser(description='Process a jsonpath over stdin.')
    parser.add_argument('jsonpath', help='valid jsonpath expression')
    # parser.print_help()

    args = parser.parse_args()
    logger.trace(f'using jsonpath: {args.jsonpath}')

    if not sys.stdin.isatty():
        data = ''.join(sys.stdin.readlines())
    else:
        logger.error("Could not read json from <stdin>")
        sys.exit(1)

    json_data = json.loads(data)
    logger.trace(f'input: {json_data}')

    # try:
    print_results([x.value for x in parse(args.jsonpath).find(json_data)])
    # except Exception as e:
    # print(e, file=sys.stderr)


if __name__ == '__main__':
    main()
