<script>
  export let result;
  export let onCopy = () => {};
</script>

<div class="narrative-report">

  <section class="overview-grid">

    <div class="status-card">
      <p class="eyebrow">PERFORMANCE STATUS</p>

      <h3>{result.performance_status}</h3>

      <span class="status-chip">
        {result.label}
      </span>
    </div>

    <div class="signal-card">
      <p class="eyebrow">SIGNALS ANALYZED</p>

      <div class="signal-number">
        {result.signal_count}
      </div>

      <p>
        Dashboard observations reviewed for executive relevance.
      </p>
    </div>

  </section>


  <section class="summary-card">

    <div class="section-heading">
      <div>
        <p class="eyebrow">EXECUTIVE SUMMARY</p>
        <h3>Leadership Narrative</h3>
      </div>

      <button
        type="button"
        class="copy-button"
        on:click={onCopy}
      >
        Copy Narrative
      </button>
    </div>

    <div class="summary-copy">
      {result.executive_summary}
    </div>

  </section>


  <div class="performance-grid">

    <section class="report-card positive">

      <div class="number">01</div>

      <p class="eyebrow">
        PERFORMANCE DRIVERS
      </p>

      <h4>What Is Working</h4>

      <p>
        {result.performance_drivers}
      </p>

    </section>


    <section class="report-card risk">

      <div class="number">02</div>

      <p class="eyebrow">
        RISKS & WATCH ITEMS
      </p>

      <h4>What Needs Attention</h4>

      <p>
        {result.risks}
      </p>

    </section>

  </div>


  <section class="action-card">

    <div class="number">03</div>

    <div>
      <p class="eyebrow">RECOMMENDED ACTION</p>

      <h4>Leadership Priority</h4>

      <p>
        {result.recommended_action}
      </p>
    </div>

  </section>


  <section class="outlook-card">

    <div class="section-heading">

      <div>
        <p class="eyebrow">OUTLOOK</p>
        <h3>Forward View</h3>
      </div>

      <span class="ready-badge">
        EXECUTIVE READY
      </span>

    </div>

    <p class="outlook-copy">
      {result.outlook}
    </p>

  </section>


  <section class="metric-strip">

    <div>
      <span>Total Signals</span>
      <strong>{result.signal_count}</strong>
    </div>

    <div>
      <span>Positive Signals</span>
      <strong>{result.positive_signal_count}</strong>
    </div>

    <div>
      <span>Risk Signals</span>
      <strong>{result.negative_signal_count}</strong>
    </div>

    <div>
      <span>Performance</span>
      <strong>{result.performance_status}</strong>
    </div>

  </section>


  <div class="actions">

    <button
      type="button"
      class="action primary-action"
      on:click={onCopy}
    >
      Copy Analysis
    </button>

    <button
      type="button"
      class="action"
      disabled
    >
      Save
      <span>Coming Soon</span>
    </button>

    <button
      type="button"
      class="action"
      disabled
    >
      Export
      <span>Coming Soon</span>
    </button>

  </div>

</div>


<style>

  .narrative-report {
    display: grid;
    gap: 18px;

    width: 100%;
    min-width: 0;
  }


  /* SHARED */

  .eyebrow {
    margin: 0 0 8px;

    color: #00f5d4;

    font-size: .7rem;
    font-weight: 900;
    letter-spacing: .13em;
    text-transform: uppercase;
  }

  h3,
  h4 {
    margin: 0;

    color: #f7f7ff;
  }

  h3 {
    font-size: 1.1rem;
  }

  h4 {
    font-size: .95rem;
  }


  /* TOP OVERVIEW */

  .overview-grid {
    display: grid;

    grid-template-columns:
      minmax(0, 1.35fr)
      minmax(190px, .65fr);

    gap: 14px;
  }

  .status-card,
  .signal-card,
  .summary-card,
  .report-card,
  .action-card,
  .outlook-card {

    border: 1px solid rgba(0, 245, 212, .22);

    background:
      linear-gradient(
        145deg,
        rgba(18, 27, 68, .9),
        rgba(5, 10, 32, .96)
      );
  }

  .status-card,
  .signal-card {
    padding: 20px;
  }

  .status-card {
    position: relative;
  }

  .status-chip {
    display: inline-block;

    margin-top: 14px;
    padding: 7px 10px;

    border: 1px solid rgba(255, 0, 127, .38);

    background: rgba(255, 0, 127, .08);
    color: #ff5bad;

    font-size: .68rem;
    font-weight: 900;
    letter-spacing: .08em;
    text-transform: uppercase;
  }

  .signal-number {
    color: #f7f7ff;

    font-size: 3.1rem;
    font-weight: 900;
    line-height: 1;
  }

  .signal-card p:last-child {
    margin: 12px 0 0;

    color: #93a1c5;

    line-height: 1.5;
    font-size: .8rem;
  }


  /* EXECUTIVE SUMMARY */

  .summary-card,
  .outlook-card {
    padding: 22px;
  }

  .section-heading {
    display: flex;

    justify-content: space-between;
    align-items: flex-start;

    gap: 20px;

    margin-bottom: 18px;
  }

  .copy-button {
    flex: 0 0 auto;

    padding: 9px 12px;

    border: 1px solid rgba(0, 245, 212, .32);
    border-radius: 5px;

    background: rgba(0, 245, 212, .06);
    color: #00f5d4;

    font-weight: 800;
    cursor: pointer;
  }

  .copy-button:hover {
    background: rgba(0, 245, 212, .12);
  }

  .summary-copy {
    padding: 22px;

    border-left: 3px solid #ff007f;

    background:
      radial-gradient(
        circle at top right,
        rgba(148, 0, 211, .08),
        transparent 35%
      ),
      rgba(0, 0, 0, .18);

    color: #ecf0ff;

    font-size: 1rem;
    line-height: 1.7;
  }


  /* DRIVERS + RISKS */

  .performance-grid {
    display: grid;

    grid-template-columns:
      repeat(2, minmax(0, 1fr));

    gap: 14px;
  }

  .report-card {
    padding: 20px;
  }

  .number {
    width: 30px;
    height: 30px;

    display: grid;
    place-items: center;

    margin-bottom: 16px;

    border: 1px solid rgba(0, 245, 212, .4);

    color: #00f5d4;

    font-size: .7rem;
    font-weight: 900;
  }

  .report-card h4,
  .action-card h4 {
    margin-bottom: 10px;
  }

  .report-card p:last-child,
  .action-card p:last-child {

    margin: 0;

    color: #c8d4f3;

    line-height: 1.65;
  }

  .positive {
    border-top: 2px solid rgba(0, 245, 212, .65);
  }

  .risk {
    border-top: 2px solid rgba(255, 0, 127, .65);
  }


  /* ACTION */

  .action-card {
    display: flex;

    gap: 16px;

    padding: 22px;
  }

  .action-card .number {
    flex: 0 0 30px;

    margin-bottom: 0;
  }


  /* OUTLOOK */

  .ready-badge {
    padding: 7px 10px;

    border: 1px solid rgba(255, 0, 127, .4);

    background: rgba(255, 0, 127, .07);

    color: #ff5bad;

    font-size: .68rem;
    font-weight: 900;
    letter-spacing: .08em;
    text-transform: uppercase;
  }

  .outlook-copy {
    margin: 0;

    color: #dce4f8;

    line-height: 1.7;
  }


  /* METRIC STRIP */

  .metric-strip {
    display: grid;

    grid-template-columns:
      repeat(4, minmax(0, 1fr));

    border: 1px solid rgba(0, 245, 212, .18);

    background: rgba(8, 15, 43, .72);
  }

  .metric-strip > div {
    min-width: 0;

    padding: 16px 18px;

    border-right:
      1px solid rgba(0, 245, 212, .12);
  }

  .metric-strip > div:last-child {
    border-right: none;
  }

  .metric-strip span {
    display: block;

    margin-bottom: 7px;

    color: #7f94c7;

    font-size: .72rem;
  }

  .metric-strip strong {
    display: block;

    color: #ffffff;

    overflow-wrap: anywhere;
  }


  /* ACTION BUTTONS */

  .actions {
    display: flex;
    flex-wrap: wrap;

    gap: 10px;

    padding-top: 4px;
  }

  .action {
    min-height: 42px;

    padding: 0 15px;

    border:
      1px solid rgba(255, 255, 255, .13);

    border-radius: 5px;

    background:
      rgba(255, 255, 255, .035);

    color: #c9d3ec;

    font-weight: 800;
  }

  .primary-action {
    border-color:
      rgba(255, 0, 127, .5);

    background:
      linear-gradient(
        90deg,
        rgba(148, 0, 211, .55),
        rgba(255, 0, 127, .55)
      );

    color: white;

    cursor: pointer;
  }

  .action:disabled {
    opacity: .45;
    cursor: not-allowed;
  }

  .action span {
    margin-left: 7px;

    color: #8290b3;

    font-size: .63rem;
    text-transform: uppercase;
  }


  /* RESPONSIVE */

  @media (max-width: 1050px) {

    .overview-grid,
    .performance-grid {
      grid-template-columns: 1fr;
    }

    .metric-strip {
      grid-template-columns:
        repeat(2, minmax(0, 1fr));
    }

  }

  @media (max-width: 640px) {

    .section-heading {
      flex-direction: column;
    }

    .metric-strip {
      grid-template-columns: 1fr;
    }

    .metric-strip > div {
      border-right: none;

      border-bottom:
        1px solid rgba(0, 245, 212, .12);
    }

    .metric-strip > div:last-child {
      border-bottom: none;
    }

  }

</style>