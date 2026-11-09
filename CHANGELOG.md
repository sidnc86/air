# CHANGELOG — AIR (Accessibility in India Repo)

All notable changes to this project are documented here. This changelog is designed for both human collaborators and AI tools (Copilot, Claude, GPT) to understand the project evolution and decision context.

---

## [v1.0.1-alpha] — 2026-11-10

### Overview

**Phase 2 Critical Legal Work**: Converted two national statutes to markdown for verifiable accessibility legal framework. Verified NBC 2016 lift requirements. Enhanced case-summary and complaint documents with direct cross-links to statutory text. Repository now provides full legal traceability for accessibility claims.

---

## Phase 2 Critical Legal Items: Statute Conversions & Verification

**Objective:** Establish legal precision by converting key statutes to markdown and verifying technical claims before Phase 2 expansion.

### Changes

#### 1. Rights of Persons with Disabilities Act, 2016: Sections 40, 44-47
- **Created:** `mandates/national/03-RPWD-Act-2016-Sections-40-44-47.md` (5.75 KB)
  - Full statutory text extracted from India Code official source
  - Sections 40 (accessibility standards), 44 (mandatory compliance), 45 (5-year timeline), 46 (2-year service provider timeline), 47 (capacity building)
  - Establishes national statutory duty for building accessibility
  - Directly cited in Marbella complaint Section 11 relief
  - Includes verification instructions and community amendment-tracking process

#### 2. Real Estate Act, 2016: Sections 11-15
- **Created:** `mandates/mh/02-Real-Estate-Act-2016-Sections-11-15.md` (16.08 KB)
  - Full statutory text extracted from India Code for national statute
  - Sections 11 (Promoter duties), 12 (Allottee rights), 13 (RERA establishment), 14 (RERA powers), 15 (Regulations)
  - **Accessibility-specific analysis section** explaining relief pathways for accessibility non-compliance
  - **Section-to-claim matrix** mapping Marbella complaint sections to statutory relief framework
  - Section 11(4)(a), (b), (d) directly used in complaint relief
  - Includes verification procedures and community tracking

#### 3. NBC 2016 Section 13 Verification
- **Status:** ✅ **VERIFIED** via cross-check against MOHUA Guidelines 2021
  - Lift Braille button requirement confirmed in both NBC 2016 and MOHUA implementation document
  - Complaint's technical claim (lift panels must have Braille) is legally sound
  - Source quality note: Current NBC 2016 markdown from non-BIS source; content verified against government-published MOHUA Guidelines 2021
  - Recommendation: Use in Marbella case; BIS official text verification deferred to Phase 2+

#### 4. Cross-Linking & Case Integration
- **Updated:** `mandates/legal-mandates-sources.md`
  - Added entries for 3 new/updated mandates
  - RPwD Act: Now shows conversion complete + verification status
  - Real Estate Act: Now shows conversion complete + accessibility annotations
  - NBC 2016: Updated with verification status (verified via MOHUA cross-check)
  
- **Updated:** `cases/mh/pune-marbella-vs-siddhant/complaints/rera/RERA-COMPLAINT.md`
  - Added inline cross-references to all 4 mandate markdown files
  - Each claim now links to supporting statutory text
  - Makes complaint fully verifiable without PDF access
  - Enables readers to cross-check legal arguments directly

### Commits

**Commit Hash:** `703f902`  
**Message:** "Phase 2 Critical Legal Work: Convert RPwD Act & Real Estate Act to markdown, verify NBC 2016, update mandate index and complaint cross-links"

### Files Affected

**Created:**
- `mandates/national/03-RPWD-Act-2016-Sections-40-44-47.md` — National statutory duty for accessibility
- `mandates/mh/02-Real-Estate-Act-2016-Sections-11-15.md` — RERA relief framework with accessibility analysis

**Modified:**
- `mandates/legal-mandates-sources.md` — Updated 3 mandate entries with conversion/verification status
- `cases/mh/pune-marbella-vs-siddhant/complaints/rera/RERA-COMPLAINT.md` — Added cross-links to mandate markdown files

### Rationale

**Legal Precision:**
- All major statutes cited in Marbella complaint now available as verifiable markdown
- Readers can cross-check claims without PDF access
- NBC lift requirement verified against government implementation document
- Relief framework (Real Estate Act) now transparent and accessible

**Accessibility & Sustainability:**
- Markdown format enables LLM analysis and future AI case-guidance tools
- Structured sections (especially Real Estate Act annotations) enable automated legal argument building
- Verification status transparent; amendments tracked via GitHub issues

**Community Readiness:**
- Case is now legally traceable and community-reviewable
- Stronger foundation for Phase 2 expansion (other states can reuse same statute conversions)
- Clear pattern established for future mandate sourcing and verification

**AI Tool Context:**
For Copilot/Claude/GPT analyzing this repo: The Phase 2 conversion pattern shows how to:
1. Source statutes from official India Code
2. Extract relevant sections to markdown
3. Add accessibility-specific annotations (see Real Estate Act example)
4. Cross-link from case materials
5. Document verification status in legal-mandates-sources.md
This pattern scales to other states' mandates in Phase 2 expansion.

---

## [v1.0.0-alpha] — 2026-11-09

**Objective:** Verify Phase 1 content integrity and prepare governance framework for publication.

### Changes

#### Case Materials Documentation
- **Created:** `cases/mh/pune-marbella-vs-siddhant/proof/proof-index.md`
  - Documents all 13 images/PDFs with purpose, relevance, and context
  - Explains how each piece of evidence supports accessibility arguments
  - Enables future contributors to understand proof documentation structure
  - No modifications to original case content (immutable integrity)

#### Legal Mandates Strategy
- **Enhanced:** `mandates/legal-mandates-sources.md`
  - Documented URL-to-markdown conversion strategy for government PDFs
  - Created source attribution framework (URL, download date, extraction method, verification status)
  - Established verification-status tracking table
  - Added process for community to flag outdated material via GitHub issues
  - Links each mandate to official government sources for live verification

#### Community Contribution Framework
- **Enhanced:** `CONTRIBUTING.md`
  - Added "Case Materials: Sharing Your Advocacy" section
  - Documented case-material contribution guidelines (what to share, what not to, how, attribution, anonymity options)
  - Explained immutability of `cases/` folder (archive model)
  - Added privacy/consent requirements for contributors
  - Clarified licensing options for case contributors

#### Mission & Transparency
- **Enhanced:** `README.md`
  - Added "Under Review" disclaimer banner
  - Created "Our Mission: Knowledge Through Cases" section
  - Updated Folder Guide with case-sharing emphasis and mandate-sources link
  - Expanded "Sources and Limits" with explicit verification-status reference
  - Updated "Contributing" section to invite case-material sharing

### Commits

**Commit Hash:** `27b3c07`  
**Message:** "Phase 1: Initial publication - AIR (Accessibility in India Repo)"

### Files Affected

**Created:**
- `cases/mh/pune-marbella-vs-siddhant/proof/proof-index.md`

**Modified:**
- `mandates/legal-mandates-sources.md`
- `CONTRIBUTING.md`
- `README.md`

### Rationale

**Governance & Clarity:**
- Clear CC BY 4.0 licensing limits scope to original educational Markdown only
- Case materials remain user-authored and immutable (archive model)
- Verification status documented for all legal citations

**Accessibility & Community:**
- Proof documentation enables future advocates to understand evidence structure
- Case-material guidelines lower barriers to community contributions
- Privacy/consent framework protects contributors while encouraging sharing
- Mission statement emphasizes lived experience as foundation

**AI Tool Context:**
For Copilot/Claude/GPT analyzing this repo: These changes establish the foundational governance that enables future contributions. The proof-index pattern shows how to document evidence. The mandate-sources strategy (URL→markdown) will be extended in Phase 1C.

---

## Phase 1B: GitHub Setup & Initial Commit

**Objective:** Publish Phase 1 to public GitHub repository with full governance framework.

### Changes

#### Repository Creation & Publication
- **Initialized:** Local git repository (`.git/`)
- **Created:** Public GitHub repository at https://github.com/sidnc86/air
  - Visibility: Public
  - Description: "AIR (Accessibility in India Repo): A collaborative platform collecting research, field reports, and lived experiences from persons with disabilities to benchmark and improve building accessibility in India."
  - Topics: accessibility, india, rera, inclusion, disability-rights, building-codes, braille, advocacy

#### Initial Content Commit
- **All Phase 1 deliverables published:**
  - Governance: LICENSE, LICENSE.md, PRIVACY.md, CONTRIBUTING.md, SOURCES.md, ROADMAP.md
  - Case Materials: Complete Marbella case folder (communication, complaints, proof with index, material, case-summary)
  - Legal Mandates: 6 government sources with verification status
  - Guides: Maharashtra RERA filing guide (preliminary, marked "Under Review")
  - Solutions: Touch-panel Braille overlay design (user-created, CC BY 4.0)
  - Templates: case-summary.md for contribution structure
  - Configuration: .gitignore for OS/editor/session files

### Commits

**Commit Hash:** `27b3c07`  
**Message:** "Phase 1: Initial publication - AIR (Accessibility in India Repo)"

### Files Affected

**Created:** 92 files, 17,521 insertions (all Phase 1 content)

### Rationale

**Accessibility Advocacy:**
- Makes real RERA evidence publicly available for community reference
- Demonstrates concrete barriers and filing process
- Establishes repository as knowledge base for accessibility advocacy

**Community Ready:**
- Clear governance and licensing upfront
- Case materials show how to document accessibility barriers
- Contribution guidelines invite similar cases
- Update-tracking framework established for sustainability

**AI Tool Context:**
For future AI agents building case-guidance tools: The complete Marbella case shows the full RERA workflow (complaint → relief-sought → evidence). The governance layer (CONTRIBUTING.md, SOURCES.md, PRIVACY.md) establishes how to handle new contributions responsibly.

---

## Phase 1C: PDF-to-Markdown Conversion & Repository Optimization

**Objective:** Fix GitHub file-size warnings by converting large PDFs to LLM-friendly markdown while retaining live government source URLs for verification and update tracking.

### Problem

**GitHub File-Size Warning:** MOHUA-building-guidelines.pdf (63.13 MB) exceeded GitHub's 50MB warning threshold, limiting repository scaling and creating maintenance friction.

### Changes

#### Large Mandate PDFs Converted to Markdown

Three large government documents converted to searchable, text-extracted markdown:

1. **MOHUA Guidelines 2021** → `mandates/national/01-MOHUA-building-guidelines-2021.md`
   - Original: 63.13 MB PDF (474+ pages)
   - Converted: Full-text markdown with section structure
   - Size: 0.56 MB
   - **Reduction: 99.1%** ✅
   - Extraction: pypdf full-text extraction
   - Content: Universal accessibility principles, building design standards, lift specifications

2. **NBC 2016 Section 13** → `mandates/national/02-NBC-2016-Section-13-ANNEX-B.md`
   - Original: 3.95 MB PDF
   - Converted: Markdown with structured sections
   - Size: 1.03 MB
   - **Reduction: 73.9%** ✅
   - Content: National Building Code lift and accessibility specifications

3. **UDCPR Maharashtra 2016** → `mandates/mh/01-UDCPR-2016-Maharashtra.md`
   - Original: 5.05 MB PDF
   - Converted: Markdown with regulation structure
   - Size: 1.06 MB
   - **Reduction: 78.9%** ✅
   - Content: Maharashtra Urban Development Regulations accessibility requirements

**Total Size Reduction:**
- Before: 72.13 MB (three large PDFs)
- After: 2.65 MB (three markdown files)
- **Overall: 96.3% reduction** ✅

#### Markdown File Structure (All Converted Files Include)
Each converted mandate markdown file includes:
- Original PDF attribution and official source URL
- Government authority and jurisdiction
- Edition/amendment date
- Extraction date and method
- Full-text content organized by section/chapter
- Verification instructions with link to official source
- Instructions for reporting extraction errors or updates
- License/attribution notes
- Anchor links to related materials

#### Update-Tracking Framework
- **Enhanced:** `mandates/legal-mandates-sources.md`
  - Added table linking to markdown files
  - Created "Last Verified" and "Updates Checked" columns
  - Documented size reduction statistics
  - Added "Community Update-Tracking" section with reporting process
  - Provided process for flagging outdated government material

#### Community Contribution Template
- **Created:** `.github/ISSUE_TEMPLATE/mandate-update.md`
  - Template for community to report outdated material
  - Verification checklist
  - Links to related cases/guides
  - Clear submission process

#### Documentation Enhancements
- **Enhanced:** `CONTRIBUTING.md`
  - Added section explaining mandate storage strategy (PDF→markdown)
  - Documented benefits for LLM integration
  - Explained file naming conventions for consistency
  - Added instructions for community update reporting

- **Enhanced:** `README.md`
  - Added note on markdown-based mandate storage
  - Explained LLM accessibility for AI models (Copilot, Claude, GPT)
  - Linked to update-tracking framework
  - Highlighted searchability and full-text availability

### Commits

**Commit Hash:** `088a209`  
**Message:** "Phase 1 Addendum: PDF-to-Markdown Conversion & Repository Optimization"

### Files Affected

**Created:**
- `mandates/national/01-MOHUA-building-guidelines-2021.md`
- `mandates/national/02-NBC-2016-Section-13-ANNEX-B.md`
- `mandates/mh/01-UDCPR-2016-Maharashtra.md`
- `.github/ISSUE_TEMPLATE/mandate-update.md`

**Modified:**
- `mandates/legal-mandates-sources.md`
- `CONTRIBUTING.md`
- `README.md`

### Rationale

**Repository Health & Scalability:**
- Eliminates 50MB+ warning that limits repository growth
- Reduces total repository size by 96.3%
- Enables sustainable scaling for future phases (new jurisdictions, translated guides)

**LLM Integration & Future AI Tools:**
- Converts PDFs to text format that AI models can directly process
- Enables Copilot/Claude/GPT to cite government provisions directly
- Foundation for AI-guided case-filing tools (future Phase 4+)
- Full-text accessible for screen-reader users

**Community Maintenance & Accuracy:**
- Live government source URLs retained in each markdown file
- Update-tracking table shows when material was last verified
- GitHub issue template enables community to flag changes easily
- Clear process for keeping mandates current as government updates them

**Accessibility & Searchability:**
- Full-text markdown enables keyword searches across all mandates
- Screen-reader accessible (no embedded PDFs)
- Markdown is human-readable and AI-parseable
- Content can be quoted, linked, and cited directly

### Benefits for Future Development

**For Phase 2 (Verified Pilot & Jurisdiction Expansion):**
- Markdown mandates can be quickly compared across jurisdictions
- Community can identify inconsistencies or gaps
- Foundation for AI agents to suggest relevant provisions for cases

**For Phase 4 (AI-Guided Case Filing):**
- Mandates are directly processable by LLM-based case-guidance agents
- Full-text search enables context-aware provision matching
- Verified accuracy ensures agent recommendations are trustworthy

**For Phase 5 (Multilingual Stewardship):**
- Markdown is easier to translate than PDFs
- Update-tracking framework scales across languages
- Community can maintain translations alongside originals

### AI Tool Context

For Copilot/Claude/GPT analyzing this repository:

1. **Architecture Decision:** PDF→Markdown conversion establishes pattern for handling government documents
2. **Maintenance Model:** Update-tracking framework shows how community sustains accuracy over time
3. **Scalability:** 96.3% reduction demonstrates commitment to sustainable growth
4. **Future Integration:** LLM-ready format directly enables AI case-guidance tools
5. **Transparency:** Retained URLs show how to verify claims against authoritative sources

This phase demonstrates how to balance "moving fast" (publish Phase 1B) with "sustainability" (optimize in Phase 1C) before major expansion phases.

---

## Future Roadmap

### Phase 2: Verified Pilot & Jurisdiction Expansion
**Planned:** Verify legal provisions, expand to Karnataka/Rajasthan/Uttar Pradesh, collect community feedback

### Phase 3: Public Repository & Accessible Website
**Planned:** Static website, accessibility testing, public-only repo version

### Phase 4: Assisted Contributions & Private Intake
**Planned:** Human-reviewed workflow, private storage, consent/retention/moderation processes

### Phase 5: Multilingual National Stewardship
**Planned:** Additional jurisdictions, reviewed translations, versioning, maintenance

---

## How This Changelog Helps AI Tools

When Copilot, Claude, GPT, or future agents analyze this repository:

1. **Understand Evolution:** Each phase shows architectural decisions and their rationale
2. **Learn Patterns:** Proof-index → update-tracking → LLM optimization shows consistent approach
3. **Make Informed Changes:** Rationale explains "why" so new work builds on solid foundation
4. **Maintain Quality:** Verification status and update-tracking provide maintenance models
5. **Enable Collaboration:** Community contribution framework shows how to welcome contributors safely

---

## Contributing & Community

For all contributors (human and AI):
- Read [`CONTRIBUTING.md`](CONTRIBUTING.md) for guidelines
- Review [`SOURCES.md`](SOURCES.md) for citation conventions
- Check [`PRIVACY.md`](PRIVACY.md) for privacy boundaries
- Reference this CHANGELOG for project evolution and decision context

---

**Repository:** https://github.com/sidnc86/air  
**License:** CC BY 4.0 (original educational content only; see LICENSE.md for scope)  
**Last Updated:** 2026-11-09
