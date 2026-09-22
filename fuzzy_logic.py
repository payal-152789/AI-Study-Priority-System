import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


def calculate_study_priority(
    days_left,
    preparation,
    difficulty,
    pending_chapters
):

    # -----------------------------
    # Input Variables
    # -----------------------------

    urgency = ctrl.Antecedent(
        np.arange(0, 31, 1),
        "urgency"
    )

    prep = ctrl.Antecedent(
        np.arange(0, 101, 1),
        "prep"
    )

    diff = ctrl.Antecedent(
        np.arange(1, 11, 1),
        "diff"
    )

    pending = ctrl.Antecedent(
        np.arange(0, 11, 1),
        "pending"
    )

    # -----------------------------
    # Output Variable
    # -----------------------------

    priority = ctrl.Consequent(
        np.arange(0, 101, 1),
        "priority"
    )

    # -----------------------------
    # Membership Functions
    # -----------------------------

    urgency["low"] = fuzz.trapmf(
        urgency.universe,
        [7, 14, 30, 30]
    )

    urgency["medium"] = fuzz.trimf(
        urgency.universe,
        [3, 7, 14]
    )

    urgency["high"] = fuzz.trapmf(
        urgency.universe,
        [0, 0, 2, 5]
    )

    prep["low"] = fuzz.trapmf(
        prep.universe,
        [0, 0, 25, 45]
    )

    prep["medium"] = fuzz.trimf(
        prep.universe,
        [30, 50, 70]
    )

    prep["high"] = fuzz.trapmf(
        prep.universe,
        [60, 80, 100, 100]
    )

    diff["low"] = fuzz.trapmf(
        diff.universe,
        [1, 1, 3, 5]
    )

    diff["medium"] = fuzz.trimf(
        diff.universe,
        [3, 5, 7]
    )

    diff["high"] = fuzz.trapmf(
        diff.universe,
        [5, 7, 10, 10]
    )

    pending["low"] = fuzz.trapmf(
        pending.universe,
        [0, 0, 1, 2]
    )

    pending["medium"] = fuzz.trimf(
        pending.universe,
        [1, 3, 5]
    )

    pending["high"] = fuzz.trapmf(
        pending.universe,
        [4, 6, 10, 10]
    )

    priority["low"] = fuzz.trapmf(
        priority.universe,
        [0, 0, 20, 40]
    )

    priority["medium"] = fuzz.trimf(
        priority.universe,
        [30, 50, 70]
    )

    priority["high"] = fuzz.trapmf(
        priority.universe,
        [60, 80, 100, 100]
    )

    # -----------------------------
    # Fuzzy Rules
    # -----------------------------

    rule1 = ctrl.Rule(
        urgency["high"] & prep["low"],
        priority["high"]
    )

    rule2 = ctrl.Rule(
        diff["high"] & prep["low"],
        priority["high"]
    )

    rule3 = ctrl.Rule(
        pending["high"] & urgency["high"],
        priority["high"]
    )

    rule4 = ctrl.Rule(
        urgency["low"] & prep["high"],
        priority["low"]
    )

    rule5 = ctrl.Rule(
        urgency["medium"] &
        prep["medium"] &
        diff["medium"],
        priority["medium"]
    )

    rule6 = ctrl.Rule(
        prep["high"] &
        diff["low"] &
        pending["low"],
        priority["low"]
    )

    rule7 = ctrl.Rule(
        urgency["medium"] & prep["low"],
        priority["high"]
    )

    rule8 = ctrl.Rule(
        urgency["low"] & prep["low"],
        priority["medium"]
    )

    # -----------------------------
    # Control System
    # -----------------------------

    study_control = ctrl.ControlSystem([
        rule1,
        rule2,
        rule3,
        rule4,
        rule5,
        rule6,
        rule7,
        rule8
    ])

    simulation = ctrl.ControlSystemSimulation(
        study_control
    )

    # -----------------------------
    # Provide Input Values
    # -----------------------------

    simulation.input["urgency"] = min(
        max(days_left, 0), 30
    )

    simulation.input["prep"] = min(
        max(preparation, 0), 100
    )

    simulation.input["diff"] = min(
        max(difficulty, 1), 10
    )

    simulation.input["pending"] = min(
        max(pending_chapters, 0), 10
    )

    # -----------------------------
    # Defuzzification
    # -----------------------------

    simulation.compute()

    score = simulation.output["priority"]

    # -----------------------------
    # Priority Category
    # -----------------------------

    if score < 40:
        category = "Low Priority"
    elif score < 70:
        category = "Medium Priority"
    else:
        category = "High Priority"

    return round(score, 2), category