---
name: notebooklm
description: Enables the Agent to interact with NotebookLM using the `notebooklm-mcp-server`. Provides comprehensive instructions for using all available NotebookLM MCP tools to manage notebooks, sources, chat, research, reports, audio/video generation, and more. Use this skill when the user wants to work with NotebookLM.
---

# NotebookLM Skill

This skill allows the AI to fully utilize the NotebookLM Model Context Protocol (MCP) server.

## Overview

NotebookLM is a personalized AI research assistant and writing tool powered by Google. The MCP server extends your capabilities by allowing you to programmatically manage notebooks, ingest varied sources (URLs, Google Drive, text), and generate rich artifacts like data tables, flashcards, mind maps, audio/video overviews, and detailed reports.

## Prerequisites

Before using the tools, make sure you are authenticated. If you get authentication errors, use the terminal to run `notebooklm-mcp-auth`. Or you can attempt to use the `refresh_auth` tool or `save_auth_tokens` (as a fallback) if the previous CLI tool failed.

## Available Capabilities & Tools

Here is a quick reference guide on how to interact with the existing tools provided by the NotebookLM MCP.

### Authentication
*   **`refresh_auth`**: Reload auth tokens from disk or run headless re-authentication. Returns status indicating if tokens were refreshed successfully.
*   **`save_auth_tokens`**: Fallback method to save explicit cookies if `notebooklm-mcp-auth` via CLI fails. *IMPORTANT: First try to instruct the user to run the normal CLI auth.*

### Managing Notebooks
*   **`notebook_list`**: List all notebooks.
*   **`notebook_create`**: Create a new notebook.
*   **`notebook_get`**: Get notebook details with sources (Requires `notebook_id`).
*   **`notebook_describe`**: Get AI-generated notebook summary with suggested topics.
*   **`notebook_rename`**: Rename an existing notebook.
*   **`notebook_delete`**: Permanently delete a notebook (*IRREVERSIBLE, requires confirm*).

### Managing Sources
*   **`notebook_add_text`**: Add pasted text as a source.
*   **`notebook_add_url`**: Add website or YouTube URL as a source.
*   **`notebook_add_drive`**: Add Google Drive document (doc|slides|sheets|pdf) using URL ID.
*   **`source_list_drive`**: List sources with types and Drive freshness status. Use before syncing to identify stale sources.
*   **`source_sync_drive`**: Sync Drive sources with their latest content (*requires confirm*).
*   **`source_describe`**: Get AI-generated source summary with keyword chips.
*   **`source_get_content`**: Get raw textual content of a source (no AI processing). Excellent for fast document export.
*   **`source_delete`**: Delete source permanently (*IRREVERSIBLE, requires confirm*).

### Querying and Chat
*   **`notebook_query`**: Ask the AI about existing sources currently inside the notebook. *Note: Only queries what's already added. Do NOT use this to find new sources on the web/drive.*
*   **`chat_configure`**: Change notebook chat settings (goal: default|learning_guide|custom, etc).

### Researching (Finding New Content)
*   **`research_start`**: Deep/fast research to *FIND NEW* sources on the web or Google Drive. (e.g., "search web for Z"). Workflow: `research_start` -> poll `research_status` -> `research_import`.
*   **`research_status`**: Poll research progress.
*   **`research_import`**: Import discovered sources from the research task into the notebook.

### Content Generation (Studio / Artifacts)
Almost all tools in this category require `confirm=True` after user approval.

*   **`audio_overview_create`**: Generate audio overview (deep_dive|brief|critique|debate).
*   **`video_overview_create`**: Generate video overview (explainer|brief, various visual styles).
*   **`slide_deck_create`**: Generate slide deck.
*   **`report_create`**: Generate text report (Briefing Doc|Study Guide|Blog Post|Create Your Own).
*   **`infographic_create`**: Generate an infographic.
*   **`flashcards_create`**: Generate flashcards based on difficulty.
*   **`quiz_create`**: Generate a quiz.
*   **`data_table_create`**: Generate a data table described by the user.
*   **`mind_map_create`**: Generate a mind map.
*   **`studio_status`**: Check content generation status of studio items and get URLs (for audio/video/infographics).
*   **`studio_delete`**: Delete studio artifact (*IRREVERSIBLE, requires confirm*).

## Example Workflow: Research, Add, and Query

1.  User asks: "Create a notebook about quantum computing advances in 2025 and give me a briefing doc."
2.  Use `research_start` with query "quantum computing advances 2025" and `mode: deep`. Provide a notebook title.
3.  Check `research_status` periodically.
4.  Use `research_import` to ingest the discovered sources.
5.  Use `report_create` format="Briefing Doc" to generate the report.
6.  Present the results to the user!
