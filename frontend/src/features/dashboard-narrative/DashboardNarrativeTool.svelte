<script>
  import DashboardNarrativeResult from './DashboardNarrativeResult.svelte';
  import { generateDashboardNarrative } from './dashboardNarrativeService.js';
  import LoadingState from '../../components/ui/LoadingState.svelte';
  import EmptyState from '../../components/ui/EmptyState.svelte';

  export let tool;

  let inputText = '';
  let result = null;
  let loading = false;
  let error = '';

  function useSample() {
    inputText = tool.sample;
    result = null;
    error = '';
  }

  async function runTool() {
    if (!inputText.trim()) {
      error = 'Paste dashboard notes first so MOL can generate the narrative.';
      return;
    }

    loading = true;
    error = '';
    result = null;

    try {
      const [data] = await Promise.all([
        generateDashboardNarrative(inputText),
        new Promise((resolve) => setTimeout(resolve, 800))
      ]);

      result = data;
    } catch (err) {
      error = 'Could not generate the dashboard narrative. Make sure the backend is running.';
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
  </div>

  {#if error}
    <p class="error">{error}</p>
  {/if}
</div>

<div class="output-panel">
  <div class="output-header">
    <div>
      <p class="eyebrow">OUTPUT</p>
      <h3>Executive dashboard narrative</h3>
    </div>
  </div>

  {#if loading}
    <LoadingState />
  {:else if result}
    <DashboardNarrativeResult {result} />
  {:else}
    <EmptyState
      title={tool.emptyTitle}
      body={tool.emptyBody}
      sample={tool.sample}
      onAction={useSample}
    />
  {/if}
</div>