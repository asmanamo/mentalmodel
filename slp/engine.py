from dataclasses import dataclass
from typing import Dict, List, Any, Tuple


LAYER_ORDER = ["CPU", "Memory", "Disk", "Network", "OS", "Runtime", "Framework", "Cloud", "AI"]

LIKELIHOOD_SCORE = {
    "Low": 1,
    "Low–Medium": 2,
    "Medium": 3,
    "Medium–High": 4,
    "High": 5,
}

@dataclass
class LayerInsight:
    name: str
    likelihood: str
    signals: List[str]
    checks: List[str]

def score_likelihood(label: str) -> int:
    # Normalize dashes (some editors convert them)
    label = label.replace("-", "–").strip()
    return LIKELIHOOD_SCORE.get(label, 3)

def summarize(scenario: Dict[str, Any]) -> Tuple[str, str, List[LayerInsight]]:
    title = scenario.get("title", "Untitled")
    desc = scenario.get("description", "")
    layers = scenario.get("layers", {})

    insights: List[LayerInsight] = []
    for layer_name in LAYER_ORDER:
        if layer_name in layers:
            obj = layers[layer_name] or {}
            insights.append(
                LayerInsight(
                    name=layer_name,
                    likelihood=obj.get("likelihood", "Medium"),
                    signals=obj.get("signals", []),
                    checks=obj.get("checks", []),
                )
            )

    # If YAML included extra layers, add them at the end
    for extra in layers.keys():
        if extra not in LAYER_ORDER:
            obj = layers[extra] or {}
            insights.append(
                LayerInsight(
                    name=extra,
                    likelihood=obj.get("likelihood", "Medium"),
                    signals=obj.get("signals", []),
                    checks=obj.get("checks", []),
                )
            )

    return title, desc, insights

def render_text(title: str, desc: str, insights: List[LayerInsight], top_n: int = 5) -> str:
    scored = sorted(
        insights,
        key=lambda x: (-score_likelihood(x.likelihood), LAYER_ORDER.index(x.name) if x.name in LAYER_ORDER else 999),
    )

    top = scored[: max(1, top_n)]
    lines: List[str] = []
    lines.append(f"System Layers Profiler (Thinking Aid)")
    lines.append(f"Scenario : {title}")
    if desc:
        lines.append(f"Why      : {desc}")
    lines.append("")
    lines.append("Top suspects (highest likelihood first):")
    for item in top:
        lines.append(f"- {item.name:<9} | Likelihood: {item.likelihood}")
        if item.signals:
            lines.append(f"  Signals : {', '.join(item.signals[:3])}{'...' if len(item.signals) > 3 else ''}")
        if item.checks:
            lines.append(f"  Checks  : {', '.join(item.checks[:3])}{'...' if len(item.checks) > 3 else ''}")
        lines.append("")

    lines.append("Full layer view:")
    for item in insights:
        lines.append(f"- {item.name:<9} | {item.likelihood}")

    lines.append("")
    lines.append("Note: This is not a profiler. It's a mental-model checklist to guide investigation.")
    return "\n".join(lines)
