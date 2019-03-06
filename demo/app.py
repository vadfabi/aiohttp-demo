"""
Simple demo application for building a REST API using aiohttp.

Some libraries to look at:
- https://pypi.python.org/pypi/aiohttp_cors/0.4.0
- https://pypi.python.org/pypi/aiohttp-json-rpc/0.5.1
"""

import logging

from aiohttp import web
import asyncio
import asyncpg
import uvloop

from demo.routes import setup_routes
from demo.middleware import setup_middlewares


async def init(loop):
    host = '0.0.0.0'
    port = 8080

    app = web.Application(
        loop=loop,
    )
    app['pool'] = await asyncpg.create_pool(
        dsn='postgres://aiodemo:aiodemopwd@db.aiodemo.com:5432/aiodemo'
    )

    setup_routes(app)
    setup_middlewares(app)

    return app, host, port


def main():
    # init logging
    logging.basicConfig(level=logging.DEBUG)

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    loop = asyncio.get_event_loop()

    app, host, port = loop.run_until_complete(init(loop))
    web.run_app(app, host=host, port=port)


if __name__ == '__main__':
    main()
