from typing import Optional
from decimal import Decimal

from dipdup.models import OperationData, Origination, Transaction
from dipdup.context import HandlerContext

import demo.models as models

from demo.types.quipuswap_fa12.parameter.tez_to_token_payment import TezToTokenPaymentParameter
from demo.types.quipuswap_fa12.storage import QuipuswapFa12Storage
from demo.types.plenty_fa12.parameter.transfer import TransferParameter
from demo.types.plenty_fa12.storage import PlentyFa12Storage


async def on_tez_to_token(
    ctx: HandlerContext,
    tez_to_token_payment: Transaction[TezToTokenPaymentParameter, QuipuswapFa12Storage],
    transfer: Transaction[TransferParameter, PlentyFa12Storage],
) -> None:
    trader_address = tez_to_token_payment.data.sender_address
    tez_qty = Decimal(tez_to_token_payment.data.amount) / (10 ** 6)
    token_qty = Decimal(transfer.parameter.value) / (10 ** 18)

    trader, _ = await models.Trader.get_or_create(address=trader_address)
    trader.trades_count += 1
    trader.trades_volume += tez_qty
    await trader.save()

    trade = models.Trade(
        trader=trader,
        side=models.TradeSide.BUY,
        tez_qty=tez_qty,
        token_qty=token_qty,
        price=tez_qty / token_qty,
        level=tez_to_token_payment.data.level,
        timestamp=tez_to_token_payment.data.timestamp
    )
    await trade.save()
