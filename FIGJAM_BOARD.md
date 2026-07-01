# FigJam Board — Developer Reference

**Purpose:** Copy-paste this into a FigJam board so the dev team can build without reading the full PRD.
**Rule:** Every claim here is a compressed version of something in `../PRD.md`. When in doubt, PRD wins.
**How to use:** Each `## FRAME` below = one section on your FigJam board. Sticky-note style, one idea per line.

---

## SUGGESTED BOARD LAYOUT

```
+----------------------+----------------------+----------------------+
|  FRAME 1: SUMMARY    |  FRAME 2: NORTH STAR |  FRAME 3: STATUS     |
+----------------------+----------------------+----------------------+
|          FRAME 4: USER JOURNEY (WIDE — spans board)                |
+----------------------+----------------------+----------------------+
|          FRAME 14: SYSTEM ARCHITECTURE (WIDE — spans board)        |
+----------------------+----------------------+----------------------+
|  FRAME 15: BACKEND   |  FRAME 16: FRONTEND  |  FRAME 17: AUTH FLOW |
|      MODULE MAP      |      APP STRUCTURE   |                      |
+----------------------+----------------------+----------------------+
|          FRAME 18: REQUEST LIFECYCLE (WIDE — spans board)          |
+----------------------+----------------------+----------------------+
|  FRAME 19: DEPLOY    |          FRAME 20: FAILURE / FALLBACK GRAPH |
|  & STORAGE           |                                             |
+----------------------+----------------------+----------------------+
|  FRAME 5: PAGE MAP   |  FRAME 6: TECH STACK |  FRAME 7: AUTH/ROLES |
+----------------------+----------------------+----------------------+
|                FRAME 8: RACI OWNERSHIP                             |
+----------------------+----------------------+----------------------+
|                FRAME 9: PHASE TIMELINE (swimlane)                  |
+----------------------+----------------------+----------------------+
|  FRAME 10: DoD       |  FRAME 11: NON-GOALS |  FRAME 12: OPEN Qs   |
+----------------------+----------------------+----------------------+
|          FRAME 13: REFERENCES + LINKS                              |
+----------------------+----------------------+----------------------+
```

---

## FRAME 1 — SUMMARY

Sticky notes (color: yellow):

- **Product:** AI-Powered Customs Declaration Automation
- **For:** Cikarang Dryport authorized staff (internal tool, not public web)
- **Job:** Read CI + PL + BoL → Validate → Explain risk → Submit to CEISA
- **Stage:** Semifinal MVP
- **Deliverable:** Working dashboard + demo video
- **Team:** 3 beginner IT students
- **Timeline:** 11–14 working days
- **Ship rule:** Working > perfect. Simulate what we can't build.

---

## FRAME 2 — NORTH STAR METRIC

Sticky notes (color: green):

- **Judge test:** Can a judge upload 3 docs and see a validated risk score with SHAP explanation in under 90 seconds?
- **Business test:** Manual PIB filing today = 15 min/doc. Our system = under 60 sec/doc.
- **Trust test:** Every risk score comes with a WHY (SHAP top-5 features).
- **Honesty test:** CEISA submission is labeled "Simulated (Demo Mode)".

---

## FRAME 3 — CURRENT STATUS

Sticky notes (color: orange):

- **Backend pipeline:** exists but uses hardcoded mock at `src/main.py:50` — MUST FIX
- **Validation engine:** built (rule + cross-doc + XGBoost + SHAP)
- **API layer:** exists at `src/validation/api.py` — needs 4 more endpoints
- **Frontend:** NOT started
- **Auth:** NOT started
- **Landing page:** NOT started
- **PRD:** locked (v2, Tier 2+)

---

## FRAME 4 — USER JOURNEY (happy path, single row)

Arrows connecting sticky notes left → right:

```
[Landing page]
      │
      ▼ click "Log in"
[Login page — demo creds shown]
      │
      ▼ enter clerk@cikarangdryport.id / demo123
[Dashboard Home — welcome + quick stats + "Start New" CTA]
      │
      ▼ click "Start New Declaration"
[New Declaration — 3 upload slots (CI + PL + BoL)]
      │
      ▼ drop 3 files → click "Start Extraction"
[Loading — 5-stage progress: Docling → PaddleOCR → LayoutLMv3 → TableTransformer → Ollama]
      │
      ▼ pipeline completes
[Results — 3 tabs with confidence-colored fields]
      │
      ▼ scroll down
[Validation panel — warnings grouped by severity]
      │
      ▼ scroll down
[Risk panel — gauge + SHAP waterfall]
      │
      ▼ scroll down
[Impact strip — Manual 15:00 vs Ours 0:47 + Cost saved card]
      │
      ▼ click "Generate CEISA Submission"
[Confirm modal — "This is a demo simulation. Continue?"]
      │
      ▼ click Submit
[Success modal — JSON payload + simulated PIB-2026-XXXXXX RECEIVED]
      │
      ▼ close modal, click sidebar "History"
[History page — the just-submitted declaration appears at top]
```

Sticky note callouts (color: pink) attached to journey:

- Between Login and Dashboard: **role-aware nav — Officer sees no "New Declaration"**
- On Loading: **~30–60s CPU / <10s GPU — use cached fixture if slow**
- On Risk panel: **THIS IS THE WOW MOMENT — SHAP must land perfectly**
- On Confirm modal: **honesty label is non-negotiable (FR-5.5)**

---

## FRAME 5 — PAGE MAP (grid, 10 cards)

Each card = one page/surface. Color by owner: blue = Frontend, gray = shared.

**Public (unauthenticated):**

| Card | FR ref | Notes |
|---|---|---|
| **Landing** | FR-8.x | 6 sections, bilingual EN+ID. See `LANDING_COPY.md` |
| **Login** | FR-9.6 | Demo creds visible; NextAuth Credentials |
| **404 / Error** | — | Simple; branded |

**Authenticated:**

| Card | FR ref | Notes |
|---|---|---|
| **Dashboard Home** | FR-11.x | Welcome + 4 stat cards + recent 5 + primary CTA |
| **New Declaration** | FR-1.x → FR-7.x | The whole workflow: upload → results → submit |
| **History** | FR-12.x | Table, filters, click row → read-only detail |
| **Settings / Profile** | FR-13.x | Name/email/role + sign out |
| **Help / About** | FR-14.x | In-app glossary + FAQ |

**Modals (shared):**

| Card | FR ref | Notes |
|---|---|---|
| **Share modal** | FR-15.x | Copy tokenized URL |
| **Confirm CEISA** | FR-16.x | "This is a demo simulation" text |

---

## FRAME 6 — TECH STACK (grouped columns)

**Frontend column** (color: blue):

- Next.js 14 (App Router)
- TypeScript (`strict: false` allowed now, MUST be `true` before submission)
- Tailwind CSS
- shadcn/ui (install: button, card, input, dialog, alert, badge, tabs, progress, sonner)
- Recharts (radial gauge + SHAP waterfall)
- Framer Motion (landing scroll animations only)
- pnpm

**Backend column** (color: green):

- Python 3.11+
- FastAPI (existing at `src/validation/api.py`)
- Pydantic v2 (existing schema)
- PaddleOCR
- Docling
- LayoutLMv3 (`microsoft/layoutlmv3-base`)
- TableTransformer (`microsoft/table-transformer-structure-recognition`)
- Ollama (local LLM)
- XGBoost + SHAP
- bcryptjs (for NextAuth password hashing) — via Node side, but seed users in DB

**Auth column** (color: purple):

- NextAuth.js v5 (Auth.js)
- Provider: Credentials only
- Database: SQLite (via Prisma)
- Sessions: JWT
- Middleware: `middleware.ts` for `/dashboard/*` routes

**Infrastructure column** (color: gray):

- Docker (Dockerfile exists)
- Localhost demo (no cloud)
- HuggingFace cache: `~/.cache/huggingface/`
- Ollama daemon: `localhost:11434`

Reference: `../docs/TECH_STACK.md` has full rationale + rejected alternatives.

---

## FRAME 7 — AUTH & ROLES (compact card)

Sticky notes (color: purple):

- **Library:** NextAuth.js v5 (do NOT hand-roll)
- **Seed users:** create at first server start via `prisma db seed`
- **Demo creds displayed on login page** — no fumbling in front of judges
- **Two roles only:** `clerk`, `officer`

**Role capability grid:**

| Feature | Clerk | Officer |
|---|---|---|
| See landing | ✓ | ✓ |
| Log in | ✓ | ✓ |
| Dashboard Home | ✓ | ✓ |
| **New Declaration flow** | ✓ | ✗ (hidden in sidebar) |
| See own history | ✓ | ✓ (org-wide) |
| Read-only review of any decl | — | ✓ |
| Sign out | ✓ | ✓ |

**Seeded accounts:**
- `clerk@cikarangdryport.id` / `demo123` → role: `clerk`
- `officer@cikarangdryport.id` / `demo123` → role: `officer`

Out of scope: forgot password, MFA, OAuth, self-signup.

---

## FRAME 8 — RACI OWNERSHIP (single grid)

Column colors: Radit = blue, Backend teammate = green, Third teammate = orange.

| Area | Radit | Backend | Third |
|---|---|---|---|
| Frontend (Next.js, shadcn/ui, Recharts) | **R/A** | I | C |
| Landing page + copy | **R** | I | A (proofread ID) |
| Auth (NextAuth + Prisma + seed) | **R/A** | C | I |
| Backend endpoints (FastAPI) | C | **R/A** | C |
| OCR → Schema mapping (Phase 1A) | C | **R/A** | C |
| LayoutLMv3 + TableTransformer | I | **R/A** | C |
| HS Code Predictor (FR-6) | C | **R** | A |
| Demo dataset (real CI/PL/BoL) | C | C | **R/A** |
| `rules.json` (Permendag) | I | C | **R/A** |
| Docs upkeep | C | C | **R/A** |
| Demo rehearsal | C | C | **R/A** |

**Rule:** every row has exactly one **A** (Accountable). No orphan work.

Reference: `../PRD.md` §14.1 for full RACI.

---

## FRAME 9 — PHASE TIMELINE (swimlane)

Draw as horizontal swimlanes. Backend on top, Frontend below, Both at bottom.

**Days 1–2:**

| Backend | Frontend | Both |
|---|---|---|
| Phase 1A: Wire OCR → Schema (fix `main.py:50`) | Phase 3: Scaffold Next.js + shadcn/ui | Phase 0: Lock API contract + commit fixtures |

**Days 2–4:**

| Backend | Frontend | Both |
|---|---|---|
| Phase 1B: Add LayoutLMv3 + TableTransformer | Phase 4A: Auth + app shell + landing | — |
| Phase 2: FastAPI endpoints matching contract | — | — |

**Days 4–7:**

| Backend | Frontend | Both |
|---|---|---|
| — | Phase 4B: Core declaration workflow | — |
| — | Phase 4C: History + Settings + Help + Share modal | — |

**Days 7–10:**

| Both |
|---|
| Phase 5: Integration & polish |
| Test with `images/4.png` + synthetic docs |
| Pre-compute canonical demo cache |

**Days 10–11+:**

| Both |
|---|
| Phase 6: Demo rehearsal |
| Record backup demo video |

**Critical path:** Phase 1A → Phase 1B → Phase 2 → Phase 5.
**If slipping:** apply R14 cut list — drop Settings theme toggle first, then Help FAQ depth, then Share modal polish, then landing bilingual copy.

---

## FRAME 10 — DEFINITION OF DONE (checklist)

Sticky notes (color: green when done):

- [ ] Frontend calls each backend endpoint without console errors
- [ ] 3 sample docs from `./images/` produce believable end-to-end results
- [ ] UI handles gracefully: missing input, OCR failure, validation error
- [ ] Total user-perceived runtime ≤ 90s (OR cached mode active)
- [ ] Login as both roles works; sign-out clears session
- [ ] Sidebar collapse state persists in localStorage
- [ ] Landing renders correctly at 1920×1080
- [ ] `README.md` in repo root gets a fresh dev started in ≤ 5 commands
- [ ] All 7 open questions answered
- [ ] Canonical demo run pre-cached in `fixtures/canonical_run.json`
- [ ] Demo rehearsed end-to-end at least twice on the actual demo machine

---

## FRAME 11 — NON-GOALS (do NOT build these)

Sticky notes (color: red):

- Real Host-to-Host to production CEISA 4.0
- Forgot password / password reset self-service
- MFA / 2FA
- OAuth (Google, GitHub)
- Multi-tenant / org signup
- Mobile responsive layouts
- Full i18n framework (landing bilingual only)
- Notifications feed beyond toasts
- Federated learning across ports
- PostgreSQL / production DB
- Public deployment (localhost only)
- Custom domain / SSL

**If a teammate starts building one, stop them.**

Reference: `../PRD.md` §10.

---

## FRAME 12 — OPEN QUESTIONS (parking lot)

Sticky notes (color: pink) — every one must be answered before or during Phase 0.

- **Q1** Who is the backend teammate? Have they read the PRD? *(Radit · Day 0)*
- **Q2** Do we have at least one real CI/PL/BoL set with consistent data? *(Backend · Day 1)*
- **Q3** What CEISA-compliant JSON schema are we targeting? *(Backend · Phase 2)*
- **Q4** Is there a GPU on the demo machine, or CPU-only? *(Radit · Day 0)*
- **Q5** If CPU-only, do we accept pre-computed cached demo runs? *(Radit · Day 0)*
- **Q6** Daily PIB volume assumption for Cost Saved calculator? *(Team · Phase 4)*
- **Q7** Indonesian labor cost (IDR/hour) — need sourceable number *(Team · Phase 4)*
- **Q8** Native Bahasa speaker to proofread landing copy *(Team · Phase 4A)*
- **Q9** Team names + university for landing footer *(Radit · Phase 4A)*
- **Q10** Logo / wordmark *(Team · Phase 4A)*
- **Q11 [BLOCKER]** Product name — locks nav, tab title, DB names, footer *(Team · Day 0)*

---

## FRAME 13 — REFERENCES (links / docs)

Sticky notes (color: gray):

- **PRD:** `../PRD.md`
- **Docs index:** `../docs/README.md`
- **Glossary:** `../docs/GLOSSARY.md`
- **Tech stack (rationale):** `../docs/TECH_STACK.md`
- **Architecture:** `../docs/ARCHITECTURE.md`
- **User stories:** `../docs/USER_STORIES.md`
- **API contract:** `../docs/API_CONTRACT.md`
- **Design system:** `../docs/DESIGN_SYSTEM.md`
- **Landing copy (bilingual):** `../docs/LANDING_COPY.md`
- **Sources & competitor analysis:** `../docs/REFERENCES.md`
- **Decision log (ADRs):** `../docs/DECISIONS.md`

External:
- Jarvis (competitor / structural reference): https://jar-vis.com/en
- NextAuth v5 docs: https://authjs.dev/
- shadcn/ui docs: https://ui.shadcn.com/docs
- HuggingFace LayoutLMv3: https://huggingface.co/microsoft/layoutlmv3-base

---

## FRAME 14 — SYSTEM ARCHITECTURE (holistic view)

The single "big picture" diagram. Every box a real component, every arrow a real call.

```
┌───────────────────────────────────────────────────────────────────────────────┐
│                              USER'S BROWSER                                   │
│                                                                               │
│  ┌─────────────────────────────────────────────────────────────────────────┐  │
│  │                    NEXT.JS 14 DASHBOARD (localhost:3000)                │  │
│  │                                                                         │  │
│  │  App Router pages:                                                      │  │
│  │    /                       → Landing                                    │  │
│  │    /login                  → Login (NextAuth Credentials)              │  │
│  │    /dashboard              → Home                                       │  │
│  │    /dashboard/new          → New Declaration workflow                   │  │
│  │    /dashboard/history      → History list                               │  │
│  │    /dashboard/history/:id  → Read-only detail                           │  │
│  │    /dashboard/settings     → Profile                                    │  │
│  │    /dashboard/help         → Glossary + FAQ                             │  │
│  │                                                                         │  │
│  │  Middleware: `middleware.ts` guards /dashboard/*                        │  │
│  │  Session: JWT cookie (NextAuth)                                         │  │
│  │  State: React Server Components + zustand for client state             │  │
│  │  UI kit: shadcn/ui + Tailwind + Recharts + Framer Motion               │  │
│  └────────────────────────────┬────────────────────────────────────────────┘  │
└───────────────────────────────┼───────────────────────────────────────────────┘
                                │  HTTPS/localhost fetch
                                │  (multipart or JSON)
                                ▼
┌───────────────────────────────────────────────────────────────────────────────┐
│                       AUTH LAYER (Node runtime, Next.js)                      │
│                                                                               │
│  NextAuth.js v5 (Credentials provider)                                        │
│  ┌─────────────────┐  ┌──────────────────┐  ┌──────────────────────────┐    │
│  │ /api/auth/login │→ │ verify bcrypt vs │→ │ SQLite (via Prisma)     │    │
│  │ /api/auth/logout│  │ Prisma `User`    │  │ ~/data.db               │    │
│  │ /api/auth/[…]   │  └──────────────────┘  │ Table: User(id, email,  │    │
│  └─────────────────┘         │              │        hashedPwd, role) │    │
│                              ▼              └──────────────────────────┘    │
│                       JWT cookie set                                          │
└───────────────────────────────────────────────────────────────────────────────┘
                                │
                                │  proxy: /api/backend/* → localhost:8000
                                │  (Next.js rewrite; adds Authorization: Bearer <jwt>)
                                ▼
┌───────────────────────────────────────────────────────────────────────────────┐
│              BACKEND — FASTAPI (Python, uvicorn, localhost:8000)              │
│                                                                               │
│  Routes:                                                                      │
│   • GET  /api/health                                                          │
│   • POST /api/extract          (multipart)                                    │
│   • POST /api/validate                                                        │
│   • POST /api/predict-hs-code                                                 │
│   • POST /api/submit-ceisa                                                    │
│                                                                               │
│  CORS: allow http://localhost:3000                                            │
│  Modes:  ?mode=fixture (returns canned fixtures)                              │
│          ?cached=true  (returns canonical demo run)                           │
└──┬──────────────────────┬────────────────────────────┬──────────────────────┘
   │                      │                            │
   │ /api/extract         │ /api/validate              │ /api/submit-ceisa
   ▼                      ▼                            ▼
┌──────────────────┐  ┌────────────────────────┐  ┌─────────────────────────┐
│ OCR + LAYOUT     │  │ VALIDATION INTELLIGENCE│  │ CEISA MAPPER (new)      │
│ PIPELINE         │  │                        │  │                         │
│                  │  │ rule_engine.py         │  │ ExtractedDocuments      │
│ docling_module   │  │   ← rules.json         │  │        │                │
│      ↓           │  │                        │  │        ▼                │
│ paddle_module    │  │ cross_document.py      │  │ ceisa_payload (JSON)    │
│      ↓           │  │                        │  │        │                │
│ layoutlm_module  │  │ ml_scoring.py          │  │        ▼                │
│      ↓           │  │   ← xgboost_risk_      │  │ Fake ack:               │
│ table_transformer│  │     model.json         │  │  PIB-2026-XXXXXX        │
│      ↓           │  │   + SHAP               │  │  status: RECEIVED       │
│ ollama_module    │  │                        │  │  simulated: true        │
│      ↓           │  │ confidence_engine.py   │  │                         │
│ ExtractedDocs    │  │   → ValidationResult   │  │                         │
└─────┬────────────┘  └─────┬──────────────────┘  └─────────────────────────┘
      │                     │
      │                     │
      ▼                     ▼
┌──────────────────┐  ┌────────────────────────┐
│ EXTERNAL DEPS    │  │ ML ARTIFACTS (disk)    │
│                  │  │                        │
│ Ollama daemon    │  │ xgboost_risk_model.json│
│ localhost:11434  │  │ rules.json             │
│  (Llama 3.2)     │  │ synthetic_data.csv     │
│                  │  │                        │
│ HuggingFace Hub  │  │ HuggingFace cache:     │
│ (first run only) │  │ ~/.cache/huggingface/  │
│                  │  │   layoutlmv3-base      │
│                  │  │   table-transformer    │
└──────────────────┘  └────────────────────────┘
```

**Legend:**
- Solid boxes = code we own
- Arrows = synchronous call (blocking)
- All communication is HTTP over localhost — no message queue, no cache layer, no cloud
- Ollama is the only external process not spawned by our code

Reference: `../docs/ARCHITECTURE.md` for narrative detail.

---

## FRAME 15 — BACKEND MODULE MAP (file tree + responsibility)

Show as a tree. Each node = one file. Sticky notes attached to each node explain the module's job in one line.

```
src/
├── main.py                                [Entry point — CLI pipeline runner]
├── module/
│   ├── docling_module.py                  [Stage 1: Doc → structured markdown/JSON]
│   ├── paddle_module.py                   [Stage 2: Image → text + bboxes + conf]
│   ├── layoutlm_module.py       [NEW]     [Stage 3: Semantic role classification]
│   ├── table_transformer_module.py [NEW]  [Stage 4: Line-item table extraction]
│   └── ollama_module.py                   [Stage 5: Enriched → ExtractedDocuments]
│
├── validation/
│   ├── api.py                             [FastAPI routes + CORS + error handling]
│   ├── schema.py                          [Pydantic: ExtractedDocuments etc.]
│   ├── rule_engine.py                     [Permendag rules (loads rules.json)]
│   ├── rules.json                         [Data: rule definitions]
│   ├── cross_document.py                  [CI/PL/BoL reconciliation]
│   ├── ml_scoring.py                      [XGBoost + SHAP]
│   ├── xgboost_risk_model.json            [Data: trained model artifact]
│   ├── confidence_engine.py               [Orchestrator → ValidationResult]
│   ├── ceisa_mapper.py          [NEW]     [ExtractedDocs → CEISA JSON + fake ack]
│   ├── hs_predictor.py          [NEW]     [Ollama HS code suggestion]
│   ├── synthetic_data.py                  [Generate training data]
│   ├── train_model.py                     [Train XGBoost]
│   └── test_engine.py                     [Backend tests]
│
└── scripts/                     [NEW]
    ├── download_models.py                 [Pre-fetch HuggingFace models]
    └── verify_models.py                   [Offline load check for demo day]
```

**Sticky note callouts:**

- `main.py:50` still has HARDCODED MOCK — Phase 1A must fix this
- `ceisa_mapper.py` and `hs_predictor.py` are Phase 1B/2 new modules
- `test_engine.py` exists but coverage is low — Phase 1A adds parser tests
- `rules.json` is the single source of truth for Permendag — Third teammate owns

---

## FRAME 16 — FRONTEND APP STRUCTURE (Next.js tree)

Show as a tree. Sticky notes on each folder explain scope.

```
dashboard/
├── app/                              [Next.js 14 App Router root]
│   ├── layout.tsx                    [Root layout: <html>, fonts, providers]
│   ├── page.tsx                      [Landing page (public)]
│   ├── login/
│   │   └── page.tsx                  [Login page (public)]
│   ├── dashboard/                    [Auth-protected route group]
│   │   ├── layout.tsx                [Dashboard shell: navbar + sidebar]
│   │   ├── page.tsx                  [Dashboard Home]
│   │   ├── new/
│   │   │   └── page.tsx              [New Declaration workflow (Clerk only)]
│   │   ├── history/
│   │   │   ├── page.tsx              [History list]
│   │   │   └── [id]/page.tsx         [Read-only detail]
│   │   ├── settings/page.tsx         [Profile / sign out]
│   │   └── help/page.tsx             [Glossary + FAQ]
│   └── api/
│       ├── auth/[...nextauth]/route.ts   [NextAuth handler]
│       └── backend/[...path]/route.ts    [Proxy to FastAPI]
│
├── components/                        [Reusable UI]
│   ├── ui/                            [shadcn/ui primitives — auto-generated]
│   ├── landing/
│   │   ├── Hero.tsx                   [FR-8.2]
│   │   ├── ProcessSteps.tsx           [FR-8.4]
│   │   ├── AutonomyLevels.tsx         [FR-8.5]
│   │   └── BeforeAfter.tsx            [FR-8.6]
│   ├── shell/
│   │   ├── Navbar.tsx                 [FR-10.1]
│   │   └── Sidebar.tsx                [FR-10.2]
│   └── declaration/
│       ├── UploadZone.tsx             [FR-1.x]
│       ├── ExtractionProgress.tsx     [FR-2.4]
│       ├── ConfidenceField.tsx        [FR-2.3]
│       ├── ValidationPanel.tsx        [FR-3.x]
│       ├── RiskGauge.tsx              [FR-4.3 radial]
│       ├── ShapWaterfall.tsx          [FR-4.3 bar]
│       ├── HsCodeSuggestion.tsx       [FR-6.x]
│       ├── ImpactStrip.tsx            [FR-7.x]
│       ├── ConfirmCeisaModal.tsx      [FR-16.x]
│       ├── CeisaSubmitModal.tsx       [FR-5.x]
│       └── ShareModal.tsx             [FR-15.x]
│
├── lib/
│   ├── api.ts                         [Typed fetch wrappers → FastAPI]
│   ├── auth.ts                        [NextAuth config]
│   ├── prisma.ts                      [Prisma client singleton]
│   ├── i18n.ts                        [Landing bilingual copy loader]
│   └── utils.ts                       [cn(), formatters, etc.]
│
├── prisma/
│   ├── schema.prisma                  [User + Role tables]
│   ├── seed.ts                        [Seed clerk + officer accounts]
│   └── data.db                        [SQLite (gitignored)]
│
├── fixtures/                          [Frontend uses these while BE catches up]
│   ├── extract.json
│   ├── validate.json
│   ├── predict-hs-code.json
│   ├── submit-ceisa.json
│   └── canonical_run.json             [Pre-computed demo run]
│
├── middleware.ts                      [Route protection]
├── next.config.mjs                    [Rewrite /api/backend/* → localhost:8000]
├── tailwind.config.ts                 [Uses design-system tokens]
├── components.json                    [shadcn/ui config]
└── package.json
```

**Sticky note callouts:**

- Role-gated: `/dashboard/new` middleware check rejects officers with 403
- `components/` grouped by domain (landing / shell / declaration) not by primitive
- `fixtures/` unblocks frontend dev while backend catches up (Phase 3–4 use these)
- `middleware.ts` is the auth gate — see FRAME 17

---

## FRAME 17 — AUTH FLOW (sequence diagram)

Draw as a swimlane sequence: User → Browser → NextAuth → Prisma → SQLite. Time flows down.

```
User          Browser         Next.js Middleware      NextAuth       Prisma          SQLite
 │              │                    │                   │              │              │
 │─visit /─────>│                    │                   │              │              │
 │              │─GET /dashboard────>│                   │              │              │
 │              │                    │─check JWT cookie──┤              │              │
 │              │                    │       (missing)   │              │              │
 │              │<─302 /login────────┤                   │              │              │
 │              │                    │                   │              │              │
 │─fill form───>│                    │                   │              │              │
 │              │─POST /api/auth/────────────────────────>│              │              │
 │              │      callback/credentials              │              │              │
 │              │                    │                   │─findUnique──>│              │
 │              │                    │                   │              │─SELECT──────>│
 │              │                    │                   │              │<─row─────────┤
 │              │                    │                   │<─User row────┤              │
 │              │                    │                   │─bcrypt.      │              │
 │              │                    │                   │  compare()   │              │
 │              │                    │                   │  matches     │              │
 │              │<─Set-Cookie: JWT───────────────────────┤              │              │
 │              │<─302 /dashboard────┤                   │              │              │
 │              │                    │                   │              │              │
 │              │─GET /dashboard────>│                   │              │              │
 │              │                    │─check JWT─────────┤              │              │
 │              │                    │  valid,           │              │              │
 │              │                    │  role in payload  │              │              │
 │              │<─render HTML───────┤                   │              │              │
 │              │                    │                   │              │              │
 │─sign out───>│                    │                   │              │              │
 │              │─POST /api/auth/─────────────────────────>│              │              │
 │              │      signout                            │              │              │
 │              │<─Set-Cookie: expire────────────────────┤              │              │
 │              │<─302 / (landing)───┤                   │              │              │
```

**Key contract:**
- JWT payload contains `{ sub, email, role, name, exp }`
- `role` determines sidebar items (FR-10.5) and route protection
- Session TTL: 7 days (default NextAuth); no refresh flow for MVP
- On expiry: middleware redirects to `/login` with `?callbackUrl=<orig>`

---

## FRAME 18 — REQUEST LIFECYCLE (end-to-end for the main workflow)

Follow one declaration from click to ack. Draw as horizontal lanes: FE → NextAuth proxy → FastAPI → Pipeline → Response.

```
[0.0s]  User drops 3 files, clicks "Start Extraction"
        │
[0.1s]  Browser: fetch('/api/backend/extract', { method: POST, body: FormData })
        │
[0.2s]  Next.js API route /api/backend/[...path]/route.ts:
          - reads JWT from cookie
          - verifies session
          - forwards multipart to http://localhost:8000/api/extract
          - adds header: X-User-Role: clerk
        │
[0.3s]  FastAPI:
          - CORS check (OK)
          - saves files to /tmp/uploads/{extraction_id}/
          - kicks off pipeline
        │
[0.3–47s]  Pipeline (sync, per document, sequential):
              Docling (~2s)
              PaddleOCR (~5s)
              LayoutLMv3 (~8s CPU / ~1s GPU)
              TableTransformer (~10s CPU / ~1s GPU)
              Ollama (~10s)
              → ExtractedDocuments
        │
[47.5s] FastAPI returns 200 + ExtractedDocuments JSON
        │
[47.6s] Next.js API route relays response to browser
        │
[47.7s] Frontend renders results tabs
        │
[47.8s] Frontend auto-fires: fetch('/api/backend/validate', { … })
        │
[48.5s] Pipeline: rule engine + cross-doc + XGBoost + SHAP → ValidationResult
        │
[48.7s] Frontend renders Validation Panel + Risk Gauge + SHAP Waterfall + Impact Strip
        │
[???]   User inspects, clicks "Generate CEISA Submission"
        │
[+0.1s] Confirm modal opens (client-side only, no API call)
        │
[+0.5s] User clicks Confirm → fetch('/api/backend/submit-ceisa', { validation_id })
        │
[+0.6s] FastAPI: ceisa_mapper builds JSON, generates fake PIB, returns
        │
[+0.7s] Frontend renders success modal with JSON viewer + fake ack card
        │
DONE
```

**Notes:**
- Total time budget: ≤ 90s user-perceived (per DoD)
- If any single stage > 90s, fall back to cached mode (`?cached=true`)
- Sidebar navigation updates optimistically after CEISA submission (adds row to History)

---

## FRAME 19 — DEPLOYMENT & STORAGE (localhost topology)

Show as a machine outline with 4 processes and 4 storage regions.

```
┌─ Demo machine (single laptop) ────────────────────────────────────────────────┐
│                                                                               │
│  Process 1: Next.js dev server                                                │
│    Command:  pnpm dev                                                         │
│    Port:     3000                                                             │
│    Runtime:  Node 20+                                                         │
│    Env:      NEXTAUTH_SECRET, DATABASE_URL=file:./data.db                     │
│                                                                               │
│  Process 2: FastAPI (uvicorn)                                                 │
│    Command:  uvicorn src.validation.api:app --host 0.0.0.0 --port 8000        │
│    Port:     8000                                                             │
│    Runtime:  Python 3.11                                                      │
│    Env:      OLLAMA_URL=http://localhost:11434, DEMO_MODE={live|cached}       │
│                                                                               │
│  Process 3: Ollama daemon                                                     │
│    Command:  ollama serve  (auto-starts on install)                           │
│    Port:     11434                                                            │
│    Model:    llama3.2:latest (~2 GB in Ollama's registry)                     │
│                                                                               │
│  Process 4 (optional): Prisma Studio for debugging                            │
│    Command:  pnpm prisma studio                                               │
│    Port:     5555                                                             │
│                                                                               │
│  ── STORAGE ──────────────────────────────────────────────────────────────  │
│                                                                               │
│  A) dashboard/prisma/data.db              [SQLite: User table + sessions]     │
│  B) ~/.cache/huggingface/hub/             [~1 GB: LayoutLMv3 + TableTransformer]│
│  C) ~/.ollama/models/                     [~2 GB: Llama 3.2]                  │
│  D) /tmp/uploads/{extraction_id}/         [ephemeral: uploaded files]         │
│  E) src/validation/xgboost_risk_model.json[~10 MB: trained model]             │
│  F) dashboard/fixtures/*.json             [demo fallback payloads]            │
│                                                                               │
│  ── PORTS SUMMARY ────────────────────────────────────────────────────────  │
│    3000 → Next.js frontend                                                    │
│    8000 → FastAPI backend                                                     │
│   11434 → Ollama                                                              │
│    5555 → Prisma Studio (optional, dev-only)                                  │
└───────────────────────────────────────────────────────────────────────────────┘
```

**Pre-demo checklist (from PRD §15.1):**

- `~/.cache/huggingface/hub/` populated? Run `python scripts/verify_models.py`
- `~/.ollama/models/` has llama3.2? Run `ollama list`
- `data.db` seeded? Run `pnpm prisma db seed`
- `xgboost_risk_model.json` trained? Run `python src/validation/train_model.py`

---

## FRAME 20 — FAILURE / FALLBACK GRAPH

Every place we can fail, and what happens. Draw as a decision tree.

```
Request comes in
      │
      ▼
   [Live mode enabled? — env DEMO_MODE]
      │
      ├─── DEMO_MODE=cached ───────────────► Return fixtures/canonical_run.json
      │                                     (skip pipeline entirely)
      │                                     (Tier 2 of PRD §15.2)
      │
      └─── DEMO_MODE=live ─────► try pipeline
                                      │
                                      ▼
                              [Docling OK?]
                                      │
                                      ├─ NO ──► log error, return partial + error in ocr_meta.errors[]
                                      │        (do NOT crash request — FR-2.5)
                                      │
                                      └─ YES ─► [PaddleOCR OK?]
                                                      │
                                                      ├─ NO ──► same partial return
                                                      │
                                                      └─ YES ─► [LayoutLMv3 OK?]
                                                                     │
                                                                     ├─ NO ──► FALLBACK: skip semantic
                                                                     │        classification, use raw
                                                                     │        PaddleOCR text (R11 mitigation)
                                                                     │
                                                                     └─ YES ─► [TableTransformer OK?]
                                                                                     │
                                                                                     ├─ NO ──► FALLBACK: use
                                                                                     │        PaddleOCR's
                                                                                     │        table detection
                                                                                     │        (R12 mitigation)
                                                                                     │
                                                                                     └─ YES ─► [Ollama OK?]
                                                                                                     │
                                                                                                     ├─ NO ──► ERROR:
                                                                                                     │        return
                                                                                                     │        503 with
                                                                                                     │        MODEL_UNAVAILABLE
                                                                                                     │        Frontend shows
                                                                                                     │        "Try cached
                                                                                                     │        demo mode"
                                                                                                     │        button
                                                                                                     │
                                                                                                     └─ YES ─► SUCCESS
```

**Tiered fallback on demo day (from PRD §15.2):**

| Tier | Trigger | Action |
|---|---|---|
| 1 (live) | Everything working | Run pipeline live on `images/4.png` |
| 2 (cached) | OCR module fails | Flip `DEMO_MODE=cached`; identical UI behavior |
| 3 (fixture) | Backend unreachable | Frontend uses `fixtures/*.json` only |
| 4 (video) | Frontend broken | Play pre-recorded demo video |

**Golden rule:** never let the user see a raw stack trace. Structured error JSON only: `{ error_code, message, details }`.

---

## APPENDIX A — 5-STAGE PIPELINE (dev cheat sheet)

Draw as horizontal boxes with arrows.

```
[INPUT: 3 files]
       ▼
┌─────────────┐
│  1. Docling │  Convert doc → structured markdown/JSON
└─────────────┘
       ▼
┌─────────────┐
│ 2. PaddleOCR│  Text + bounding boxes + per-token confidence
└─────────────┘
       ▼
┌─────────────┐
│ 3. LayoutLMv3│ Semantic roles (HEADER/FIELD/LINE_ITEM/TOTAL)
└─────────────┘
       ▼
┌───────────────┐
│ 4. TableTrans │ Row × column extraction for line items
└───────────────┘
       ▼
┌─────────────┐
│  5. Ollama  │  Map enriched input → ExtractedDocuments JSON
└─────────────┘
       ▼
[OUTPUT: ExtractedDocuments Pydantic object with confidence_scores]
```

Fallback: if 3 or 4 fails, degrade gracefully to Docling + PaddleOCR + Ollama only. Log the fallback.

---

## APPENDIX B — SHAP MOMENT (the wow spec)

Draw as a card showing the risk panel layout.

```
┌────────────────────────────────────────────────────────┐
│  Risk Assessment                                       │
│                                                        │
│      ┌────────┐       Why this score?                  │
│      │  HIGH  │       ────────────────────────────     │
│      │ 99.97% │       Weight mismatch across docs ▓▓▓▓▓│
│      │  ⌒⌒⌒   │       Missing import permit      ▓▓▓▓ │
│      └────────┘       Total qty mismatch CI/PL   ▓▓   │
│                       ─── Baseline ───                 │
│                       HS format correct           −▓   │
│      Radial gauge     SHAP waterfall (top 5)          │
└────────────────────────────────────────────────────────┘
```

**Why this matters:** Judges have seen risk scores before. They have not seen "the AI explaining why it flagged this." This is our moat vs. Jarvis and every generic OCR tool. Do NOT deprioritize this component.

---

## APPENDIX C — QUICK-REFERENCE COMMANDS

For the dev team's terminal cheat sheet.

**Backend:**
```bash
# Setup
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Pre-download models (day 0, or before demo)
python scripts/download_models.py

# Generate training data + train XGBoost
python src/validation/synthetic_data.py
python src/validation/train_model.py

# Run API
uvicorn src.validation.api:app --host 0.0.0.0 --port 8000 --reload

# Run pipeline standalone (for testing)
python src/main.py
```

**Frontend:**
```bash
# Setup
pnpm create next-app@latest dashboard --typescript --tailwind --app
cd dashboard
pnpm add next-auth@beta @prisma/client bcryptjs recharts framer-motion
pnpm add -D prisma @types/bcryptjs

# shadcn/ui setup
pnpm dlx shadcn@latest init
pnpm dlx shadcn@latest add button card input dialog alert badge tabs progress sonner

# Prisma
pnpm prisma init --datasource-provider sqlite
pnpm prisma migrate dev --name init
pnpm prisma db seed

# Run
pnpm dev  # localhost:3000
```

**Ollama:**
```bash
# Once, before demo
ollama pull llama3.2:latest
ollama run llama3.2:latest "warm up"  # keep the daemon warm
```

---

## HOW TO IMPORT INTO FIGJAM

1. Open a new FigJam board
2. Create 13 rectangular sections labeled "FRAME 1: SUMMARY" through "FRAME 13: REFERENCES"
3. Use the layout at the top of this file as a rough map
4. For each `## FRAME X` block below, copy bullet-by-bullet into sticky notes inside the corresponding section
5. Use the sticky color hints per frame (yellow / green / orange / etc.)
6. For the workflow (FRAME 4) and pipeline (APPENDIX A), use FigJam shape tools (rectangles + arrows) instead of sticky notes
7. Pin this doc as a URL sticky in FRAME 13 so anyone can jump to the source

**Estimated time to populate the board:** 45–60 minutes for one person, or 25 minutes if two people split it.
