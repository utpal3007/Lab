from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType
from pathlib import Path
import subprocess

from src.shared.approval_logic.plan_parser import parse_terraform_plan_output
from src.shared.approval_logic.approval_rules import needs_approval
from src.shared.devops.trigger_pipeline import trigger_azure_devops_pipeline

WORKING_DIR = Path(__file__).resolve().parents[2] / "infra" / "terraform"

def terraform_plan_tool(_: str) -> str:
  proc = subprocess.run(
      ["bash", "-lc", f"cd {WORKING_DIR} && terraform init && terraform plan"],
      capture_output=True,
      text=True
  )
  return proc.stdout + "\n" + proc.stderr

def devops_deploy_tool(branch: str) -> str:
  run_id = trigger_azure_devops_pipeline(
      org="YOUR_ORG",
      project="YOUR_PROJECT",
      pipeline_id=1,
      branch=branch,
      pat_token="YOUR_PAT"
  )
  return f"Triggered Azure DevOps pipeline run: {run_id}"

def main():
  llm = ChatOpenAI(
      model="gpt-4o",
      temperature=0,
  )

  tools = [
      Tool(
          name="terraform_plan",
          func=terraform_plan_tool,
          description="Run terraform plan in infra/terraform and return the raw output."
      ),
      Tool(
          name="devops_deploy",
          func=devops_deploy_tool,
          description="Trigger Azure DevOps pipeline for the given branch name."
      ),
  ]

  agent = initialize_agent(
      tools,
      llm,
      agent=AgentType.OPENAI_FUNCTIONS,
      verbose=True
  )

  system_prompt = (
      "You are an infrastructure deployment assistant. "
      "1) Generate or modify Terraform in infra/terraform (describe changes in natural language). "
      "2) Call terraform_plan to see the plan. "
      "3) Summarize adds/changes/destroys and ask the user for explicit approval. "
      "4) Only if the user clearly approves, call devops_deploy with branch 'main'. "
      "Never deploy without explicit approval."
  )

  while True:
      user_input = input("you> ")
      if not user_input:
          break

      # You can keep conversation state with a memory if needed.
      response = agent.run(f"{system_prompt}\nUser request: {user_input}")
      print(f"agent> {response}")

if __name__ == "__main__":
  main()
