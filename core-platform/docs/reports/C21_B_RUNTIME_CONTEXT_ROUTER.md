# C21-B Runtime Context Router

## Status

Implemented.

## What Changed

The desktop chat no longer sends every prompt directly to the local model.
It now uses a runtime context router:

- Date/time questions -> local system time
- Weather, web, or latest questions -> blocked with a no-hallucination response until tools are enabled
- Project, repo, Agent, RAG, or MCP questions -> Repo Memory search
- Capability questions -> platform capability summary
- Normal chat -> local model inference

## Why

This prevents the local model from hallucinating real-time facts or project-specific facts.

## Test Cases

1. `今天是几月几号`
   Expected: returns local system date/time.
2. `帮我查一下广州天气`
   Expected: says the weather tool is not enabled, and does not invent weather.
3. `我们有哪些 MCP 相关仓库`
   Expected: queries Repo Memory service.
4. `你好，请介绍你自己`
   Expected: local model response.

## Next

C21-C should add real web search, weather, and time tool services.
