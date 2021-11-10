## JSONPath CLI tool

Example scenarios:

```shell
$ cat sample.json | jpt $.store.bicycle.color
"red"

$ cat sample.json | jpt $.store.book[*].title
"Sayings of the Century"
"Sword of Honour"
"Moby Dick"
"The Lord of the Rings"

$ cat sample.json | jpt $..book[?(@.category='fiction')].isbn
"0-553-21311-3"
"0-395-19395-8"
```
