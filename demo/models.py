from tortoise import Model, fields
from enum import IntEnum


class TradeSide(IntEnum):
    BUY = 0
    SELL = 1


class Trade(Model):
    id = fields.IntField(pk=True)
    trader = fields.ForeignKeyField('models.Trader', 'trades')
    side = fields.IntEnumField(enum_type=TradeSide)
    tez_qty = fields.DecimalField(decimal_places=6, max_digits=16)
    token_qty = fields.DecimalField(decimal_places=18, max_digits=32)
    price = fields.DecimalField(decimal_places=6, max_digits=32)
    level = fields.BigIntField()
    timestamp = fields.DatetimeField()


class Trader(Model):
    address = fields.CharField(max_length=36, pk=True)
    trades_count = fields.BigIntField(default=0)
    trades_volume = fields.DecimalField(decimal_places=6, max_digits=32, default=0)