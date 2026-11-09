# Versioning & Release Strategy

**AIR (Accessibility in India Repo)** follows Semantic Versioning (SemVer) with phase-based governance and pre-release stability indicators.

---

## Version Format

```
MAJOR.MINOR.PATCH[-PRERELEASE]
```

### Current Version

**v1.0.1-alpha** (as of 2026-11-10)

---

## Semantic Versioning Rules

### MAJOR Version Changes (Breaking Changes)

Bump major version when making breaking changes that affect:
- **Repository structure** — Moving, renaming, or removing entire directories/sections
- **Phase gating** — Declaring a phase complete that blocks subsequent phases
- **License scope** — Changes to what is and isn't CC BY 4.0
- **Public API** — Significant changes to how external systems access or cite this material

**Examples of MAJOR bumps:**
- v1.0.0 → v2.0.0: Phase 3 completion (public repository launched; breaking from alpha-only status)
- Phase 2 completion and declaration of Phase 3 readiness
- Change from CC BY 4.0 licensed scope to different licensing terms

### MINOR Version Changes (Feature Additions)

Bump minor version when adding new features, material, or functionality without breaking existing content:
- **New state mandates** — Expanding to a new state's legal framework
- **New case materials** — Adding a new case to `cases/`
- **New guides or solutions** — Adding guides or solution proposals
- **Significant documentation improvements** — New sections or clarifications
- **Phase checkpoint completion** — Documented verification milestones within a phase

**Examples of MINOR bumps:**
- v1.0.1 → v1.1.0: Add Maharashtra RERA procedure guide
- v1.1.0 → v1.2.0: Expand to new state (e.g., Karnataka)
- v1.2.0 → v1.3.0: Phase 2 Marbella verification checkpoint complete (v1.0.1-alpha → v1.0.1)

### PATCH Version Changes (Bugfixes & Documentation)

Bump patch version when making corrections, clarifications, or minor updates:
- **Typo fixes** — Grammar, spelling, formatting
- **Link corrections** — Dead links, path fixes
- **Clarifications** — Improved wording without changing meaning
- **Metadata updates** — Source verification date, status clarifications
- **Minor doc improvements** — README updates, navigation enhancements

**Do NOT bump patch for:**
- New feature additions (use MINOR)
- Structural changes (use MAJOR)
- Updating already-published case material (case materials are immutable; create new dated entry)

### Pre-Release Versions

Pre-release versions follow SemVer convention: `MAJOR.MINOR.PATCH-PRERELEASE`

#### `-alpha`
- **Meaning:** Work in progress; core features incomplete; verification pending
- **Use when:** Phase work is ongoing; material is not yet verified or ready for community review
- **Typical duration:** During active phase work
- **Stability:** Not recommended for external reliance
- **Example:** v1.0.1-alpha (Phase 2 legal verification in progress)

#### `-beta`
- **Meaning:** Core features complete; ready for community review; minor issues may exist
- **Use when:** Phase checkpoint reached; material verified but not yet formally released
- **Typical duration:** Between phase completion and formal release
- **Stability:** Acceptable for external reference with awareness of pre-release status
- **Example:** v1.1.0-beta (Phase 2 checkpoint passed; ready for contributor feedback)

#### `-rc` (Release Candidate)
- **Meaning:** Ready for release; all major work complete; awaiting final approval
- **Use when:** All phase work done; external review/approval pending
- **Typical duration:** Final review period before release
- **Stability:** Recommended for external reference; final release imminent
- **Example:** v1.1.0-rc (Phase 2 complete; awaiting legal/community review before v1.1.0)

---

## Release Workflow

### Step 1: Track Work in CHANGELOG.md

All work goes into CHANGELOG.md under a provisional version heading:
```markdown
## [v1.0.1-alpha] — YYYY-MM-DD

### Overview
[Summary of what this version accomplishes]

### Changes
[Detailed change list]

### Commits
[Associated commit hashes]
```

### Step 2: Update Version When Appropriate

When criteria for a version bump are met:

1. **Increment version number** in CHANGELOG.md heading
2. **Add pre-release suffix** if phase work is still in progress
   - `-alpha`: Phase work ongoing
   - `-beta`: Phase checkpoint complete, ready for review
   - `-rc`: Phase complete, awaiting final approval
3. **Update readme.md** to reference current version
4. **Create git tag** with `git tag -a vX.Y.Z-PRERELEASE -m "Release vX.Y.Z-PRERELEASE"`

### Step 3: Connect Versions to Phases

| Phase | Initial Version | Checkpoint Versions | Release Version |
|-------|---|---|---|
| Phase 1 (Foundation) | v1.0.0-alpha | v1.0.0-beta, v1.0.0-rc | v1.0.0 |
| Phase 2 (Verified pilot) | v1.0.1-alpha | v1.1.0-beta, v1.1.0-rc | v1.1.0 |
| Phase 3 (Public repository) | v1.2.0-alpha | v1.2.0-beta, v1.2.0-rc | v2.0.0 |
| Phase 4 (Assisted contributions) | v2.1.0-alpha | v2.1.0-beta, v2.1.0-rc | v2.1.0 |
| Phase 5 (Multilingual stewardship) | v2.2.0-alpha | v2.2.0-beta, v2.2.0-rc | v2.2.0 |

**Rationale:**
- **Phase 1 → v1.0.0**: Foundation stable; repository ready for limited use
- **Phase 2 → v1.1.0**: Verification added; pilot case demonstrated
- **Phase 3 → v2.0.0**: MAJOR bump because Phase 3 completion is a breaking change from alpha-only repository to public, reviewed release
- **Phase 4/5**: Continue MINOR bumps within v2.x series

---

## Versioning Rules by File

### CHANGELOG.md
- **Always has version numbers** in section headings
- **Format:** `## [vX.Y.Z-PRERELEASE] — YYYY-MM-DD`
- **Update:** Whenever work is completed or version changes
- **Example:**
  ```markdown
  ## [v1.0.1-alpha] — 2026-11-10
  ## [v1.1.0-beta] — 2026-11-15
  ## [v1.1.0-rc] — 2026-11-18
  ```

### readme.md
- **Shows current stable version** in a badge or link (optional)
- **References version in context** when discussing phase status
- **Format:** "See [`CHANGELOG.md`](CHANGELOG.md) for v1.0.1-alpha details"
- **Update:** When moving to a new release (stable or pre-release milestone)

### Git Tags
- **Created for every version** (alpha, beta, rc, stable)
- **Format:** `vX.Y.Z-PRERELEASE` (matching version heading in CHANGELOG)
- **Command:** `git tag -a vX.Y.Z-PRERELEASE -m "Release vX.Y.Z-PRERELEASE with [1-line summary]"`
- **Update:** After updating CHANGELOG and readme; push with `git push origin vX.Y.Z-PRERELEASE`

### ROADMAP.md
- **References phase gates** tied to versions
- **Format:** "Status: Not started; gated on v1.1.0 stable release"
- **Update:** When version changes affect roadmap dependencies

---

## Decision Tree: When to Bump Version

```
Is this a breaking change?
├─ YES → Major bump (e.g., v1.0.0 → v2.0.0)
└─ NO
   ├─ Is this a new feature, case, or state mandate?
   │  ├─ YES → Minor bump (e.g., v1.0.0 → v1.1.0)
   │  └─ NO
   │     ├─ Is this a bugfix or documentation clarification?
   │     │  ├─ YES → Patch bump (e.g., v1.0.0 → v1.0.1)
   │     │  └─ NO → Probably doesn't need version bump (internal work)
   │
   └─ What's the stability status?
      ├─ Phase work ongoing → Use -alpha suffix
      ├─ Phase checkpoint done, awaiting review → Use -beta suffix
      └─ Ready to release → Use -rc or remove suffix for stable release
```

---

## Current Status (v1.0.1-alpha)

**Released:** 2026-11-10  
**Phase:** Phase 2 (Verified pilot) — In progress  
**Status:** -alpha (Phase 2 checkpoint completed; broader Phase 2 work ongoing)

### What's Included
- ✅ Marbella case verification complete
- ✅ 3 key statutes converted and verified
- ✅ Cross-linked complaint to statutory sources
- 🔄 Broader Phase 2 expansion work (UDCPR verification, rights reconciliation)

### What's Next
- **v1.0.1-beta**: When Phase 2 checkpoint review is complete
- **v1.1.0-alpha**: When expanding to new states/mandates
- **v1.1.0-rc**: When Phase 2 is declared complete
- **v1.1.0** (stable): After final Phase 2 approval

---

## FAQ

### Q: Why start with v1.0.0 instead of v0.1.0?
**A:** Phase 1 completion established a stable, usable foundation for case materials and basic guides. The repository is suitable for limited public use, so v1.0.0 reflects maturity despite being in early phases.

### Q: When should I make a pre-release tag?
**A:** Create a tag whenever:
- A phase checkpoint is documented and verified (e.g., v1.0.1-alpha)
- Phase work is ready for community review (e.g., v1.1.0-beta)
- Phase is complete and awaiting final approval (e.g., v1.1.0-rc)

### Q: Can I have multiple alpha versions (v1.0.1-alpha, v1.0.2-alpha)?
**A:** Avoid this. Use patch bumps only for releasing stable versions. If Phase 2 has multiple checkpoints, document them in CHANGELOG but keep the version as v1.0.1-alpha until a formal release decision is made. Only bump the patch number (v1.0.1 → v1.0.2) when releasing a stable version.

### Q: What if I need to hotfix a stable release?
**A:** Patch the stable version:
- v1.0.0 stable with a bugfix → v1.0.1 (stable)
- v1.0.1 stable with a clarification → v1.0.2 (stable)

### Q: How do I track which commit corresponds to which version?
**A:** Git tags do this automatically. See all releases with:
```bash
git tag -l
git show vX.Y.Z  # Shows the tagged commit
```

---

## References

- [Semantic Versioning (semver.org)](https://semver.org/)
- [CHANGELOG.md](CHANGELOG.md) — Detailed version history
- [ROADMAP.md](ROADMAP.md) — Phase gates and dependencies
