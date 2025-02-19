from contextlib import AsyncExitStack
from datetime import datetime
from os.path import dirname
from os.path import join
from unittest import IsolatedAsyncioTestCase

from pytz import UTC

from dipdup.config import DipDupConfig
from dipdup.context import pending_indexes
from dipdup.dipdup import IndexDispatcher
from dipdup.enums import IndexStatus
from dipdup.enums import IndexType
from dipdup.exceptions import ReindexingRequiredError
from dipdup.models import Index
from dipdup.test import create_test_dipdup


async def _create_index(hash_: str) -> None:
    await Index.create(
        **{
            'level': 1365000,
            'name': 'hen_mainnet',
            'template': None,
            'config_hash': hash_,
            'created_at': datetime(2021, 10, 8, 18, 43, 35, 744412, tzinfo=UTC),
            'template_values': {},
            'status': IndexStatus.NEW,
            'updated_at': datetime(2021, 10, 8, 18, 43, 35, 744449, tzinfo=UTC),
            'type': IndexType.operation,
        }
    )


async def spawn_index(dispatcher: IndexDispatcher, name: str) -> None:
    await dispatcher._ctx.spawn_index(name)
    dispatcher._indexes[name] = pending_indexes.pop()


class IndexStateTest(IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        name = 'hic_et_nunc.yml'
        config_path = join(dirname(__file__), '..', 'integration_tests', name)
        self.config = DipDupConfig.load([config_path])

        self.new_hash = '1ac841facf593f2ef2de2e747c7b547d4a05891a8633c4a238ad73c28a421f71'

    async def test_first_run(self) -> None:
        async with AsyncExitStack() as stack:
            # Arrange
            dipdup = await create_test_dipdup(self.config, stack)
            dispatcher = IndexDispatcher(dipdup._ctx)

            # Act
            await spawn_index(dispatcher, 'hen_mainnet')

            # Assert
            index = await Index.filter().get()
            self.assertEqual(self.new_hash, index.config_hash)

    async def test_new_hash(self) -> None:
        async with AsyncExitStack() as stack:
            # Arrange
            dipdup = await create_test_dipdup(self.config, stack)
            dispatcher = IndexDispatcher(dipdup._ctx)
            await _create_index(self.new_hash)

            # Act
            await dispatcher._load_index_states()

            # Assert
            index = await Index.filter().get()
            self.assertEqual(self.new_hash, index.config_hash)

    async def test_invalid_hash(self) -> None:
        async with AsyncExitStack() as stack:
            # Arrange
            dipdup = await create_test_dipdup(self.config, stack)
            dispatcher = IndexDispatcher(dipdup._ctx)
            await _create_index('hehehe')

            # Act, Assert
            with self.assertRaises(ReindexingRequiredError):
                await dispatcher._load_index_states()
