<script>
  import LoadingState from '../../components/ui/LoadingState.svelte';
  import EmptyState from '../../components/ui/EmptyState.svelte';
  import KpiCleanerResult from './KpiCleanerResult.svelte';
  import { cleanKpi } from './kpiCleanerService.js';

  export let tool;

  let inputText = '';
  let result = null;
  let loading = false;
  let error = '';
  let copiedLabel = '';

  function useSample() {
    inputText = tool.sample;
    result = null;
    error = '';
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
      setTimeout(() => copiedLabel = '', 1800);
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
      error = 'Could not clean KPI text. Make sure the backend is running.';
    } finally {
      loading = false;
    }
  }
</script>

<div class="input-panel">
  <div class="panel-top">
    <p class="eyebrow">{tool.eyebrow}</p>
    <button class="mini" on:click={useSample}>Use sample</button>
  </div>

  <h2>{tool.title}</h2>
  <p class="description">{tool.description}</p>

  <textarea bind:value={inputText} placeholder={tool.placeholder}></textarea>

  <div class="actions">
    <button class="run-button" on:click={runTool} disabled={loading}>
      {#if loading}
        <span class="loader"></span>
        Processing Signal...
      {:else}
        Run {tool.label}
      {/if}
    </button>

    {#if inputText}
      <button class="secondary" on:click={() => copyText(inputText, 'Input copied')}>
        Copy Input
      </button>
    {/if}
  </div>

  {#if error}
    <p class="error">{error}</p>
  {/if}

  {#if copiedLabel}
    <p class="copied">{copiedLabel}</p>
  {/if}
</div>

<div class="output-panel">
  <div class="output-header">
    <div>
      <p class="eyebrow">OUTPUT</p>
      <h3>Cleaned KPI response</h3>
    </div>
  </div>

  {#if loading}
    <LoadingState />
  {:else if result}
    <KpiCleanerResult
      {result}
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
</div>