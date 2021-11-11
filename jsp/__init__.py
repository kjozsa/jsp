import argparse
import json
import sys
from json import JSONDecodeError

from jsonpath_ng.ext import parse
from loguru import logger
from pygments import highlight, lexers, formatters

__version__ = '0.8'
parser = None


def get_args():
    global parser
    parser = argparse.ArgumentParser(description='%(prog)s v' + __version__ + ' - Process a JSONPath expression over a JSON read from <stdin>.')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s v' + __version__)
    parser.add_argument('jsonpath', help='valid jsonpath expression', nargs='?', default='$')
    parser.add_argument('--color', help='enable/disable colored highlights', action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument('-f', '--format', '-i', '--indent', help='enable/disable formatting output', action=argparse.BooleanOptionalAction, default=False)

    args = parser.parse_args()
    logger.trace(f'using parsed arguments: {args}')
    return args


def read_input() -> list:
    if not sys.stdin.isatty():
        try:
            lines = [line for line in sys.stdin.readlines() if line.strip() != '']
            return [json.loads(line) for line in lines]
        except JSONDecodeError:
            logger.trace(f'falling back to multiline input')
            return [json.loads(''.join(lines))]

    else:
        logger.error("Could not read json from <stdin>")
        parser.print_help()
        sys.exit(1)


def colorize(json_data):
    return highlight(json_data, lexers.JsonLexer(), formatters.TerminalFormatter()).strip()


def print_results(results, color, format):
    for result in results:
        logger.trace(f'json parsing result: {result} {type(result)}')
        output = json.dumps(result, indent=3) if format else json.dumps(result)
        print(colorize(output) if color else output)


def main():
    try:
        args = get_args()
        for data in read_input():
            print_results([x.value for x in parse(args.jsonpath).find(data)], args.color, args.format)

    except Exception as e:
        print(e, file=sys.stderr)


if __name__ == '__main__':
    main()
