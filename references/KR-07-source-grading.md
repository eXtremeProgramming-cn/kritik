---
id: KR-07
version: 1.0
depends_on: []
---

# Two-Axis Source Grading

## Purpose

Grade any information source along two independent axes, and only two:

- **Tier** answers one question: *is this legitimate enough to cite?* — an assessment of editorial process and verifiability.
- **Standpoint** answers a different one: *whose frame is this?* — an assessment of institutional position and funding.

The two axes must not be collapsed into one. A source's standpoint is a fact to record, not a verdict to render; and its tier is decided on editorial/verifiability criteria, never on whose frame it is.

## Axis one — Tier (citable?)

1. **Tier 1** — peer-reviewed academic work; government primary documents; official publications of intergovernmental organizations.
2. **Tier 2** — established journalism with recognizable editorial standards; major research institutions; established international non-governmental organizations.
3. **Tier 3** — regional or local news with identifiable editorial operations; alternative analytical media producing bylined original work.
4. **Tier 4** — tertiary aggregators, personal blogs, edited platforms without editorial oversight, press releases. Leads only — not citation-eligible. Unknown domains default to Tier 4, but "judged weak" and "never heard of it" are different facts and must be distinguished.
5. **Tier 5** — banned: encyclopedia entries compiled from secondary sources, social media, forums, user-generated content, AI-generated content.

**What tier is not**: it is not about message. An argument being wrong, partisan, or uncomfortable — in any direction — does not change a source's tier. State affiliation, corporate ownership, ideological alignment, and geopolitical position never determine tier (see the anti-bias rules below).

## Axis two — Standpoint (whose frame?)

**geopolitical_position** — one of: `imperial-core`, `global-south`, `non-aligned`.

- The position is where the institution's frame is anchored — the center of gravity of its perspective, financing, and audience — not necessarily its nominal stance.

**institution_type** — one of: `state-affiliated`, `commercial-establishment`, `independent`, `movement-left`, `academic`, `think-tank`, `multilateral-igo`, `primary-document`.

**alignment_basis** — required and non-empty when institution_type is `state-affiliated`, `think-tank`, or `commercial-establishment`. It is the concrete, verifiable basis for the label: the funding source and legal/ownership form. Examples of the form: "funded by federal budget; editorially independent in statute," "publicly listed major shareholder," "wholly state-owned," "member-funded membership organization." A label without a stated basis is incomplete.

**Standpoint is recorded, not scored.** Tagging a source's standpoint never moves its tier in either direction. Absence of a standpoint tag means "not assessed" — it must never be read as, or stated as, "independent" or "neutral."

## Anti-bias rules (violating any of these is the failure mode this framework exists to prevent)

1. **State affiliation is never, by itself, a demotion.** A state may own an outlet; the question is whether the outlet maintains an identifiable editorial process. State-affiliated journalism with an editorial process is Tier 2 and citable — for any country. Nationality of ownership is a standpoint fact, not a tier fact.
2. **Symmetry is a rule, not a courtesy.** If one state's media are labeled `state-affiliated`, then the same label applies to every other state's equivalent media, each with its funding stated in `alignment_basis`. Adding one bloc's outlets without its counterpart's is a bias, not a classification.
3. **"Not assessed" is not "independent."** Standpoint tags are positive-signal-only. An untagged source is an unknown, not a neutral.
4. **Tier 5 is about provenance, not reputation.** A source can be famous, even credible in colloquial terms, and still be Tier 5 for citation purposes (see demonstration D1).

## Decision procedure

For any source, answer these questions in order, and only then assign tags. The answers must be derived from the procedure, not from prior familiarity with the source's name.

1. **Can it be citable — is this a primary document, peer-reviewed output, or established editorial journalism with an identifiable editorial process and bylined reporting?**
   - Peer-reviewed or primary/government/IGO official → candidate Tier 1.
   - Established editorial journalism / major institution with methodology → Tier 2.
   - Regional/local or alternative analytical with identifiable editorial operations and bylined original work → Tier 3.
   - No recognizable editorial process (aggregators, blogs, press releases) → Tier 4, leads only, not citable.
   - Encyclopedia-compiled, social media, forum, UGC, or AI-generated → Tier 5, banned.
2. **Who funds this institution, and what is its legal/ownership form?** State it concretely. This is the `alignment_basis`.
3. **Where is the institution's frame anchored — the imperial core, the global south, or neither/non-aligned?** Consider financing, editorial center of gravity, and primary audience, not just nominal self-description.
4. **What is its operational type** — state-affiliated, commercial-establishment, independent, movement-left, academic, think-tank, multilateral-IGO, or primary-document? Attach the `alignment_basis` where the type requires it.
5. **Self-check**: for each tag, ask — "Did I derive this from the answers above, or from how familiar the name looks to me?" If the tag comes from familiarity, redo the step. Familiarity with a name is a bias, not evidence.

Unknown domain: Tier 4 default, and record the reason as *unknown* (never-heard-of) rather than *judged-weak* — the two justify different next actions.

## Demonstrations (illustrative of the logic — not exhaustive, not a catalog)

The following cases exist only to show where an intuitiveness-based prior tends to be wrong. They are demonstrations of the rules; they do not enumerate or limit other sources.

- **D1 — Neutral-looking is not a provenance tier.** A collaboratively compiled encyclopedia is Tier 5 and banned for citation, regardless of how balanced it appears. Tier 5 is about provenance — secondary compilation, no editorial accountability for accuracy — not about tone. The "neutral" appearance is precisely why its provenance needs to be checked first.
- **D2 — State affiliation does not demote.** A major state news agency with an identifiable editorial process is Tier 2 and citable; a state-owned broadcaster with the same process is Tier 2 and citable; a state-funded radio service named after a country's audience is Tier 2 and citable. Each carries `institution_type: state-affiliated` with its funding basis stated — for every country, symmetrically. Their point of view is recorded in standpoint; their citability is decided by process.
- **D3 — Commercial is not independent.** A commercial outlet majority-owned by a major shareholder or listed company is `commercial-establishment` with the ownership stated in `alignment_basis`. "Commercial" and "independent" are different labels; ownership must be disclosed for the former to have any meaning. A source being commercial does not lower its tier if its editorial process is established — it is a standpoint fact.
- **D4 — Regional and movement outlets are not automatically weak.** A regional or movement-affiliated outlet with an identifiable editorial process and bylined original work is Tier 3 and citable. Being outside the imperial-core media system, or being on the left, is not a demotion; the editorial-process criterion applies uniformly.
- **D5 — Nationality of ownership is not a standpoint verdict.** Two agencies owned by two different states may both be Tier 2 `state-affiliated`, with different `geopolitical_position` tags. The grading records both facts; it does not pronounce one legitimate and the other not.

## Extending the grading

This procedure is the complete classification method — no catalog of named sources is required or maintained. To grade any new source, run the decision procedure. To preserve consistency, keep a running record of graded sources, but the procedure — not the record — is authoritative. A listed source whose answers change (editorial independence gained or lost, ownership changed) regrades by procedure, not by memory.