from fuzzy_expert.rule import FuzzyRule
import core.inferenceSystems.base.baseRules as r

MATERIAL_DEFECTS_RULES = [
    FuzzyRule(
        premise=[
            ("wall_thickness", "Small"),
            ("AND", "isothermal_transformation_time", "Unsuitable")
        ],
        consequence=[("decision", "Unsuitable")],
    ),
    FuzzyRule(
        premise=[
            ("wall_thickness", "Medium"),
            ("AND", "isothermal_transformation_time", "Unsuitable")
        ],
        consequence=[("decision", "Unsuitable")],
    ),
    FuzzyRule(
        premise=[
            ("wall_thickness", "High"),
            ("AND", "isothermal_transformation_time", "Unsuitable")
        ],
        consequence=[("decision", "Unsuitable")],
    ),
    FuzzyRule(
        premise=[
            ("wall_thickness", "Small"),
            ("AND", "isothermal_transformation_time", "Very_Short")
        ],
        consequence=[("decision", "Optimal")],
    ),
    FuzzyRule(
        premise=[
            ("wall_thickness", "Medium"),
            ("AND", "isothermal_transformation_time", "Very_Short")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("wall_thickness", "High"),
            ("AND", "isothermal_transformation_time", "Very_Short")
        ],
        consequence=[("decision", "Unsuitable")],
    ),
    FuzzyRule(
        premise=[
            ("wall_thickness", "Small"),
            ("AND", "isothermal_transformation_time", "Short")
        ],
        consequence=[("decision", "Optimal")],
    ),
    FuzzyRule(
        premise=[
            ("wall_thickness", "Medium"),
            ("AND", "isothermal_transformation_time", "Short")
        ],
        consequence=[("decision", "Optimal")],
    ),
    FuzzyRule(
        premise=[
            ("wall_thickness", "High"),
            ("AND", "isothermal_transformation_time", "Short")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("wall_thickness", "Small"),
            ("AND", "isothermal_transformation_time", "Medium")
        ],
        consequence=[("decision", "Optimal")],
    ),
    FuzzyRule(
        premise=[
            ("wall_thickness", "Medium"),
            ("AND", "isothermal_transformation_time", "Medium")
        ],
        consequence=[("decision", "Optimal")],
    ),
    FuzzyRule(
        premise=[
            ("wall_thickness", "High"),
            ("AND", "isothermal_transformation_time", "Medium")
        ],
        consequence=[("decision", "Optimal")],
    ),
    FuzzyRule(
        premise=[
            ("wall_thickness", "Small"),
            ("AND", "isothermal_transformation_time", "Long")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("wall_thickness", "Medium"),
            ("AND", "isothermal_transformation_time", "Long")
        ],
        consequence=[("decision", "Optimal")],
    ),
    FuzzyRule(
        premise=[
            ("wall_thickness", "High"),
            ("AND", "isothermal_transformation_time", "Long")
        ],
        consequence=[("decision", "Optimal")],
    ),
    FuzzyRule(
        premise=[
            ("wall_thickness", "Small"),
            ("AND", "isothermal_transformation_time", "Very_Long")
        ],
        consequence=[("decision", "Unsuitable")],
    ),
    FuzzyRule(
        premise=[
            ("wall_thickness", "Medium"),
            ("AND", "isothermal_transformation_time", "Very_Long")
        ],
        consequence=[("decision", "Average")],
    ),
    FuzzyRule(
        premise=[
            ("wall_thickness", "High"),
            ("AND", "isothermal_transformation_time", "Very_Long")
        ],
        consequence=[("decision", "Optimal")],
    ),
]


class IsothermalTransformationRulesWrapper(r.BaseRulesWrapper):
    def __init__(self):
        global MATERIAL_DEFECTS_RULES
        super().__init__()

    def set_rules(self):
        self._fuzzy_rules = MATERIAL_DEFECTS_RULES
