# base12
To spread the core values of Chinese socialism. 

The project is named base12 but actually it's a base16 encoding with the following alphabet:

| code/value | code/value | code/value | code/value |
| ---------- | ---------- | ---------- | ---------- |
| 社会/0 | 主义/4 | 核心/8 | 价值/C |
| 富强/1 | 民主/5 | 文明/9 | 和谐/D |
| 自由/2 | 平等/6 | 公正/A | 法治/E |
| 爱国/3 | 敬业/7 | 诚信/B | 友善/F |

A tcp tunnel is also provided for convenience. 

## Install

```bash
$ git clone https://github.com/fduxiao/base12/
$ cd base12
# Tests
$ python setup.py test  # optional
$ pip install .
```

## Usage
```bash
# show help
$ base12 -h
# encode
$ base12 [inputfile=stdin] [-o outputfile=stdout]
# decode
$ base12 -d [inputfile=stdin] [-o outputfile=stdout]
```

## Example
```bash
$ base12
> Hello world.
主义核心平等民主平等价值平等价值平等友善自由社会敬业敬业平等友善敬业自由平等价值平等主义自由法治社会公正
$ base12 -d
> 主义核心平等民主平等价值平等价值平等友善自由社会敬业敬业平等友善敬业自由平等价值平等主义自由法治社会公正
Hello world.
```