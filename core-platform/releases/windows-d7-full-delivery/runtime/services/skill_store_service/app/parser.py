"""SKILL.md parser for skill store service."""

import re
from typing import Dict, List


def parse_skill_md_text(text: str) -> Dict[str, any]:
    """
    Parse SKILL.md content into structured data.

    Expected format:
    # Skill Name
    Name: skill-name
    Version: 1.0.0
    Description: Skill description
    Agents: agent1, agent2
    Tags: tag1, tag2

    ## Description
    Detailed description...
    """
    lines = text.splitlines()
    
    # Initialize with defaults
    parsed = {
        "name": "",
        "version": "0.1.0",
        "description": "",
        "agents": [],
        "tags": [],
        "format": "SKILL.md",
    }

    # Extract metadata
    for i, line in enumerate(lines):
        t = line.strip()
        low = t.lower()

        # Try YAML-style metadata (Name: value)
        if low.startswith("name:"):
            parsed["name"] = t.split(":", 1)[1].strip()
        elif low.startswith("version:"):
            parsed["version"] = t.split(":", 1)[1].strip()
        elif low.startswith("description:"):
            parsed["description"] = t.split(":", 1)[1].strip()
        elif low.startswith("agents:"):
            parsed["agents"] = [x.strip() for x in t.split(":", 1)[1].split(",") if x.strip()]
        elif low.startswith("tags:"):
            parsed["tags"] = [x.strip() for x in t.split(":", 1)[1].split(",") if x.strip()]

        # Try Markdown header for name
        elif low.startswith("# ") and not parsed["name"]:
            parsed["name"] = t[2:].strip()

        # Try section header for description
        elif (low.startswith("## description") or low.startswith("## ## description")) and not parsed["description"]:
            # Get next non-empty line as description
            for j in range(i + 1, len(lines)):
                next_line = lines[j].strip()
                if next_line and not next_line.startswith("#"):
                    parsed["description"] = next_line
                    break
                elif next_line.startswith("#"):
                    break

    # Fallback: extract name from first line if it's a header
    if not parsed["name"] and lines:
        first_line = lines[0].strip()
        if first_line.startswith("# "):
            parsed["name"] = first_line[2:].strip()

    # Fallback name
    if not parsed["name"]:
        parsed["name"] = "untitled-skill"

    # Normalize version (add default if invalid)
    if not re.match(r'^\d+\.\d+\.\d+', parsed["version"]):
        parsed["version"] = "0.1.0"

    return parsed


def validate_skill_md_text(text: str) -> Dict[str, any]:
    """
    Validate SKILL.md content and return validation results.
    """
    parsed = parse_skill_md_text(text)
    errors = []
    warnings = []

    # Required fields
    if not parsed["name"] or parsed["name"] == "untitled-skill":
        errors.append("Skill name is missing")

    if not parsed["description"]:
        warnings.append("Skill description is missing")

    # Validate version format
    if not re.match(r'^\d+\.\d+\.\d+', parsed["version"]):
        errors.append(f"Invalid version format: {parsed['version']}")

    # Validate agents
    for agent in parsed["agents"]:
        if not agent.strip():
            warnings.append("Empty agent name detected")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
        "parsed": parsed,
    }


def extract_code_blocks(text: str) -> List[Dict[str, str]]:
    """
    Extract code blocks from SKILL.md content.

    Returns list of {language, code} dicts.
    """
    pattern = r'```(\w*)\n([\s\S]*?)```'
    matches = re.findall(pattern, text)
    
    blocks = []
    for lang, code in matches:
        blocks.append({
            "language": lang or "text",
            "code": code.strip(),
        })
    
    return blocks


def extract_tool_definitions(text: str) -> List[Dict[str, any]]:
    """
    Extract tool definitions from SKILL.md content.

    Expected format:
    @tool tool_name
    Description: Tool description
    @end
    """
    pattern = r'@tool\s+(\w+)\s*\nDescription:\s*(.+?)(?:\n|$)'
    matches = re.findall(pattern, text, re.MULTILINE)
    
    tools = []
    for name, description in matches:
        tools.append({
            "name": name,
            "description": description.strip(),
        })
    
    return tools
