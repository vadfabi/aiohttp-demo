import logging

from aiohttp_utils import Response

from schematics.exceptions import ModelValidationError

import ujson

from demo import __version__
from demo import status
from demo.models import User

logger = logging.getLogger(__name__)


async def hello(request):
    return Response({'message': "Hello, world!"})


async def version(request):
    return Response({'version': __version__})


async def get_user(request):
    user_id = request.match_info.get('id', None)
    logger.debug(user_id)

    pool = request.app['pool']
    # Take a connection from the pool.
    async with pool.acquire() as connection:
        # # Open a transaction.
        # async with connection.transaction(readonly=True):
        # Run the query passing the request argument.
        result = await connection.fetchrow(
            'SELECT * FROM accounts_user WHERE id=$1',
            user_id
        )

        if result:
            logger.debug(result)
            user = User(dict(result.items()))
            return Response(user.to_primitive())

    return Response(status=status.HTTP_404_NOT_FOUND)


async def profile_validation(request):
    """Simple email validation"""
    data = await request.json(loads=ujson.loads)
    user = User(data)

    try:
        user.validate()
    except ModelValidationError as e:
        logger.debug(e.messages['email'].messages)
        return Response({
            'valid': False,
            'errors': e.messages,
        }, status=status.HTTP_409_CONFLICT)

    return Response({'valid': True})
