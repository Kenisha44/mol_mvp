<script>
  import ExportActions from '../../components/ui/ExportActions.svelte';

  export let result;
  export let onCopy = () => {};
  export let inputText = '';

  $: issues = Number(result?.issues_found ?? 0);

  $: statusLabel =
    issues === 0
      ? 'Clean'
      : issues <= 2
        ? 'Minor Cleanup'
        : issues <= 5
          ? 'Needs Standardization'
          : 'High Cleanup Needed';

  $: statusMessage =
    issues === 0
      ? 'No major KPI naming issues were detected.'
      : issues <= 2
        ? 'The KPI set is mostly consistent with a few naming issues.'
        : issues <= 5
          ? 'Several KPI labels need normalization for consistent reporting.'
          : 'The KPI set contains significant inconsistencies that should be standardized.';
</script>


<div class="kpi-result">

  <!-- OVERVIEW -->
  <section class="result-overview">

    <div class="issue-card">

      <div class="issue-top">

        <div>
          <p class="eyebrow">
            Issues Found
          </p>

          <div class="issue-count">
            {issues}
          </div>
        </div>

        <span class="status-chip">
          {statusLabel}
        </span>

      </div>


      <p class="status-message">
        {statusMessage}
      </p>

    </div>


    <div class="analysis-card">

      <p class="eyebrow">
        Cleanup Status
      </p>

      <strong>
        {result.label}
      </strong>

      <span>
        MOL reviewed the KPI list for naming consistency,
        abbreviations, readability, and reporting readiness.
      </span>

    </div>

  </section>


  <!-- CLEANED OUTPUT -->
  <section class="cleaned-card">

    <div class="card-heading">

      <div>
        <p class="eyebrow">
          Cleaned KPI Output
        </p>

        <h3>
          Standardized KPI Labels
        </h3>
      </div>


      <button
        type="button"
        class="copy-button"
        on:click={onCopy}
      >
        Copy Output
      </button>

    </div>


    <div class="cleaned-output">
      <pre>{result.result}</pre>
    </div>

  </section>


  <!-- CLEANUP SIGNALS -->
  <section class="cleanup-signals">

    <div class="signal">

      <span class="signal-number">
        01
      </span>

      <div>
        <strong>
          Naming Consistency
        </strong>

        <p>
          Standardizes inconsistent KPI naming conventions.
        </p>
      </div>

    </div>


    <div class="signal">

      <span class="signal-number">
        02
      </span>

      <div>
        <strong>
          Executive Readability
        </strong>

        <p>
          Converts shorthand into clearer business-ready labels.
        </p>
      </div>

    </div>


    <div class="signal">

      <span class="signal-number">
        03
      </span>

      <div>
        <strong>
          Reporting Readiness
        </strong>

        <p>
          Makes metric names easier to use across dashboards and reports.
        </p>
      </div>

    </div>

  </section>


  <!-- ACTIONS -->
  <section class="result-actions">

    <button
      type="button"
      class="copy-analysis"
      on:click={onCopy}
    >
      Copy Analysis
    </button>


    <ExportActions
      toolId="kpi-cleaner"
      toolName="KPI Cleaner"
      title="KPI Cleanup Analysis"
      status={`${result.label} • ${issues} issue${issues === 1 ? '' : 's'}`}
      preview={
        result.result ||
        inputText.slice(0, 140)
      }
      input={inputText}
      {result}
    />

  </section>

</div>


<style>
  .kpi-result {
    display: grid;
    gap: 18px;
  }


  /* OVERVIEW */

  .result-overview {
    display: grid;

    grid-template-columns:
      minmax(0, 1.25fr)
      minmax(210px, .75fr);

    gap: 14px;
  }


  .issue-card,
  .analysis-card,
  .cleaned-card {
    border:
      1px solid rgba(0, 245, 212, .22);

    background:
      linear-gradient(
        145deg,
        rgba(18, 27, 68, .9),
        rgba(5, 10, 32, .96)
      );
  }


  .issue-card,
  .analysis-card {
    padding: 20px;
  }


  .eyebrow {
    margin: 0 0 8px;

    color: #00f5d4;

    font-size: .7rem;
    font-weight: 900;
    letter-spacing: .13em;

    text-transform: uppercase;
  }


  /* ISSUES */

  .issue-top {
    display: flex;

    justify-content: space-between;
    align-items: flex-start;

    gap: 20px;
  }


  .issue-count {
    color: #f7f7ff;

    font-size: 3.4rem;
    font-weight: 900;

    line-height: 1;
  }


  .status-chip {
    padding: 7px 10px;

    border:
      1px solid rgba(255, 0, 127, .38);

    background:
      rgba(255, 0, 127, .08);

    color: #ff5bad;

    font-size: .68rem;
    font-weight: 900;
    letter-spacing: .08em;

    text-transform: uppercase;
  }


  .status-message {
    margin: 18px 0 0;

    color: #aebbd8;

    line-height: 1.55;

    font-size: .84rem;
  }


  /* ANALYSIS */

  .analysis-card {
    display: flex;
    flex-direction: column;
  }


  .analysis-card strong {
    margin-bottom: 8px;

    color: #f7f7ff;

    font-size: 1.05rem;
  }


  .analysis-card span {
    color: #93a1c5;

    line-height: 1.5;

    font-size: .8rem;
  }


  /* CLEANED OUTPUT */

  .cleaned-card {
    padding: 22px;
  }


  .card-heading {
    display: flex;

    justify-content: space-between;
    align-items: flex-start;

    gap: 20px;

    margin-bottom: 18px;
  }


  h3 {
    margin: 0;

    color: #f7f7ff;

    font-size: 1.1rem;
  }


  .copy-button {
    flex: 0 0 auto;

    padding: 9px 12px;

    border:
      1px solid rgba(0, 245, 212, .32);

    border-radius: 5px;

    background:
      rgba(0, 245, 212, .06);

    color: #00f5d4;

    font-weight: 800;

    cursor: pointer;
  }


  .copy-button:hover {
    background:
      rgba(0, 245, 212, .12);
  }


  .cleaned-output {
    border-left:
      3px solid #ff007f;

    background:
      rgba(0, 0, 0, .18);
  }


  pre {
    margin: 0;

    padding: 20px;

    white-space: pre-wrap;
    overflow-wrap: anywhere;
    word-break: break-word;

    color: #ecf0ff;

    font-family: inherit;

    line-height: 1.7;
  }


  /* SIGNALS */

  .cleanup-signals {
    display: grid;

    grid-template-columns:
      repeat(3, minmax(0, 1fr));

    gap: 12px;
  }


  .signal {
    display: flex;

    gap: 12px;

    padding: 16px;

    border:
      1px solid rgba(255, 255, 255, .08);

    background:
      rgba(255, 255, 255, .025);
  }


  .signal-number {
    flex: 0 0 28px;

    width: 28px;
    height: 28px;

    display: grid;
    place-items: center;

    border:
      1px solid rgba(0, 245, 212, .25);

    color: #00f5d4;

    font-size: .64rem;
    font-weight: 900;
  }


  .signal strong {
    color: #f7f7ff;

    font-size: .82rem;
  }


  .signal p {
    margin: 5px 0 0;

    color: #8797bc;

    line-height: 1.45;

    font-size: .74rem;
  }


  /* ACTIONS */

  .result-actions {
    display: flex;

    align-items: flex-start;
    flex-wrap: wrap;

    gap: 10px;

    padding-top: 4px;
  }


  .copy-analysis {
    min-height: 40px;

    padding: 0 15px;

    border:
      1px solid rgba(255, 0, 127, .5);

    border-radius: 5px;

    background:
      linear-gradient(
        90deg,
        rgba(148, 0, 211, .55),
        rgba(255, 0, 127, .55)
      );

    color: white;

    font-family: inherit;
    font-weight: 800;

    cursor: pointer;
  }


  .copy-analysis:hover {
    filter: brightness(1.08);
  }


  /* RESPONSIVE */

  @media (max-width: 1050px) {
    .result-overview,
    .cleanup-signals {
      grid-template-columns: 1fr;
    }
  }


  @media (max-width: 640px) {
    .card-heading,
    .issue-top {
      flex-direction: column;
    }

    .result-actions {
      flex-direction: column;
    }
  }
</style>