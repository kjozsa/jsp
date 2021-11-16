## JSONPath command line tool with syntax highlight and formatting
_it's like `jq`, but using JSONPath syntax_

### Install / upgrade
Use the standard python package manager: 
`pip install -U jsp`

### Basic examples

```shell
$ cat sample.json | jsp $.store.bicycle.color
"red"

$ cat sample.json | jsp $.store.book[*].title
"Sayings of the Century"
"Sword of Honour"
"Moby Dick"
"The Lord of the Rings"

$ cat sample.json | jsp -f $..book[2]   # -f for formatting the output
{
   "category": "fiction",
   "author": "Herman Melville",
   "title": "Moby Dick",
   "isbn": "0-553-21311-3",
   "price": 8.99
}

$ cat sample.json | jsp $..book[?(@.category='fiction')].isbn
"0-553-21311-3"
"0-395-19395-8"
```

Simply parse JSON input without specifying a JSONPath expression (also handles multiple JSON objects from stdin):
```shell
cat sample-multi.json | jsp
{"category": "reference", "author": "Nigel Rees", "title": "Sayings of the Century", "price": 8.95}
{"category": "fiction", "author": "Evelyn Waugh", "title": "Sword of Honour", "price": 12.99}
{"category": "fiction", "author": "Herman Melville", "title": "Moby Dick", "isbn": "0-553-21311-3", "price": 8.99}
{"category": "fiction", "author": "J. R. R. Tolkien", "title": "The Lord of the Rings", "isbn": "0-395-19395-8", "price": 22.99}
```

### Usage instructions
```
usage: jsp [-h] [-c | --color | --no-color] [-f | --format | --no-format] [-i INDENT] [-v] [jsonpath]

jsp v0.8.6 - Process a JSONPath expression over a JSON read from <stdin>.

positional arguments:
  jsonpath              valid jsonpath expression

optional arguments:
  -h, --help            show this help message and exit
  -c, --color, --no-color
                        enable/disable colored highlights (default: True)
  -f, --format, --no-format
                        enable/disable formatting output (default: False)
  -i INDENT, --indent INDENT
                        number of spaces for indent on formatting
  -v, --version         show program's version number and exit

```

### About the name
Originally the name of this project was meant to be JPT as JsonPath Tools, but PyPI had a same-named obsolete package. Therefore, this will now run by the name JSP - hopefully noone remembers Java Server Pages anymore anyway 😀 
