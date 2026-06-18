# Rules for this repo

## Images

- All images must be placed in the `images/` folder at repo root, never in repo root directly
- If a new image file appears in the repo root (e.g. `Pasted image *.png`), it must be moved to `images/`
- Image references in markdown files must use standard Markdown syntax: `![alt](images/filename.png)`, not Obsidian `![[filename]]` syntax
- If an Obsidian-style `![[filename]]` reference is found in any markdown file, replace it with the correct `![alt](images/filename.png)` syntax
- Image filenames with spaces: use `%20` URL encoding in markdown paths (e.g. `images/Pasted%20image%2020260613181945.png`)
- Every image file in the `images/` folder must be referenced (used) in at least one markdown file; orphaned images should be removed

## Markdown comments

- Obsidian-style comments (`%% comment %%`) are NOT standard Markdown and will render as visible text on GitHub
- Replace them with HTML comments: `<!-- comment -->`
- If an Obsidian `%% ... %%` comment is found in any markdown file, convert it to `<!-- ... -->`

## Mermaid diagrams

- Mermaid code blocks in markdown must use standard fenced code: ` ```mermaid `
- Russian/non-ASCII text in mermaid node labels must be wrapped in double quotes: `A["Текст на русском"]`

## Markdown structure

- Every heading (`#`, `##`, `###`, etc.) must be preceded by a blank line
- A pre-commit hook (`.githooks/pre-commit`) enforces this automatically — activate it with `git config core.hooksPath .githooks`

## Typography

- In Russian text, use em-dash `—` instead of double hyphen `--` between words (e.g. "Spring — это фреймворк")
- Do NOT replace `--` inside:
  - Code blocks ( ` ``` ` )
  - Mermaid diagrams (e.g. `-->` arrows)
  - Inline code `` `--flag` ``
  - URLs and file paths
  - Command-line arguments (`--option`, `--flag`)
- If a mass replacement of `--` → `—` is done across the repo, always verify that mermaid diagrams and code blocks are not affected
