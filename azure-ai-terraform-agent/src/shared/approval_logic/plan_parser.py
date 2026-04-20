import re
from typing import Dict


def parse_terraform_plan_output(plan_output: str) -> Dict:
    """
    Parse raw `terraform plan` stdout and return a summary dict.

    Returns:
        {
            "adds":     int,
            "updates":  int,
            "destroys": int,
            "raw":      str   # full output for the agent to read
        }
    """
    adds = updates = destroys = 0

    # Terraform >= 0.13 summary line:
    # "Plan: 2 to add, 1 to change, 0 to destroy."
    summary_match = re.search(
        r"Plan:\s+(\d+) to add,\s+(\d+) to change,\s+(\d+) to destroy",
        plan_output,
    )
    if summary_match:
        adds     = int(summary_match.group(1))
        updates  = int(summary_match.group(2))
        destroys = int(summary_match.group(3))

    return {
        "adds":     adds,
        "updates":  updates,
        "destroys": destroys,
        "raw":      plan_output,
    }
