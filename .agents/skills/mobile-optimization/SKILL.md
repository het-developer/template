---
name: mobile-optimization
description: Specialized workflow for optimizing desktop websites for mobile devices. Focuses on fluid typography, enforcing safe margins/padding, ensures touch-friendly interfaces, optimizes media, and guarantees responsive navigation.
---

# Mobile Optimization Skill

This skill provides a strict and detailed framework for adapting desktop-first web designs to mobile screens. It prioritizes readability, touch usability, performance, and aesthetic precision.

## Core Directives

### 1. Foundation: Viewport Metatag
**Rule:** The responsive engine must be initialized correctly.
- **Action**: Ensure the `<head>` contains the viewport meta tag.
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

### 2. Grid & Layout (Fluidity)
**Rule:** No fixed widths in pixels (`width: 1200px` is forbidden).
- **Units**: Use relative units: `%`, `vw`, `vh`, `rem`.
- **Flow**:
    - **Desktop**: `flex-direction: row`
    - **Mobile**: `flex-direction: column` (Stack blocks vertically).
- **Breakpoints**: Standardize media queries at `320px` (small mobile), `480px` (large mobile), `768px` (tablet).

### 3. Typography & Readability
**Rule:** Text must be readable without zooming or squinting.
- **Font Size**: Minimum `16px` for body text. (Prevents iOS zoom-on-focus).
- **Line Height**: Increase to `1.5` (150%) to prevent lines from merging visually.
- **Contrast**: Ensure text passes WCAG contrast checks (especially outdoors in sunlight).

### 4. Touch Targets (Elements Control)
**Rule:** Design for thumbs, not cursors.
- **Size**: Interactive elements must be at least **44x44px**.
- **Spacing**: Add margin between buttons to prevent "fat finger" errors.
- **States**: Remove `:hover` logic for critical mobile interactions; state must be visible by default.

### 5. Media Optimization
**Rule:** Assets must be light and responsive.
- **Images**: Force fluidity with `max-width: 100%; height: auto;`.
- **Formats**: Convert heavy assets to WebP/AVIF (-30% size).
- **Video**: Disable autoplay for heavy videos or replace with static posters on mobile.

### 6. Navigation
**Rule:** Patterns must adapt to limited width.
- **Menu**: Collapse horizontal navbars into a "Hamburger" or bottom sheet menu.
- **Sticky Header**: Pin the header for easy access on long pages, but keep it minimal height.

### 7. Sanity Checklist (The "Reality Check")
- **No Horizontal Scroll**: The site must ONLY scroll vertically.
- **Usable Forms**: Inputs must be large enough to tap easily (`padding: 12px+`).
- **Speed**: Page loads under 3 seconds on 3G network simulation.
- **Pop-ups**: Modals must have massive "Close" buttons and not trap the user.

## Implementation Workflow

1.  **View Source Audit**: Check for `<meta viewport>`.
2.  **Layout Pass**: Apply `flex-direction: column` to main containers at `max-width: 768px`.
3.  **Typography Bump**: Set `body { font-size: 1rem; line-height: 1.5; }`.
4.  **Touch Audit**: specific inspection of buttons < 44px.
5.  **Media Constraint**: Apply global rule `img, video { max-width: 100%; height: auto; }`.

## Example CSS Strategy

```css
@media (max-width: 768px) {
  /* Layout: Stack Everything */
  .container {
    flex-direction: column;
    padding-inline: 1.25rem; /* Safe edges */
  }

  /* Typography: Readable & Tall */
  html { font-size: 16px; }
  p { line-height: 1.5; }

  /* Touch Targets */
  button, a.btn {
    min-height: 44px;
    min-width: 44px;
  }

  /* Navigation */
  .nav-desktop { display: none; }
  .nav-mobile { display: flex; }
}
```
