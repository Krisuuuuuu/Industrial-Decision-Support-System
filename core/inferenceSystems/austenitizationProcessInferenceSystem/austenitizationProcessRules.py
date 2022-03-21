from fuzzy_expert.rule import FuzzyRule
import core.inferenceSystems.base.baseRules as r

AUSTENIZATION_PROCESS_RULES = [
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


class AustenitizationProcessRulesWrapper(r.BaseRulesWrapper):
    def __init__(self):
        global AUSTENIZATION_PROCESS_RULES
        super().__init__()

    def set_rules(self):
        self._fuzzy_rules = AUSTENIZATION_PROCESS_RULES
