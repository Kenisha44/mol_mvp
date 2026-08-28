<script>
  import { saveAnalysis } from '../../lib/analysisStorage.js';
  import { saveAnalysisToCloud } from '../../lib/analysisCloudStorage.js';

  import {
    exportAnalysisPDF,
    exportAnalysisDOCX
  } from '../../lib/exportService.js';

  import {
    canExport,
    recordExportUsage
  } from '../../lib/usageService.js';

  import UsageLimitNotice
  from './UsageLimitNotice.svelte';

  export let toolId = '';
  export let toolName = '';
  export let title = 'Saved Analysis';
  export let status = 'Saved';
  export let preview = '';
  export let input = '';
  export let result = null;

  export let showSave = true;
  export let showPDF = true;
  export let showDOCX = true;
  export let onUpgrade = () => {};

  let isSaved = false;
  let savedLabel = '';

  let isExportingPDF = false;
  let isExportingDOCX = false;
  let exportError = '';

  $: exportLimitReached =
    exportError?.includes(
      'You have reached your 3 free exports'
    );

  function buildPayload() {
    return {
      toolId,
      toolName,
      title,
      status,
      preview,
      input,
      result,
      createdAt: new Date().toISOString()
    };
  }


  async function saveCurrentAnalysis() {
  if (isSaved || !result) return;

  exportError = '';

  const payload = buildPayload();

  try {
    saveAnalysis(payload);

    await saveAnalysisToCloud({
      toolId: payload.toolId,
      title: payload.title,
      input: {
        text: payload.input,
        toolName: payload.toolName,
        status: payload.status,
        preview: payload.preview
      },
      result: payload.result
    });

    isSaved = true;
    savedLabel = 'Saved to Workspace';

    setTimeout(() => {
      savedLabel = '';
    }, 1800);
  } catch (error) {
    console.error(error);

    exportError =
      error?.message ||
      'Unable to save analysis.';
  }
}


  async function handlePDFExport() {
    if (isExportingPDF || !result) return;

    exportError = '';

    const usageCheck = canExport();

    if (!usageCheck.allowed) {
      exportError = usageCheck.reason;
      return;
    }

    isExportingPDF = true;

    try {
      await exportAnalysisPDF(
        buildPayload()
      );

      await recordExportUsage();

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
  if (isExportingDOCX || !result) return;

  exportError = '';

  const usageCheck = canExport();

  if (!usageCheck.allowed) {
    exportError = usageCheck.reason;
    return;
  }

  isExportingDOCX = true;

  try {
    await exportAnalysisDOCX(
      buildPayload()
    );

    await recordExportUsage();

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


<div class="export-actions">

  {#if showSave}
    <button
      type="button"
      class="save-action"
      class:saved={isSaved}
      on:click={saveCurrentAnalysis}
      disabled={isSaved || !result}
    >
      {#if isSaved}
        Saved ✓
      {:else}
        Save to Workspace
      {/if}
    </button>
  {/if}


  {#if showDOCX}
    <button
      type="button"
      class="export-action"
      on:click={handleDOCXExport}
      disabled={isExportingDOCX || !result}
    >
      {#if isExportingDOCX}
        Exporting DOCX...
      {:else}
        Export DOCX
      {/if}
    </button>
  {/if}


  {#if showPDF}
    <button
      type="button"
      class="export-action"
      on:click={handlePDFExport}
      disabled={isExportingPDF || !result}
    >
      {#if isExportingPDF}
        Exporting PDF...
      {:else}
        Export PDF
      {/if}
    </button>
  {/if}

</div>


{#if savedLabel}
  <div class="saved-message">
    {savedLabel}
  </div>
{/if}


{#if exportLimitReached}

  <UsageLimitNotice
    message="You've used all 3 exports included with your Free plan. Upgrade to MOL Pro for unlimited exports."
    type="export"
    {onUpgrade}
  />

{:else if exportError}

  <div class="export-error">
    {exportError}
  </div>

{/if}


<style>
  .export-actions {
    display: flex;
    align-items: center;
    flex-wrap: wrap;

    gap: 10px;
  }


  .export-actions button {
    min-height: 40px;

    padding: 0 14px;

    border-radius: 5px;

    font-family: inherit;
    font-weight: 800;
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


  .export-action {
    border:
      1px solid rgba(255, 0, 127, .36);

    background:
      rgba(255, 0, 127, .045);

    color: #ff67b4;

    cursor: pointer;
  }


  .export-action:hover:not(:disabled) {
    background:
      rgba(255, 0, 127, .10);
  }


  .export-actions button:disabled {
    opacity: .55;

    cursor: not-allowed;
  }


  .saved-message,
  .export-error {
    margin-top: 10px;

    padding: 10px 13px;

    font-size: .78rem;
    font-weight: 700;
  }


  .saved-message {
    border:
      1px solid rgba(0, 245, 212, .22);

    background:
      rgba(0, 245, 212, .05);

    color: #00f5d4;
  }


  .export-error {
    border:
      1px solid rgba(255, 0, 127, .30);

    background:
      rgba(255, 0, 127, .05);

    color: #ff5bad;
  }


  @media (max-width: 640px) {
    .export-actions {
      width: 100%;
    }

    .export-actions button {
      flex: 1 1 auto;
    }
  }
</style>