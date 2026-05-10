"""DESIGN.md parser for design system service."""

import re
from typing import Dict, List, Any


def parse_design_md_text(text: str) -> Dict[str, any]:
    """
    Parse DESIGN.md content into structured data.

    Expected format:
    # Design System Name
    Name: my-design
    Version: 1.0.0
    Description: Design system description

    ## Colors
    Primary: #3B82F6
    Secondary: #10B981

    ## Fonts
    Regular: Inter
    Bold: Inter Bold

    ## Spacing
    xs: 4px
    sm: 8px
    md: 16px

    ## Border Radius
    sm: 4px
    md: 8px

    ## Components
    Button, Card, Modal
    """
    lines = text.splitlines()
    
    # Initialize with defaults
    parsed = {
        "name": "",
        "version": "1.0.0",
        "description": "",
        "colors": {},
        "fonts": {},
        "spacing": {},
        "border_radius": {},
        "components": [],
        "ui_constraints": {},
        "format": "DESIGN.md",
    }
    
    current_section = None
    in_section = False
    
    for i, line in enumerate(lines):
        t = line.strip()
        low = t.lower()
        
        # Try YAML-style metadata (Name: value)
        if low.startswith("name:"):
            parsed["name"] = t.split(":",1)[1].strip()
        elif low.startswith("version:"):
            parsed["version"] = t.split(":",1)[1].strip()
        elif low.startswith("description:"):
            parsed["description"] = t.split(":",1)[1].strip()
        
        # Try Markdown header for name
        elif low.startswith("# ") and not parsed["name"]:
            parsed["name"] = t[2:].strip()
        
        # Section headers
        elif low.startswith("## colors"):
            current_section = "colors"
            in_section = True
        elif low.startswith("## fonts"):
            current_section = "fonts"
            in_section = True
        elif low.startswith("## spacing"):
            current_section = "spacing"
            in_section = True
        elif low.startswith("## border_radius"):
            current_section = "border_radius"
            in_section = True
        elif low.startswith("## components"):
            current_section = "components"
            in_section = True
        elif low.startswith("## ui_constraints"):
            current_section = "ui_constraints"
            in_section = True
        elif low.startswith("##") and not any(x in low for x in ["colors", "fonts", "spacing", "border_radius", "components", "ui_constraints"]):
            # Different section
            current_section = None
            in_section = False
        
        # Parse section content
        elif in_section and ":" in t:
            # Key: Value format
            parts = t.split(":", 1)
            key = parts[0].strip().lower()
            value = parts[1].strip() if len(parts) > 1 else ""
            
            if current_section == "colors":
                parsed["colors"][key] = value
            elif current_section == "fonts":
                parsed["fonts"][key] = value
            elif current_section == "spacing":
                parsed["spacing"][key] = value
            elif current_section == "border_radius":
                parsed["border_radius"][key] = value
            elif current_section == "ui_constraints":
                parsed["ui_constraints"][key] = value
        
        # Component list parsing
        elif current_section == "components" and t and not t.startswith("##"):
            components = [c.strip() for c in t.split(",")]
            parsed["components"].extend([c for c in components if c])
    
    # Fallback: extract name from first line if it's a header
    if not parsed["name"] and lines:
        first_line = lines[0].strip()
        if first_line.startswith("# "):
            parsed["name"] = first_line[2:].strip()
    
    # Fallback name
    if not parsed["name"]:
        parsed["name"] = "untitled-design"
    
    return parsed


def validate_design_md_text(text: str) -> Dict[str, any]:
    """
    Validate DESIGN.md content and return validation results.
    """
    parsed = parse_design_md_text(text)
    errors = []
    warnings = []
    
    # Required fields
    if not parsed["name"] or parsed["name"] == "untitled-design":
        errors.append("Design system name is missing")
    
    if not parsed["version"]:
        errors.append("Version is missing")
    
    # Validate sections
    if not parsed["colors"]:
        warnings.append("Colors section is missing")
    
    if not parsed["fonts"]:
        warnings.append("Fonts section is missing")
    
    if not parsed["spacing"]:
        warnings.append("Spacing section is missing")
    
    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
        "parsed": parsed,
    }


def extract_color_tokens(colors: Dict[str, str]) -> List[Dict[str, any]]:
    """Extract color tokens from colors dict."""
    tokens = []
    for name, value in colors.items():
        tokens.append({
            "token": f"color-{name}",
            "value": value,
            "category": "colors",
            "description": f"{name.capitalize()} color",
        })
    return tokens


def extract_spacing_tokens(spacing: Dict[str, str]) -> List[Dict[str, any]]:
    """Extract spacing tokens from spacing dict."""
    tokens = []
    for name, value in spacing.items():
        tokens.append({
            "token": f"spacing-{name}",
            "value": value,
            "category": "spacing",
            "description": f"{name.capitalize()} spacing",
        })
    return tokens
