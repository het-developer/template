---
name: design-enhancement
description: Audits and improves website design based on professional principles: White space, Typography, Contrast, Imagery, and Usability. Use to refine the visual quality and user experience of a site.
---

# Design Enhancement Skill

This skill applies 5 core principles of professional web design to transform a "beginner" layout into a polished, high-trust user interface.

## Core Directives

### 1. Spacing & "Air" (White Space)
**Principle**: "Professional design breathes."
- **Outer Margins**: Increase space between major sections (e.g., `80px` to `120px` gap).
- **Inner vs. Outer Rule**: The space *inside* a logical block (elements to container) must be significantly smaller than the space *between* blocks.
    - *Example*: Use `gap: 1.5rem` for card content, but `padding: 3rem` for the section.
- **Goal**: Help the user focus by reducing density.

### 2. Typography
**Principle**: "80% of the web is text."
- **Font Limit**: strict maximum of 2 font families.
- **Hierarchy**: H1 must be visually dominant. H2 distinct from body.
    - *Check*: If H1 and H2 look similar, double the size of H1.
- **Readability**:
    - **Line Length**: Limit text containers to 45–75 characters per line (`max-width: 65ch`).
    - **Line Height**: Set `line-height: 1.5` (150%) to `1.6` (160%) for body text.

### 3. Visual Accent & Contrast
**Principle**: "User decides in 2 seconds."
- **Primary CTA**: Only **ONE** main action button per screen/view.
    - Style: High contrast, solid color, shadow.
- **Secondary Actions**: Demote competing buttons ("Learn More", "Back") to outline styles or simple text links.
- **Goal**: Clear visual path.

### 4. Content & Imagery
**Principle**: "Trust above all."
- **No Plastic Stock**: Ban generic stock photos (artificial smiles, suits). Replace with:
    - Authentic, candid photography.
    - Abstract or stylized illustrations.
    - High-quality product shots.
- **Consistency**: All icons must share a style (Stroke vs. Fill, Line weight, Corner radius).

### 5. Usability (UX)
**Principle**: "Functional beauty."
- **3-Click Rule**: Information must be accessible within 3 interactions.
- **Mobile Thumb Zone**: Interactive elements must be easily reachable and sized correctly (min `44px` height).
- **Performance**: Heavy images are design failures. Enforce WebP/AVIF formats and lazy loading.

## Implementation Checklist

1.  **Audit Spacing**: Double the current whitespace between sections.
2.  **Fix Typography**: Add `max-width: 65ch` to all paragraphs. Increase `line-height`.
3.  **Clarify Actions**: Identify the #1 goal of the page and style that button exclusively as Primary. Greyscale the rest.
4.  **Purge Assets**: Remove inconsistent icons and "fake" stock photos.

## Example CSS Strategy

```css
/* Typography Fix */
body {
  line-height: 1.6;
  color: var(--text-primary);
}

p, li {
  max-width: 65ch; /* Optimal reading length */
}

/* Spacing Fix */
section {
  padding-block: 6rem; /* More air */
}

/* CTA Hierarchy */
.btn-primary {
  background: var(--brand-color);
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.btn-secondary {
  background: transparent;
  border: 1px solid var(--border-color);
  box-shadow: none;
}
```
