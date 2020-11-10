from itertools import cycle
import sys
import asyncio

@asyncio.coroutine
def spin(msg):
    write,flush = sys.stdout.write,sys.stdout.flush
    for i in cycle('-\|/'):
        write(i + ' ' + msg)
        flush()
        write('\x08' * (len(msg)+2))
        try:
            yield from asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
        write(' ' * (len(msg)+2) + '\x08' * (len(msg)+2))
@asyncio.coroutine
def slow_function():
    yield from asyncio.sleep(3)
    return 43
@asyncio.coroutine
def supervisor():
    spinner = asyncio.create_task(spin('thinking!'))
    print(spinner)
    result = yield from slow_function()
    spinner.cancel()
    return result

def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(supervisor())
    loop.close()
    print('answer'+' '+str(result))
if __name__ == '__main__':
    main()
