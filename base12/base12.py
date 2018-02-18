import base64


base12_table = {
    '社会'.encode(): b'0',
    '富强'.encode(): b'1',
    '自由'.encode(): b'2',
    '爱国'.encode(): b'3',
    '主义'.encode(): b'4',
    '民主'.encode(): b'5',
    '平等'.encode(): b'6',
    '敬业'.encode(): b'7',
    '核心'.encode(): b'8',
    '文明'.encode(): b'9',
    '公正'.encode(): b'A',
    '诚信'.encode(): b'B',
    '价值'.encode(): b'C',
    '和谐'.encode(): b'D',
    '法治'.encode(): b'E',
    '友善'.encode(): b'F',
}


def b12encode(bs):
    base16 = base64.b16encode(bs)
    for k, v in base12_table.items():
        base16 = base16.replace(v, k)
    return base16


def b12decode(bs):
    for k, v in base12_table.items():
        bs = bs.replace(k, v)
    return base64.b16decode(bs)
