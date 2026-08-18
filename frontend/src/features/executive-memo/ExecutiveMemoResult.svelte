<script>
  import { saveAnalysis } from '../../lib/analysisStorage.js';

  import {
    exportAnalysisPDF,
    exportAnalysisDOCX
  } from '../../lib/exportService.js';

  export let result;
  export let onCopy = () => {};
  export let inputText = '';

  let isSaved = false;
  let savedLabel = '';

  let isExportingPDF = false;
  let isExportingDOCX = false;
  let exportError = '';


  function saveCurrentAnalysis() {
    if (isSaved) return;

    saveAnalysis({
      toolId: 'executive-memo',
      toolName: 'Executive Memo Studio',

      title:
        result?.title ||
        'Executive Memo',

      status:
        result?.memo_type ||
        'Executive Ready',

      preview:
        result?.summary ||
        result?.background ||
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


  function getExportPayload() {
    return {
      toolId: 'executive-memo',
      toolName: 'Executive Memo Studio',

      title:
        result?.title ||
        'Executive Memo',

      status:
        result?.memo_type ||
        'Executive Ready',

      createdAt: new Date().toISOString(),

      input: inputText,

      result
    };
  }


  async function handlePDFExport() {
    if (isExportingPDF) return;

    isExportingPDF = true;
    exportError = '';

    try {
      await exportAnalysisPDF(
        getExportPayload()
      );
    } catch (error) {
      console.error(error);

      exportError =
        error?.message ||
        'Unable to export PDF.';
    } finally {
      isExportingPDF = false;
    }
  }


  async function handleDOCXExport() {
    if (isExportingDOCX) return;

    isExportingDOCX = true;
    exportError = '';

    try {
      await exportAnalysisDOCX(
        getExportPayload()
      );
    } catch (error) {
      console.error(error);

      exportError =
        error?.message ||
        'Unable to export DOCX.';
    } finally {
      isExportingDOCX = false;
    }
  }
</script>


<div class="memo-report">

  <section class="memo-document">

    <!-- HEADER -->
    <div class="memo-header">

      <div>
        <p class="eyebrow">
          EXECUTIVE MEMO
        </p>

        <h2>
          {result.title}
        </h2>
      </div>


      <div class="memo-actions">

        <button
          type="button"
          class="copy-action"
          on:click={onCopy}
        >
          Copy Memo
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
          class="docx-action"
          on:click={handleDOCXExport}
          disabled={isExportingDOCX}
        >
          {#if isExportingDOCX}
            Exporting DOCX...
          {:else}
            Export DOCX
          {/if}
        </button>


        <button
          type="button"
          class="pdf-action"
          on:click={handlePDFExport}
          disabled={isExportingPDF}
        >
          {#if isExportingPDF}
            Exporting PDF...
          {:else}
            Export PDF
          {/if}
        </button>

      </div>

    </div>


    <!-- STATUS MESSAGES -->
    {#if savedLabel}
      <div class="saved-message">
        {savedLabel}
      </div>
    {/if}


    {#if exportError}
      <div class="export-error">
        {exportError}
      </div>
    {/if}


    <!-- META -->
    <div class="memo-meta">
      <span>Leadership Communication</span>
      <span>Structured Executive Format</span>
      <span>Decision-Ready Output</span>
    </div>


    <!-- EXECUTIVE SUMMARY -->
    <section class="summary-card">

      <p class="section-label">
        EXECUTIVE SUMMARY
      </p>

      <div class="summary-copy">
        {result.summary}
      </div>

    </section>


    <!-- BACKGROUND + FINDINGS -->
    <div class="memo-grid">

      <section class="memo-card">

        <div class="section-number">
          01
        </div>

        <div>
          <p class="section-label">
            BACKGROUND
          </p>

          <h3>
            Situation & Context
          </h3>

          <p>
            {result.background}
          </p>
        </div>

      </section>


      <section class="memo-card">

        <div class="section-number">
          02
        </div>

        <div>
          <p class="section-label">
            KEY FINDINGS
          </p>

          <h3>
            What Leadership Should Know
          </h3>

          <p>
            {result.findings}
          </p>
        </div>

      </section>

    </div>


    <!-- IMPACT + RECOMMENDATIONS -->
    <div class="memo-grid">

      <section class="memo-card impact">

        <div class="section-number">
          03
        </div>

        <div>
          <p class="section-label">
            BUSINESS IMPACT
          </p>

          <h3>
            Why It Matters
          </h3>

          <p>
            {result.impact}
          </p>
        </div>

      </section>


      <section class="memo-card recommendations">

        <div class="section-number">
          04
        </div>

        <div>
          <p class="section-label">
            RECOMMENDATIONS
          </p>

          <h3>
            Leadership Direction
          </h3>

          <p>
            {result.recommendations}
          </p>
        </div>

      </section>

    </div>


    <!-- NEXT STEP -->
    <section class="next-step-card">

      <div class="section-heading">

        <div>
          <p class="section-label">
            NEXT STEP
          </p>

          <h3>
            Decision & Follow-Up
          </h3>
        </div>

        <span class="ready-badge">
          READY TO SHARE
        </span>

      </div>

      <p>
        {result.next_steps}
      </p>

    </section>

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

    border:
      1px solid rgba(0, 245, 212, .22);

    background:
      radial-gradient(
        circle at top right,
        rgba(148, 0, 211, .08),
        transparent 34%
      ),
      rgba(5, 10, 32, .88);
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


  /* HEADER ACTIONS */

  .memo-actions {
    display: flex;

    align-items: center;
    justify-content: flex-end;

    gap: 10px;

    flex-wrap: wrap;
  }


  .memo-actions button {
    min-height: 40px;

    padding: 0 14px;

    border-radius: 5px;

    font-family: inherit;
    font-weight: 800;
  }


  .copy-action {
    border:
      1px solid rgba(255, 0, 127, .5);

    background:
      linear-gradient(
        90deg,
        rgba(148, 0, 211, .7),
        rgba(255, 0, 127, .7)
      );

    color: white;

    cursor: pointer;
  }


  .copy-action:hover {
    filter: brightness(1.08);
  }


  .save-action {
    border:
      1px solid rgba(0, 245, 212, .42);

    background:
      rgba(0, 245, 212, .06);

    color: #00f5d4;

    cursor: pointer;
  }


  .save-action:hover:not(:disabled) {
    background:
      rgba(0, 245, 212, .12);
  }


  .save-action.saved {
    border-color:
      rgba(0, 245, 212, .35);

    background:
      rgba(0, 245, 212, .10);

    color: #00f5d4;

    opacity: .75;

    cursor: default;
  }


  .docx-action,
  .pdf-action {
    border:
      1px solid rgba(0, 245, 212, .32);

    background:
      rgba(0, 245, 212, .045);

    color: #00f5d4;

    cursor: pointer;
  }


  .docx-action:hover:not(:disabled),
  .pdf-action:hover:not(:disabled) {
    background:
      rgba(0, 245, 212, .11);
  }


  .docx-action:disabled,
  .pdf-action:disabled {
    opacity: .55;

    cursor: wait;
  }


  /* MESSAGES */

  .saved-message {
    padding: 10px 13px;

    border:
      1px solid rgba(0, 245, 212, .22);

    background:
      rgba(0, 245, 212, .05);

    color: #00f5d4;

    font-size: .78rem;
    font-weight: 700;
  }


  .export-error {
    padding: 10px 13px;

    border:
      1px solid rgba(255, 0, 127, .3);

    background:
      rgba(255, 0, 127, .05);

    color: #ff5bad;

    font-size: .78rem;
    font-weight: 700;
  }


  /* META */

  .memo-meta {
    display: flex;
    flex-wrap: wrap;

    gap: 8px;
  }


  .memo-meta span {
    padding: 6px 9px;

    border:
      1px solid rgba(255, 255, 255, .08);

    background:
      rgba(255, 255, 255, .025);

    color: #8193bd;

    font-size: .7rem;
  }


  /* SUMMARY */

  .summary-card {
    padding: 22px;

    border:
      1px solid rgba(255, 0, 127, .25);

    background:
      linear-gradient(
        135deg,
        rgba(148, 0, 211, .08),
        rgba(255, 0, 127, .03)
      );
  }


  .summary-copy {
    padding: 20px;

    border-left:
      3px solid #ff007f;

    background:
      rgba(0, 0, 0, .18);

    color: #f7f7ff;

    font-size: 1rem;

    line-height: 1.7;

    white-space: pre-wrap;
    overflow-wrap: anywhere;
  }


  /* GRID */

  .memo-grid {
    display: grid;

    grid-template-columns:
      repeat(2, minmax(0, 1fr));

    gap: 14px;
  }


  .memo-card {
    display: flex;

    gap: 14px;

    min-width: 0;

    padding: 20px;

    border:
      1px solid rgba(0, 245, 212, .18);

    background:
      rgba(16, 27, 69, .68);
  }


  .section-number {
    flex: 0 0 30px;

    width: 30px;
    height: 30px;

    display: grid;
    place-items: center;

    border:
      1px solid rgba(0, 245, 212, .35);

    color: #00f5d4;

    font-size: .68rem;
    font-weight: 900;
  }


  .memo-card p:last-child {
    margin: 10px 0 0;

    color: #c8d4f3;

    line-height: 1.65;

    overflow-wrap: anywhere;
  }


  .impact {
    border-top:
      2px solid rgba(255, 0, 127, .55);
  }


  .recommendations {
    border-top:
      2px solid rgba(0, 245, 212, .55);
  }


  /* NEXT STEP */

  .next-step-card {
    padding: 22px;

    border:
      1px solid rgba(0, 245, 212, .22);

    background:
      rgba(8, 15, 43, .72);
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

    border:
      1px solid rgba(255, 0, 127, .4);

    background:
      rgba(255, 0, 127, .07);

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

    overflow-wrap: anywhere;
  }


  /* RESPONSIVE */

  @media (max-width: 1100px) {
    .memo-header {
      flex-direction: column;
    }

    .memo-actions {
      justify-content: flex-start;
    }
  }


  @media (max-width: 900px) {
    .memo-grid {
      grid-template-columns: 1fr;
    }
  }


  @media (max-width: 640px) {
    .section-heading {
      flex-direction: column;
    }

    .memo-actions {
      width: 100%;
    }

    .memo-actions button {
      flex: 1 1 auto;
    }
  }

</style>