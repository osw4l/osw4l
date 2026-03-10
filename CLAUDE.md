# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

GitHub profile repo (`osw4l/osw4l`) — a README-driven profile page with vaporwave + hacker aesthetic, dark/light mode support, and auto-generated widgets.

Key files:
- `README.md` — Profile README with vaporwave-hacker aesthetic
- `main.py` — Terminal GIF generator using `gifos` (github-readme-terminal)
- `setting.json` — Vaporwave color config for 3D contribution graph
- `fonts/` — Font files for the terminal GIF (bitmap + display fonts)
- `.github/workflows/profile-3d.yml` — 3D contrib SVG generation (daily + on push)
- `.github/workflows/terminal-gif.yml` — Terminal GIF generation (daily + manual)
- `profile-3d-contrib/` — Generated 3D SVGs (auto-committed by workflow)

## Design system

**Theme:** Vaporwave + hacker fusion
**Color palette:** `#ff71ce` (pink), `#b967ff` (purple), `#01cdfe` (cyan), `#1a1b3a` (dark navy), `#6c3483` (deep purple)
**Section headers:** `## ~/section --flag` (terminal-style)
**Badges:** `for-the-badge` style from shields.io
**Dark/light:** ALL images use `<picture>` + `prefers-color-scheme`
**Style:** No emojis (especially no flowers/feminine). Masculine/neutral tone only.

## Terminal GIF (main.py)

Uses `x0rzavi/github-readme-terminal` (gifos library). Sequence: BIOS boot → GIF OS logo → login → fetch.sh with live GitHub stats.
- Color scheme: `dracula` (set via `GIFOS_GENERAL_COLOR_SCHEME` env var)
- Fonts: `gohufont-uni-14.pil` (bitmap), `vtks-blocketo.regular.ttf` (logo)
- GitHub stats fetched live via `gifos.utils.fetch_github_stats("osw4l")`
- Top langs hardcoded: Python, Go, Elixir

## 3D contribution graph

Uses `yoshi389111/github-profile-3d-contrib@latest`.
- `SETTING_JSON` must be a **file path** (e.g., `setting.json`), NOT inline JSON
- Custom colors generate `profile-customize.svg` only
- Workflow needs `permissions: contents: write`

## Stack categories (README badges)

Languages → Frameworks → Databases & Messaging → Cloud & DevOps → AI / Agentic

## Git conventions

- Commits as `osw4l` only — no co-author lines, no bot attribution
- Always commit + push after completing changes (no need to ask)
- Workflow commits: `chore: update 3d contrib` / `chore: update terminal gif`
- Profile update commits: descriptive message without prefix convention
- Contact: LinkedIn=https://linkedin.com/in/osw4l, Email=ioswxd@gmail.com
