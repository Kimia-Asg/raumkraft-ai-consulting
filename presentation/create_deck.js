const pptxgen = require("pptxgenjs");
const fs = require("fs");

const pres = new pptxgen();
pres.layout = "LAYOUT_16x9";

// === PALETTE ===
const C = {
  primary: "065A82",
  secondary: "1C7293",
  accent: "21295C",
  light: "E8F4F8",
  white: "FFFFFF",
  offWhite: "F5F7FA",
  text: "1A1A2E",
  muted: "6B7280",
  success: "059669",
  warning: "D97706",
  red: "DC2626",
};
const TITLE = "Cambria";
const BODY = "Calibri";

// Load images as base64
function img(path) {
  const data = fs.readFileSync(path);
  return "image/png;base64," + data.toString("base64");
}
const realListing = img("/home/claude/capstone-round1/dashboard/real_listing_dashboard.png");
const realEnquiry = img("/home/claude/capstone-round1/dashboard/real_enquiry_dashboard.png");

// ============================================================
// SLIDE 1 — TITLE
// ============================================================
let slide = pres.addSlide();
slide.background = { color: C.accent };
slide.addText("AI for RaumKraft", {
  x: 0.8, y: 1.0, w: 8.4, h: 1.3,
  fontSize: 48, fontFace: TITLE, color: C.white, bold: true,
  isTextBox: true, margin: 0,
});
slide.addText("Transparent.  Practical.  Measurable.", {
  x: 0.8, y: 2.5, w: 8.4, h: 0.6,
  fontSize: 24, fontFace: BODY, color: "CADCFC", italic: true,
  isTextBox: true, margin: 0,
});
slide.addText("Prepared for Chleo, CEO  •  RaumKraft Immobilien & Design\nKimi  |  Ironhack AI Consulting Bootcamp 2026", {
  x: 0.8, y: 4.2, w: 8.4, h: 0.8,
  fontSize: 14, fontFace: BODY, color: "8EAFC0",
  lineSpacingMultiple: 1.6, isTextBox: true, margin: 0,
});
slide.addNotes("Introduce yourself. 'I'm Kimi, and today I'll show you how AI can help RaumKraft work faster — transparently, practically, and measurably.' (30 seconds)");

// ============================================================
// SLIDE 2 — WHO IS RAUMKRAFT (the situation)
// ============================================================
slide = pres.addSlide();
slide.background = { color: C.white };
slide.addText("RaumKraft Today", {
  x: 0.8, y: 0.4, w: 8.4, h: 0.7,
  fontSize: 40, fontFace: TITLE, color: C.accent, bold: true,
  isTextBox: true, margin: 0,
});

// 3 big stat cards
const stats = [
  { num: "150", label: "Employees", sub: "4 regional offices" },
  { num: "200", label: "Listings / month", sub: "Each takes 30-45 min to write" },
  { num: "8.5h", label: "Avg response time", sub: "Target: under 2 hours" },
];
stats.forEach((s, i) => {
  const x = 0.6 + i * 3.1;
  slide.addShape(pres.ShapeType.roundRect, {
    x: x, y: 1.4, w: 2.8, h: 2.4,
    fill: { color: C.offWhite },
    rectRadius: 0.15,
    shadow: { type: "outer", blur: 4, offset: 2, angle: 90, color: "000000", opacity: 0.08 },
  });
  slide.addText(s.num, {
    x: x, y: 1.6, w: 2.8, h: 0.9,
    fontSize: 48, fontFace: TITLE, color: C.primary, bold: true,
    align: "center", isTextBox: true, margin: 0,
  });
  slide.addText(s.label, {
    x: x, y: 2.5, w: 2.8, h: 0.4,
    fontSize: 16, fontFace: BODY, color: C.text, bold: true,
    align: "center", isTextBox: true, margin: 0,
  });
  slide.addText(s.sub, {
    x: x, y: 3.0, w: 2.8, h: 0.5,
    fontSize: 12, fontFace: BODY, color: C.muted,
    align: "center", isTextBox: true, margin: 0,
  });
});

// Chleo's concern
slide.addShape(pres.ShapeType.roundRect, {
  x: 0.6, y: 4.2, w: 8.8, h: 0.9,
  fill: { color: C.light },
  rectRadius: 0.1,
});
slide.addText('Chleo\'s concern:  "AI is simply not transparent — what is it doing?"', {
  x: 0.8, y: 4.2, w: 8.4, h: 0.9,
  fontSize: 16, fontFace: BODY, color: C.primary, italic: true,
  valign: "middle", isTextBox: true, margin: 0,
});
slide.addNotes("'RaumKraft is a 150-person real estate and interior design firm. Agents spend 30-45 min per listing, response times are over 8 hours — way above the 2-hour target. Chleo is worried AI is a black box. Let me show you it doesn't have to be.' (1 minute)");

// ============================================================
// SLIDE 3 — BUSINESS OVERVIEW (stat cards, from real CSV data — not a dashboard screenshot)
// ============================================================
slide = pres.addSlide();
slide.background = { color: C.offWhite };
slide.addText("Business Overview", {
  x: 0.5, y: 0.3, w: 9.0, h: 0.6,
  fontSize: 32, fontFace: TITLE, color: C.accent, bold: true,
  isTextBox: true, margin: 0,
});
slide.addText("2-year revenue by service line (synthetic dataset)", {
  x: 0.5, y: 0.9, w: 9.0, h: 0.35,
  fontSize: 13, fontFace: BODY, color: C.muted, italic: true,
  isTextBox: true, margin: 0,
});

const revenueRows = [
  { label: "Brokerage", value: 7516500, color: C.primary },
  { label: "Interior Design", value: 3205200, color: C.secondary },
  { label: "Property Management", value: 1326000, color: "8EAFC0" },
];
const maxRev = 7516500;
revenueRows.forEach((r, i) => {
  const y = 1.5 + i * 0.6;
  slide.addText(r.label, {
    x: 0.6, y: y, w: 2.1, h: 0.4,
    fontSize: 14, fontFace: BODY, color: C.text,
    valign: "middle", isTextBox: true, margin: 0,
  });
  const barW = (r.value / maxRev) * 5.0;
  slide.addShape(pres.ShapeType.rect, {
    x: 2.8, y: y + 0.05, w: barW, h: 0.3,
    fill: { color: r.color },
  });
  slide.addText(`€${(r.value / 1e6).toFixed(1)}M`, {
    x: 2.9 + barW, y: y, w: 1.2, h: 0.4,
    fontSize: 13, fontFace: BODY, color: C.text, bold: true,
    valign: "middle", isTextBox: true, margin: 0,
  });
});

// Stat cards row (real counts from the CSVs)
const bizStats = [
  { num: "500", label: "Properties (2yr)" },
  { num: "1,200", label: "Enquiries (2yr)" },
  { num: "80", label: "Design projects" },
  { num: "23", label: "Active projects now" },
];
bizStats.forEach((s, i) => {
  const x = 0.6 + i * 2.3;
  slide.addShape(pres.ShapeType.roundRect, {
    x: x, y: 3.5, w: 2.1, h: 1.4,
    fill: { color: C.white },
    rectRadius: 0.1,
    shadow: { type: "outer", blur: 3, offset: 1, angle: 90, color: "000000", opacity: 0.08 },
  });
  slide.addText(s.num, {
    x: x, y: 3.6, w: 2.1, h: 0.7,
    fontSize: 30, fontFace: TITLE, color: C.primary, bold: true,
    align: "center", isTextBox: true, margin: 0,
  });
  slide.addText(s.label, {
    x: x, y: 4.3, w: 2.1, h: 0.5,
    fontSize: 12, fontFace: BODY, color: C.muted,
    align: "center", isTextBox: true, margin: 0,
  });
});
slide.addNotes("'RaumKraft's business: €7.5M in brokerage, €3.2M in interior design, €1.3M property management, over the last 2 years. 500 properties listed, 1,200 enquiries, 80 design projects with 23 currently active.' (1 minute)");

// ============================================================
// SLIDE 4 — LISTING PERFORMANCE DASHBOARD
// ============================================================
slide = pres.addSlide();
slide.background = { color: C.offWhite };
slide.addText("Where Time Is Lost: Listings", {
  x: 0.5, y: 0.2, w: 9.0, h: 0.5,
  fontSize: 28, fontFace: TITLE, color: C.accent, bold: true,
  isTextBox: true, margin: 0,
});
slide.addImage({
  data: realListing, x: 0.5, y: 0.8, w: 9.0, h: 4.5,
});
slide.addNotes("'Listings per month swing between 12 and 29. Half of all properties are apartments. Days-to-publish varies wildly — from 4 days up to 36 days for the same type of listing. That inconsistency is exactly what AI-assisted drafting can standardise.' (1 minute)");

// ============================================================
// SLIDE 5 — ENQUIRY DASHBOARD
// ============================================================
slide = pres.addSlide();
slide.background = { color: C.offWhite };
slide.addText("Where Time Is Lost: Enquiries", {
  x: 0.5, y: 0.2, w: 9.0, h: 0.5,
  fontSize: 28, fontFace: TITLE, color: C.accent, bold: true,
  isTextBox: true, margin: 0,
});
slide.addImage({
  data: realEnquiry, x: 0.4, y: 0.75, w: 9.2, h: 4.6,
});
slide.addNotes("'40-65 enquiries per month, spread across Contact Form, Email, Phone, and WhatsApp. Viewing Requests and Pricing Questions are the two largest categories — routine, auto-draftable types. Response time bounces between 4 and 8 hours, well above the 2-hour target. AI can triage and draft responses for agent approval.' (1 minute)");

// ============================================================
// SLIDE 6 — THREE USE CASES
// ============================================================
slide = pres.addSlide();
slide.background = { color: C.white };
slide.addText("Three AI Use Cases", {
  x: 0.8, y: 0.3, w: 8.4, h: 0.7,
  fontSize: 38, fontFace: TITLE, color: C.accent, bold: true,
  isTextBox: true, margin: 0,
});

const useCases = [
  { num: "01", title: "Listing Generation", desc: "Property data → AI draft → agent reviews → publish", tag: "PRIMARY", tagColor: C.success, icon: "📝" },
  { num: "02", title: "Enquiry Triage", desc: "Auto-classify → draft response → agent approves → send", tag: "SECONDARY", tagColor: C.secondary, icon: "📨" },
  { num: "03", title: "Design Brief Generator", desc: "Meeting notes → structured brief → designer refines", tag: "FUTURE", tagColor: C.warning, icon: "🎨" },
];

useCases.forEach((uc, i) => {
  const y = 1.3 + i * 1.35;
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.8, y: y, w: 8.4, h: 1.15,
    fill: { color: C.offWhite },
    rectRadius: 0.1,
    shadow: { type: "outer", blur: 3, offset: 1, angle: 90, color: "000000", opacity: 0.07 },
  });
  slide.addText(uc.icon, {
    x: 1.0, y: y + 0.15, w: 0.7, h: 0.7,
    fontSize: 32, align: "center", valign: "middle",
    isTextBox: true, margin: 0,
  });
  slide.addText(uc.title, {
    x: 1.8, y: y + 0.1, w: 5.5, h: 0.4,
    fontSize: 20, fontFace: BODY, color: C.text, bold: true,
    isTextBox: true, margin: 0,
  });
  slide.addText(uc.desc, {
    x: 1.8, y: y + 0.55, w: 5.5, h: 0.4,
    fontSize: 14, fontFace: BODY, color: C.muted,
    isTextBox: true, margin: 0,
  });
  // Tag
  slide.addShape(pres.ShapeType.roundRect, {
    x: 7.8, y: y + 0.35, w: 1.2, h: 0.35,
    fill: { color: uc.tagColor },
    rectRadius: 0.05,
  });
  slide.addText(uc.tag, {
    x: 7.8, y: y + 0.35, w: 1.2, h: 0.35,
    fontSize: 10, fontFace: BODY, color: C.white, bold: true,
    align: "center", valign: "middle",
    isTextBox: true, margin: 0,
  });
});
slide.addNotes("'Three use cases. UC1 is our primary — listing generation. Structured data goes in, AI writes the draft, agent reviews before publishing. UC2 handles routine enquiries — 69% are auto-draftable. UC3 is future — converting meeting notes into design briefs. All three keep humans in the loop.' (1.5 minutes)");

// ============================================================
// SLIDE 7 — HOW IT WORKS (visual flow)
// ============================================================
slide = pres.addSlide();
slide.background = { color: C.white };
slide.addText("How It Works", {
  x: 0.8, y: 0.3, w: 8.4, h: 0.7,
  fontSize: 38, fontFace: TITLE, color: C.accent, bold: true,
  isTextBox: true, margin: 0,
});

const steps = [
  { icon: "📝", label: "Agent enters\nproperty data", color: C.secondary },
  { icon: "⚙️", label: "Data formatted\nfor AI", color: C.secondary },
  { icon: "🤖", label: "AI generates\nlisting draft", color: C.primary },
  { icon: "👤", label: "Agent reviews\n& approves", color: C.secondary },
  { icon: "📊", label: "Everything\nlogged", color: C.success },
];

steps.forEach((step, i) => {
  const x = 0.4 + i * 1.95;
  slide.addShape(pres.ShapeType.ellipse, {
    x: x + 0.3, y: 1.5, w: 1.1, h: 1.1,
    fill: { color: step.color },
  });
  slide.addText(step.icon, {
    x: x + 0.3, y: 1.55, w: 1.1, h: 1.0,
    fontSize: 36, align: "center", valign: "middle",
    isTextBox: true, margin: 0,
  });
  slide.addText(step.label, {
    x: x, y: 2.8, w: 1.7, h: 0.7,
    fontSize: 12, fontFace: BODY, color: C.text, bold: true,
    align: "center", lineSpacingMultiple: 1.3,
    isTextBox: true, margin: 0,
  });
  if (i < 4) {
    slide.addText("→", {
      x: x + 1.5, y: 1.7, w: 0.5, h: 0.7,
      fontSize: 28, color: C.muted, align: "center", valign: "middle",
      isTextBox: true, margin: 0,
    });
  }
});

// Transparency box
slide.addShape(pres.ShapeType.roundRect, {
  x: 0.8, y: 3.8, w: 8.4, h: 1.3,
  fill: { color: C.light },
  rectRadius: 0.1,
});
slide.addText("Transparency = Trust", {
  x: 1.0, y: 3.85, w: 8.0, h: 0.4,
  fontSize: 18, fontFace: BODY, color: C.primary, bold: true,
  isTextBox: true, margin: 0,
});

const transPoints = [
  "Every prompt and response logged in LangSmith",
  "Human reviews every output before it goes live",
  "Costs tracked per call — no surprise bills",
];
transPoints.forEach((tp, i) => {
  slide.addText("✓  " + tp, {
    x: 1.0, y: 4.3 + i * 0.25, w: 8.0, h: 0.25,
    fontSize: 13, fontFace: BODY, color: C.text,
    isTextBox: true, margin: 0,
  });
});
slide.addNotes("'Here's the workflow. Property data goes in, gets formatted, AI writes the draft, agent reviews, and everything is logged. Chleo, you can see every single AI interaction. Nothing is a black box. Nothing publishes without human approval.' (1 minute)");

// ============================================================
// SLIDE 8 — AI OPPORTUNITY + COST (combined)
// ============================================================
slide = pres.addSlide();
slide.background = { color: C.white };
slide.addText("Impact & Investment", {
  x: 0.8, y: 0.3, w: 8.4, h: 0.7,
  fontSize: 38, fontFace: TITLE, color: C.accent, bold: true,
  isTextBox: true, margin: 0,
});

// Opportunity KPIs (top row) — plain stat cards, our own estimates (not a dashboard screenshot)
slide.addText("Estimated opportunity (based on current volumes)", {
  x: 0.5, y: 1.05, w: 9.0, h: 0.3,
  fontSize: 12, fontFace: BODY, color: C.muted, italic: true,
  isTextBox: true, margin: 0,
});
const oppKpis = [
  { num: "250h", label: "Hours saved on listings / year", sub: "500 listings × 30 min", col: C.success },
  { num: "69%", label: "Enquiries eligible for auto-draft", sub: "routine types", col: C.primary },
  { num: "240h", label: "Brief hours saveable / year", sub: "80 projects × avg 3h", col: C.primary },
  { num: "~1 mo", label: "Payback period", sub: "€12–15k upfront → €15–31k/mo value", col: C.warning },
];
oppKpis.forEach((k, i) => {
  const x = 0.5 + i * 2.3;
  slide.addShape(pres.ShapeType.roundRect, {
    x: x, y: 1.45, w: 2.1, h: 1.5,
    fill: { color: C.offWhite },
    line: { color: k.col, width: 1.5 },
    rectRadius: 0.08,
  });
  slide.addText(k.num, {
    x: x, y: 1.55, w: 2.1, h: 0.55,
    fontSize: 26, fontFace: TITLE, color: k.col, bold: true,
    align: "center", isTextBox: true, margin: 0,
  });
  slide.addText(k.label, {
    x: x + 0.1, y: 2.1, w: 1.9, h: 0.5,
    fontSize: 10.5, fontFace: BODY, color: C.text, bold: true,
    align: "center", isTextBox: true, margin: 0,
  });
  slide.addText(k.sub, {
    x: x + 0.1, y: 2.6, w: 1.9, h: 0.3,
    fontSize: 9, fontFace: BODY, color: C.muted,
    align: "center", isTextBox: true, margin: 0,
  });
});

// Cost summary (bottom)
slide.addShape(pres.ShapeType.roundRect, {
  x: 0.8, y: 3.4, w: 4.0, h: 1.8,
  fill: { color: C.offWhite },
  rectRadius: 0.1,
});
slide.addText("Investment", {
  x: 0.8, y: 3.45, w: 4.0, h: 0.35,
  fontSize: 16, fontFace: BODY, color: C.primary, bold: true,
  align: "center", isTextBox: true, margin: 0,
});
const costItems = [
  ["POC setup + consulting", "€12–15k"],
  ["Monthly running cost", "€185–365"],
  ["Monthly value created", "€15–31k"],
];
costItems.forEach((c, i) => {
  const y = 3.9 + i * 0.4;
  slide.addText(c[0], {
    x: 1.0, y: y, w: 2.5, h: 0.35,
    fontSize: 13, fontFace: BODY, color: C.text,
    isTextBox: true, margin: 0,
  });
  slide.addText(c[1], {
    x: 3.3, y: y, w: 1.3, h: 0.35,
    fontSize: 13, fontFace: BODY, color: C.primary, bold: true,
    align: "right", isTextBox: true, margin: 0,
  });
});

// Timeline (bottom right)
slide.addShape(pres.ShapeType.roundRect, {
  x: 5.2, y: 3.4, w: 4.0, h: 1.8,
  fill: { color: C.offWhite },
  rectRadius: 0.1,
});
slide.addText("Timeline to Production", {
  x: 5.2, y: 3.45, w: 4.0, h: 0.35,
  fontSize: 16, fontFace: BODY, color: C.primary, bold: true,
  align: "center", isTextBox: true, margin: 0,
});
const timeline = [
  ["Wk 1–2", "Discovery"],
  ["Wk 3–5", "POC build + demo"],
  ["Wk 6–9", "Pilot (5 agents)"],
  ["Wk 10–11", "Production rollout"],
];
timeline.forEach((t, i) => {
  const y = 3.85 + i * 0.32;
  slide.addShape(pres.ShapeType.roundRect, {
    x: 5.4, y: y, w: 0.75, h: 0.28,
    fill: { color: C.secondary },
    rectRadius: 0.04,
  });
  slide.addText(t[0], {
    x: 5.4, y: y, w: 0.75, h: 0.28,
    fontSize: 9, fontFace: BODY, color: C.white, bold: true,
    align: "center", valign: "middle",
    isTextBox: true, margin: 0,
  });
  slide.addText(t[1], {
    x: 6.3, y: y, w: 2.5, h: 0.28,
    fontSize: 12, fontFace: BODY, color: C.text,
    valign: "middle", isTextBox: true, margin: 0,
  });
});
slide.addNotes("'250 hours saved on listings per year. 69% of enquiries are auto-draftable. Payback in about 1 month. The POC costs €12-15k — mainly consulting time. Monthly running costs are under €400. We estimate €15-31k in monthly value from time savings alone. Timeline: 11 weeks from discovery to production, with decision gates at each phase.' (1.5 minutes)");

// ============================================================
// SLIDE 9 — RISKS
// ============================================================
slide = pres.addSlide();
slide.background = { color: C.white };
slide.addText("Risks We've Addressed", {
  x: 0.8, y: 0.3, w: 8.4, h: 0.7,
  fontSize: 38, fontFace: TITLE, color: C.accent, bold: true,
  isTextBox: true, margin: 0,
});

const risks = [
  { risk: "AI invents features", fix: "Structured input only — AI can't hallucinate what it wasn't given", sev: "HIGH", col: C.red },
  { risk: "GDPR violation", fix: "EU-hosted endpoints + data processing agreements + anonymisation", sev: "HIGH", col: C.red },
  { risk: "Staff resistance", fix: "Framed as assistant, not replacement. Pilot with volunteers first", sev: "MED", col: C.warning },
  { risk: "Surprise costs", fix: "Per-call monitoring. ~€0.002 per listing. Monthly budget caps", sev: "LOW", col: C.success },
];

risks.forEach((r, i) => {
  const y = 1.3 + i * 1.0;
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.8, y: y, w: 0.8, h: 0.8,
    fill: { color: r.col },
    rectRadius: 0.08,
  });
  slide.addText(r.sev, {
    x: 0.8, y: y, w: 0.8, h: 0.8,
    fontSize: 11, fontFace: BODY, color: C.white, bold: true,
    align: "center", valign: "middle",
    isTextBox: true, margin: 0,
  });
  slide.addText(r.risk, {
    x: 1.8, y: y + 0.05, w: 3.0, h: 0.35,
    fontSize: 16, fontFace: BODY, color: C.text, bold: true,
    isTextBox: true, margin: 0,
  });
  slide.addText(r.fix, {
    x: 1.8, y: y + 0.4, w: 7.0, h: 0.35,
    fontSize: 13, fontFace: BODY, color: C.muted,
    isTextBox: true, margin: 0,
  });
});
slide.addNotes("'We've thought about the risks. Hallucination — solved by structured inputs. GDPR — EU endpoints and proper agreements. Staff resistance — we pilot with volunteers, frame AI as an assistant. Costs — each listing costs a fraction of a cent, with monthly caps.' (1 minute)");

// ============================================================
// SLIDE 10 — NEXT STEPS (closing)
// ============================================================
slide = pres.addSlide();
slide.background = { color: C.accent };
slide.addText("Next Steps", {
  x: 0.8, y: 0.6, w: 8.4, h: 0.8,
  fontSize: 42, fontFace: TITLE, color: C.white, bold: true,
  isTextBox: true, margin: 0,
});

const nextSteps = [
  "2-hour discovery session with your sales and design leads",
  "3-week POC build with RaumKraft data (no client PII)",
  "4-week pilot with 5 volunteer agents",
  "Review results — then decide whether to scale",
];
nextSteps.forEach((step, i) => {
  const y = 1.8 + i * 0.8;
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.8, y: y, w: 0.55, h: 0.55,
    fill: { color: C.primary },
    rectRadius: 0.08,
  });
  slide.addText(`${i + 1}`, {
    x: 0.8, y: y, w: 0.55, h: 0.55,
    fontSize: 22, fontFace: BODY, color: C.white, bold: true,
    align: "center", valign: "middle",
    isTextBox: true, margin: 0,
  });
  slide.addText(step, {
    x: 1.6, y: y, w: 7.5, h: 0.55,
    fontSize: 18, fontFace: BODY, color: "CADCFC",
    valign: "middle", isTextBox: true, margin: 0,
  });
});

slide.addText("AI doesn't have to be a black box.\nLet's prove it — together.", {
  x: 0.8, y: 4.6, w: 8.4, h: 0.7,
  fontSize: 20, fontFace: BODY, color: C.white, italic: true,
  align: "center", lineSpacingMultiple: 1.5,
  isTextBox: true, margin: 0,
});
slide.addNotes("'Four steps. Discovery session, 3-week POC, 4-week pilot, then you decide. Each phase has a gate — you commit one step at a time. AI doesn't have to be a black box. Let's prove it together. Thank you.' (30 seconds)");

// ============================================================
const outPath = "/home/claude/capstone-round1/presentation/round1_pitch_v2.pptx";
pres.writeFile({ fileName: outPath }).then(() => {
  console.log("Deck saved:", outPath);
}).catch(err => console.error(err));
