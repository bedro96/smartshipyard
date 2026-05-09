from __future__ import annotations

import argparse
import json
import os
from typing import Any

from dotenv import load_dotenv
from flask import Flask, jsonify, request

from ontology import build_shipyard_snapshot


load_dotenv()


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/health")
    def health() -> Any:
        return jsonify(
            {
                "status": "ok",
                "project": "smartshipyard",
                "model": os.getenv("MODEL_NAME", "not-configured"),
            }
        )

    @app.post("/responses")
    def responses() -> Any:
        payload = request.get_json(silent=True) or {}
        prompt = _extract_prompt(payload)
        snapshot = build_shipyard_snapshot()
        answer = _build_response(prompt=prompt, snapshot=snapshot)

        return jsonify(
            {
                "id": "smartshipyard-response",
                "status": "completed",
                "output": [
                    {
                        "type": "message",
                        "role": "assistant",
                        "content": [
                            {
                                "type": "output_text",
                                "text": answer,
                            }
                        ],
                    }
                ],
                "metadata": {
                    "prompt": prompt,
                    "snapshot_summary": {
                        "vessels": len(snapshot["vessels"]),
                        "workers": snapshot["analytics"]["total_workers"],
                        "equipment": snapshot["analytics"]["total_equipment"],
                        "sensors": snapshot["analytics"]["total_sensors"],
                    },
                },
            }
        )

    return app


def _extract_prompt(payload: dict[str, Any]) -> str:
    if isinstance(payload.get("input"), str):
        return payload["input"]

    inputs = payload.get("input") or []
    for item in inputs:
        if item.get("type") == "message":
            for content in item.get("content", []):
                if content.get("type") in {"input_text", "text", "output_text"}:
                    text = content.get("text")
                    if isinstance(text, str) and text.strip():
                        return text.strip()
    return "Summarize the current smart shipyard state."


def _build_response(prompt: str, snapshot: dict[str, Any]) -> str:
    analytics = snapshot["analytics"]
    lines = [
        f"Prompt: {prompt}",
        f"Vessels: {analytics['total_vessels']}",
        f"Workers: {analytics['total_workers']}",
        f"Equipment: {analytics['total_equipment']}",
        f"Sensors: {analytics['total_sensors']}",
        f"Processes: {analytics['total_processes']}",
        f"Average vessel completion: {analytics['average_completion_percentage']:.1f}%",
        "Top vessels:",
    ]
    for vessel in snapshot["vessels"]:
        lines.append(
            f"- {vessel['name']} ({vessel['type']}): {vessel['completion_percentage']}% complete, status={vessel['status']}"
        )
    lines.append("High priority processes:")
    for process in snapshot["high_priority_processes"]:
        lines.append(
            f"- {process['name']} [{process['status']}] supervised by {process['supervisor']}"
        )
    lines.append("Inventory overview:")
    for material in snapshot["materials"]:
        lines.append(f"- {material['name']}: quantity={material['quantity']}")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Smart Shipyard HTTP agent")
    parser.add_argument("--server", action="store_true", help="Run as HTTP server")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8088)
    parser.add_argument("--dump-snapshot", action="store_true")
    args = parser.parse_args()

    if args.dump_snapshot:
        print(json.dumps(build_shipyard_snapshot(), indent=2))
        return

    if args.server:
        app = create_app()
        app.run(host=args.host, port=args.port)
        return

    print(_build_response("Summarize the current smart shipyard state.", build_shipyard_snapshot()))


if __name__ == "__main__":
    main()