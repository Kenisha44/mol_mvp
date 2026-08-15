<script>
  export let result;
  export let onCopy = () => {};
</script>

<div class="memo-report">

  <section class="memo-document">

    <div class="memo-header">
      <div>
        <p class="eyebrow">EXECUTIVE MEMO</p>
        <h2>{result.title}</h2>
      </div>

      <button
        type="button"
        class="copy-button"
        on:click={onCopy}
      >
        Copy Memo
      </button>
    </div>

    <div class="memo-meta">
      <span>Leadership Communication</span>
      <span>Structured Executive Format</span>
      <span>Decision-Ready Output</span>
    </div>


    <section class="summary-card">
      <p class="section-label">EXECUTIVE SUMMARY</p>

      <div class="summary-copy">
        {result.summary}
      </div>
    </section>


    <div class="memo-grid">

      <section class="memo-card">
        <div class="section-number">01</div>

        <div>
          <p class="section-label">BACKGROUND</p>
          <h3>Situation & Context</h3>

          <p>{result.background}</p>
        </div>
      </section>


      <section class="memo-card">
        <div class="section-number">02</div>

        <div>
          <p class="section-label">KEY FINDINGS</p>
          <h3>What Leadership Should Know</h3>

          <p>{result.findings}</p>
        </div>
      </section>

    </div>


    <div class="memo-grid">

      <section class="memo-card impact">
        <div class="section-number">03</div>

        <div>
          <p class="section-label">BUSINESS IMPACT</p>
          <h3>Why It Matters</h3>

          <p>{result.impact}</p>
        </div>
      </section>


      <section class="memo-card recommendations">
        <div class="section-number">04</div>

        <div>
          <p class="section-label">RECOMMENDATIONS</p>
          <h3>Leadership Direction</h3>

          <p>{result.recommendations}</p>
        </div>
      </section>

    </div>


    <section class="next-step-card">

      <div class="section-heading">

        <div>
          <p class="section-label">NEXT STEP</p>
          <h3>Decision & Follow-Up</h3>
        </div>

        <span class="ready-badge">
          READY TO SHARE
        </span>

      </div>

      <p>
        {result.next_steps}
      </p>

    </section>


    <div class="memo-actions">

      <button
        type="button"
        class="action primary"
        on:click={onCopy}
      >
        Copy Full Memo
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
        Export DOCX
        <span>Coming Soon</span>
      </button>

      <button
        type="button"
        class="action"
        disabled
      >
        Export PDF
        <span>Coming Soon</span>
      </button>

    </div>

  </section>

</div>


<style>

  .memo-report {
    width: 100%;
    min-width: 0;
  }


  .memo-document {
    display: grid;
    gap: 18px;

    padding: 24px;

    border: 1px solid rgba(0,245,212,.22);

    background:
      radial-gradient(
        circle at top right,
        rgba(148,0,211,.08),
        transparent 34%
      ),
      rgba(5,10,32,.88);
  }


  /* HEADER */

  .memo-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;

    gap: 20px;
  }

  .eyebrow,
  .section-label {
    margin: 0 0 8px;

    color: #00f5d4;

    font-size: .7rem;
    font-weight: 900;
    letter-spacing: .12em;
    text-transform: uppercase;
  }

  h2,
  h3 {
    margin: 0;

    color: #f7f7ff;
  }

  h2 {
    font-size: 1.5rem;
  }

  h3 {
    font-size: 1rem;
  }

  .copy-button {
    flex: 0 0 auto;

    padding: 9px 12px;

    border: 1px solid rgba(0,245,212,.32);
    border-radius: 5px;

    background: rgba(0,245,212,.06);
    color: #00f5d4;

    font-weight: 800;

    cursor: pointer;
  }

  .copy-button:hover {
    background: rgba(0,245,212,.12);
  }


  /* META */

  .memo-meta {
    display: flex;
    flex-wrap: wrap;

    gap: 8px;
  }

  .memo-meta span {
    padding: 6px 9px;

    border: 1px solid rgba(255,255,255,.08);

    background: rgba(255,255,255,.025);

    color: #8193bd;

    font-size: .7rem;
  }


  /* SUMMARY */

  .summary-card {
    padding: 22px;

    border: 1px solid rgba(255,0,127,.25);

    background:
      linear-gradient(
        135deg,
        rgba(148,0,211,.08),
        rgba(255,0,127,.03)
      );
  }

  .summary-copy {
    padding: 20px;

    border-left: 3px solid #ff007f;

    background: rgba(0,0,0,.18);

    color: #f7f7ff;

    font-size: 1rem;
    line-height: 1.7;
  }


  /* GRID */

  .memo-grid {
    display: grid;

    grid-template-columns:
      repeat(2, minmax(0,1fr));

    gap: 14px;
  }

  .memo-card {
    display: flex;

    gap: 14px;

    padding: 20px;

    border: 1px solid rgba(0,245,212,.18);

    background: rgba(16,27,69,.68);
  }

  .section-number {
    flex: 0 0 30px;

    width: 30px;
    height: 30px;

    display: grid;
    place-items: center;

    border: 1px solid rgba(0,245,212,.35);

    color: #00f5d4;

    font-size: .68rem;
    font-weight: 900;
  }

  .memo-card p:last-child {
    margin: 10px 0 0;

    color: #c8d4f3;

    line-height: 1.65;
  }

  .impact {
    border-top: 2px solid rgba(255,0,127,.55);
  }

  .recommendations {
    border-top: 2px solid rgba(0,245,212,.55);
  }


  /* NEXT STEP */

  .next-step-card {
    padding: 22px;

    border: 1px solid rgba(0,245,212,.22);

    background: rgba(8,15,43,.72);
  }

  .section-heading {
    display: flex;

    justify-content: space-between;
    align-items: flex-start;

    gap: 20px;

    margin-bottom: 14px;
  }

  .ready-badge {
    padding: 7px 10px;

    border: 1px solid rgba(255,0,127,.4);

    background: rgba(255,0,127,.07);

    color: #ff5bad;

    font-size: .68rem;
    font-weight: 900;
    letter-spacing: .08em;
    text-transform: uppercase;
  }

  .next-step-card > p {
    margin: 0;

    color: #dce4f8;

    line-height: 1.7;
  }


  /* ACTIONS */

  .memo-actions {
    display: flex;
    flex-wrap: wrap;

    gap: 10px;

    padding-top: 4px;
  }

  .action {
    min-height: 42px;

    padding: 0 15px;

    border: 1px solid rgba(255,255,255,.13);
    border-radius: 5px;

    background: rgba(255,255,255,.035);
    color: #c9d3ec;

    font-weight: 800;
  }

  .primary {
    border-color: rgba(255,0,127,.5);

    background:
      linear-gradient(
        90deg,
        rgba(148,0,211,.55),
        rgba(255,0,127,.55)
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

  @media (max-width: 900px) {

    .memo-grid {
      grid-template-columns: 1fr;
    }

  }

  @media (max-width: 640px) {

    .memo-header,
    .section-heading {
      flex-direction: column;
    }

  }

</style>