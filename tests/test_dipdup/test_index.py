import datetime
from unittest import IsolatedAsyncioTestCase
from unittest.mock import AsyncMock

from dipdup.config import ContractConfig
from dipdup.config import OperationHandlerConfig
from dipdup.config import OperationHandlerTransactionPatternConfig
from dipdup.config import OperationIndexConfig
from dipdup.config import OperationType
from dipdup.config import TzktDatasourceConfig
from dipdup.index import OperationIndex
from dipdup.index import extract_operation_subgroups
from dipdup.models import OperationData

add_liquidity_operations = (
    OperationData(
        type='transaction',
        id=76905130,
        level=1676582,
        timestamp=datetime.datetime(2021, 9, 8, 16, 2, 14, tzinfo=datetime.timezone.utc),
        hash='opWVrmpgeuQ2tz65DcV5USnCFW7j7x97XQ2BzEAcmefPEjUfkMw',
        counter=15811432,
        sender_address='tz1cmAfyjWW3Rf3tH3M3maCpwsiAwBKbtmG4',
        target_address='KT1BEC9uHmADgVLXCm3wxN52qJJ85ohrWEaU',
        initiator_address=None,
        amount=None,
        status='applied',
        has_internals=True,
        storage={
            'admin': 'KT1Kfu13FmNbcZSjTPZLrAUbEYNZim6vtg6d',
            'lpFee': '400',
            'paused': False,
            'token1Id': '0',
            'token2Id': '0',
            'systemFee': '1000',
            'token1_Fee': '0',
            'token2_Fee': '0',
            'token1Check': False,
            'token1_pool': '470000000000000000000',
            'token2Check': False,
            'token2_pool': '16000000',
            'totalSupply': '86717933554715',
            'maxSwapLimit': '40',
            'token1Address': 'KT1GRSvLoikDsXujKgZPsGLX8k8VvR2Tq95b',
            'token2Address': 'KT1TwzD6zV3WeJ39ukuqxcfK2fJCnhvrdN1X',
            'lpTokenAddress': 'KT1NLZah1MKeWuveQvdsCqAUCjksKw8J296z',
        },
        block=None,
        sender_alias=None,
        nonce=None,
        target_alias='PLENTY / SMAK Swap',
        initiator_alias=None,
        entrypoint='AddLiquidity',
        parameter_json={
            'recipient': 'tz1cmAfyjWW3Rf3tH3M3maCpwsiAwBKbtmG4',
            'token1_max': '470000000000000000000',
            'token2_max': '16000000',
        },
        originated_contract_address=None,
        originated_contract_alias=None,
        originated_contract_type_hash=None,
        originated_contract_code_hash=None,
    ),
    OperationData(
        type='transaction',
        id=76905131,
        level=1676582,
        timestamp=datetime.datetime(2021, 9, 8, 16, 2, 14, tzinfo=datetime.timezone.utc),
        hash='opWVrmpgeuQ2tz65DcV5USnCFW7j7x97XQ2BzEAcmefPEjUfkMw',
        counter=15811432,
        sender_address='KT1BEC9uHmADgVLXCm3wxN52qJJ85ohrWEaU',
        target_address='KT1GRSvLoikDsXujKgZPsGLX8k8VvR2Tq95b',
        initiator_address='tz1cmAfyjWW3Rf3tH3M3maCpwsiAwBKbtmG4',
        amount=None,
        status='applied',
        has_internals=False,
        storage={
            'paused': False,
            'balances': 3943,
            'metadata': 3944,
            'lastUpdate': '1676287',
            'totalSupply': '14712639179877222051752285',
            'administrator': 'KT1GpTEq4p2XZ8w9p5xM7Wayyw5VR7tb3UaW',
            'token_metadata': 3945,
            'tokensPerBlock': '50000000000000000000',
        },
        block=None,
        sender_alias='PLENTY / SMAK Swap',
        nonce=0,
        target_alias='PLENTY',
        initiator_alias=None,
        entrypoint='transfer',
        parameter_json={
            'to': 'KT1BEC9uHmADgVLXCm3wxN52qJJ85ohrWEaU',
            'from': 'tz1cmAfyjWW3Rf3tH3M3maCpwsiAwBKbtmG4',
            'value': '470000000000000000000',
        },
        originated_contract_address=None,
        originated_contract_alias=None,
        originated_contract_type_hash=None,
        originated_contract_code_hash=None,
        diffs=(
            {
                'bigmap': 3943,
                'path': 'balances',
                'action': 'update_key',
                'content': {
                    'hash': 'exprtkqafR3YBedPSHP6Lts8WVHn4jj853RfRZiTpzYNP8KKLaU12H',
                    'key': 'tz1cmAfyjWW3Rf3tH3M3maCpwsiAwBKbtmG4',
                    'value': {
                        'balance': '1141847967508578897233841',
                        'approvals': {
                            'KT19Dskaofi6ZTkrw3Tq4pK7fUqHqCz4pTZ3': '0',
                            'KT1AbuUaPQmYLsB8n8FdSzBrxvrsm8ctwW1V': '0',
                            'KT1BEC9uHmADgVLXCm3wxN52qJJ85ohrWEaU': '0',
                            'KT1HUnqM6xFJa51PM2xHfLs7s6ARvXungtyq': '0',
                            'KT1HZkD2T4uczgYkZ6fb9gm1fymeJoRuezLz': '9060000000000000000000',
                            'KT1NtsnKQ1c3rYB12ZToP77XaJs8WDBvF221': '0',
                            'KT1PuPNtDFLR6U7e7vDuxunDoKasVT6kMSkz': '0',
                            'KT1UNBvCJXiwJY6tmHM7CJUVwNPew53XkSfh': '0',
                            'KT1VeNQa4mucRj36qAJ9rTzm4DTJKfemVaZT': '0',
                            'KT1X1LgNkQShpF9nRLYw3Dgdy4qp38MX617z': '0',
                            'KT1XVrXmWY9AdVri6KpxKo4CWxizKajmgzMt': '0',
                            'KT1XXAavg3tTj12W1ADvd3EEnm1pu6XTmiEF': '550000000000000000',
                            'KT1XutoFJ9dXvWxT7ttG86N2tSTUEpatFVTm': '0',
                        },
                    },
                },
            },
            {
                'bigmap': 3943,
                'path': 'balances',
                'action': 'add_key',
                'content': {
                    'hash': 'exprugvwjodjwqmGVVryY5uqz9fcg6BndukYj6bproCFShQ6nkuG8e',
                    'key': 'KT1BEC9uHmADgVLXCm3wxN52qJJ85ohrWEaU',
                    'value': {'balance': '470000000000000000000', 'approvals': {}},
                },
            },
        ),
    ),
    OperationData(
        type='transaction',
        id=76905132,
        level=1676582,
        timestamp=datetime.datetime(2021, 9, 8, 16, 2, 14, tzinfo=datetime.timezone.utc),
        hash='opWVrmpgeuQ2tz65DcV5USnCFW7j7x97XQ2BzEAcmefPEjUfkMw',
        counter=15811432,
        sender_address='KT1BEC9uHmADgVLXCm3wxN52qJJ85ohrWEaU',
        target_address='KT1TwzD6zV3WeJ39ukuqxcfK2fJCnhvrdN1X',
        initiator_address='tz1cmAfyjWW3Rf3tH3M3maCpwsiAwBKbtmG4',
        amount=None,
        status='applied',
        has_internals=False,
        storage={
            'freezer': 'KT1TwzD6zV3WeJ39ukuqxcfK2fJCnhvrdN1X',
            'balances': 1798,
            'metadata': 1800,
            'totalSupply': '896083333000',
            'administrator': 'KT1TwzD6zV3WeJ39ukuqxcfK2fJCnhvrdN1X',
            'token_metadata': 1801,
            'frozen_accounts': 1799,
        },
        block=None,
        sender_alias='PLENTY / SMAK Swap',
        nonce=1,
        target_alias='Smartlink',
        initiator_alias=None,
        entrypoint='transfer',
        parameter_json={'to': 'KT1BEC9uHmADgVLXCm3wxN52qJJ85ohrWEaU', 'from': 'tz1cmAfyjWW3Rf3tH3M3maCpwsiAwBKbtmG4', 'value': '16000000'},
        originated_contract_address=None,
        originated_contract_alias=None,
        originated_contract_type_hash=None,
        originated_contract_code_hash=None,
        diffs=(
            {
                'bigmap': 1798,
                'path': 'balances',
                'action': 'update_key',
                'content': {
                    'hash': 'exprtkqafR3YBedPSHP6Lts8WVHn4jj853RfRZiTpzYNP8KKLaU12H',
                    'key': 'tz1cmAfyjWW3Rf3tH3M3maCpwsiAwBKbtmG4',
                    'value': {'balance': '208684', 'approvals': {'KT1BEC9uHmADgVLXCm3wxN52qJJ85ohrWEaU': '0'}},
                },
            },
            {
                'bigmap': 1798,
                'path': 'balances',
                'action': 'add_key',
                'content': {
                    'hash': 'exprugvwjodjwqmGVVryY5uqz9fcg6BndukYj6bproCFShQ6nkuG8e',
                    'key': 'KT1BEC9uHmADgVLXCm3wxN52qJJ85ohrWEaU',
                    'value': {'balance': '16000000', 'approvals': {}},
                },
            },
        ),
    ),
    OperationData(
        type='transaction',
        id=76905133,
        level=1676582,
        timestamp=datetime.datetime(2021, 9, 8, 16, 2, 14, tzinfo=datetime.timezone.utc),
        hash='opWVrmpgeuQ2tz65DcV5USnCFW7j7x97XQ2BzEAcmefPEjUfkMw',
        counter=15811432,
        sender_address='KT1BEC9uHmADgVLXCm3wxN52qJJ85ohrWEaU',
        target_address='KT1NLZah1MKeWuveQvdsCqAUCjksKw8J296z',
        initiator_address='tz1cmAfyjWW3Rf3tH3M3maCpwsiAwBKbtmG4',
        amount=None,
        status='applied',
        has_internals=False,
        storage={
            'balances': 14107,
            'metadata': 14108,
            'totalSupply': '86717933554615',
            'administrator': 'tz1ZnK6zYJrC9PfKCPryg9tPW6LrERisTGtg',
            'securityCheck': True,
            'token_metadata': 14109,
            'exchangeAddress': 'KT1BEC9uHmADgVLXCm3wxN52qJJ85ohrWEaU',
        },
        block=None,
        sender_alias='PLENTY / SMAK Swap',
        nonce=2,
        target_alias='PLENTY / SMAK LP Token',
        initiator_alias=None,
        entrypoint='mint',
        parameter_json={'value': '86717933554615', 'address': 'tz1cmAfyjWW3Rf3tH3M3maCpwsiAwBKbtmG4'},
        originated_contract_address=None,
        originated_contract_alias=None,
        originated_contract_type_hash=None,
        originated_contract_code_hash=None,
        diffs=(
            {
                'bigmap': 14107,
                'path': 'balances',
                'action': 'add_key',
                'content': {
                    'hash': 'exprtkqafR3YBedPSHP6Lts8WVHn4jj853RfRZiTpzYNP8KKLaU12H',
                    'key': 'tz1cmAfyjWW3Rf3tH3M3maCpwsiAwBKbtmG4',
                    'value': {'balance': '86717933554615', 'approvals': {}},
                },
            },
        ),
    ),
)

index_config = OperationIndexConfig(
    datasource=TzktDatasourceConfig(kind='tzkt', url='https://api.tzkt.io', http=None),
    kind='operation',
    handlers=(
        OperationHandlerConfig(
            callback='on_fa12_and_fa12_add_liquidity',
            pattern=(
                OperationHandlerTransactionPatternConfig(
                    type='transaction',
                    source=None,
                    destination=ContractConfig(address='KT1BEC9uHmADgVLXCm3wxN52qJJ85ohrWEaU', typename='plenty_smak_amm'),
                    entrypoint='AddLiquidity',
                    optional=False,
                ),
                OperationHandlerTransactionPatternConfig(
                    type='transaction',
                    source=None,
                    destination=ContractConfig(address='KT1GRSvLoikDsXujKgZPsGLX8k8VvR2Tq95b', typename='plenty_token'),
                    entrypoint='transfer',
                    optional=False,
                ),
                OperationHandlerTransactionPatternConfig(
                    type='transaction',
                    source=None,
                    destination=ContractConfig(address='KT1TwzD6zV3WeJ39ukuqxcfK2fJCnhvrdN1X', typename='smak_token'),
                    entrypoint='transfer',
                    optional=False,
                ),
                OperationHandlerTransactionPatternConfig(
                    type='transaction',
                    source=None,
                    destination=ContractConfig(address='KT1NLZah1MKeWuveQvdsCqAUCjksKw8J296z', typename='plenty_smak_lp'),
                    entrypoint='mint',
                    optional=False,
                ),
            ),
        ),
    ),
    types=(OperationType.transaction, OperationType.origination),
    contracts=[ContractConfig(address='KT1BEC9uHmADgVLXCm3wxN52qJJ85ohrWEaU', typename='plenty_smak_amm')],
    first_level=0,
    last_level=0,
)
index_config.name = 'asdf'


class MatcherTest(IsolatedAsyncioTestCase):
    async def test_match_smak_add_liquidity(self) -> None:
        index = OperationIndex(None, index_config, None)  # type: ignore
        index._prepare_handler_args = AsyncMock()  # type: ignore

        all_filtered = tuple(extract_operation_subgroups(add_liquidity_operations, set(), set()))
        assert not all_filtered

        operation_subgroups = tuple(
            extract_operation_subgroups(
                add_liquidity_operations,
                addresses=index_config.address_filter,
                entrypoints=index_config.entrypoint_filter,
            )
        )
        assert len(operation_subgroups) == 1

        matched_handlers = await index._match_operation_subgroup(operation_subgroups[0])
        assert len(matched_handlers) == 1
        index._prepare_handler_args.assert_called()
