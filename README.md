# base12
To spread the core values of Chinese socialism. 

The project is named base12 but actually it's a base16 encoding with the following alphabet:

| code/value | code/value | code/value | code/value |
| ---------- | ---------- | ---------- | ---------- |
| 社会/0 | 主义/4 | 核心/8 | 价值/C |
| 富强/1 | 民主/5 | 文明/9 | 和谐/D |
| 自由/2 | 平等/6 | 公正/A | 法治/E |
| 爱国/3 | 敬业/7 | 诚信/B | 友善/F |


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

## b12tunnel
A tcp tunnel is provided named `b12tunnel`. 
An example for a client and a server to communicate is shown below. 
```bash
# b12tunnel -h for help
$ nc -l -p 1234  # a nc server
# setup a b12tunnel to send decoded data to nc server
# b12tunnel -r remote_server -p remote_port -l local_port -t tunnel_type 
$ b12tunnel -r localhost -p 1234 -l 1236 -t decode 
# Then setup another b12tunnel connected to the decoding server
# b12tunnel -r remote_server -p remote_port -l local_port -t tunnel_type 
$ b12tunnel -r localhost -p 1236 -l 1237 -t encode 
# Then start a nc client as usual but with the port of the tunnel
$ nc localhost 1237
```