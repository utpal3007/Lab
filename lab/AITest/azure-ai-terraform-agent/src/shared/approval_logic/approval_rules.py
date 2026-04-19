from typing import Tuple, Dict

def needs_approval(plan_summary: Dict, estimated_cost_delta: float) -> Tuple[bool, str]:
  """
  Decide if we must ask the user for approval.
  """
  reasons = []

  if plan_summary["destroys"] > 0:
      reasons.append(f"{plan_summary['destroys']} resources will be destroyed")

  if estimated_cost_delta > 20.0:
      reasons.append(f"Estimated monthly cost increase is €{estimated_cost_delta:.2f}")

  if plan_summary["adds"] + plan_summary["updates"] > 20:
      reasons.append("Large number of changes (>20)")

  if reasons:
      return True, "; ".join(reasons)

  return True, "All deployments require explicit approval in chat."
