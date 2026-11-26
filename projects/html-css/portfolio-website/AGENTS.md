# Portfolio Website — Agent Guidelines & Project Context

## Project Overview
This repository contains the source code for **Luis Lazu's personal developer portfolio website**. The site serves as a professional showcase of engineering experience, technical capabilities, projects, and case studies.

---

## Tech Stack & Architecture
- **Core:** Vanilla HTML5 & Vanilla CSS3 (Zero build step, zero runtime dependencies).
- **Styling Architecture:**
  - Do **not** install or introduce CSS frameworks (e.g., Tailwind, Bootstrap) unless explicitly requested.
  - Leverage modern native CSS capabilities: CSS variables, Flexbox, Grid, CSS transitions, and GPU-friendly transforms.
  - Prioritize vector and mathematical CSS effects (gradients, translucent overlays) over heavy raster media for instant load times and zero payload bloat.
- **Typography:** Google Fonts (`DM Sans`).
- **Icons & Media:** Local assets stored in `assests/` and `favicon.ico`.

---

## Design System & Aesthetic Principles
1. **Dark Mode Palette:**
   - Base Background: Deep midnight navy (`#0a0f1e`).
   - Radial Ambient Glow: Purple glow (`rgba(108, 99, 255, 0.25)`).
   - Brand Accents: Purple/indigo (`#6c63ff`) to cyan (`#00d4ff`) linear gradients.
   - Text Hierarchy: Crisp white (`#ffffff`) for headings, high-contrast readable tints for body text.
2. **Glassmorphism & Depth:**
   - Sticky navigation and overlay elements utilize subtle borders (`rgba(255, 255, 255, 0.1)`), translucent dark fills, and `backdrop-filter: blur(10px)`.
3. **Micro-Interactions & Polish:**
   - Interactive elements (cards, navigation links, buttons) should include smooth easing transitions (`transition: ... 0.3s ease`) and subtle micro-movements (e.g., `transform: translateY(-4px)` on card hover).
4. **Accessibility (WCAG):**
   - Maintain accessible contrast ratios against dark backgrounds.
   - Use semantic HTML tags (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`, `<article>`).

---

## Directory Structure
```text
porfolio-website/
├── assests/        # Static images, icons, and media
├── sprints-tutorials/ # Sprint tracking, architectural tutorials, and concept guides
├── .gitignore      # Ignored files and local notes
├── AGENTS.md       # Project-specific guidelines and conventions (this file)
├── favicon.ico     # Browser tab favicon
├── index.html      # Primary document structure & markup
└── styles.css      # Design tokens, layout rules, and component styles
```

---

## Development & Collaboration Rules
- **Luis in the Driver's Seat:** Explain structural, layout, and CSS concepts clearly before modifying files. Guide and propose solutions rather than silently overwriting code.
- **Maintain Documentation Integrity:** When introducing new design patterns or complex visual math (such as gradient stacking or flex calculations), preserve or document them in `sprints-tutorials/` for recurring reference.
- **Semantic Consistency:** Ensure new sections follow established class naming conventions (`.hero`, `.navbar`, `.cards`, `.card`, `.pill`, etc.).
