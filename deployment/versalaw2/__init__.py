"""
VERSALAW2 - Comprehensive Indonesian Legal AI Platform
"""

# Import international law modules (yang sudah kita buat)
from .international_law.international_treaties import InternationalTreatyAnalyzer
from .international_law.diplomatic_law import DiplomaticLawAnalyzer
from .international_law.law_of_the_sea import LawOfTheSeaAnalyzer
from .international_law.international_humanitarian import InternationalHumanitarianAnalyzer
from .international_law.international_trade import InternationalTradeAnalyzer
from .international_law.extradition_mutual_legal import ExtraditionMLATAnalyzer

# Import specialized crime modules (yang sudah kita buat)
from .indonesian_law.specialized_law.anti_corruption import AntiCorruptionAnalyzer
from .indonesian_law.specialized_law.money_laundering import MoneyLaunderingAnalyzer
from .indonesian_law.specialized_law.human_trafficking import HumanTraffickingAnalyzer
from .indonesian_law.specialized_law.illegal_mining import IllegalMiningAnalyzer
from .indonesian_law.specialized_law.illegal_logging import IllegalLoggingAnalyzer
from .indonesian_law.specialized_law.narcotics import NarcoticsAnalyzer
from .indonesian_law.specialized_law.smuggling import SmugglingAnalyzer
from .indonesian_law.specialized_law.cyber_crime import CyberCrimeAnalyzer

__all__ = [
    # International Law Modules
    'InternationalTreatyAnalyzer',
    'DiplomaticLawAnalyzer',
    'LawOfTheSeaAnalyzer',
    'InternationalHumanitarianAnalyzer',
    'InternationalTradeAnalyzer',
    'ExtraditionMLATAnalyzer',
    
    # Specialized Crime Modules
    'AntiCorruptionAnalyzer',
    'MoneyLaunderingAnalyzer',
    'HumanTraffickingAnalyzer',
    'IllegalMiningAnalyzer',
    'IllegalLoggingAnalyzer',
    'NarcoticsAnalyzer',
    'SmugglingAnalyzer',
    'CyberCrimeAnalyzer'
]
