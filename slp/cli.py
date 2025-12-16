import argparse
from pathlib import Path
import yaml

from .engine import summarize, render_text


def load_scenarios(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

def main():
    parser = argparse.ArgumentParser(
        prog="slp",
        description="System Layers Profiler (Thinking Aid): prompts layer-by-layer thinking for performance issues.",
    )
    parser.add_argument(
        "scenario",
        nargs="?",
        default="api_latency",
        help="Scenario key (e.g., api_latency, high_cpu, memory_leak). Use --list to see all.",
    )
    parser.add_argument("--list", action="store_true", help="List available scenarios and exit.")
    parser.add_argument("--top", type=int, default=5, help="How many top suspects to show (default: 5).")
    parser.add_argument(
        "--scenarios-file",
        default=str(Path(__file__).with_name("scenarios.yaml")),
        help="Path to scenarios.yaml",
    )

    args = parser.parse_args()
    data = load_scenarios(Path(args.scenarios_file))
    scenarios = (data or {}).get("scenarios", {})

    if args.list:
        print("Available scenarios:")
        for k, v in scenarios.items():
            title = (v or {}).get("title", "")
            print(f"- {k}: {title}")
        return

    if args.scenario not in scenarios:
        print(f"Unknown scenario: {args.scenario}")
        print("Use --list to see available scenarios.")
        return

    title, desc, insights = summarize(scenarios[args.scenario])
    print(render_text(title, desc, insights, top_n=args.top))


if __name__ == "__main__":
    main()
