import logging

from aiohttp_utils import Response

from demo import status


logger = logging.getLogger(__name__)

async def request_logging_middleware(app, handler):
    async def middleware_handler(request):
        logger.info(request)
        return await handler(request)
    return middleware_handler


async def auth_middleware(app, handler):
    async def middleware(request):
        request.user = None
        token = request.headers.get('authorization', None)

        if token != 'abc123':
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        # do user lookup here, maybe
        return await handler(request)
    return middleware


def setup_middlewares(app):
    app.middlewares.append(request_logging_middleware)
    app.middlewares.append(auth_middleware)
