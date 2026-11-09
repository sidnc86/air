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
| [`the_rights_of_persons_with_disabilities_act,_2016.pdf`](national/the_rights_of_persons_with_disabilities_act,_2016.pdf) | National Statute | **Source URL:** https://indiacode.nic.in (India Code) / Gemini-sourced Oct 2026  **Format:** PDF  **Local Path:** `mandates/national/`  **Status:** Original text verified on official DEPwD Acts index. | Sections 44-45 text not yet verified in this pass. Claim that sections prohibit completion certificate is unestablished; do not rely on it. The Acts index at [DEPwD](https://depwd.gov.in/en/acts/) confirms publication. | Pending markdown extraction of relevant disability-rights and accessibility provisions for case reference. | Government publication (likely public domain); verify reuse terms on India Code or DEPwD site before republishing extracts. |
| [`NBC-2016-Section-13-ANNEX-B-.pdf`](national/NBC-2016-Section-13-ANNEX-B-.pdf) | National Building Code | **Source URL:** enableme-access.com (non-BIS hosted)  **Format:** PDF  **Local Path:** `mandates/national/`  **Status:** PDF source not independently authenticated from BIS or government domain. Edition, text, and amendments not verified. | Claim that all residential lifts must have Braille buttons and voice announcements is **withdrawn**—unverified and pending review from authoritative, applicable NBC edition. Page and annex pinpoint also unverified. | ✅ **CONVERTED:** [02-NBC-2016-Section-13-ANNEX-B.md](national/02-NBC-2016-Section-13-ANNEX-B.md) — Full text extraction via pypdf. Extracted 2026-11-09. | BIS/government reproduction rights unchecked; do not quote or redistribute without verification of official source and reuse license. |
| [`MOHUA-building-guidelines.pdf`](national/MOHUA-building-guidelines.pdf) | National Guidance (MoHUA, 2021) | **Source URL:** NIUA domain / DEPwD Acts guidance index  **Format:** PDF  **Local Path:** `mandates/national/`  **Status:** DEPwD index lists a 2021 MoHUA guideline; PDF link hosted on NIUA domain. Title page and relevant text not checked in this pass. | Chapter 5, pages, 1:12 ramp ratio, tactile-indicator claims, and applicability not verified. No lift-Braille grade or contraction claim established. | ✅ **CONVERTED:** [01-MOHUA-building-guidelines-2021.md](national/01-MOHUA-building-guidelines-2021.md) — Full text extraction via pypdf (474 pages). Extracted 2026-11-09. Repo optimized: 63.13 MB PDF → 0.55 MB markdown. | Check MoHUA/NIUA publication reuse terms before republishing extracts. |
| [`UDCPR_compressed_2.pdf`](mh/UDCPR_compressed_2.pdf) | Maharashtra Development Regulations | **Source URL:** MMRDA website (https://www.mmrda.maharashtra.gov.in/)  **Format:** PDF  **Local Path:** `mandates/mh/`  **Status:** Official Maharashtra authority host; PDF edition, amendments, and text not independently verified. | Regulation 33.0/33.1, cited page range, and claim that these mandate ramps, accessible lifts, and tactile paths for all buildings remain **unverified**. Amendments post-download not checked. | ✅ **CONVERTED:** [01-UDCPR-2016-Maharashtra.md](mh/01-UDCPR-2016-Maharashtra.md) — Full text extraction via pypdf. Extracted 2026-11-09. | Check MMRDA issuing source and reuse permission before redistributing extracts. |
| [`Real_Estate_Act_2016-26-03-2016.pdf`](mh/Real_Estate_Act_2016-26-03-2016.pdf) | National Statute; Maharashtra Copy | **Source URL:** Karnataka RERA allottee quick links (cross-jurisdiction reference)  **Format:** PDF  **Local Path:** `mandates/mh/`  **Status:** Copy sourced from official state RERA portal; text and amendment status not reviewed in this pass. | No specific provisions summarized in this table pending Section analysis for RERA complaint relevance. | Pending markdown extraction of sections relevant to RERA complaint filing, allottee rights, developer obligations, and accessibility/building-code compliance clauses. | Check local copy source and official RERA publication reuse terms. |
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




