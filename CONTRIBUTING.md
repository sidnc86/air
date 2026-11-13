# Contributing

This project collects source-attributed information about making buildings in India accessible to disabled people, older people, families, practitioners, and others who use or maintain them.

**Read [`PRIVACY.md`](PRIVACY.md) before contributing anything about a real case.** It sets out what may be published (Tiers A, B and C). Where this guide and `PRIVACY.md` seem to differ, `PRIVACY.md` applies.

---

## Ways to contribute

| What | Tier | Route |
|---|---|---|
| Flag an outdated or broken mandate source | A | [Mandate update issue](.github/ISSUE_TEMPLATE/mandate-update.md) |
| Correct or improve a guide, solution or template | A | Pull request |
| Add a new mandate record or guide | A | Pull request, following `SOURCES.md` |
| Share your accessibility case | B | Private contact first, then a reviewed pull request |
| Original agreements, payment records, ID documents, others' data | C | Not accepted |

If you cannot use GitHub, contact the maintainer for a non-technical route. Do not send Tier C material through any route.

---

## Before proposing material

- Start with an official source where possible. Record the issuer, title, edition or date, URL, date checked, pinpoint (only if verified) and rights status, as set out in `SOURCES.md`.
- Keep source text separate from your summary, experience and recommendations. Mark what is unverified. Do not claim legal applicability or compliance without support.
- Public availability is not permission to republish. Keep third-party text short, cite it, and do not upload source documents unless reuse rights are clear.
- Use descriptive file names with hyphens, no spaces, and no personal details in file or folder names.

---

## Sharing your case

Cases show others how the law applies in practice and what a complaint actually involves. A case is shared as a written summary and your own filings, never as your original evidence bundle.

### What a published case contains

- `case-summary.md`, written using [`templates/case-summary.md`](templates/case-summary.md)
- Your own filed text (complaint, relief sought, submissions), with identifiers removed
- Authority orders and notices, where they are public record and contain no Tier C details
- Photos of common areas showing the barrier, with metadata stripped and no people, name plates, flat numbers or vehicle numbers visible
- Your own measurements, timelines and proposed solutions

### What stays with you

Agreements, Index II, demand letters, payment statements, receipts, ID documents, portal screenshots with personal details, medical records, and anything containing other people's personal data. Keep these safely for your own case. They are not published here, even redacted.

### How to submit a case

1. **Contact the maintainer privately** with a short description: state, authority, building type, status, and the barriers involved. Do not attach evidence at this stage.
2. **Prepare the case together.** Agree what will be published, how you will be credited, and which licence applies.
3. **Privacy review.** A reviewer other than you checks the material against the checklist in `PRIVACY.md`, including file metadata. For now, there is no dedicated reviewer appointed. Anybody with relevant legal experience willing to volunteer is welcome. Till then, it would be the maintainor having access to the dedicated email and yourself together getting this right.
4. **Pull request.** Only reviewed material is committed, in a new folder: `cases/<state-code>/<city>-<short-slug>/`. Do not name individuals in the slug.

Pull requests that add case material without this review will be closed and, where needed, removed from history.

### Corrections and withdrawal

Filed documents are not rewritten to change their meaning. Add updates as new, dated files in your case folder. Privacy corrections and withdrawals are always allowed: see `PRIVACY.md`.

---

## Tools for preparing a case

1. **Case formulation prompt** ([`prompts/formulate-case.md`](prompts/formulate-case.md)): structures your narrative, links barriers to applicable mandates (RPwD Act, RERA, NBC, MOHUA), identifies evidence gaps and runs a publication checklist.
2. **Legal claims verification prompt** ([`prompts/verify-legal-claims.md`](prompts/verify-legal-claims.md)): checks claims against the statutes, rates evidence as supported, partially supported or insufficient, and suggests relevant RERA sections.

See [`QUICK-START-GOVERNANCE-UTILITIES.md`](QUICK-START-GOVERNANCE-UTILITIES.md) for examples. These prompts run on third-party AI services: remove Tier C details before pasting any case material into them. Their output is a starting point, not legal advice.

---

## Mandates as Markdown

Large government mandates and building codes are converted to Markdown so they are searchable, small to store, and usable by AI tools. Each file records its official source URL, document date and edition, and extraction date.

To convert a PDF:

```bash
cd scripts
pip install -r requirements.txt

# Single PDF
python pdf-to-markdown.py input.pdf output.md --url "https://source.gov/doc.pdf" --date "2016-01-01"

# Batch conversion
python pdf-to-markdown.py --batch config.json
```

See [`scripts/README.md`](scripts/README.md) for OCR, batch processing and troubleshooting.

Locations:

- National mandates: `mandates/national/0X-<name>.md`
- State mandates: `mandates/<STATE>/0X-<name>.md`

Record each conversion in [`mandates/legal-mandates-sources.md`](mandates/legal-mandates-sources.md) with its verification and rights status. Converting a document does not give permission to redistribute it: check rights before committing full text.

---

## Where material belongs

- `mandates/`: records and Markdown conversions of laws, rules, standards and official guidance, with source and verification status.
- `guides/`: independently written, sourced procedures, with verification gaps stated.
- `solutions/`: practical ideas and technical references, clearly distinguished from tested or standards-compliant designs.
- `cases/`: reviewed case folders as described above. Not an upload destination for unreviewed material.
- `templates/`: blank contribution aids.
- `prompts/`: reusable AI prompts.

---

## Credit and licence

- **Credit:** by name, by pseudonym, or anonymously. Your choice is recorded before publication.
- **Anonymous cases** use a reference such as "Maharashtra, 2026, residential tower" without your name or address.
- **Licence:** original project text is covered by [`LICENSE.md`](LICENSE.md). Your case material remains your copyright unless you choose to license it under CC BY 4.0.

## Contact

For private case discussions, contact the maintainer at: [sidnc86.air@gmail.com](mailto:sidnc86.air@gmail.com)
