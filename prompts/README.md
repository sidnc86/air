# Prompts Documentation

This folder contains reusable system prompts designed for accessibility case management agents and workflows. These prompts are **token-efficient, future-proof, and agent-agnostic**—they can be used with any LLM or agent framework (GitHub Copilot, Anthropic Claude, OpenAI GPT, etc.).

---

## Contents

### 1. **verify-legal-claims.md**
**System Prompt for Legal Claims Verification Agent**

**Purpose:** Validate case submissions against Indian legal mandates (RPWD Act 2016, Real Estate Act 2016, NBC 2016, MOHUA Guidelines)

**Audience:** Legal teams, accessibility advocates, RERA complaint processors

**What it does:**
- Maps each claim to applicable statute sections
- Assesses evidence adequacy (supported/partially supported/insufficient/unsupported)
- Identifies evidence gaps
- Recommends applicable relief (RERA remedies, RPWD Act penalties)

**Input:** Case narrative, submitted claims, evidence inventory  
**Output:** Claim-by-claim verification report with legal references and recommendations

**Use cases:**
- Pre-filing claim validation (before submitting RERA complaint)
- Case review by advocacy organization
- Evidence gap identification
- Statutory relief recommendation

---

### 2. **formulate-case.md**
**System Prompt for Case Structuring Agent**

**Purpose:** Guide accessibility advocates and affected individuals in organizing case narratives into structured legal format

**Audience:** Disabled people, family advocates, legal assistants, knowledge base contributors

**What it does:**
- Extracts and organizes case facts (parties, building, accessibility issues)
- Maps barriers to applicable legal standards
- Catalogs evidence (what exists, what's missing)
- Identifies applicable RERA sections and remedies
- Ensures publication readiness (privacy, rights review)

**Input:** Case narrative, experience description, evidence list  
**Output:** Structured case summary following `templates/case-summary.md` format

**Use cases:**
- Preparing RERA complaint filing
- Structuring case for knowledge base contribution
- Organizing evidence for legal review
- Identifying evidence gaps before filing
- Privacy and rights review before public sharing

---

## How to Use These Prompts

### As GitHub Copilot Agent System Prompts

1. **Create an `.agent.md` or `.instructions.md` file** in your workspace:
   ```markdown
   # Copilot Agent Configuration
   
   You are a case structuring assistant for accessibility advocacy.
   
   [Paste content from formulate-case.md here]
   ```

2. **Reference in your GitHub Copilot settings** to apply this as the agent's system instructions

3. **Alternatively, create separate agent definitions** for each purpose:
   - Claim verification agent (uses verify-legal-claims.md)
   - Case formulation agent (uses formulate-case.md)

### As Standalone LLM Prompts

**For any LLM (Claude, GPT, etc.):**

1. Copy the system prompt content
2. Paste as the system message when starting a conversation
3. Provide case materials as user input
4. Request specific output (verification report, case summary, etc.)

**Example with Claude:**
```python
from anthropic import Anthropic

client = Anthropic()

system_prompt = open("verify-legal-claims.md").read()

response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=2048,
    system=system_prompt,
    messages=[
        {
            "role": "user",
            "content": """
            Case: Marbella Residential Tower, Pune
            
            Claim 1: Lift buttons lack Braille labels and are positioned 1.45m high
            Evidence: Photos, measurements, builder correspondence
            
            Please verify these claims against applicable law.
            """
        }
    ]
)

print(response.content[0].text)
```

### As Workflow Integration

**Complete Accessibility Case Workflow:**

```
User Input (Case Narrative)
    ↓
[Formulate Case] → Structured Case Summary
    ↓
[Verify Legal Claims] → Claim Verification Report
    ↓
Gap Identification & Evidence Gathering
    ↓
Refined Case Summary → Ready for RERA Filing or KB Contribution
```

---

## Prompt Contents at a Glance

### verify-legal-claims.md

**Sections:**
- Legal Framework Reference (RPWD Act, Real Estate Act, NBC, MOHUA)
- Verification Process (5-step methodology)
- Output Format (claim-by-claim analysis structure)
- Important Constraints (accuracy, jurisdiction, privacy)
- Example claim and verification output

**Key Features:**
- References specific statute sections
- Distinguishes evidence types (direct vs. circumstantial)
- Flags missing documentation
- Recommends remedies under RERA Section 36 and RPWD Act penalties
- Includes privacy guardrails

### formulate-case.md

**Sections:**
- Case Structure Reference (aligns with templates/case-summary.md)
- Applicable Legal Mandates (RPWD Act, RERA, NBC, MOHUA)
- Case Formulation Process (5 phases from narrative capture to publication readiness)
- Output Structure (record, scope, accessibility issues, evidence, publication checklist)
- Important Constraints (privacy, rights, legal accuracy)
- Example case narrative and formulation output

**Key Features:**
- Extracts structured case data from free-form narratives
- Maps issues to legal categories and standards
- Catalogs evidence inventory
- Supports anonymization for privacy
- Publication readiness checklist
- Evidence gap prioritization

---

## Legal Standards Referenced

Both prompts reference the following Indian legal framework:

### National
- **RPWD Act 2016** – Rights of Persons with Disabilities (Sections 40–44, 47)
- **Real Estate Act 2016** – RERA (Sections 11, 14, 18, 36, 38, 61)
- **NBC 2016, Section 13, Annex B** – Building accessibility standards
- **MOHUA Guidelines 2021** – Universal design and accessibility implementation

### State (Maharashtra Example)
- Maharashtra RERA notification and rules
- State-specific complaint procedures and timelines

---

## Important Notes

### Accuracy and Verification
- These prompts reference statutes stored in `mandates/` folder
- Verify all legal citations against current versions
- Do not use outdated statute references
- Flag unverified claims and allegations clearly

### Privacy and Rights
- Prompts include guardrails against requesting private information
- Anonymization supported for privacy protection
- Third-party materials must not be included without consent
- No confidential or proprietary documents

### Not Legal Advice
- These prompts provide information structuring and verification, not legal advice
- Recommend consultation with qualified lawyer before filing complaints
- Accessibility audit by professional recommended for complex cases

---

## Integration with Repository

### Reference to Other Repository Resources

**Mandates Folder** (`mandates/`)
- Prompts reference specific mandates by name and section
- Updates to mandates automatically improve prompt accuracy
- Legal sources are verifiable against government documents

**Templates Folder** (`templates/case-summary.md`)
- Formulation prompt aligns output with case summary template
- Ensures consistent structure for knowledge base contributions
- Supports publication workflow

**Cases Folder** (`cases/`)
- Formulation prompt prepares structured input for case contribution
- Verification prompt validates claims against existing case material
- Immutable archive model preserved (no modifications to filed materials)

**Guides Folder** (`guides/`)
- Prompts complement procedural guides for accessibility advocacy
- Reference applicable sections and timelines from guides

---

## Usage Examples

### Example 1: Pre-Filing Claim Validation

**Input to verify-legal-claims.md:**
```
Case: Marbella Residential, Pune
Building: Residential (2021, RERA registered)

Claims:
1. Lift control buttons positioned 1.45m high; No Braille labels
2. Entrance ramp slope exceeds 1:12 (measured 1:8)
3. Accessible parking not provided (0 accessible spaces; should be 2 minimum)

Evidence:
- Lift photos and measurements
- Entrance ramp photos and slope calculation
- Building plan showing parking layout (from RERA registration)
```

**Output:** Verification report mapping each claim to RPWD Act sections 40/41, NBC 2016 Section 13, MOHUA guidelines; recommending RERA Section 36 specific performance relief

### Example 2: Case Formulation Before Filing

**Input to formulate-case.md:**
```
Story: "I'm a wheelchair user. When I moved into my apartment last year, I couldn't use the lift because the buttons were too high. There's no Braille, and the building has no accessible parking. I took measurements and photos but don't know how to file a complaint."
```

**Output:** Structured case summary with:
- Record (title, jurisdiction, building type)
- Identified accessibility issues (lift, parking) linked to standards
- Evidence inventory (photos, measurements available; expert audit missing)
- Applicable RERA sections (11, 36)
- Suggested remedy (retrofit lift buttons, provide accessible parking)
- Next steps for filing complaint

### Example 3: Knowledge Base Contribution

**Combined workflow:**
1. **Formulate** → Case summary from contributor's narrative
2. **Verify** → Validate claims against mandates
3. **Refine** → Gather additional evidence for unsupported claims
4. **Publication check** → Privacy review, consent, rights verification
5. **Contribute** → Immutable case archive entry

---

## Future Enhancements

### Planned Integrations
- **GitHub Copilot Agent**: Agent configuration files (`.agent.md`) using these prompts
- **Accessibility Audit Tool**: Prompts updated with audit finding templates
- **Case Filing Wizard**: Multi-step agent using both prompts sequentially
- **Evidence Recommendation Engine**: Dynamic evidence gap suggestions based on jurisdiction

### Extensibility
- Add state-specific procedure prompts (Maharashtra, Gujarat, Karnataka, etc.)
- Create specialized prompts for specific building types (residential, commercial, public facilities)
- Develop remedy-tracking prompts for post-filing compliance monitoring
- Build legal reference augmentation (embedding statute text for context)

---

## Contributing Updates

### To Update Prompts
1. Verify changes against current legal sources (government websites, official legal databases)
2. Test updated prompts against existing case material (cases/ folder)
3. Update legal citations in `mandates/legal-mandates-sources.md`
4. Document changes with date and verification status
5. Submit via GitHub issue or PR with legal source references

### To Add New Prompts
- Follow the structure and format of existing prompts
- Include legal framework, process steps, output structure, constraints, and examples
- Link to relevant mandates in `mandates/` folder
- Document jurisdiction scope and limitations
- Create corresponding usage documentation

---

## Contact and Feedback

For questions, feedback, or contributions related to these prompts:

1. **Documentation issues**: Open GitHub issue with prompt reference and clarification needed
2. **Legal accuracy concerns**: Submit with statute reference and current version link
3. **Integration requests**: Describe desired agent or workflow integration
4. **Example contributions**: Share case formulation or verification workflows

See [CONTRIBUTING.md](../CONTRIBUTING.md) for contribution guidelines.
