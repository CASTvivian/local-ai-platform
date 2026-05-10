"""Business logic layer for design system service."""

from datetime import datetime
from typing import List, Optional, Dict, Any

from .models import (
    DesignSystem,
    BrandProfile,
    DesignToken,
    ComponentSpec,
    ParsedDesignMd,
    StoreFile,
    RegisterDesignSystemRequest,
    ParseDesignMdRequest,
    RegisterBrandProfileRequest,
    AddDesignTokenRequest,
    RegisterComponentSpecRequest,
    SuggestUiConstraintsRequest,
    ComponentType,
)
from .storage import (
    load_store,
    save_store,
    append_event,
    append_error,
    recent_events,
    make_design_system_id,
    make_brand_profile_id,
    make_token_id,
    make_component_spec_id,
    BASE_DIR,
)
from .parser import parse_design_md_text, extract_color_tokens, extract_spacing_tokens
from .validation import (
    validate_design_system,
    validate_brand_profile,
    validate_design_token,
    validate_component_spec,
)


def now_ts() -> float:
    """Get current timestamp."""
    return datetime.utcnow().timestamp()


def register_design_system(req: RegisterDesignSystemRequest) -> DesignSystem:
    """Register a new design system."""
    # Validate name
    name_errors = validate_design_system_name(req.name)
    if name_errors:
        raise ValueError(f"Invalid design system name: {', '.join(name_errors)}")

    # Generate design system ID
    ds_id = make_design_system_id(req.name)
    ts = now_ts()

    # Create design system record
    record = DesignSystem(
        id=ds_id,
        name=req.name,
        version=req.version,
        description=req.description,
        source=req.source,
        enabled=True,
        created_at=ts,
        updated_at=ts,
    )

    # Validate
    errors = validate_design_system(record)
    if errors:
        raise ValueError(f"Invalid design system: {', '.join(errors)}")

    # Check for duplicates
    store = load_store()
    for existing in store.design_systems:
        if existing.name == record.name:
            raise ValueError(f"Design system {record.name} already exists")

    # Store record
    store.design_systems.append(record)
    save_store(store)
    append_event("register_design_system", {"id": ds_id, "name": req.name, "version": req.version})

    return record


def validate_design_system_name(name: str) -> List[str]:
    """Validate design system name."""
    errors: List[str] = []

    if not name:
        errors.append("name is required")
    elif len(name) < 2:
        errors.append("name must be at least 2 characters")

    return errors


def parse_design_md(req: ParseDesignMdRequest) -> ParsedDesignMd:
    """Parse DESIGN.md content."""
    parsed = parse_design_md_text(req.text)
    return ParsedDesignMd(**parsed)


def list_design_systems() -> List[DesignSystem]:
    """List all design systems."""
    store = load_store()
    return store.design_systems


def get_design_system(ds_id: str) -> Optional[DesignSystem]:
    """Get design system by ID."""
    store = load_store()
    for record in store.design_systems:
        if record.id == ds_id:
            return record
    return None


def register_brand_profile(req: RegisterBrandProfileRequest) -> BrandProfile:
    """Register brand profile."""
    brand_id = make_brand_profile_id()
    ts = now_ts()

    # Create brand profile
    profile = BrandProfile(
        id=brand_id,
        colors=req.colors,
        fonts=req.fonts,
        border_radius=req.border_radius,
        spacing=req.spacing,
        shadows=req.shadows,
        logo=req.logo,
    )

    # Validate
    errors = validate_brand_profile(profile)
    if errors:
        raise ValueError(f"Invalid brand profile: {', '.join(errors)}")

    # Store profile
    store = load_store()
    store.brand_profiles.append(profile)
    save_store(store)
    append_event("register_brand_profile", {"id": brand_id})

    return profile


def add_design_token(req: AddDesignTokenRequest) -> DesignToken:
    """Add design token."""
    token_id = make_token_id()
    ts = now_ts()

    # Create token
    token = DesignToken(
        id=token_id,
        category=req.category,
        name=req.name,
        value=req.value,
        description=req.description,
        tokens=req.tokens,
    )

    # Validate
    errors = validate_design_token(token)
    if errors:
        raise ValueError(f"Invalid design token: {', '.join(errors)}")

    # Store token
    store = load_store()
    store.design_tokens.append(token)
    save_store(store)
    append_event("add_design_token", {"id": token_id, "category": req.category, "name": req.name})

    return token


def register_component_spec(req: RegisterComponentSpecRequest) -> ComponentSpec:
    """Register component specification."""
    component_id = make_component_spec_id()
    ts = now_ts()

    # Create component spec
    spec = ComponentSpec(
        id=component_id,
        component_type=req.component_type,
        name=req.name,
        props=req.props,
        variants=req.variants,
        description="",
    )

    # Validate
    errors = validate_component_spec(spec)
    if errors:
        raise ValueError(f"Invalid component spec: {', '.join(errors)}")

    # Store spec
    store = load_store()
    store.component_specs.append(spec)
    save_store(store)
    append_event("register_component_spec", {"id": component_id, "type": req.component_type})

    return spec


def export_design_system(ds_id: str) -> Optional[Dict[str, Any]]:
    """Export design system as tokens and components."""
    store = load_store()
    
    # Find design system
    design_system = next((ds for ds in store.design_systems if ds.id == ds_id), None)
    if not design_system:
        return None
    
    # Get related data
    brand_profile = next((bp for bp in store.brand_profiles if bp.id.startswith(ds_id[:16])), None)
    tokens = [t for t in store.design_tokens if t.tokens.get("design_system_id") == ds_id]
    components = [c for c in store.component_specs if c.props.get("design_system_id") == ds_id]
    
    return {
        "design_system": design_system.model_dump(),
        "brand_profile": brand_profile.model_dump() if brand_profile else None,
        "tokens": [t.model_dump() for t in tokens],
        "components": [c.model_dump() for c in components],
    }


def suggest_ui_constraints(req: SuggestUiConstraintsRequest) -> Dict[str, Any]:
    """Suggest UI constraints based on component type."""
    suggestions = {
        "spacing": {},
        "colors": {},
        "typography": {},
        "components": [],
    }
    
    # Component-specific suggestions
    if req.component_type == ComponentType.button:
        suggestions.update({
            "spacing": {"padding": "8px 16px", "margin": "4px 8px"},
            "colors": {"background": "primary", "text": "primary.contrast"},
            "typography": {"font_size": "14px", "font_weight": "500"},
            "components": ["button"],
        })
    elif req.component_type == ComponentType.input:
        suggestions.update({
            "spacing": {"padding": "8px 12px", "margin": "4px 0"},
            "colors": {"border": "neutral", "background": "white", "text": "neutral.dark"},
            "typography": {"font_size": "14px"},
            "components": ["input", "label"],
        })
    elif req.component_type == ComponentType.card:
        suggestions.update({
            "spacing": {"padding": "16px", "margin": "16px"},
            "colors": {"background": "white", "border": "neutral"},
            "typography": {"title": "16px", "body": "14px"},
            "components": ["card", "card.header", "card.body"],
        })
    
    return suggestions


def get_recent_events(limit: int = 50) -> List[Dict[str, Any]]:
    """Get recent events."""
    return recent_events(limit)


def get_health_info() -> Dict[str, Any]:
    """Get health information."""
    store = load_store()
    return {
        "service": "design_system_service",
        "version": "0.3.1-enterprise",
        "kind": "design_system",
        "description": "DESIGN.md、UI token、品牌风格、AI 前端生成约束。",
        "store_version": store.store_version,
        "design_systems_count": len(store.design_systems),
        "brand_profiles_count": len(store.brand_profiles),
        "design_tokens_count": len(store.design_tokens),
        "component_specs_count": len(store.component_specs),
    }
