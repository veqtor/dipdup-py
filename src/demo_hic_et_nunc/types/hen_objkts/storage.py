# generated by datamodel-codegen:
#   filename:  storage.json

from __future__ import annotations

from typing import Any, Dict, List

from pydantic import BaseModel, Extra


class Key(BaseModel):
    address: str
    nat: str


class LedgerItem(BaseModel):
    key: Key
    value: str


class Metadata(BaseModel):
    class Config:
        extra = Extra.allow

    __root__: str


class Key1(BaseModel):
    owner: str
    operator: str
    token_id: str


class Operator(BaseModel):
    key: Key1
    value: Dict[str, Any]


class TokenInfo(BaseModel):
    class Config:
        extra = Extra.allow

    __root__: str


class TokenMetadata(BaseModel):
    class Config:
        extra = Extra.allow

    token_id: str
    token_info: Dict[str, TokenInfo]


class Storage(BaseModel):
    administrator: str
    all_tokens: str
    ledger: List[LedgerItem]
    metadata: Dict[str, Metadata]
    operators: List[Operator]
    paused: bool
    token_metadata: Dict[str, TokenMetadata]
