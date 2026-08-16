<script>
  import { saveAnalysis } from '../../lib/analysisStorage.js';

  export let result;
  export let inputText = '';

  let isSaved = false;
  let savedLabel = '';

$: score = Number(result?.overall_score ?? 0);

$: healthLabel =
  score >= 90
    ? 'Excellent'
    : score >= 75
      ? 'Healthy'
      : score >= 60
        ? 'Watch'
        : score >= 40
          ? 'At Risk'
          : 'Critical';

$: healthMessage =
  score >= 90
    ? 'Business performance is strong with limited immediate concern.'
    : score >= 75
      ? 'Overall performance is healthy, with a few areas that warrant monitoring.'
      : score >= 60
        ? 'Performance is mixed and several indicators should be reviewed closely.'
        : score >= 40
          ? 'Multiple performance risks are present and leadership action is recommended.'
          : 'The KPI profile indicates significant business pressure requiring immediate attention.';

  function copyAnalysis() {
    const output = [
      `Overall Health Score: ${result.overall_score}%`,
      '',
      `Summary:`,
      result.summary,
      '',
      `Strengths:`,
      ...(result.strengths ?? []).map((item) => `- ${item}`),
      '',
      `Concerns:`,
      ...(result.concerns ?? []).map((item) => `- ${item}`),
      '',
      `Recommendations:`,
      ...(result.recommendations ?? []).map((item) => `- ${item}`)
    ].join('\n');

    navigator.clipboard.writeText(output);
  }

  function saveCurrentAnalysis() {
    if (isSaved) return;

    saveAnalysis({
      toolId: 'kpi-health',
      toolName: 'KPI Health Checker',

      title: 'KPI Health Analysis',

      status: `${result.overall_score}% Health Score`,

      preview:
        result.summary ||
        result.concerns?.[0] ||
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

<div class="health-report">

<div class="health-actions">

  <button
    type="button"
    class="copy-action"
    on:click={copyAnalysis}
  >
    Copy Analysis
  </button>

  <button
    type="button"
    class="save-action"
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
    class="export-action"
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
 <section class="health-overview">
        
        <div class="score-card">

            <div class="score-top">

                <div>
                    <p class="eyebrow">OVERALL HEALTH SCORE</p>

                    <div class="score-line">
                        <strong>{score}</strong>
                        <span>/100</span>
                    </div>
                </div>

                <span class="health-chip">
                    {healthLabel}
                </span>

            </div>

            <div class="score-track">
                <div
                    class="score-fill"
                    style={`width: ${Math.min(Math.max(score, 0), 100)}%`}
                ></div>
            </div>

            <p class="health-message">
                {healthMessage}
            </p>

        </div>


        <div class="assessment-card">

            <p class="eyebrow">
                EXECUTIVE ASSESSMENT
            </p>

            <h3>Business Health Summary</h3>

            <p>
                {result.summary}
            </p>

        </div>

    </section>


    <div class="diagnostic-grid">

        <section class="diagnostic-card strength">

            <div class="card-heading">
                <div>
                    <p class="eyebrow">STRENGTHS</p>
                    <h3>What Is Working</h3>
                </div>

                <span class="count-badge">
                    {result.strengths?.length ?? 0}
                </span>
            </div>

            <div class="item-list">

                {#each result.strengths ?? [] as item, index}
                    <div class="health-item">

                        <span class="item-number">
                            {String(index + 1).padStart(2, "0")}
                        </span>

                        <p>{item}</p>

                    </div>
                {/each}

            </div>

        </section>


        <section class="diagnostic-card concern">

            <div class="card-heading">
                <div>
                    <p class="eyebrow">CONCERNS</p>
                    <h3>What Needs Attention</h3>
                </div>

                <span class="count-badge risk">
                    {result.concerns?.length ?? 0}
                </span>
            </div>

            <div class="item-list">

                {#each result.concerns ?? [] as item, index}
                    <div class="health-item">

                        <span class="item-number risk-number">
                            {String(index + 1).padStart(2, "0")}
                        </span>

                        <p>{item}</p>

                    </div>
                {/each}

            </div>

        </section>

    </div>


    <section class="priority-card">

        <div class="card-heading">

            <div>
                <p class="eyebrow">PRIORITY ACTIONS</p>
                <h3>Recommended Next Moves</h3>
            </div>

            <span class="priority-badge">
                ACTION REQUIRED
            </span>

        </div>

        <div class="priority-list">

            {#each result.recommendations ?? [] as item, index}

                <div class="priority-item">

                    <span class="priority-number">
                        {String(index + 1).padStart(2, "0")}
                    </span>

                    <div>
                        <strong>
                            Priority {index + 1}
                        </strong>

                        <p>
                            {item}
                        </p>
                    </div>

                </div>

            {/each}

        </div>

    </section>


    <section class="health-footer">

        <div>
            <span>Health Status</span>
            <strong>{healthLabel}</strong>
        </div>

        <div>
            <span>Strengths</span>
            <strong>{result.strengths?.length ?? 0}</strong>
        </div>

        <div>
            <span>Concerns</span>
            <strong>{result.concerns?.length ?? 0}</strong>
        </div>

        <div>
            <span>Priority Actions</span>
            <strong>{result.recommendations?.length ?? 0}</strong>
        </div>

    </section>
    
</div>


<style>

    .health-report {
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


    h3 {
        margin: 0;

        color: #f7f7ff;

        font-size: 1.05rem;
    }


    /* OVERVIEW */

    .health-overview {
        display: grid;

        grid-template-columns:
            minmax(0, 1.2fr)
            minmax(220px, .8fr);

        gap: 14px;
    }


    .score-card,
    .assessment-card,
    .diagnostic-card,
    .priority-card {

        border:
            1px solid rgba(0,245,212,.22);

        background:
            linear-gradient(
                145deg,
                rgba(18,27,68,.9),
                rgba(5,10,32,.96)
            );
    }


    .score-card,
    .assessment-card {
        padding: 22px;
    }


    .score-top {
        display: flex;

        justify-content: space-between;
        align-items: flex-start;

        gap: 20px;
    }


    .score-line {
        display: flex;

        align-items: flex-end;

        line-height: 1;
    }


    .score-line strong {
        color: #f7f7ff;

        font-size: 3.7rem;
        font-weight: 900;
    }


    .score-line span {
        padding-bottom: 7px;

        color: #8190b6;

        font-size: .9rem;
        font-weight: 700;
    }


    .health-chip {
        padding: 7px 10px;

        border:
            1px solid rgba(255,0,127,.4);

        background:
            rgba(255,0,127,.08);

        color: #ff5bad;

        font-size: .68rem;
        font-weight: 900;
        letter-spacing: .08em;
        text-transform: uppercase;
    }


    .score-track {
        height: 7px;

        margin: 20px 0 14px;

        overflow: hidden;

        background:
            rgba(255,255,255,.07);
    }


    .score-fill {
        height: 100%;

        background:
            linear-gradient(
                90deg,
                #ff007f,
                #9400d3,
                #00f5d4
            );

        transition:
            width .5s ease;
    }


    .health-message {
        margin: 0;

        color: #aebbd8;

        line-height: 1.55;

        font-size: .84rem;
    }


    .assessment-card p:last-child {
        margin: 14px 0 0;

        color: #c8d4f3;

        line-height: 1.65;
    }


    /* DIAGNOSTICS */

    .diagnostic-grid {
        display: grid;

        grid-template-columns:
            repeat(2, minmax(0,1fr));

        gap: 14px;
    }


    .diagnostic-card {
        padding: 20px;
    }


    .strength {
        border-top:
            2px solid rgba(0,245,212,.65);
    }


    .concern {
        border-top:
            2px solid rgba(255,0,127,.65);
    }


    .card-heading {
        display: flex;

        justify-content: space-between;
        align-items: flex-start;

        gap: 16px;

        margin-bottom: 18px;
    }


    .count-badge {
        min-width: 30px;
        height: 30px;

        display: grid;
        place-items: center;

        border:
            1px solid rgba(0,245,212,.35);

        color: #00f5d4;

        font-size: .72rem;
        font-weight: 900;
    }


    .count-badge.risk {
        border-color:
            rgba(255,0,127,.4);

        color: #ff5bad;
    }


    .item-list {
        display: grid;

        gap: 10px;
    }


    .health-item {
        display: flex;

        align-items: flex-start;

        gap: 12px;

        padding: 12px;

        border:
            1px solid rgba(255,255,255,.07);

        background:
            rgba(255,255,255,.025);
    }


    .health-item p {
        margin: 0;

        color: #c8d4f3;

        line-height: 1.5;

        font-size: .82rem;
    }


    .item-number {
        flex: 0 0 28px;

        width: 28px;
        height: 28px;

        display: grid;
        place-items: center;

        border:
            1px solid rgba(0,245,212,.28);

        color: #00f5d4;

        font-size: .63rem;
        font-weight: 900;
    }


    .risk-number {
        border-color:
            rgba(255,0,127,.32);

        color: #ff5bad;
    }


    /* PRIORITIES */

    .priority-card {
        padding: 22px;
    }


    .priority-badge {
        padding: 7px 10px;

        border:
            1px solid rgba(255,0,127,.4);

        background:
            rgba(255,0,127,.07);

        color: #ff5bad;

        font-size: .67rem;
        font-weight: 900;
        letter-spacing: .08em;
        text-transform: uppercase;
    }


    .priority-list {
        display: grid;

        gap: 10px;
    }


    .priority-item {
        display: flex;

        gap: 14px;

        padding: 15px;

        border:
            1px solid rgba(255,255,255,.08);

        background:
            rgba(5,10,32,.45);
    }


    .priority-number {
        flex: 0 0 32px;

        width: 32px;
        height: 32px;

        display: grid;
        place-items: center;

        border:
            1px solid rgba(255,0,127,.38);

        color: #ff5bad;

        font-size: .65rem;
        font-weight: 900;
    }


    .priority-item strong {
        color: #f7f7ff;

        font-size: .8rem;
    }


    .priority-item p {
        margin: 5px 0 0;

        color: #b7c4e0;

        line-height: 1.55;

        font-size: .8rem;
    }


    /* FOOTER */

    .health-footer {
        display: grid;

        grid-template-columns:
            repeat(4, minmax(0,1fr));

        border:
            1px solid rgba(0,245,212,.18);

        background:
            rgba(8,15,43,.72);
    }


    .health-footer > div {
        min-width: 0;

        padding: 15px 18px;

        border-right:
            1px solid rgba(0,245,212,.12);
    }


    .health-footer > div:last-child {
        border-right: none;
    }


    .health-footer span {
        display: block;

        margin-bottom: 6px;

        color: #7f94c7;

        font-size: .7rem;
    }


    .health-footer strong {
        color: #ffffff;
    }


    /* ACTIONS */

    .actions {
        display: flex;

        flex-wrap: wrap;

        gap: 10px;
    }


    .action {
        min-height: 42px;

        padding: 0 15px;

        border:
            1px solid rgba(255,255,255,.13);

        border-radius: 5px;

        background:
            rgba(255,255,255,.035);

        color: #c9d3ec;

        font-weight: 800;
    }


    .primary {
        border-color:
            rgba(255,0,127,.5);

        background:
            linear-gradient(
                90deg,
                rgba(148,0,211,.55),
                rgba(255,0,127,.55)
            );

        color: white;
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

.health-actions {
  display: flex;
  align-items: center;
  gap: 10px;
  flex-wrap: wrap;
}

.health-actions button {
  min-height: 40px;
  padding: 0 14px;
  border-radius: 5px;
  font-family: inherit;
  font-weight: 800;
}

.copy-action {
  border: 1px solid rgba(255, 0, 127, .5);
  background: linear-gradient(
    90deg,
    rgba(148, 0, 211, .7),
    rgba(255, 0, 127, .7)
  );
  color: white;
  cursor: pointer;
}

.save-action {
  border: 1px solid rgba(0, 245, 212, .42);
  background: rgba(0, 245, 212, .06);
  color: #00f5d4;
  cursor: pointer;
}

.save-action:hover:not(:disabled) {
  background: rgba(0, 245, 212, .12);
}

.save-action.saved {
  opacity: .7;
  cursor: default;
}

.export-action {
  border: 1px solid rgba(255, 255, 255, .13);
  background: rgba(255, 255, 255, .035);
  color: #8290b3;
  cursor: not-allowed;
}

.export-action span {
  margin-left: 6px;
  font-size: .61rem;
  text-transform: uppercase;
}

.saved-message {
  padding: 10px 13px;
  border: 1px solid rgba(0, 245, 212, .22);
  background: rgba(0, 245, 212, .05);
  color: #00f5d4;
  font-size: .78rem;
  font-weight: 700;
}

    /* RESPONSIVE */

    @media (max-width: 1050px) {

        .health-overview,
        .diagnostic-grid {
            grid-template-columns: 1fr;
        }

        .health-footer {
            grid-template-columns:
                repeat(2, minmax(0,1fr));
        }

    }


    @media (max-width: 640px) {

        .score-top,
        .card-heading {
            flex-direction: column;
        }

        .health-footer {
            grid-template-columns: 1fr;
        }

        .health-footer > div {
            border-right: none;

            border-bottom:
                1px solid rgba(0,245,212,.12);
        }

        .health-footer > div:last-child {
            border-bottom: none;
        }

    }

</style>