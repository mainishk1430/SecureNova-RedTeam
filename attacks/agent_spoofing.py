import json
from datetime import datetime, timezone
from pathlib import Path

# Controlled local simulation: no real agents or external systems.

TRUSTED_AGENT = "agent-orchestrator-01"
WORKER_AGENT = "agent-worker-02"
ATTACKER_AGENT = "agent-attacker-99"

spoofed_message = {
    "claimed_sender": TRUSTED_AGENT,
    "actual_sender": ATTACKER_AGENT,
    "action": "DELETE_TEST_RECORD",
    "privileged": True
}

def vulnerable_agent(message):
    # Insecure: trusts the claimed sender identity.
    if message["claimed_sender"] == TRUSTED_AGENT:
        return {
            "status": "ATTACK_SUCCEEDED",
            "action_executed": message["action"],
            "reason": "Claimed identity trusted without verification."
        }

    return {"status": "REJECTED"}

def secure_agent(message):
    # Secure simulation: compares actual authenticated identity.
    if message["actual_sender"] != TRUSTED_AGENT:
        return {
            "status": "ATTACK_BLOCKED",
            "action_executed": None,
            "reason": "Authenticated sender identity mismatch."
        }

    return {
        "status": "AUTHORIZED",
        "action_executed": message["action"]
    }

results = {
    "test": "Agent Identity Spoofing",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "agents": {
        "orchestrator": TRUSTED_AGENT,
        "worker": WORKER_AGENT,
        "attacker": ATTACKER_AGENT
    },
    "spoofed_message": spoofed_message,
    "vulnerable_agent": vulnerable_agent(spoofed_message),
    "secure_agent": secure_agent(spoofed_message),
    "simulation_limitation": (
        "Deterministic local simulation, not a real authenticated "
        "multi-agent protocol."
    )
}

print(json.dumps(results, indent=4))

Path("evidence/attack2_results.json").write_text(
    json.dumps(results, indent=4),
    encoding="utf-8"
)

print("\nEvidence saved: evidence/attack2_results.json")
