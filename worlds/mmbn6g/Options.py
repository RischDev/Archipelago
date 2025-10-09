from dataclasses import dataclass
from Options import Choice, Range, DefaultOnToggle, Toggle, PerGameCommonOptions


class IncludeJobs(DefaultOnToggle):
    """
    Whether Jobs can contain progression or useful items.
    """
    display_name = "Include Jobs"


class TradeQuestHinting(Choice):
    """
    Whether NPCs offering Chip Trades should show what item they provide.
    None - NPCs will not provide any information on what item they will give
    Partial - NPCs will state if an item is progression or not, but not the specific item
    Full - NPCs will state what item they will give, providing an Archipelago Hint when doing so
    """
    display_name = "Trade Quest Hinting"
    option_none = 0
    option_partial = 1
    option_full = 2
    default = 2


@dataclass
class MMBN6Options(PerGameCommonOptions):
    include_jobs: IncludeJobs
    trade_quest_hinting: TradeQuestHinting
