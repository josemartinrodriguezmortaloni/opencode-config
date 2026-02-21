# OpenCode Agent Configuration

This repository contains an advanced, custom configuration for **OpenCode**, featuring specialized agent personalities, a robust architectural philosophy, and a comprehensive collection of development skills.

## 🧠 Core Agent Personalities

The system is configured with three distinct, highly-specialized agent modes defined in `opencode.json` and `prompts/`:

1. **Gentleman (Primary Mode)**
   A Senior Architect mentor with 15+ years of experience (GDE & Microsoft MVP). He acts as a collaborative partner who helps first but doesn't hesitate to challenge bad practices. Driven by the "Jarvis" philosophy: humans direct, AI executes. Communicates warmly but directly (supports Rioplatense Spanish and English).

2. **SDD Orchestrator**
   A delegate-only orchestrator built for Spec-Driven Development (SDD). It coordinates the complex Directed Acyclic Graph (DAG) of software creation (Proposal → Specs/Design → Tasks → Apply → Verify → Archive) and always delegates execution to sub-agents.

3. **Socrates**
   An educational tutor based on the Socratic method and First Principles thinking. Instead of giving direct answers, Socrates guides you to discover the solutions yourself, fostering genuine learning and structural understanding.

## 🏛️ ARL Architecture Philosophy

The agents are deeply rooted in the **ARL (Architecture, Responsibility, Locality)** philosophy:
*   **Axiom Zero:** Software exists to solve human problems and must be able to evolve.
*   **Executable Models:** Code structure must reflect the business problem, not the technical solution.
*   **The Law of Locality:** Every decision and behavior lives in exactly one place and can change without propagating shockwaves.
*   **The Three Pillars:**
    1. Localized Single Responsibility
    2. Cohesion by Reason of Change
    3. Intentional Coupling

## 🛠️ Specialized Skills

The repository includes a vast collection of Just-In-Time (JIT) loaded skills under the `skill/` directory. These skills provide exact context and best practices when working with specific technologies or tasks:

*   **Frontend & UI:** React 19, Next.js 15, Tailwind 4, Zustand 5, Web Design Guidelines.
*   **Backend & API:** Python Code Generation, Django DRF, Zod 4.
*   **Architecture & Process:** Designing Systems, Spec-Driven Development (SDD) phases, Git Release management.
*   **Security & Testing:** Securing Code, Playwright, Pytest.
*   **AI Integration:** Vercel AI SDK 5, Agent Generation.
*   **Terminal UI:** OpenTUI (React, Solid, Core).

## ⚙️ Integrations (MCP)

Configured to seamlessly integrate with external context providers via MCP (Model Context Protocol):
*   **Engram:** For persistent, cross-session memory and architectural decision tracking.
*   **Context7:** For retrieving up-to-date documentation.
*   **Exa:** For live web search and context gathering.

## 🚀 Getting Started

This configuration is intended to be used with OpenCode. Simply clone or link this directory to your OpenCode configuration path to enable the plugins, themes, and agent profiles.
