<script>
  import { saveAnalysis } from '../../lib/analysisStorage.js';

  export let result;
  export let onCopy = () => {};
  export let inputText = '';

  let isSaved = false;
  let savedLabel = '';

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

  function saveCurrentAnalysis() {
    if (isSaved) return;

    saveAnalysis({
      toolId: 'kpi-cleaner',
      toolName: 'KPI Cleaner',
      title: 'KPI Cleanup Analysis',
      status: `${result.label} • ${issues} issue${issues === 1 ? '' : 's'}`,
      preview:
        result.result ||
        inputText.slice(0, 140),
      input: inputText,
      result
    });

    isSaved = true;
    savedLabel = 'Saved to Workspace';

    setTimeout(() => {
      savedLabel = '';
    }, 1800);
  }
</script>

<div class="kpi-result">
  <section class="result-overview">
    <div class="issue-card">
      <div class="issue-top">
        <div>
          <p class="eyebrow">Issues Found</p>

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
      <p class="eyebrow">Cleanup Status</p>

      <strong>{result.label}</strong>

      <span>
        MOL reviewed the KPI list for naming consistency, abbreviations,
        readability, and reporting readiness.
      </span>
    </div>
  </section>

  <section class="cleaned-card">
    <div class="card-heading">
      <div>
        <p class="eyebrow">Cleaned KPI Output</p>
        <h3>Standardized KPI Labels</h3>
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

  <section class="cleanup-signals">
    <div class="signal">
      <span class="signal-number">01</span>

      <div>
        <strong>Naming Consistency</strong>
        <p>
          Standardizes inconsistent KPI naming conventions.
        </p>
      </div>
    </div>

    <div class="signal">
      <span class="signal-number">02</span>

      <div>
        <strong>Executive Readability</strong>
        <p>
          Converts shorthand into clearer business-ready labels.
        </p>
      </div>
    </div>

    <div class="signal">
      <span class="signal-number">03</span>

      <div>
        <strong>Reporting Readiness</strong>
        <p>
          Makes metric names easier to use across dashboards and reports.
        </p>
      </div>
    </div>
  </section>

  <div class="actions">
    <button
      type="button"
      class="action primary"
      on:click={onCopy}
    >
      Copy Analysis
    </button>
{#if savedLabel}
  <div class="saved-message">
    {savedLabel}
  </div>
{/if}
<button
  type="button"
  class="action save-action"
  class:saved={isSaved}
  on:click={saveCurrentAnalysis}
  disabled={isSaved}
>
  {#if isSaved}
    Saved ✓
  {:else}
    Save to Workspace
  {/if}
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
  .kpi-result {
    display: grid;
    gap: 18px;
  }

  .result-overview {
    display: grid;
    grid-template-columns: minmax(0, 1.25fr) minmax(210px, .75fr);
    gap: 14px;
  }

  .issue-card,
  .analysis-card,
  .cleaned-card {
    border: 1px solid rgba(0, 245, 212, .22);

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

    border: 1px solid rgba(255, 0, 127, .38);

    background: rgba(255, 0, 127, .08);
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

  .cleaned-output {
    border-left: 3px solid #ff007f;

    background: rgba(0, 0, 0, .18);
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

  .cleanup-signals {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 12px;
  }

  .signal {
    display: flex;
    gap: 12px;

    padding: 16px;

    border: 1px solid rgba(255, 255, 255, .08);

    background: rgba(255, 255, 255, .025);
  }

  .signal-number {
    flex: 0 0 28px;

    width: 28px;
    height: 28px;

    display: grid;
    place-items: center;

    border: 1px solid rgba(0, 245, 212, .25);

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

  .actions {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;

    padding-top: 4px;
  }

  .action {
    min-height: 42px;

    padding: 0 15px;

    border: 1px solid rgba(255, 255, 255, .13);
    border-radius: 5px;

    background: rgba(255, 255, 255, .035);
    color: #c9d3ec;

    font-weight: 800;
  }

  .primary {
    border-color: rgba(255, 0, 127, .5);

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

.save-action {
  border-color: rgba(0, 245, 212, .28);
  background: rgba(0, 245, 212, .06);
  color: #00f5d4;
  cursor: pointer;
}

.save-action:hover:not(:disabled) {
  background: rgba(0, 245, 212, .12);
}

.save-action.saved {
  border-color: rgba(0, 245, 212, .35);
  background: rgba(0, 245, 212, .10);
  color: #00f5d4;
  opacity: 1;
  cursor: default;
}

.saved-message {
  padding: 10px 12px;

  border: 1px solid rgba(0, 245, 212, .25);

  background: rgba(0, 245, 212, .06);
  color: #00f5d4;

  font-size: .78rem;
  font-weight: 800;
}

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
  }
</style>