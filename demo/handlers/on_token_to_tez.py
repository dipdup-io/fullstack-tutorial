from typing import Optional
from decimal import Decimal

from dipdup.models import OperationData, Origination, Transaction
from dipdup.context import HandlerContext

import demo.models as models

from demo.types.quipuswap_fa12.parameter.token_to_tez_payment import TokenToTezPaymentParameter
from demo.types.quipuswap_fa12.storage import QuipuswapFa12Storage
from demo.types.plenty_fa12.parameter.transfer import TransferParameter
from demo.types.plenty_fa12.storage import PlentyFa12Storage



async def on_token_to_tez(
    ctx: HandlerContext,
    token_to_tez_payment: Transaction[TokenToTezPaymentParameter, QuipuswapFa12Storage],
    transfer: Transaction[TransferParameter, PlentyFa12Storage],
    transaction_0: OperationData,
) -> None:
    trader_address = token_to_tez_payment.data.sender_address
    tez_qty = Decimal(transaction_0.amount) / (10 ** 6)
    token_qty = Decimal(transfer.parameter.value) / (10 ** 18)

    trader, _ = await models.Trader.get_or_create(address=trader_address)
    trader.trades_count += 1
    trader.trades_volume += tez_qty
    await trader.save()

    trade = models.Trade(
        trader=trader,
        side=models.TradeSide.SELL,
        tez_qty=tez_qty,
        token_qty=token_qty,
        price=tez_qty / token_qty,
        level=token_to_tez_payment.data.level,
        timestamp=token_to_tez_payment.data.timestamp
    )
    await trade.save()
