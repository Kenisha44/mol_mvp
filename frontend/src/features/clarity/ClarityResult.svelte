<script>
  export let result;
  export let onCopy = () => {};

  $: score = Number(result?.score ?? 0);

  $: scoreLabel =
    score >= 90
      ? 'Executive Ready'
      : score >= 75
        ? 'Strong'
        : score >= 60
          ? 'Needs Refinement'
          : 'Needs Attention';

  $: scoreMessage =
    score >= 90
      ? 'The copy is concise, focused, and well positioned for executive communication.'
      : score >= 75
        ? 'The message is strong, with a few opportunities to improve focus and decision clarity.'
        : score >= 60
          ? 'The core message is present, but the communication can be sharper and more executive-focused.'
          : 'The content would benefit from significant simplification, prioritization, and clearer direction.';
</script>

<div class="clarity-result">
  <section class="result-overview">
    <div class="score-card">
      <div class="score-top">
        <div>
          <p class="eyebrow">Clarity Score</p>

          <div class="score-line">
            <strong>{score}</strong>
            <span>/100</span>
          </div>
        </div>

        <span class="score-status">
          {scoreLabel}
        </span>
      </div>

      <div class="score-track">
        <div
          class="score-fill"
          style={`width: ${Math.min(Math.max(score, 0), 100)}%`}
        ></div>
      </div>

      <p class="score-message">
        {scoreMessage}
      </p>
    </div>
    
<div class="recommendation-card">
  <p class="eyebrow">RECOMMENDATION</p>
  <p>{result.recommendation}</p>
</div>
    <div class="status-card">
      <p class="eyebrow">Analysis Status</p>

      <strong>
        {result.label}
      </strong>

      <span>
        MOL reviewed the copy for executive clarity, focus, and decision-readiness.
      </span>
    </div>
  </section>

  <section class="rewrite-card">
    <div class="card-header">
      <div>
        <p class="eyebrow">Executive-Ready Version</p>
        <h3>Refined Executive Copy</h3>
      </div>

      <button
        type="button"
        class="copy-button"
        on:click={onCopy}
      >
        Copy Output
      </button>
    </div>

   <div class="refined-copy">
  <p>{result.refined_text}</p>
</div>
  </section>

  <section class="analysis-footer">
    <div class="signal">
      <span class="signal-icon">01</span>

      <div>
        <strong>Executive Focus</strong>
        <p>
          Prioritizes the information leadership needs to understand first.
        </p>
      </div>
    </div>

    <div class="signal">
      <span class="signal-icon">02</span>

      <div>
        <strong>Decision Clarity</strong>
        <p>
          Pushes the communication toward implications and next-step thinking.
        </p>
      </div>
    </div>

    <div class="signal">
      <span class="signal-icon">03</span>

      <div>
        <strong>Concise Language</strong>
        <p>
          Reduces unnecessary wording while preserving the core business message.
        </p>
      </div>
    </div>
  </section>

  <div class="future-actions">
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
      title="Coming with Workspace"
    >
      Save
      <span>Coming Soon</span>
    </button>

    <button
      type="button"
      class="action"
      disabled
      title="Coming with Export Center"
    >
      Export
      <span>Coming Soon</span>
    </button>
  </div>
</div>

<style>
  .clarity-result {
    display: grid;
    gap: 18px;
  }

  .result-overview {
    display: grid;
    grid-template-columns: minmax(0, 1.35fr) minmax(190px, .65fr);
    gap: 14px;
  }

  .score-card,
  .status-card,
  .rewrite-card {
    border: 1px solid rgba(0, 245, 212, .22);
    background:
      linear-gradient(
        145deg,
        rgba(18, 27, 68, .9),
        rgba(5, 10, 32, .96)
      );
  }

  .score-card,
  .status-card {
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

  .score-top {
    display: flex;
    justify-content: space-between;
    gap: 20px;
    align-items: flex-start;
  }

  .score-line {
    display: flex;
    align-items: flex-end;
    line-height: 1;
  }

  .score-line strong {
    color: #f7f7ff;
    font-size: 3.3rem;
    font-weight: 900;
  }

  .score-line span {
    padding-bottom: 6px;
    color: #8190b6;
    font-size: .9rem;
    font-weight: 700;
  }

  .score-status {
    padding: 7px 10px;
    border: 1px solid rgba(255, 0, 127, .38);
    background: rgba(255, 0, 127, .08);
    color: #ff5bad;
    font-size: .68rem;
    font-weight: 900;
    letter-spacing: .08em;
    text-transform: uppercase;
  }

  .score-track {
    height: 6px;
    margin: 18px 0 14px;
    overflow: hidden;
    background: rgba(255, 255, 255, .07);
  }

  .score-fill {
    height: 100%;
    background: linear-gradient(
      90deg,
      #9400d3,
      #ff007f,
      #00f5d4
    );
    transition: width .5s ease;
  }

  .score-message {
    margin: 0;
    color: #aebbd8;
    line-height: 1.55;
    font-size: .84rem;
  }

  .status-card {
    display: flex;
    flex-direction: column;
  }

  .status-card strong {
    margin-bottom: 9px;
    color: #f7f7ff;
    font-size: 1.05rem;
  }

  .status-card span {
    color: #93a1c5;
    line-height: 1.5;
    font-size: .8rem;
  }

  .rewrite-card {
    padding: 22px;
  }

  .card-header {
    display: flex;
    justify-content: space-between;
    gap: 20px;
    align-items: flex-start;
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

  .rewrite {
    padding: 20px;
    border-left: 3px solid #ff007f;
    background: rgba(0, 0, 0, .18);
    color: #ecf0ff;
    line-height: 1.7;
    white-space: pre-wrap;
    overflow-wrap: anywhere;
  }

  .analysis-footer {
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

  .signal-icon {
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

  .future-actions {
    display: flex;
    gap: 10px;
    padding-top: 4px;
    flex-wrap: wrap;
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

  .primary-action {
    border-color: rgba(255, 0, 127, .5);
    background: linear-gradient(
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
.refined-copy {
  margin-top: 16px;
  padding: 22px;

  border-left: 3px solid #ff007f;
  background: rgba(5, 8, 23, 0.45);

  color: #f7f7ff;
  font-size: 1rem;
  line-height: 1.7;

  white-space: pre-wrap;
  overflow-wrap: anywhere;
}

.refined-copy p {
  margin: 0;
}

.recommendation-card {
  margin-top: 18px;
  padding: 18px 20px;

  border: 1px solid rgba(0, 245, 212, 0.2);
  background: rgba(0, 245, 212, 0.04);

  color: #c7d2ee;
  line-height: 1.55;
}

.recommendation-card p:last-child {
  margin-bottom: 0;
}
  @media (max-width: 1050px) {
    .result-overview,
    .analysis-footer {
      grid-template-columns: 1fr;
    }
  }

  @media (max-width: 640px) {
    .card-header,
    .score-top {
      flex-direction: column;
    }
  }
</style>