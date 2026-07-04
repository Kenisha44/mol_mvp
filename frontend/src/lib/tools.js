export const tools = [
  {
    id: 'clarity',
    label: 'Clarity Analyzer',
    endpoint: '/clarity/analyze',
    eyebrow: 'TOOL 01',
    title: 'Executive Clarity Analyzer',
    description: 'Turn messy report copy, slide bullets, and notes into sharper executive-ready direction.',
    placeholder: 'Paste report text, slide bullets, or meeting notes...',
    emptyTitle: 'Paste messy executive text.',
    emptyBody: 'Use this for rough reports, board updates, slide bullets, meeting notes, or strategy summaries.',
    sample: 'Sales increased in Q1 but customer churn also increased slightly. We launched two campaigns and the email campaign did better than expected. Support tickets are still high and leadership wants recommendations for next quarter.'
  },
  {
    id: 'kpi',
    label: 'KPI Cleaner',
    endpoint: '/kpi-cleaner/clean',
    eyebrow: 'TOOL 02',
    title: 'KPI Cleaner',
    description: 'Standardize messy KPI names into polished, business-ready labels and categories.',
    placeholder: 'Paste KPIs, one per line. Example: rev growth q1, cust churn, mrr...',
    emptyTitle: 'Paste messy KPI names.',
    emptyBody: 'Use this for raw dashboard labels, spreadsheet headers, reporting terms, and inconsistent metric names.',
    sample: 'rev growth q1\ncust churn\nmrr growth\ncac\nprofit margin\nconv rate'
  },
  {
    id: 'insights',
    label: 'Insight Generator',
    endpoint: '/insights/generate',
    eyebrow: 'TOOL 03',
    title: 'Insight Generator Lite',
    description: 'Generate executive insights, so-what statements, slide titles, and chart suggestions.',
    placeholder: 'Paste data notes, observations, or a rough summary...',
    emptyTitle: 'Paste raw data notes.',
    emptyBody: 'Use this for trend notes, research findings, analyst observations, KPI changes, and report summaries.',
    sample: 'Revenue increased 18% in Q1.\nCustomer churn increased 4%.\nMarketing costs decreased.\nSupport tickets increased after onboarding redesign.\nEnterprise accounts had the highest growth.'
  },
  {
    id: 'dashboard',
    label: 'Dashboard Narrative',
    endpoint: '/dashboard-narrative/generate',
    eyebrow: 'TOOL 04',
    title: 'Dashboard Narrative Generator',
    description: 'Transform dashboard notes and KPI changes into executive-ready narratives.',
    placeholder: 'Paste dashboard notes, KPI changes, or executive reporting content...',
    emptyTitle: 'Paste dashboard observations.',
    emptyBody: 'Use this for KPI summaries, Power BI exports, Tableau notes, leadership dashboards, or business metrics.',
    sample: 'Revenue increased 18% in Q2. Customer churn increased 4%. Support tickets increased after onboarding redesign. Enterprise accounts had the highest growth.'
  },


{
  id: "executive-memo",

  label: "Executive Memo",

  endpoint: "/executive-memo/generate",

  eyebrow: "TOOL 05",

  title: "Executive Memo Studio",

  description:
      "Transform executive notes into polished leadership-ready memos.",

  placeholder:
      "Paste executive notes, dashboard summaries, meeting notes, or project updates...",

  emptyTitle:
      "Generate an executive memo.",

  emptyBody:
      "Choose a memo type and audience, then generate a polished memo.",

  sample:
`Revenue increased 18% this quarter.
Customer churn declined by 3%.
Support backlog improved after workflow automation.
Marketing campaign exceeded forecast by 22%.
Leadership requested recommendations for next quarter.`
}
];