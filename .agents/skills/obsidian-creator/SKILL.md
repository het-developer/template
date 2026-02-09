---
name: obsidian-creator
description: Create new Obsidian notes ensuring they are placed in the correct location. Use this skill when the user asks to create a new note, record, or entry in their Obsidian vault.
---

# Obsidian Creator

This skill ensures that all new Obsidian notes are created in the designated `new/` directory.

## Core Instructions

When the user asks to create a new, note, or record:

1.  **Target Directory**: You MUST always create the file inside the `new/` directory.
    - Example: if user asks for "Meeting with Alice", target file is `new/Meeting with Alice.md`.
    - If the `new/` directory does not exist, create it.

2.  **File Naming**:
    - Use the user's requested title for the filename.
    - Ensure it ends with `.md`.
    - sanitize filenames (remove illegal characters).

3.  **Content**:
    - If the user provides content, write it to the file.
    - If not, create an empty note or one with a simple header `# Title`.

## Examples

**User**: "Create a note for Project X"
**Action**: Create `new/Project X.md`

**User**: "New daily note"
**Action**: Create `new/Daily Note 2024-01-28.md` (or relevant date)

## Constraints

- NEVER create notes in the root directory.
- ALWAYS check if `new/` exists (though `write_to_file` tool manages directories, be aware of the path).
