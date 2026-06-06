import os
from API_Gateway_Layer.gateway import NexusAPIGateway
from Event_State_Engine.state_machine import UniversalTransactionStateMachine
from AI_Router_Module.ai_router import NexusAIRouter
from Deterministic_Rule_Engine.rule_engine import DeterministicRuleEngine
from Immutable_Audit_Layer.audit_logger import ImmutableAuditLogger

def run_pipeline(tenant_id, event_type, payload):
    gateway = NexusAPIGateway()
    state = UniversalTransactionStateMachine()
    router = NexusAIRouter()
    rules = DeterministicRuleEngine()
    audit = ImmutableAuditLogger()

    try:
        ingress = gateway.process_incoming_request(tenant_id, "NEXUS_SECURE_AUTH_KEY", payload)
        obj = state.normalize_to_state_object(ingress["validated_tenant_id"], event_type, ingress["forward_payload"])
        obj = router.assign_agent_workflow(obj)
        obj = rules.enforce_guardrails(obj)

        audit_path = os.path.join(os.getcwd(), "Immutable_Audit_Layer", "ledger.json")
        audit.commit_to_ledger(obj, audit_path)

        print("[NEXUS] Pipeline complete")

    except Exception as e:
        print("[NEXUS ERROR]", e)

if __name__ == "__main__":
    run_pipeline("tenant_lumencore_gaming_01", "MESSAGE", {"message": "hello"})
    run_pipeline("tenant_lumencore_gaming_01", "PAYMENT", {"amount": 7500})
