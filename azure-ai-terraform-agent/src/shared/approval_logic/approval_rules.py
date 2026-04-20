from typing import Dict, Tuple


def needs_approval(plan_summary: Dict, estimated_cost_delta: float) -> Tuple[bool, str]:
    """
    Decide whether the agent must ask the user for explicit approval.

    Always returns True — every deployment requires approval.
    The reason string explains *why* this particular plan is flagged.
    """
    reasons = []

    if plan_summary["destroys"] > 0:
        reasons.append(f"{plan_summary['destroys']} resource(s) will be destroyed")

    if estimated_cost_delta > 20.0:
        reasons.append(f"estimated monthly cost increase is €{estimated_cost_delta:.2f}")

    if plan_summary["adds"] + plan_summary["updates"] > 20:
        reasons.append("large number of changes (>20)")

    if reasons:
        return True, "; ".join(reasons)

    return True, "All deployments require explicit approval in chat."
