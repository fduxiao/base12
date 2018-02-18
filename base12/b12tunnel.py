import asyncio
import argparse
from .base12 import b12decode, b12encode


def tunnel(remote, port, sender_filter=lambda x: x, receiver_filter=lambda x: x, loop=None, size=-1):
    async def handler(reader, writer):
        try:
            remote_reader, remote_writer = await asyncio.open_connection(remote, port, loop=loop)
        except Exception as err:
            print(err)
            return

        async def read_from_local():
            try:
                d = await reader.read(size)
            except KeyboardInterrupt:
                return None, None
            except Exception as e:
                return 'error', str(e)
            return 'local', d

        async def read_from_remote():
            try:
                d = await remote_reader.read(size)
            except KeyboardInterrupt:
                return None, None
            except Exception as e:
                return 'error', str(e)
            return 'remote', d

        pending = {
            read_from_local(),
            read_from_remote(),
        }

        while True:
            if reader.at_eof() or remote_reader.at_eof():
                break

            done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED, loop=loop)

            flag = False
            for f in done:
                where, data = f.result()
                if where is None:  # keyboard interrupt
                    exit(0)
                elif where == 'error':
                    print(data)
                    flag = True
                    break

                if len(data) == 0:
                    flag = True
                    break
                if where == 'local':
                    remote_writer.write(sender_filter(data))
                    await remote_writer.drain()
                    pending.add(read_from_local())
                elif where == 'remote':
                    writer.write(receiver_filter(data))
                    await writer.drain()
                    pending.add(read_from_remote())
            if flag:
                break

        writer.close()
        remote_writer.close()
    return handler


def start_server(host, local, remote, port, loop=None, server_type='p'):
    if loop is None:
        loop = asyncio.get_event_loop()

    receiver_filter = sender_filter = lambda x: x
    if server_type.startswith('p'):
        receiver_filter = sender_filter = lambda x: x
    elif server_type.startswith('s'):  # sending encoded data
        # remote is the decoding server
        receiver_filter = b12decode
        sender_filter = b12encode
    elif server_type.startswith('r'):  # receiving encoded data
        # remote is a plain tcp server
        receiver_filter = b12encode
        sender_filter = b12decode

    loop.run_until_complete(asyncio.start_server(tunnel(
        remote,
        port,
        loop=loop,
        receiver_filter=receiver_filter,
        sender_filter=sender_filter,
        size=8192
    ), host, local))
    try:
        loop.run_forever()
    finally:
        loop.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--server', default='0.0.0.0', help='the address to listen on')
    parser.add_argument('-l', '--local', default=1235, type=int, help='local port')
    parser.add_argument('-r', '--remote', help='remote address')
    parser.add_argument('-p', '--port', default=1235, help='remote port')
    parser.add_argument('-t', '--type', default='p', help='s[ender]/r[eceiver]/p[lain]')

    args = parser.parse_args()
    start_server(args.server, args.local, args.remote, args.port, server_type=args.type)


if __name__ == '__main__':
    main()
