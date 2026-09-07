#!/usr/bin/env python3
"""Deterministic repository policy checks for ADEGA DOS 7.

Uses only the Python standard library so it can run locally and in GitHub Actions
without dependency installation.
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = [
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    ".agents/README.md",
    ".agents/config.json",
    ".agents/specs/execution-model.md",
    ".agents/specs/completion-contract.md",
    ".agents/rules/brand-integrity.md",
    ".agents/rules/agent-asset-supply-chain.md",
    ".agents/rules/completion-and-evidence.md",
    ".agents/rules/context-efficiency.md",
    ".agents/rules/memory-and-context.md",
    ".agents/rules/change-promotion.md",
    ".agents/skills/repository-discovery/SKILL.md",
    ".agents/skills/planning/SKILL.md",
    ".agents/skills/task-completion/SKILL.md",
    ".agents/skills/image-production/SKILL.md",
    ".agents/skills/design-review/SKILL.md",
    ".agents/skills/asset-management/SKILL.md",
    ".agents/skills/agent-asset-vetting/SKILL.md",
    ".agents/skills/documentation/SKILL.md",
    ".agents/memory/README.md",
    ".agents/memory/INDEX.md",
    ".agents/runs/README.md",
    ".agents/schemas/agent-config.schema.json",
    ".agents/schemas/completion-run.schema.json",
    ".agents/schemas/agent-asset-assessment.schema.json",
    ".github/copilot-instructions.md",
    ".github/instructions/assets.instructions.md",
    ".github/instructions/documentation.instructions.md",
    ".github/agents/art-director.agent.md",
    ".github/agents/brand-guardian.agent.md",
    ".github/agents/design-qa.agent.md",
    ".github/agents/visual-researcher.agent.md",
    ".github/prompts/research-theme.prompt.md",
    ".github/prompts/design-blueprint.prompt.md",
    ".github/prompts/create-themed-image.prompt.md",
    ".github/prompts/review-image.prompt.md",
    ".github/prompts/record-provenance.prompt.md",
    ".github/prompts/vet-agent-asset.prompt.md",
    "docs/agent-compatibility.md",
    "docs/agent-assets.md",
    "docs/design-system.md",
    "docs/image-construction-workflow.md",
    "docs/image-generation-prompt.md",
    "docs/asset-management.md",
    "docs/references.md",
    "scripts/validate_assets.py",
]

TEXT_EXTENSIONS = {".md", ".json", ".yml", ".yaml", ".py", ".txt"}
FORBIDDEN_ASSET_TOKENS = ("-final", "_final", "-definitivo", "-corrigido", "-v2", "-v3")
# Regex intentionally uses whitespace tokens so the validator does not match its own source literal.
BRAND_PATTERN = re.compile(r"adega\s+dos\s+7", re.IGNORECASE)
RUN_STATUSES = {"PENDING", "IN_PROGRESS", "BLOCKED", "READY_FOR_HUMAN_REVIEW", "DONE"}
REQUIREMENT_STATUSES = RUN_STATUSES | {"NOT_APPLICABLE"}


def error(errors: list[str], message: str) -> None:
    errors.append(message)


def iter_text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT)
        if rel.parts and rel.parts[0] in {".git", "assets"}:
            continue
        if path.suffix.lower() in TEXT_EXTENSIONS or path.name in {"AGENTS.md", "CLAUDE.md", "GEMINI.md"}:
            files.append(path)
    return files


def parse_frontmatter(path: Path, errors: list[str]) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        error(errors, f"{path.relative_to(ROOT)}: missing YAML frontmatter")
        return {}
    try:
        _, raw, _ = text.split("---", 2)
    except ValueError:
        error(errors, f"{path.relative_to(ROOT)}: malformed YAML frontmatter")
        return {}

    data: dict[str, str] = {}
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def check_required_paths(errors: list[str]) -> None:
    for rel in REQUIRED_PATHS:
        if not (ROOT / rel).exists():
            error(errors, f"missing required path: {rel}")


def check_json(errors: list[str]) -> None:
    for path in ROOT.rglob("*.json"):
        if ".git" in path.parts:
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001 - validation wants full error context
            error(errors, f"{path.relative_to(ROOT)}: invalid JSON: {exc}")

    config_path = ROOT / ".agents/config.json"
    if config_path.exists():
        config = json.loads(config_path.read_text(encoding="utf-8"))
        if config.get("canonicalInstructions") != "../AGENTS.md":
            error(errors, ".agents/config.json: canonicalInstructions must be ../AGENTS.md")
        execution = config.get("execution", {})
        if execution.get("workingBranchRequired") is not True:
            error(errors, ".agents/config.json: workingBranchRequired must be true")
        if execution.get("pullRequestRequired") is not True:
            error(errors, ".agents/config.json: pullRequestRequired must be true")
        context = config.get("context", {})
        if context.get("skillsRoot") != "skills":
            error(errors, ".agents/config.json: context.skillsRoot must be skills")


def check_run_files(errors: list[str]) -> None:
    runs_dir = ROOT / ".agents/runs"
    if not runs_dir.exists():
        return

    required = {"taskId", "objective", "status", "requirements", "lastCheckpoint"}
    for path in sorted(runs_dir.glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue  # check_json reports the parse error with the file context

        rel = path.relative_to(ROOT)
        if not isinstance(data, dict):
            error(errors, f"{rel}: run must be a JSON object")
            continue

        missing = sorted(required - data.keys())
        if missing:
            error(errors, f"{rel}: missing required run fields: {', '.join(missing)}")

        status = data.get("status")
        if status not in RUN_STATUSES:
            error(errors, f"{rel}: invalid run status {status!r}")

        requirements = data.get("requirements")
        if not isinstance(requirements, list):
            error(errors, f"{rel}: requirements must be a list")
        else:
            for index, requirement in enumerate(requirements):
                if not isinstance(requirement, dict):
                    error(errors, f"{rel}: requirement {index} must be an object")
                    continue
                if not requirement.get("id"):
                    error(errors, f"{rel}: requirement {index} needs an id")
                requirement_status = requirement.get("status")
                if requirement_status not in REQUIREMENT_STATUSES:
                    error(errors, f"{rel}: invalid status for requirement {requirement.get('id')!r}: {requirement_status!r}")

        checkpoint = data.get("lastCheckpoint")
        if isinstance(checkpoint, str):
            try:
                datetime.fromisoformat(checkpoint.replace("Z", "+00:00"))
            except ValueError:
                error(errors, f"{rel}: lastCheckpoint must be an ISO-8601 date-time")


def check_brand_casing(errors: list[str]) -> None:
    for path in iter_text_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for match in BRAND_PATTERN.finditer(text):
            if match.group(0) != "ADEGA DOS 7":
                line = text.count("\n", 0, match.start()) + 1
                error(
                    errors,
                    f"{path.relative_to(ROOT)}:{line}: brand must be written as 'ADEGA DOS 7', found {match.group(0)!r}",
                )


def check_skills(errors: list[str]) -> None:
    skills_root = ROOT / ".agents/skills"
    if not skills_root.exists():
        return
    for skill_file in sorted(skills_root.glob("*/SKILL.md")):
        metadata = parse_frontmatter(skill_file, errors)
        expected = skill_file.parent.name
        if metadata.get("name") != expected:
            error(errors, f"{skill_file.relative_to(ROOT)}: name must equal directory name {expected!r}")
        if not metadata.get("description"):
            error(errors, f"{skill_file.relative_to(ROOT)}: description is required")

    duplicate_root = ROOT / ".github/skills"
    if duplicate_root.exists() and any(duplicate_root.rglob("SKILL.md")):
        error(errors, ".github/skills contains SKILL.md; use canonical .agents/skills to avoid duplicate sources")


def check_github_customizations(errors: list[str]) -> None:
    for path in sorted((ROOT / ".github/agents").glob("*.md")):
        metadata = parse_frontmatter(path, errors)
        if not metadata.get("description"):
            error(errors, f"{path.relative_to(ROOT)}: custom agent description is required")

    for path in sorted((ROOT / ".github/prompts").glob("*.prompt.md")):
        metadata = parse_frontmatter(path, errors)
        if not metadata.get("description"):
            error(errors, f"{path.relative_to(ROOT)}: prompt description is required")

    for path in sorted((ROOT / ".github/instructions").glob("*.instructions.md")):
        metadata = parse_frontmatter(path, errors)
        if not metadata.get("applyTo"):
            error(errors, f"{path.relative_to(ROOT)}: path instruction applyTo is required")


def check_asset_names(errors: list[str]) -> None:
    assets = ROOT / "assets"
    if not assets.exists():
        return
    for path in assets.rglob("*"):
        if not path.is_file():
            continue
        lower = path.name.lower()
        if any(token in lower for token in FORBIDDEN_ASSET_TOKENS):
            error(errors, f"{path.relative_to(ROOT)}: asset filename contains forbidden revision suffix")


def main() -> int:
    errors: list[str] = []
    check_required_paths(errors)
    check_json(errors)
    check_run_files(errors)
    check_brand_casing(errors)
    check_skills(errors)
    check_github_customizations(errors)
    check_asset_names(errors)

    if errors:
        print("Repository validation FAILED:")
        for item in errors:
            print(f"- {item}")
        return 1

    print("Repository validation OK")
    print(f"- required paths: {len(REQUIRED_PATHS)}")
    print(f"- canonical skills: {len(list((ROOT / '.agents/skills').glob('*/SKILL.md')))}")
    print("- brand casing: ADEGA DOS 7")
    return 0


if __name__ == "__main__":
    sys.exit(main())
