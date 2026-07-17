class PaziWorkflowAlignerClient:
    def create_workflow(self, action_trigger: str) -> dict:
        steps = [f"Detect trigger: {action_trigger}"]
        if "invoice" in action_trigger.lower():
            steps.extend(["Parse PDF", "Apply tax Nexus", "Trigger Stripe charge"])
        else:
            steps.append("General task log execution")
        return {"workflow_path": steps}