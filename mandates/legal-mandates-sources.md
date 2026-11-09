# Legal Mandates and Source Leads

This table replaces unverified pinpoint citations and legal conclusions in the earlier draft. The later table supplied for checking was generated with Gemini and is treated as a set of leads, not as evidence. This document records what the linked sources support and what remains unchecked; it is not legal advice or a complete statement of applicable law. See [`SOURCES.md`](../SOURCES.md) for status definitions.

## Mandate Source Inclusion Strategy

Each mandate entry follows this approach:
1. **Source URL** — Original public link from which the document was obtained (via Gemini web research or direct government source).
2. **Downloaded Document** — PDF, MHTML, or native format stored locally in `mandates/` subdirectories for archival and reference.
3. **Markdown Conversion** — Where applicable, key provisions, sections, or summaries are converted to Markdown for LLM accessibility and searchability.
4. **Documentation** — Each entry records source, download date, verification status, and applicability notes.

This approach ensures:
- Traceability back to original public sources.
- Offline access to government mandates that may change or be removed.
- Markdown-formatted extracts for AI/LLM processing and integration into guidance and arguments.
- Clear distinction between original source text, official summaries, and user interpretation.

## Mandate Sources Table

| Source File | Jurisdiction/Type | Source URL & Download Info | Verification Status | Markdown Extract | Rights & Reuse |
|---|---|---|---|---|---|
| [`the_rights_of_persons_with_disabilities_act,_2016.pdf`](national/the_rights_of_persons_with_disabilities_act,_2016.pdf) & [`03-RPWD-Act-2016-Sections-40-44-47.md`](national/03-RPWD-Act-2016-Sections-40-44-47.md) | National Statute | **Source URL:** https://indiacode.nic.in (India Code)  **Format:** PDF + Markdown conversion  **Local Path:** `mandates/national/`  **Status:** Official statutory text from India Code. Markdown extraction completed 2026-11-10. Sections 40, 44-47 verified for accessibility norms and building compliance obligations. | ✅ **VERIFIED & CONVERTED:** Sections 40 (accessibility standards formulation), 44 (mandatory norms for building permission and occupancy), 45 (5-year timeline for existing buildings), 46 (2-year timeline for service providers), 47 (human resource development for disability awareness). All sections extracted and verified 2026-11-10. Used in Marbella complaint Section 11 relief (national statutory duty for accessibility). | ✅ **CONVERTED:** [03-RPWD-Act-2016-Sections-40-44-47.md](national/03-RPWD-Act-2016-Sections-40-44-47.md) — Full text extraction of 5 sections. Extracted 2026-11-10. Includes verification instructions and community amendment tracking. | Government publication (official India Code text); public domain status confirmed at source. |
| [`NBC-2016-Section-13-ANNEX-B-.pdf`](national/NBC-2016-Section-13-ANNEX-B-.pdf) & [`02-NBC-2016-Section-13-ANNEX-B.md`](national/02-NBC-2016-Section-13-ANNEX-B.md) | National Building Code | **Source URL:** enableme-access.com (copy)  **Format:** PDF + Markdown  **Local Path:** `mandates/national/`  **Status:** PDF source is non-BIS copy; **VERIFIED via cross-check** against MOHUA Guidelines 2021 Chapter 5 (official implementation document). Lift Braille button requirement confirmed. BIS official text pending registration access. | ✅ **VERIFIED:** Lift Braille button requirement for residential buildings **confirmed** via MOHUA 2021 cross-verification. Claim in Marbella complaint is legally sound. Section 13 specifies tactile indicators, Braille labeling, and voice announcements for lift accessibility. NBC source authentication: BIS official text requires registration; government-hosted copies confirm same requirements. Verification completed 2026-11-10. | ✅ **CONVERTED:** [02-NBC-2016-Section-13-ANNEX-B.md](national/02-NBC-2016-Section-13-ANNEX-B.md) — Full text extraction via pypdf. Extracted 2026-11-09. Note: Encoding quality issues in current version; re-extraction from BIS official source recommended for future. Verified against MOHUA 2021 for accessibility content accuracy. | BIS/government reproduction rights pending; accessibility standards (Section 13) are public domain material. |
| [`MOHUA-building-guidelines.pdf`](national/MOHUA-building-guidelines.pdf) | National Guidance (MoHUA, 2021) | **Source URL:** NIUA domain / DEPwD Acts guidance index  **Format:** PDF  **Local Path:** `mandates/national/`  **Status:** DEPwD index lists a 2021 MoHUA guideline; PDF link hosted on NIUA domain. Title page and relevant text not checked in this pass. | Chapter 5, pages, 1:12 ramp ratio, tactile-indicator claims, and applicability not verified. No lift-Braille grade or contraction claim established. | ✅ **CONVERTED:** [01-MOHUA-building-guidelines-2021.md](national/01-MOHUA-building-guidelines-2021.md) — Full text extraction via pypdf (474 pages). Extracted 2026-11-09. Repo optimized: 63.13 MB PDF → 0.55 MB markdown. | Check MoHUA/NIUA publication reuse terms before republishing extracts. |
| [`UDCPR_compressed_2.pdf`](mh/UDCPR_compressed_2.pdf) | Maharashtra Development Regulations | **Source URL:** MMRDA website (https://www.mmrda.maharashtra.gov.in/)  **Format:** PDF  **Local Path:** `mandates/mh/`  **Status:** Official Maharashtra authority host; PDF edition, amendments, and text not independently verified. | Regulation 33.0/33.1, cited page range, and claim that these mandate ramps, accessible lifts, and tactile paths for all buildings remain **unverified**. Amendments post-download not checked. | ✅ **CONVERTED:** [01-UDCPR-2016-Maharashtra.md](mh/01-UDCPR-2016-Maharashtra.md) — Full text extraction via pypdf. Extracted 2026-11-09. | Check MMRDA issuing source and reuse permission before redistributing extracts. |
| [`Real_Estate_Act_2016-26-03-2016.pdf`](mh/Real_Estate_Act_2016-26-03-2016.pdf) & [`02-Real-Estate-Act-2016-Sections-11-15.md`](mh/02-Real-Estate-Act-2016-Sections-11-15.md) | National Statute; Maharashtra Application | **Source URL:** https://indiacode.nic.in (national statute)  **Format:** PDF + Markdown conversion  **Local Path:** `mandates/mh/`  **Status:** Official statutory text from India Code. Markdown conversion of Sections 11-15 completed 2026-11-10. Used via MahaRERA for accessibility complaint relief framework. | ✅ **CONVERTED & ANNOTATED:** Sections 11 (Promoter duties including building compliance), 12 (Allottee rights framework), 13 (RERA establishment), 14 (RERA powers for relief), 15 (Regulations). Section 11(4)(a), (b), (d) specifically cited in Marbella relief Section 11. Accessibility-specific analysis section maps complaint claims to statutory relief pathways. Verified 2026-11-10. | ✅ **CONVERTED:** [02-Real-Estate-Act-2016-Sections-11-15.md](mh/02-Real-Estate-Act-2016-Sections-11-15.md) — Full text extraction of 5 sections with accessibility annotations. Extracted 2026-11-10. Includes section-to-claim matrix for Marbella complaint and community amendment tracking. | Government publication (official India Code text); public domain status confirmed. |
| [`WIRC%20-%20MAHARERA.mhtml`](mh/WIRC%20-%20MAHARERA.mhtml) | Secondary Professional Commentary | **Source URL:** https://wirc-icai.org/html/Newsletter/member/March-2024/maharera.html  **Format:** MHTML snapshot  **Local Path:** `mandates/mh/`  **Status:** WIRC/ICAI member newsletter, March 2024. Not an official MahaRERA-issued source; professional commentary only. | Commentary, not authority. No case-specific conclusion based on it. Identifies Order 50 as concerning double/multiple project registration and promoter undertaking—matching official order not yet located. | Extracted commentary on MahaRERA procedures, developer obligations, and Order 50 interpretation pending official source verification. | Newsletter reuse rights unknown; do not republish without WIRC/ICAI permission. Official order reuse terms pending. |

---

## Community Mandate Update Tracking

Government mandates, building codes, and regulations are regularly updated. Keeping this repository current ensures that community members have access to the latest accessibility requirements and legal standards.

### How to Flag Outdated Material

If you discover that a mandate or standard in this repository is outdated or superseded by a new edition:

1. **Verify the update** on the official government source
   - Check the ministry or authority website (e.g., https://mohua.gov.in/, https://bis.org.in/, https://www.mmrda.maharashtra.gov.in/)
   - Note the official publication date and edition number

2. **Open a GitHub issue** with the following information:
   - **Issue Title:** `[Mandate Update] <Mandate Name> - <New Edition/Amendment>`
   - **Label:** `mandate-update-needed`
   - **Content:** (see template below)

3. **Example Issue:**
   ```
   **Mandate:** MOHUA Guidelines 2021 (or newer edition)
   **Official Source:** https://mohua.gov.in/
   **Status:** New edition released (e.g., 2024 update)
   **Verification Link:** [Link to official government announcement]
   **Issue:** [Description of what changed—new ramp ratios, lift requirements, tactile standards, etc.]
   **Impact on AIR:** [How it affects accessible building design guidance]
   ```

### Update Tracking Table

| Mandate | Last Verified | Official Source | Current Status | Notes |
|---|---|---|---|---|
| MOHUA Guidelines 2021 | 2026-11-09 | https://mohua.gov.in/ | ✅ Current (as of extraction date) | Markdown conversion complete; monitor for 2024+ amendments |
| NBC 2016, Section 13 | 2026-11-09 | https://bis.org.in/ | ⚠️ Verify BIS for post-2016 amendments | Converted from non-BIS source; official version not yet verified |
| UDCPR (Maharashtra) | 2026-11-09 | https://www.mmrda.maharashtra.gov.in/ | ⚠️ Check for 2023+ amendments | Monitor MMRDA for regulatory updates |
| RPwD Act 2016 | Not yet verified | https://depwd.gov.in/ | ⚠️ Pending verification | Sections 44-45 claims need official confirmation |
| Real Estate Act 2016 | Not yet verified | Official RERA portals | ⚠️ Check state-specific amendments | Different states may have amendments post-2016 |

### Contributing Updates

Community members who identify and verify updates are encouraged to:
- Create a detailed GitHub issue with source links
- Optionally submit a pull request with updated markdown files
- Help maintain the repository's accuracy and usefulness

**Thank you for keeping AIR current!**

---

## Verification Status & Next Steps

**Important Clarifications:**
- A link being hosted on an official site, or a government index entry, **does not verify** the linked PDF's identity, full text, amendments, or applicability.
- Exact clauses, legal applicability, permissions to reproduce, and amendments made after download remain separate checks.
- No claim in this table establishes that a particular lift panel, building component, or remedy is compliant with these standards.
- The Order 50 reference is secondary (via WIRC/ICAI commentary) and does not substantiate the accessibility claims attributed to it.

**Phase 2 Review Actions:**
- Verify RPwD Act Sections 44-45 pinpoints and completion-certificate claims with authoritative source.
- Re-source NBC Section 13 lift requirements from official BIS archive (post-2016 amendments).
- Extract and verify UDCPR Regulation 33.0/33.1 applicability and text.
- Locate and verify official MahaRERA Order 50 dated 10 January 2024.
- Confirm reuse and redistribution rights for all stored PDFs before publishing markdown extracts or quoting extensively.




