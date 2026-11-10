# Attack 5 ? CVSS 3.1 and MITRE ATLAS Assessment

## Executive Summary

Four attack categories were tested through controlled, deterministic local simulations. The vulnerable branches demonstrated the modeled failure conditions, while secure branches demonstrated defensive checks. The fifth finding separates role escalation from system-prompt extraction for risk assessment.

**Important limitation:** These results are not evidence of successful exploitation of a production LLM, real identity provider, real customer records, or live MCP server. All credentials and tool outputs were synthetic or mocked. CVSS values below are provisional scenario-based estimates and must be reassessed against a real deployment before being treated as organizational vulnerability scores.

## CVSS 3.1 Findings

| ID | Finding | Score | Severity |
|---|---|---:|---|
| F-01 | Indirect Prompt Injection ? Credential Disclosure | 8.2 | High |
| F-02 | Agent Identity Spoofing ? Privileged Action | 8.2 | High |
| F-03 | System Prompt Extraction | 4.3 | Medium |
| F-04 | User-to-Admin Role Escalation | 8.1 | High |
| F-05 | RAG Poisoning and MCP Tool Abuse | 8.9 | High |

## Detailed Findings

### F-01 ? Indirect Prompt Injection ? Credential Disclosure
- **CVSS 3.1 Base Score:** 8.2 (High)
- **Vector:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:L/A:N`
- **MITRE ATLAS mapping:** AML.T0066 ? Retrieval Content Crafting (closest mapping); AML.T0057 ? LLM Data Leakage
- **Simulation result:** Vulnerable branch disclosed a synthetic JWT; secure branch blocked it.

### F-02 ? Agent Identity Spoofing ? Privileged Action
- **CVSS 3.1 Base Score:** 8.2 (High)
- **Vector:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:L`
- **MITRE ATLAS mapping:** AML.T0073 ? Impersonation (closest sender-spoofing analogy); AML.T0053 ? AI Agent Tool Invocation
- **Simulation result:** Vulnerable branch accepted spoofed identity; secure branch rejected the sender mismatch.

### F-03 ? System Prompt Extraction
- **CVSS 3.1 Base Score:** 4.3 (Medium)
- **Vector:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N`
- **MITRE ATLAS mapping:** AML.T0056 ? Extract LLM System Prompt
- **Simulation result:** Vulnerable simulation disclosed its synthetic prompt; secure branch blocked extraction.

### F-04 ? User-to-Admin Role Escalation
- **CVSS 3.1 Base Score:** 8.1 (High)
- **Vector:** `CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N`
- **MITRE ATLAS mapping:** AML.T0054 ? LLM Jailbreak (closest prompt-based mapping); no exact ATLAS identity-role escalation equivalent identified
- **Simulation result:** Vulnerable simulation changed the role to admin; secure branch retained user role.

### F-05 ? RAG Poisoning and MCP Tool Abuse
- **CVSS 3.1 Base Score:** 8.9 (High)
- **Vector:** `CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:C/C:H/I:H/A:L`
- **MITRE ATLAS mapping:** AML.T0070 ? RAG Poisoning; AML.T0053 ? AI Agent Tool Invocation
- **Simulation result:** Vulnerable simulation triggered a mock MCP export; secure branch blocked the poisoned instruction.

## MITRE ATLAS Mapping Notes

- AML.T0066 describes crafted retrieval content intended to influence a system using retrieved information.
- AML.T0070 covers malicious content injected into data indexed by a RAG system.
- AML.T0056 covers attempts to extract an LLM system prompt.
- AML.T0053 covers invocation of tools available to an AI agent.
- AML.T0073 describes impersonation; it is used as a closest analogy for the simulated spoofed sender identity. No real identity protocol was tested.
- AML.T0074 and AML.T0054 are closest analogies for the modeled spoofing and prompt-based role escalation scenarios; they are not exact identity-spoofing equivalents.

## Three Hardening Recommendations

1. Treat all retrieved documents, emails, and RAG chunks as untrusted data. Never allow retrieved content to override system instructions.
2. Enforce authenticated agent-to-agent identity, signed messages, least-privilege roles, and server-side authorization for every privileged action.
3. Place MCP tools behind strict allowlists, argument validation, approval gates for sensitive operations, and detailed audit logging.

## Assessment Conclusion

The simulations illustrate how untrusted instructions, weak identity verification, prompt disclosure, role authorization failures, and unsafe tool execution can create risk in AI-enabled systems. The secure branches demonstrate basic defensive patterns, but production readiness requires integration testing, authenticated identity controls, policy enforcement outside the model, and independent security validation.

## References

- FIRST, CVSS v3.1 Specification: https://www.first.org/cvss/v3-1/specification-document
- MITRE ATLAS: https://atlas.mitre.org/
- MITRE ATLAS AML.T0070 ? RAG Poisoning
- MITRE ATLAS AML.T0056 ? Extract LLM System Prompt
- MITRE ATLAS AML.T0053 ? AI Agent Tool Invocation