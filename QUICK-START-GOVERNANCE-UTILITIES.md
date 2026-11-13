# Quick Start: Governance Utilities

Three reusable tools to ease contributions and support accessibility case management.

---

## 🚀 Quick Links

| Tool | Purpose | Location | Best For |
|------|---------|----------|----------|
| **PDF Converter** | Convert government PDFs to markdown | `scripts/pdf-to-markdown.py` | Digitizing mandates (MOHUA, NBC, RPWD Act) |
| **Claims Verifier** | Validate case claims against law | `prompts/verify-legal-claims.md` | Pre-filing validation, evidence gap identification |
| **Case Formulator** | Structure case narratives | `prompts/formulate-case.md` | Preparing RERA complaints, KB contributions |

---

## 1️⃣ PDF to Markdown Converter

### Install
```bash
cd scripts
pip install -r requirements.txt
```

### Convert One PDF
```bash
python pdf-to-markdown.py input.pdf output.md \
  --url "https://source.gov/doc.pdf" \
  --date "2016-01-01"
```

### Convert Multiple PDFs
Create `batch-config.json`:
```json
{
  "conversions": [
    {
      "input": "mohua.pdf",
      "output": "mandates/national/01-MOHUA-guidelines.md",
      "url": "https://mohua.gov.in/...",
      "date": "2021-10-15"
    }
  ]
}
```

Run: `python pdf-to-markdown.py --batch batch-config.json`

📖 Full guide: [scripts/README.md](scripts/README.md)

---

## 2️⃣ Legal Claims Verification Prompt

### Setup (Any LLM)

**Option A: Claude (Python)**
```python
from anthropic import Anthropic

client = Anthropic()
system_prompt = open("prompts/verify-legal-claims.md").read()

response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=2048,
    system=system_prompt,
    messages=[{
        "role": "user",
        "content": "Verify these case claims against Indian law: ..."
    }]
)
```

**Option B: Any LLM UI**
1. Copy content of `prompts/verify-legal-claims.md`
2. Paste as "System Prompt" or "Instructions"
3. Paste your case material in user message
4. Request verification

### What It Does
- Maps claims to statute sections (RPWD Act, RERA, NBC, MOHUA)
- Assesses evidence adequacy
- Identifies missing evidence
- Recommends applicable relief

### Example Input
```
Case: Lift buttons lack Braille; positioned 1.45m high
Evidence: Photos, measurements, builder email
```

### Example Output
```
Verification Status: SUPPORTED

Applicable Statutes:
- RPWD Act 2016, Section 40 (building accessibility)
- NBC 2016, Part 3, Clause 13 and Annex B (lift requirements)

Evidence Gaps:
- Missing: NBC Part 3, Clause 13 technical specification text
- Missing: Professional accessibility audit

Recommended Relief:
- RERA Section 36: Specific performance (retrofit accessible lift)
```

📖 Full guide: [prompts/README.md](prompts/README.md)

---

## 3️⃣ Case Formulation Prompt

### Setup (Any LLM)

**Option A: Claude (Python)**
```python
from anthropic import Anthropic

client = Anthropic()
system_prompt = open("prompts/formulate-case.md").read()

response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=4096,
    system=system_prompt,
    messages=[{
        "role": "user",
        "content": "Please structure this case narrative: I'm a blind resident..."
    }]
)
```

**Option B: Any LLM UI**
1. Copy content of `prompts/formulate-case.md`
2. Paste as "System Prompt"
3. Describe your case in user message
4. Request case formulation

### What It Does
- Extracts accessibility issues from narratives
- Maps to applicable legal standards
- Catalogs evidence (what you have, what's missing)
- Suggests applicable relief (RERA sections, remedies)
- Prepares publication checklist

### Example Input
```
I'm a wheelchair user in a Pune residential tower. 
The lift buttons are too high and there's no ramp 
to the clubhouse. I have photos but not sure what 
to include in a RERA complaint.
```

### Example Output (Simplified)
```
# Case Formulation Summary

## Accessibility Issues Identified

### Issue 1: Lift Button Accessibility
- Technical facts: Buttons positioned 1.45m (above the 1 100 mm upper limit in NBC B-6.4.5)
- Applicable law: RPWD Act Section 40, NBC Part 3, Clause 13
- Relief: RERA Section 36 (specific performance)
- Evidence gaps: Measurements, expert audit

### Issue 2: Clubhouse Access
- Technical facts: Stairs only, no ramp
- Applicable law: NBC Part 3, Clause 13 (ramp requirements)
- Relief: RERA Section 36 (specific performance)
- Evidence gaps: Building plan, slope measurements

## Next Steps
1. Gather measurements (priority!)
2. File RERA complaint under Section 11
3. Attach evidence package
```

📖 Full guide: [prompts/README.md](prompts/README.md)

---

## 🧪 Examples from Real Cases

See [prompts/VALIDATION-TESTS.md](prompts/VALIDATION-TESTS.md) for real-world examples of both prompts applied to the actual Marbella accessibility case in this repository.

---

## 📚 Complete Documentation

- **Scripts:** [scripts/README.md](scripts/README.md) – PDF converter usage, troubleshooting, advanced options
- **Prompts:** [prompts/README.md](prompts/README.md) – GitHub Copilot agent integration, workflow examples
- **Validation:** [prompts/VALIDATION-TESTS.md](prompts/VALIDATION-TESTS.md) – Real case examples
- **Full Summary:** [GOVERNANCE-UTILITIES-SUMMARY.md](GOVERNANCE-UTILITIES-SUMMARY.md) – Complete deliverables overview

---

## ❓ Common Questions

**Q: Can I use these without Python/LLM coding?**  
A: Yes! Copy the prompt content into any LLM chat interface (ChatGPT, Claude, Gemini, etc.)

**Q: Do I need to install the PDF converter?**  
A: Only if you're digitizing PDFs. The prompts work with any LLM without installation.

**Q: Can I integrate these into GitHub Copilot?**  
A: Yes! See [prompts/README.md](prompts/README.md) for agent configuration instructions.

**Q: Are these legal advice?**  
A: No. They help structure and validate cases, but always consult a lawyer before filing.

**Q: Can I modify these for my jurisdiction?**  
A: Yes! They're designed for extensibility. See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## 📞 Support

- **PDF converter issues:** See [scripts/README.md](scripts/README.md) troubleshooting section
- **Prompt questions:** See [prompts/README.md](prompts/README.md) usage notes
- **Contributing updates:** See [CONTRIBUTING.md](CONTRIBUTING.md)

---

**Ready to get started?** Pick your use case above and follow the Quick Start section! 🚀
