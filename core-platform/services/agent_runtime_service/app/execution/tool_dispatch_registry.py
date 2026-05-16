"""Runtime tool dispatch registry.

Executor resolves handlers from this registry instead of hardcoded if/elif
chains.  Handler implementations can still live in executor / tools / runtime
modules during migration, but dispatch lookup is centralised here.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

ToolHandler = Callable[[dict[str, Any]], dict[str, Any]]


class ToolDispatchRegistry:
    """Centralised tool dispatch — register handlers, resolve by name."""

    def __init__(self) -> None:
        self._handlers: dict[str, ToolHandler] = {}

    # -- mutation ---------------------------------------------------------

    def register(self, name: str, handler: ToolHandler) -> None:
        if not name:
            raise ValueError("tool name is required")
        self._handlers[name] = handler

    # -- query ------------------------------------------------------------

    def has(self, name: str) -> bool:
        return name in self._handlers

    def names(self) -> list[str]:
        return sorted(self._handlers.keys())

    # -- execute ----------------------------------------------------------

    def execute(self, name: str, args: dict[str, Any] | None = None) -> Any:
        """Dispatch *name* through the registry.

        Returns whatever the handler returns (typically a ToolResult or dict).
        Unknown tools get a plain error dict.
        """
        handler = self._handlers.get(name)
        if not handler:
            return {
                "ok": False,
                "tool": name,
                "error": "tool_not_registered",
                "available_tools": self.names(),
            }
        payload = args if isinstance(args, dict) else {}
        try:
            return handler(payload)
        except Exception as exc:
            return {
                "ok": False,
                "tool": name,
                "error": str(exc),
                "error_type": type(exc).__name__,
            }


# -- module-level singleton + convenience API ------------------------------

_REGISTRY = ToolDispatchRegistry()


def register_tool(name: str, handler: ToolHandler) -> None:
    """Register *handler* under *name* in the global dispatch registry."""
    _REGISTRY.register(name, handler)


def execute_registered_tool(name: str, args: dict[str, Any] | None = None) -> Any:
    """Dispatch *name* through the global registry; returns handler result or error dict."""
    return _REGISTRY.execute(name, args=args)


def list_registered_tools() -> list[str]:
    return _REGISTRY.names()


def has_registered_tool(name: str) -> bool:
    return _REGISTRY.has(name)
