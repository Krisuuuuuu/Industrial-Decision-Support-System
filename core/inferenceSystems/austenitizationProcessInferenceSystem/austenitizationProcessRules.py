from fuzzy_expert.rule import FuzzyRule

from core.inferenceSystems.base.baseRules import BaseRulesWrapper

AUSTENIZATION_PROCESS_RULES: list[FuzzyRule] = [
    FuzzyRule(
        premise=[
            ("wall_thickness", "Small"),
            ("AND", "austenitization_process_time", "Unsuitable")
        ],
        consequence=[("decision", "Unsuitable")],
    ),
    FuzzyRule(
        premise=[
            ("wall_thickness", "Medium"),
            ("AND", "austenitization_process_time", "Unsuitable")
        ],
        consequence=[("decision", "Unsuitable")],
    ),
    FuzzyRule(
        premise=[
            ("wall_thickness", "High"),
            ("AND", "austenitization_process_time", "Unsuitable")
        ],
        consequence=[("decision", "Unsuitable")],
    ),
    FuzzyRule(
        premise=[
            ("wall_thickness", "Small"),
            ("AND", "austenitization_process_time", "Very_Short")
        ],
        consequence=[("decision", "Optimal")],
    ),
    FuzzyRule(
        premise=[
            ("wall_thickness", "Medium"),
            ("AND", "austenitization_process_time", "Very_Short")
        ],
        consequence=[("decision", "Optimal")],
    ),
    FuzzyRule(
        premise=[
            ("wall_thickness", "High"),
            ("AND", "austenitization_process_time", "Very_Short")
        ],
        consequence=[("decision", "Unsuitable")],
    ),
    FuzzyRule(
        premise=[
            ("wall_thickness", "Small"),
            ("AND", "austenitization_process_time", "Short")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("wall_thickness", "Medium"),
            ("AND", "austenitization_process_time", "Short")
        ],
        consequence=[("decision", "Optimal")],
    ),
    FuzzyRule(
        premise=[
            ("wall_thickness", "High"),
            ("AND", "austenitization_process_time", "Short")
        ],
        consequence=[("decision", "Unsuitable")],
    ),
    FuzzyRule(
        premise=[
            ("wall_thickness", "Small"),
            ("AND", "austenitization_process_time", "Medium")
        ],
        consequence=[("decision", "Unsuitable")],
    ),
    FuzzyRule(
        premise=[
            ("wall_thickness", "Medium"),
            ("AND", "austenitization_process_time", "Medium")
        ],
        consequence=[("decision", "Optimal")],
    ),
    FuzzyRule(
        premise=[
            ("wall_thickness", "High"),
            ("AND", "austenitization_process_time", "Medium")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("wall_thickness", "Small"),
            ("AND", "austenitization_process_time", "Long")
        ],
        consequence=[("decision", "Unsuitable")],
    ),
    FuzzyRule(
        premise=[
            ("wall_thickness", "Medium"),
            ("AND", "austenitization_process_time", "Long")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("wall_thickness", "High"),
            ("AND", "austenitization_process_time", "Long")
        ],
        consequence=[("decision", "Optimal")],
    ),
    FuzzyRule(
        premise=[
            ("wall_thickness", "Small"),
            ("AND", "austenitization_process_time", "Very_Long")
        ],
        consequence=[("decision", "Unsuitable")],
    ),
    FuzzyRule(
        premise=[
            ("wall_thickness", "Medium"),
            ("AND", "austenitization_process_time", "Very_Long")
        ],
        consequence=[("decision", "Unsuitable")],
    ),
    FuzzyRule(
        premise=[
            ("wall_thickness", "High"),
            ("AND", "austenitization_process_time", "Very_Long")
        ],
        consequence=[("decision", "Optimal")],
    ),
]


class AustenitizationProcessRulesWrapper(BaseRulesWrapper):
    def __init__(self):
        global AUSTENIZATION_PROCESS_RULES
        super().__init__()

    def set_rules(self) -> None:
        self._fuzzy_rules = AUSTENIZATION_PROCESS_RULES
