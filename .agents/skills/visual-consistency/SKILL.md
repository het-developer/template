---
name: visual-consistency
description: Enforces design uniformity across the website. Ensures standardized typography (headings, fonts), consistent spacing/margins, uniform color usage, and identical component styles across all blocks.
---

# Visual Consistency Skill

This skill acts as a "Design QA" agent. Its purpose is to eliminate visual drift and ensure every element on the website looks like it belongs to the same coherent design system.

## Core Directives

### 1. Typography Standardization
**Rule:** Deviation in font properties for the same semantic element is forbidden.
- **Headings**: 
    - All `H2`s must share the exact same `font-family`, `font-size`, `font-weight`, `line-height`, and `letter-spacing`.
    - All `H3`s must be identical to other `H3`s.
- **Body Text**: Define a single "base" body style. Deviations (e.g., small captions, lead text) must be significantly distinct and used consistently.
- **Action**: Use CSS variables (e.g., `var(--font-h2)`, `var(--text-body)`) instead of hardcoded pixels.

### 2. Spacing & Rhythm
**Rule:** Spacing must follow a strict mathematical scale or global variables.
- **Vertical Rhythm**: The gap between sections must be uniform (e.g., always `120px` or `var(--section-gap)`).
- **Internal Spacing**: Padding inside similar components (e.g., Cards) must be identical.
- **Verification**: If Section A has `padding-top: 80px`, Section B cannot have `padding-top: 75px` or `padding-top: 100px`.

### 3. Component Uniformity
**Rule:** Reusable UI elements must use the same code or classes.
- **Buttons**: All primary buttons must look identical (color, border-radius, hover effect). Use a common `.btn-primary` class.
- **Cards**: Shadows, border-radii, and background colors must control consistently.
- **Icons**: Icons should share the same stroke weight, size, and style (filled vs. outlined).

### 4. Color Discipline
**Rule**: No "magic colors". Use the palette.
- **Action**: Replace hex codes (e.g., `#333`, `#2d2d2d`) with semantic variables (e.g., `var(--color-text-primary)`).
- **Check**: Ensure hover states are consistent (e.g., all links darken by 10% or use the same accent color).

## Implementation Workflow

1.  **Variable Audit**: Check `root` or `index.css` for defined design tokens.
    - *If missing*: Create them first.
2.  **Element Scan**: Iterate through pages/sections:
    - Identify all H2s. Are they identical?
    - Identify all buttons. Are they identical?
3.  **Refactor**: Replace specific/inline styles with global classes or variables.
    - *Bad*: `style="font-size: 24px; margin-bottom: 20px"`
    - *Good*: `class="heading-secondary"`
4.  **Legacy Cleanup**: Remove unused CSS classes that introduce slight variations.

## Example Design System Enforcer (CSS)

```css
:root {
  /* Typography Tokens */
  --font-h1: 700 3.5rem/1.1 'Inter', sans-serif;
  --font-h2: 600 2.5rem/1.2 'Inter', sans-serif;
  --font-body: 400 1rem/1.6 'Roboto', sans-serif;

  /* Spacing Tokens */
  --spacing-section: 8rem;
  --spacing-card-padding: 2rem;

  /* Component Tokens */
  --radius-card: 12px;
  --shadow-card: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

/* Enforced Classes */
h2, .h2 { font: var(--font-h2); }
.section { padding-block: var(--spacing-section); }
.card {
  padding: var(--spacing-card-padding);
  border-radius: var(--radius-card);
  box-shadow: var(--shadow-card);
}
```
