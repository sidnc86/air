# Privacy and Publication Rules

This repository is public. Anything committed here can be copied, forked, cached and indexed, and deleting it later may not remove those copies. These rules apply to every contributor, including the maintainer, and to every route into the repository: pull requests, issues, discussions, and any future web form.

## The rule

**Nothing that identifies a person, their home, or their money is published here, and nothing about a case is published without review.**

A case is shared as an independently written summary plus the contributor's own filings with identifiers removed. Original evidence stays with the person who owns it.

## What may be published

| Tier | Material | Condition |
|---|---|---|
| A. Open | Mandate records, guides, solutions, templates | Source rules in `SOURCES.md` and rights rules below |
| B. Reviewed | Case summaries; the contributor's own filed text (complaint, relief sought, submissions); photos of common areas | Privacy review below, contributor consent, credit choice recorded |
| C. Never | Everything in "Never publish" below | Not publishable in any form, including redacted copies |

### Never publish

- Sale agreements, Index II, allotment letters, demand letters, payment statements, receipts, bank or transaction records
- Identity documents and numbers: Aadhaar, PAN, passport, voter ID, driving licence
- Phone numbers, email addresses, home addresses, flat or unit numbers, vehicle numbers, signatures
- Portal screenshots that show login details, contact details or personal dashboards
- Medical records, disability certificates, or health details beyond what the contributor chooses to state in general terms
- Personal data of anyone other than the contributor (neighbours, family, staff, officials' personal contacts)
- Private correspondence written by someone else, and builders' internal or confidential documents

## Privacy review (Tier B)

Before Tier B material is merged, a reviewer other than the contributor confirms that:

1. No Tier C item appears, including in images, scanned pages, file names and folder names.
2. People's faces, name plates, flat numbers and vehicle numbers are not visible in photos.
3. File metadata is removed: photo EXIF (GPS location, device, time), and author fields in PDF and Office files.
4. Statements about builders, officials or others are labelled as allegation, party submission or authority finding, with a source for each.
5. The contributor has consented to publication and chosen how to be credited (name, pseudonym, or anonymous).

Complaint and case numbers can be searched on authority portals and linked to a person's name. Publish them only if the contributor chooses to.

## Integrity and corrections

Filed documents are not rewritten to change their meaning. Corrections and updates are added as new, dated entries.

Privacy overrides integrity. Redacting, removing or withdrawing material for privacy or rights reasons is always allowed. When it happens, the history is rewritten where needed and the change is noted in `CHANGELOG.md` without repeating the removed details.

## Withdrawal

A contributor can ask for their material to be removed at any time. It will be removed from the repository and its history. Copies already made by others (forks, clones, caches, search engines) cannot be recalled, which is why review happens before publication rather than after.

## Using AI tools with case material

The prompts in `prompts/` work with third-party AI services. Remove Tier C details before pasting case material into any of them. Treat those services as you would any other outside party.

## Third-party material

Publicly accessible does not mean freely reusable. Laws, standards, official PDFs, images and articles are reproduced only where permission or a legal basis has been checked. Record rights status separately from attribution: crediting a source is not permission to copy it. Prefer short quotations with a pinpoint citation and a link to the official source.

## Submitting material

There is currently no private upload service. Until one exists:

- **Tier A:** open an issue or pull request as described in `CONTRIBUTING.md`.
- **Tier B:** contact the maintainer privately first (see `CONTRIBUTING.md`). Do not attach evidence to a public issue or pull request.
- **Tier C:** do not send it anywhere through this project.

A planned web form will hold submissions privately until they pass review, and only then open a pull request. Its consent, retention and deletion terms will be published here before it accepts anything.
