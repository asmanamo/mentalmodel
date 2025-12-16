# Mental Model — System Layers Profiler (SLP)

A small CLI tool designed as a **thinking aid**, not a system profiler.

This project helps engineers reason about performance and reliability issues
by encouraging **layer-by-layer thinking** across modern systems.

> Most performance problems are thinking problems — not code problems.

---

## Why this exists

Modern systems are fast, distributed, abstracted, and increasingly assisted by AI.
When something feels slow or unstable, engineers often jump between tools,
dashboards, logs, and metrics — randomly and reactively.

This tool exists **before metrics**, not instead of them.

It helps answer a simpler question first:

> *Which system layers should I be thinking about — and why?*

---

## What this tool is (and is not)

### ✅ What it **is**
- A **mental-model checklist** for debugging and architecture discussions
- A way to externalize experienced engineers’ intuition
- A calm, structured guide to reduce random guessing
- Useful for learning, onboarding, incident reviews, and design thinking

### ❌ What it **is not**
- Not a profiler
- Not a monitoring tool
- Not a metrics collector
- Not an automatic “health checker”

This tool does **not** test your system.  
It helps you test your **thinking**.

---

## The layers it encourages you to think about

Every scenario is viewed through common system layers:

- CPU
- Memory
- Disk
- Network
- Operating System
- Runtime (Python / JVM / Node / etc.)
- Framework
- Cloud / Infrastructure
- AI (when applicable)

Abstractions don’t remove complexity — they relocate it.
This tool helps make those layers visible again.

---

## Installation

```bash
pip install -r requirements.txt
