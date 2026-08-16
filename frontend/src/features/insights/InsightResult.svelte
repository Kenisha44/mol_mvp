<script>
  import { saveAnalysis } from '../../lib/analysisStorage.js';

  export let result;
  export let onCopy = () => {};
  export let inputText = '';

  let isSaved = false;
  let savedLabel = '';

  function saveCurrentAnalysis() {
    if (isSaved) return;

    saveAnalysis({
      toolId: 'insights',
      toolName: 'Insight Generator',
      title: result.executive_title || 'Executive Insight Analysis',
      status: result.insight_type || result.label || 'Saved',
      preview:
        result.primary_insight ||
        result.so_what ||
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

<div class="insight-results">

  <!-- PRIMARY INSIGHT -->
  <section class="primary-card">
    <div class="section-heading">
      <div>
        <p class="eyebrow">PRIMARY INSIGHT</p>
        <h3>Executive Intelligence</h3>
      </div>

      <button class="copy-button" on:click={onCopy}>
        Copy Analysis
      </button>
    </div>

    <p class="primary-text">
      {result.primary_insight}
    </p>
  </section>


  <!-- SO WHAT + ACTION -->
  <div class="decision-grid">

    <section class="decision-card">
      <div class="number">01</div>

      <p class="eyebrow">SO WHAT?</p>

      <h4>Executive Implication</h4>

      <p>
        {result.so_what}
      </p>
    </section>


    <section class="decision-card">
      <div class="number">02</div>

      <p class="eyebrow">RECOMMENDED ACTION</p>

      <h4>Decision Direction</h4>

      <p>
        {result.recommended_action}
      </p>
    </section>

  </div>


  <!-- EXECUTIVE COMMUNICATION -->
  <section class="communication-card">

    <div class="communication-header">
      <div>
        <p class="eyebrow">EXECUTIVE COMMUNICATION</p>
        <h3>Presentation Guidance</h3>
      </div>

      <span class="ready-badge">
        READY TO USE
      </span>
    </div>


    <div class="communication-grid">

      <div class="communication-item">
        <p class="item-label">
          SUGGESTED EXECUTIVE TITLE
        </p>

        <h4>
          {result.executive_title}
        </h4>

        <p class="helper">
          Use as a slide title, report heading, or executive summary headline.
        </p>
      </div>


      <div class="communication-item">
        <p class="item-label">
          SUGGESTED VISUALIZATION
        </p>

        <p class="visualization">
          {result.chart_suggestion}
        </p>

        <p class="helper">
          Recommended visual structure for communicating the finding.
        </p>
      </div>

    </div>

  </section>


<!-- SIGNAL SUMMARY -->
<section class="signal-strip">
  <div>
    <span>Signals analyzed</span>
    <strong>{result.signal_count ?? '—'}</strong>
  </div>

  <div>
    <span>Positive signals</span>
    <strong>{result.positive_signal_count ?? '—'}</strong>
  </div>

  <div>
    <span>Risk signals</span>
    <strong>{result.negative_signal_count ?? '—'}</strong>
  </div>

  <div>
    <span>Analysis type</span>
    <strong>{result.insight_type}</strong>
  </div>
</section>


<!-- RESULT ACTIONS -->
<div class="insight-actions">
  <button
    type="button"
    class="insight-action primary-action"
    on:click={onCopy}
  >
    Copy Analysis
  </button>

  <button
    type="button"
    class="insight-action save-action"
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
    class="insight-action export-action"
    disabled
  >
    Export
    <span>Coming Soon</span>
  </button>
</div>

{#if savedLabel}
  <div class="saved-message">
    {savedLabel}
  </div>
{/if}

</div>


<style>
  .insight-results {
    display: flex;
    flex-direction: column;
    gap: 18px;
    width: 100%;
    min-width: 0;
  }


  /* PRIMARY INSIGHT */

  .primary-card {
    padding: 24px;
    border: 1px solid rgba(0, 245, 212, 0.28);
    background:
      linear-gradient(
        135deg,
        rgba(148, 0, 211, 0.08),
        rgba(0, 245, 212, 0.025)
      );
  }

  .section-heading,
  .communication-header {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 20px;
    margin-bottom: 22px;
  }

  .eyebrow {
    margin: 0 0 7px;
    color: #00f5d4;
    font-size: 0.72rem;
    font-weight: 800;
    letter-spacing: 0.11em;
  }

  h3,
  h4,
  p {
    overflow-wrap: anywhere;
  }

  h3 {
    margin: 0;
    color: #ffffff;
    font-size: 1.15rem;
  }

  h4 {
    margin: 0;
    color: #ffffff;
  }

  .primary-text {
    margin: 0;
    padding: 22px;
    border-left: 3px solid #ff007f;
    background: rgba(4, 8, 31, 0.55);
    color: #ffffff;
    font-size: 1.05rem;
    line-height: 1.75;
  }


  /* COPY BUTTON */

  .copy-button {
    flex-shrink: 0;
    padding: 10px 14px;
    border: 1px solid rgba(0, 245, 212, 0.55);
    background: rgba(0, 245, 212, 0.05);
    color: #00f5d4;
    font-weight: 700;
    cursor: pointer;
  }

  .copy-button:hover {
    background: rgba(0, 245, 212, 0.12);
  }


  /* SO WHAT + ACTION */

  .decision-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 14px;
  }

  .decision-card {
    position: relative;
    min-width: 0;
    padding: 22px;
    border: 1px solid rgba(120, 148, 210, 0.22);
    background: rgba(16, 27, 69, 0.72);
  }

  .decision-card .number {
    display: inline-flex;
    align-items: center;
    justify-content: center;

    width: 30px;
    height: 30px;
    margin-bottom: 18px;

    border: 1px solid rgba(0, 245, 212, 0.45);

    color: #00f5d4;
    font-size: 0.72rem;
    font-weight: 800;
  }

  .decision-card h4 {
    margin-bottom: 10px;
    font-size: 1rem;
  }

  .decision-card > p:last-child {
    margin: 0;
    color: #c8d4f3;
    line-height: 1.65;
  }


  /* EXECUTIVE COMMUNICATION */

  .communication-card {
    padding: 24px;
    border: 1px solid rgba(255, 0, 127, 0.28);
    background: rgba(12, 18, 55, 0.78);
  }

  .ready-badge {
    flex-shrink: 0;
    padding: 8px 11px;

    border: 1px solid rgba(255, 0, 127, 0.5);
    background: rgba(255, 0, 127, 0.08);

    color: #ff45a1;
    font-size: 0.68rem;
    font-weight: 800;
    letter-spacing: 0.08em;
  }

  .communication-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 14px;
  }

  .communication-item {
    min-width: 0;
    padding: 20px;

    border: 1px solid rgba(120, 148, 210, 0.18);
    background: rgba(4, 8, 31, 0.5);
  }

  .item-label {
    margin: 0 0 12px;

    color: #8ea6e8;
    font-size: 0.7rem;
    font-weight: 800;
    letter-spacing: 0.08em;
  }

  .communication-item h4 {
    font-size: 1.08rem;
    line-height: 1.45;
  }

  .visualization {
    margin: 0;
    color: #ffffff;
    font-weight: 600;
    line-height: 1.6;
  }

  .helper {
    margin: 12px 0 0;
    color: #7f94c7;
    font-size: 0.78rem;
    line-height: 1.5;
  }


  /* SIGNAL SUMMARY */

  .signal-strip {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));

    border: 1px solid rgba(0, 245, 212, 0.18);
    background: rgba(8, 15, 43, 0.72);
  }

  .signal-strip > div {
    min-width: 0;
    padding: 16px 18px;
    border-right: 1px solid rgba(0, 245, 212, 0.12);
  }

  .signal-strip > div:last-child {
    border-right: none;
  }

  .signal-strip span {
    display: block;
    margin-bottom: 7px;

    color: #7f94c7;
    font-size: 0.72rem;
  }

  .signal-strip strong {
    display: block;
    color: #ffffff;
    overflow-wrap: anywhere;
  }

.insight-actions {
  display: flex !important;
  flex-direction: row !important;
  align-items: center;
  justify-content: flex-start;
  flex-wrap: wrap;
  gap: 10px;

  width: 100%;
  padding-top: 14px;
}

.insight-actions > .insight-action {
  display: inline-flex !important;
  align-items: center;
  justify-content: center;

  width: auto !important;
  min-width: 0 !important;
  min-height: 42px;

  flex: 0 0 auto !important;

  padding: 0 15px;

  border: 1px solid rgba(255, 255, 255, .13);
  border-radius: 5px;

  background: rgba(255, 255, 255, .035);
  color: #c9d3ec;

  font-family: inherit;
  font-weight: 800;
}

.insight-actions .primary-action {
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

.insight-actions .save-action {
  border-color: rgba(0, 245, 212, .28);
  background: rgba(0, 245, 212, .06);
  color: #00f5d4;
  cursor: pointer;
}

.insight-actions .save-action.saved {
  border-color: rgba(0, 245, 212, .35);
  background: rgba(0, 245, 212, .10);
  color: #00f5d4;
  opacity: 1;
  cursor: default;
}

.insight-actions .insight-action:disabled {
  opacity: .45;
  cursor: not-allowed;
}

.insight-actions .insight-action span {
  margin-left: 7px;
  color: #8290b3;
  font-size: .63rem;
  text-transform: uppercase;
}

.insight-actions .save-action:hover:not(:disabled) {
  background: rgba(0, 245, 212, .12);
}

.insight-actions .export-action {
  border-color: rgba(255, 255, 255, .13);
  background: rgba(255, 255, 255, .035);
  color: #c9d3ec;
}

.saved-message {
  padding: 10px 12px;

  border: 1px solid rgba(0, 245, 212, .25);

  background: rgba(0, 245, 212, .06);
  color: #00f5d4;

  font-size: .78rem;
  font-weight: 800;
}

  /* RESPONSIVE */

  @media (max-width: 900px) {
    .decision-grid,
    .communication-grid {
      grid-template-columns: 1fr;
    }

    .signal-strip {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .signal-strip > div:nth-child(2) {
      border-right: none;
    }
  }

  @media (max-width: 600px) {
    .section-heading,
    .communication-header {
      flex-direction: column;
    }

    .signal-strip {
      grid-template-columns: 1fr;
    }

    .signal-strip > div {
      border-right: none;
      border-bottom: 1px solid rgba(0, 245, 212, 0.12);
    }

    .signal-strip > div:last-child {
      border-bottom: none;
    }
  }
</style>