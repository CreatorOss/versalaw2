"""
VERSALAW2 Specialized Law Modules
Analisis hukum khusus untuk kejahatan kompleks
"""

from .anti_corruption import AntiCorruptionAnalyzer
from .money_laundering import MoneyLaunderingAnalyzer
from .human_trafficking import HumanTraffickingAnalyzer

__all__ = [
    'AntiCorruptionAnalyzer',
    'MoneyLaunderingAnalyzer', 
    'HumanTraffickingAnalyzer'
]
from .illegal_mining import IllegalMiningAnalyzer
from .illegal_logging import IllegalLoggingAnalyzer

__all__ += [
    'IllegalMiningAnalyzer',
    'IllegalLoggingAnalyzer'
]
from .narcotics import NarcoticsAnalyzer
from .smuggling import SmugglingAnalyzer
from .cyber_crime import CyberCrimeAnalyzer

__all__ += [
    'NarcoticsAnalyzer',
    'SmugglingAnalyzer', 
    'CyberCrimeAnalyzer'
]
from .terrorism_law import TerrorismLawAnalyzer

__all__ += [
    'TerrorismLawAnalyzer'
]
