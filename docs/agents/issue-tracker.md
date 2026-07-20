# Issue tracker: GitHub

Issues and PRDs for this repo live as GitHub issues. Use the `gh` CLI for all operations.

## Conventions

- Create, read, comment on, label, assign, and close issues with `gh issue`.
- Infer the repository from the current Git remote.
- Pull requests are not treated as a triage request surface.

## Wayfinding operations

- A map is an issue labelled `wayfinder:map`.
- Decision tickets are GitHub sub-issues labelled by type:
  `wayfinder:research`, `wayfinder:prototype`, `wayfinder:grilling`, or `wayfinder:task`.
- Use GitHub's native issue dependencies for blocking relationships.
- The frontier consists of open, unblocked, unassigned child issues.
- Claim a ticket by assigning it to the driving developer before beginning work.
- Resolve a ticket by recording its answer in a comment, closing it, and appending a linked gist to the map's Decisions-so-far section.
- If sub-issues or dependencies are unavailable, fall back to linked task lists and explicit `Blocked by:` lines.
