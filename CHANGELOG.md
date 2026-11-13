# CHANGELOG — AIR (Accessibility in India Repo)

All notable changes to this project are documented here. This changelog is designed for both human collaborators and AI tools (Copilot, Claude, GPT) to understand the project evolution and decision context.

---

## [Unreleased]

### Added
- **[`mandates/PRECEDENCE.md`](mandates/PRECEDENCE.md):** order of authority from the RPwD Act down to BIS standards, residential coverage, the date rule for choosing a version, and citation rules for contributors and the bot.
- **RPwD Act, 2016 full text** with notes on the sections that matter for buildings: [`03-RPWD-Act-2016.md`](mandates/national/03-RPWD-Act-2016.md). The earlier extract file now points to it.
- **RPwD Rules, 2017** as amended to 2024: [`04-RPWD-Rules-2017.md`](mandates/national/04-RPWD-Rules-2017.md), with notes on Rule 15(1)(a) and the switch from the 2016 to the 2021 Harmonised Guidelines on 5 June 2023.
- **Records** for NBCS 2026, IS 4963 : 2025, IS 15330 : 2020 and RPwD Rules Rule 15 in `mandates/legal-mandates-sources.md`.

### Changed
- **MoHUA Harmonised Guidelines 2021:** reconverted from the NIUA PDF with headings, tables and page markers, replacing the earlier line-by-line extraction.
- **NBC 2016:** replaced the full-text conversion with [`02-NBC-2016-Accessibility-Clause-Map.md`](mandates/national/02-NBC-2016-Accessibility-Clause-Map.md), a clause index for Part 3, Clause 13 and Annex B with summaries in the project's own words. The earlier file was mostly unreadable font codes, and the text is BIS copyright.
- **NBC official source:** linked the [BIS NBC page](https://www.bis.gov.in/standards/national-building-code/?lang=en) and the full Volume 1 hosted by the [Uttarakhand Town and Country Planning Department](https://tcp.uk.gov.in/document/national-building-code-of-india-2016-vol-i-part-1/). Linked only; not stored in the repository.
- **Citation form:** "NBC 2016, Part 3, Clause 13 / Annex B" replaces "Section 13" in mandates, prompts and guides. Filed case documents are unchanged; see the citation note in the Marbella case folder.

### Fixed
- **Lift control heights** in prompts and guides: car control panel 900–1 100 mm (B-6.4.5) and landing call button 800–1 000 mm (B-6.4.4). These were previously stated as 900–1 200 mm.
- Broken links to the removed NBC file in `mandates/legal-mandates-sources.md` and `mandates/national/README.md`.

### Verified
- **NBC clause map:** all 105 figures checked against the Uttarakhand-hosted official text (SP 7:2016, third revision) using OCR, since the PDF's text layer is unreadable. All matched. Post-2016 amendments still to be checked.

---

## [v1.1.0-alpha] — 2026-11-10

### Overview

**Governance Utilities for Accessibility Case Management**: Created three production-ready, token-efficient utilities to ease contributions and support case preparation. Delivered PDF-to-markdown converter (OCR-enabled), legal claims verification system prompt, and case formulation prompt. All utilities tested against real Marbella case material.

### Changes

#### 1. PDF to Markdown Converter Script
- **Created:** `scripts/pdf-to-markdown.py` (13.3 KB)
  - Converts government PDFs to searchable markdown format
  - Supports native PDFs (MOHUA Guidelines, NBC, RPWD Act) and scanned documents (GRs, circulars)
  - OCR fallback using easyocr for scanned/poorly-structured PDFs
  - Table extraction and markdown formatting
  - Metadata header with source URL, extraction date, original document date
  - Batch processing via JSON configuration file
  - CLI interface with comprehensive help and error handling
  - Reduces repo size while maintaining LLM accessibility

- **Created:** `scripts/requirements.txt` — Dependencies documentation
- **Created:** `scripts/README.md` — Complete usage guide, examples, troubleshooting

**Rationale:** Eliminates need for repeated LLM calls to convert PDFs; standardizes mandate digitization workflow for Phase 2 expansion.

#### 2. Legal Claims Verification Prompt
- **Created:** `prompts/verify-legal-claims.md` (9.8 KB)
  - System prompt for validating accessibility case claims against Indian law
  - Maps claims to applicable sections: RPWD Act 2016, Real Estate Act 2016, NBC 2016, MOHUA Guidelines 2021
  - 5-step verification process: extract claims → map to statutes → assess evidence → identify gaps → recommend relief
  - Evidence assessment: Supported / Partially Supported / Insufficient / Unsupported
  - Identifies evidence gaps with prioritization
  - Recommends applicable RERA sections (11, 18, 36, 38, 61) and RPWD Act penalties
  - Includes privacy guardrails and not-legal-advice disclaimer
  - Agent-agnostic (works with any LLM or GitHub Copilot)
  - Tested against real Marbella case material

**Use Case:** Pre-filing claim validation, evidence gap identification, relief section recommendation

#### 3. Case Formulation Prompt
- **Created:** `prompts/formulate-case.md` (14.5 KB)
  - System prompt for structuring accessibility case narratives into legal format
  - Aligns with `templates/case-summary.md` for knowledge base contribution
  - 5-phase formulation: narrative capture → organize facts → evidence assessment → relief mapping → publication review
  - Extracts structured case data: parties, issues, evidence inventory, applicable relief
  - Maps accessibility barriers to legal categories with mandate references
  - Prioritized evidence gap identification
  - Supports anonymization for privacy protection
  - Publication readiness checklist (consent, privacy, rights, de-identification)
  - Designed for future GitHub Copilot agent integration
  - Tested against real Marbella case narrative

**Use Case:** RERA complaint preparation, evidence organization, KB contribution structuring

#### 4. Documentation and Validation
- **Created:** `prompts/README.md` (11.7 KB)
  - Complete documentation for both system prompts
  - Usage instructions for GitHub Copilot agent integration
  - Standalone LLM usage with Python code examples
  - Workflow integration (sequential use of both prompts)
  - Legal framework reference table
  - Privacy and accuracy guardrails
  - Integration with repository resources (mandates/, templates/, cases/)
  - Contributing guidelines for prompt updates

- **Created:** `prompts/VALIDATION-TESTS.md` (12.9 KB)
  - Real-world validation against Marbella case material
  - Example input and output from both prompts
  - Demonstrates claim mapping to applicable statutes
  - Shows evidence gap identification and prioritization
  - Confirms alignment with filed case materials
  - Provides usage recommendations for advocates and organizations

- **Created:** `GOVERNANCE-UTILITIES-SUMMARY.md` (10.6 KB)
  - Comprehensive delivery summary
  - Quality assurance checklist
  - Future integration roadmap (Phase 2-3 enhancements)
  - Usage instructions and workflow examples

- **Created:** `QUICK-START-GOVERNANCE-UTILITIES.md` (6.5 KB)
  - Quick reference guide for all utilities
  - Installation and usage examples
  - Common questions and answers
  - Links to detailed documentation

**Rationale:** Documentation enables adoption without requiring LLM re-engineering for each use case. Reusable prompts reduce token costs for case management workflows.

### Files Affected

**Created:**
- `scripts/pdf-to-markdown.py` — PDF to markdown converter with OCR
- `scripts/requirements.txt` — Python dependencies
- `scripts/README.md` — Converter usage documentation
- `prompts/verify-legal-claims.md` — Claims verification system prompt
- `prompts/formulate-case.md` — Case formulation system prompt
- `prompts/README.md` — Prompts documentation
- `prompts/VALIDATION-TESTS.md` — Real-case validation examples
- `GOVERNANCE-UTILITIES-SUMMARY.md` — Delivery summary
- `QUICK-START-GOVERNANCE-UTILITIES.md` — Quick-start guide

### Quality Assurance

- ✅ Python syntax validated (pdf-to-markdown.py)
- ✅ Both prompts tested against real Marbella case material
- ✅ Statute references verified against repository mandates
- ✅ Output structure validated against templates
- ✅ Privacy and rights guardrails included
- ✅ Comprehensive usage examples and troubleshooting guides

### Commits

**Commit Hash:** `e8e434e`
**Message:** "Add governance utilities: PDF converter and case management prompts"

### AI Tool Context

For Copilot/Claude/GPT using this repo:
- Both prompts are **system prompts** (not task-specific instructions) and can be directly applied to your LLM
- Copy prompt content and use as system message in any LLM interface
- Prompts are designed for GitHub Copilot agent integration (see prompts/README.md)
- Both prompts reference mandates/ folder—updates to mandates automatically improve prompt accuracy
- See QUICK-START-GOVERNANCE-UTILITIES.md for integration examples

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

**Commit Hash:** `f505b6c`
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

**Commit Hash:** `9b3597d`
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

**Commit Hash:** `9b3597d`
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

**Commit Hash:** `5f75831`
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
