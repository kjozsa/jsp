## JSONPath CLI tool with syntax highlight

Example scenarios:

```shell
$ cat sample.json | jsp $.store.bicycle.color
"red"

$ cat sample.json | jsp $.store.book[*].title
"Sayings of the Century"
"Sword of Honour"
"Moby Dick"
"The Lord of the Rings"

$ cat sample.json | jsp $..book[?(@.category='fiction')].isbn
"0-553-21311-3"
"0-395-19395-8"
```

The original name of this project was meant to be JPT as JsonPath Tools, but PyPI had a same-named obsolete package. Therefore for now, this will run by the name JSP - hopefully noone remembers Java Server Pages anymore anyway 😀 