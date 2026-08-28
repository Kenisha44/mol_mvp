<script>
  import LoadingState from '../../components/ui/LoadingState.svelte';
  import EmptyState from '../../components/ui/EmptyState.svelte';
  import KpiCleanerResult from './KpiCleanerResult.svelte';
  import { cleanKpi } from './kpiCleanerService.js';
  import UsageLimitNotice
    from '../../components/ui/UsageLimitNotice.svelte';

  export let onUpgrade = () => {};
  export let tool;

  let inputText = '';
  let result = null;
  let loading = false;
  let error = '';
  let copiedLabel = '';

  $: analysisLimitReached =
    error?.includes(
      'You have reached your 5 free analyses'
    );

  $: lineCount = inputText.trim()
    ? inputText.trim().split(/\r?\n/).filter(Boolean).length
    : 0;

  $: characterCount = inputText.length;

  function useSample() {
    inputText = tool.sample;
    result = null;
    error = '';
    copiedLabel = '';
  }

  function clearInput() {
    inputText = '';
    result = null;
    error = '';
    copiedLabel = '';
  }

  function outputText() {
    if (!result) return '';

    return [
      'Moon Onyx Labs — KPI Cleaner',
      '',
      `Issues Found: ${result.issues_found}`,
      `Status: ${result.label}`,
      '',
      result.result
    ].join('\n');
  }

  async function copyText(text, label = 'Copied') {
    try {
      await navigator.clipboard.writeText(text);
      copiedLabel = label;

      setTimeout(() => {
        copiedLabel = '';
      }, 1800);
    } catch {
      error = 'Copy failed. You can manually highlight and copy the output.';
    }
  }

  async function runTool() {
    if (!inputText.trim()) {
      error = 'Paste KPI text first so MOL can clean it.';
      return;
    }

    loading = true;
    error = '';
    result = null;
    copiedLabel = '';

    try {
      const [data] = await Promise.all([
        cleanKpi(inputText),
        new Promise((resolve) => setTimeout(resolve, 800))
      ]);

      result = data;
    } catch (err) {
      console.error(err);

      error =
        err?.message ||
        'Unable to complete the analysis. Please try again.';
    } finally {
      loading = false;
    }
  }
</script>

<div class="kpi-tool">
  <section class="input-panel">
    <div class="panel-header">
      <div>
        <p class="eyebrow">{tool.eyebrow}</p>
        <h2>{tool.title}</h2>

        <p class="description">
          {tool.description}
        </p>
      </div>

      <button
        type="button"
        class="sample-button"
        on:click={useSample}
      >
        Use Sample
      </button>
    </div>

    <div class="editor-shell">
      <div class="editor-label-row">
        <label for="kpi-input">Raw KPI List</label>

        <div class="editor-meta">
          <span>{lineCount} KPI{lineCount === 1 ? '' : 's'}</span>
          <span>{characterCount} characters</span>
        </div>
      </div>

      <textarea
        id="kpi-input"
        bind:value={inputText}
        placeholder={tool.placeholder}
      ></textarea>

      <div class="editor-footer">
        <span>
          Add one KPI per line for the cleanest result.
        </span>

        {#if inputText}
          <button
            type="button"
            class="text-action"
            on:click={clearInput}
          >
            Clear
          </button>
        {/if}
      </div>
    </div>

    <div class="format-hint">
      <p class="hint-label">Recommended Input Format</p>

      <div class="hint-grid">
        <span>rev growth q1</span>
        <span>cust churn</span>
        <span>mrr</span>
        <span>cac</span>
      </div>
    </div>

    <div class="actions">
      <button
        type="button"
        class="run-button"
        on:click={runTool}
        disabled={loading}
      >
        {#if loading}
          <span class="loader"></span>
          Cleaning KPI Signal...
        {:else}
          Run KPI Cleaner
        {/if}
      </button>

      {#if inputText}
        <button
          type="button"
          class="secondary-button"
          on:click={() => copyText(inputText, 'Input copied')}
        >
          Copy Input
        </button>
      {/if}
    </div>

    {#if analysisLimitReached}

    <UsageLimitNotice
      message="You've used all 5 analyses included with your Free plan. Upgrade to MOL Pro for up to 100 analyses each month."
      type="analysis"
      {onUpgrade}
    />

  {:else if error}

    <div class="error-message">
      {error}
    </div>

  {/if}

    {#if copiedLabel}
      <div class="message success">
        {copiedLabel}
      </div>
    {/if}
  </section>

  <section class="output-panel">
    <div class="output-header">
      <div>
        <p class="eyebrow">KPI Analysis</p>
        <h3>Cleaned KPI response</h3>
      </div>

      {#if result}
        <span class="status-badge">
          Cleanup Complete
        </span>
      {/if}
    </div>

    {#if loading}
      <LoadingState />
    {:else if result}
<KpiCleanerResult
  {result}
  inputText={inputText}
  onCopy={() => copyText(outputText(), 'Output copied')}
/>
    {:else}
      <EmptyState
        title={tool.emptyTitle}
        body={tool.emptyBody}
        sample={tool.sample}
        onAction={useSample}
      />
    {/if}
  </section>
</div>

<style>
  .kpi-tool {
    display: grid;
    grid-template-columns: minmax(320px, .82fr) minmax(0, 1.5fr);
    min-height: 520px;

    border: 1px solid rgba(0, 245, 212, .28);

    background:
      radial-gradient(
        circle at top right,
        rgba(148, 0, 211, .08),
        transparent 32%
      ),
      #0b1230;
  }

  .input-panel {
    padding: 28px;
    border-right: 1px solid rgba(0, 245, 212, .22);
  }

  .output-panel {
    min-width: 0;
    padding: 28px;
    overflow: hidden;
  }

  .panel-header,
  .output-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 18px;
  }

  .eyebrow {
    margin: 0 0 8px;

    color: #00f5d4;

    font-size: .72rem;
    font-weight: 800;
    letter-spacing: .14em;
    text-transform: uppercase;
  }

  h2,
  h3 {
    margin: 0;
    color: #f7f7ff;
  }

  h2 {
    font-size: 1.8rem;
    line-height: 1.05;
  }

  h3 {
    font-size: 1.2rem;
  }

  .description {
    max-width: 38rem;
    margin: 12px 0 0;

    color: #b7c4e0;

    line-height: 1.55;
  }

  .sample-button {
    flex: 0 0 auto;

    padding: 9px 12px;

    border: 1px solid rgba(255, 255, 255, .16);
    border-radius: 6px;

    background: rgba(255, 255, 255, .04);
    color: #f7f7ff;

    font-weight: 700;
    cursor: pointer;
  }

  .sample-button:hover {
    border-color: rgba(0, 245, 212, .55);
  }

  .editor-shell {
    margin-top: 26px;

    border: 1px solid rgba(0, 245, 212, .24);

    background: rgba(3, 8, 27, .64);
  }

  .editor-label-row,
  .editor-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 16px;
  }

  .editor-label-row {
    padding: 12px 14px;

    border-bottom: 1px solid rgba(255, 255, 255, .08);
  }

  .editor-label-row label {
    color: #f7f7ff;

    font-size: .82rem;
    font-weight: 800;
    letter-spacing: .08em;
    text-transform: uppercase;
  }

  .editor-meta {
    display: flex;
    gap: 12px;

    color: #8293ba;

    font-size: .72rem;
  }

  textarea {
    display: block;

    width: 100%;
    min-height: 250px;

    box-sizing: border-box;

    padding: 18px;

    border: 0;
    outline: 0;

    resize: vertical;

    background: transparent;
    color: #f7f7ff;

    font: inherit;
    line-height: 1.65;
  }

  textarea::placeholder {
    color: #68779e;
  }

  textarea:focus {
    box-shadow:
      inset 0 0 0 1px rgba(0, 245, 212, .5);
  }

  .editor-footer {
    padding: 10px 14px;

    border-top: 1px solid rgba(255, 255, 255, .08);

    color: #8293ba;

    font-size: .72rem;
  }

  .text-action {
    padding: 0;

    border: 0;

    background: transparent;
    color: #00f5d4;

    font-weight: 800;
    cursor: pointer;
  }

  .format-hint {
    margin-top: 14px;
    padding: 14px;

    border: 1px solid rgba(255, 255, 255, .07);

    background: rgba(255, 255, 255, .025);
  }

  .hint-label {
    margin: 0 0 10px;

    color: #8190b6;

    font-size: .68rem;
    font-weight: 800;
    letter-spacing: .08em;
    text-transform: uppercase;
  }

  .hint-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 7px;
  }

  .hint-grid span {
    padding: 5px 8px;

    border: 1px solid rgba(0, 245, 212, .18);

    background: rgba(0, 245, 212, .04);
    color: #aab8d8;

    font-family: monospace;
    font-size: .7rem;
  }

  .actions {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;

    margin-top: 18px;
  }

  .run-button,
  .secondary-button {
    min-height: 46px;

    padding: 0 18px;

    border-radius: 6px;

    font-weight: 800;
  }

  .run-button {
    flex: 1;

    min-width: 210px;

    border: 1px solid #ff007f;

    background:
      linear-gradient(
        90deg,
        #9400d3,
        #ff007f
      );

    color: white;

    cursor: pointer;
  }

  .run-button:hover:not(:disabled) {
    filter: brightness(1.08);
  }

  .run-button:disabled {
    opacity: .6;
    cursor: wait;
  }

  .secondary-button {
    border: 1px solid rgba(0, 245, 212, .28);

    background: rgba(0, 245, 212, .06);
    color: #00f5d4;

    cursor: pointer;
  }

  .secondary-button:hover {
    background: rgba(0, 245, 212, .11);
  }

  .output-header {
    margin-bottom: 18px;
    padding-bottom: 18px;

    border-bottom: 1px solid rgba(255, 255, 255, .08);
  }

  .status-badge {
    padding: 7px 10px;

    border: 1px solid rgba(0, 245, 212, .28);

    background: rgba(0, 245, 212, .07);
    color: #00f5d4;

    font-size: .7rem;
    font-weight: 800;
    letter-spacing: .08em;
    text-transform: uppercase;
  }

  .message {
    margin-top: 14px;
    padding: 12px 14px;

    border-radius: 6px;

    font-size: .82rem;
    font-weight: 700;
  }

  .error {
    border: 1px solid rgba(255, 95, 117, .35);

    background: rgba(255, 95, 117, .08);
    color: #ff8fa3;
  }

  .success {
    border: 1px solid rgba(0, 245, 212, .28);

    background: rgba(0, 245, 212, .06);
    color: #00f5d4;
  }

  .loader {
    display: inline-block;

    width: 10px;
    height: 10px;

    margin-right: 8px;

    border: 2px solid rgba(255, 255, 255, .35);
    border-top-color: white;
    border-radius: 999px;

    animation: spin .7s linear infinite;
  }

  @keyframes spin {
    to {
      transform: rotate(360deg);
    }
  }

  @media (max-width: 980px) {
    .kpi-tool {
      grid-template-columns: 1fr;
    }

    .input-panel {
      border-right: 0;
      border-bottom: 1px solid rgba(0, 245, 212, .22);
    }
  }

  @media (max-width: 640px) {
    .input-panel,
    .output-panel {
      padding: 20px;
    }

    .panel-header,
    .output-header,
    .editor-label-row,
    .editor-footer {
      flex-direction: column;
      align-items: flex-start;
    }

    .editor-meta {
      flex-wrap: wrap;
    }
  }
</style>