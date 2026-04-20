import requests
from typing import Optional


def trigger_azure_devops_pipeline(
    org: str,
    project: str,
    pipeline_id: int,
    branch: str,
    pat_token: str,
) -> Optional[str]:
    url = (
        f"https://dev.azure.com/{org}/{project}"
        f"/_apis/pipelines/{pipeline_id}/runs?api-version=7.1-preview.1"
    )

    payload = {
        "resources": {
            "repositories": {
                "self": {"refName": f"refs/heads/{branch}"}
            }
        }
    }

    response = requests.post(url, json=payload, auth=("", pat_token))
    response.raise_for_status()
    return response.json().get("id")
