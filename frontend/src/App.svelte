<script>
  import { tools } from './lib/tools.js';
  import { apiPost } from './lib/api.js';
  import EmptyState from './components/ui/EmptyState.svelte';
  import LoadingState from './components/ui/LoadingState.svelte';
  import ResultBlock from "./components/ui/ResultBlock.svelte";

  let activeTool = tools[0];
  let inputText = '';
  let result = null;
  let loading = false;
  let error = '';
  let copiedLabel = '';

  function switchTool(tool) {
    activeTool = tool;
    inputText = '';
    result = null;
    error = '';
    copiedLabel = '';
  }

  function useSample() {
    inputText = activeTool.sample;
    error = '';
    result = null;
  }

  async function runTool() {
    if (!inputText.trim()) {
      error = 'Paste content first so MOL can analyze it.';
      return;
    }

    loading = true;
    error = '';
    result = null;
    copiedLabel = '';

    try {
      const [data] = await Promise.all([
  apiPost(activeTool.endpoint, { text: inputText }),
  new Promise((resolve) => setTimeout(resolve, 800))
]);

result = data;
    } catch (err) {
      error = 'Could not connect to the backend. Make sure FastAPI is running on http://127.0.0.1:8000.';
    } finally {
      loading = false;
    }
  }

  function outputText() {
    if (!result) return '';

    if (activeTool.id === 'clarity') {
      return [
        'Moon Onyx Labs — Executive Clarity Analyzer',
        '',
        `Score: ${result.score}/100`,
        `Status: ${result.label}`,
        '',
        result.result
      ].join('\n');
    }

    if (activeTool.id === 'kpi') {
      return [
        'Moon Onyx Labs — KPI Cleaner',
        '',
        `Issues Found: ${result.issues_found}`,
        `Status: ${result.label}`,
        '',
        result.result
      ].join('\n');
    }

    if (activeTool.id === 'insights') {
      return [
        'Moon Onyx Labs — Insight Generator',
        '',
        `Insight Type: ${result.insight_type}`,
        `Status: ${result.label}`,
        '',
        result.result
      ].join('\n');
    }

    return JSON.stringify(result, null, 2);
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
</script>

<main class="shell">
  <section class="hero-grid">
    <div class="brand-panel cut">
      <div class="logo-mark"><span>◐</span></div>
      <div>
        <p class="kicker">MOON ONYX LABS</p>
        <h1>Executive Insight Engine</h1>
        <p class="subhead">A futuristic micro-tool suite for turning messy data, KPIs, and report notes into executive-ready direction.</p>
      </div>
    </div>
    <div class="status-panel cut"><p class="status-label">MVP V2.1</p><p class="status-number">3</p><p class="status-copy">distinct tools in one platform</p></div>
  </section>

  <section class="tool-nav">
    {#each tools as tool}
      <button class:active={activeTool.id===tool.id} on:click={()=>switchTool(tool)}><span>{tool.eyebrow}</span>{tool.label}</button>
    {/each}
  </section>

  <section class="workspace cut">
    <div class="input-panel">
      <div class="panel-top"><p class="eyebrow">{activeTool.eyebrow}</p><button class="mini" on:click={useSample}>Use sample</button></div>
      <h2>{activeTool.title}</h2>
      <p class="description">{activeTool.description}</p>
      <textarea bind:value={inputText} placeholder={activeTool.placeholder}></textarea>
      <div class="actions">
        <button class="run-button" on:click={runTool} disabled={loading}>{#if loading}<span class="loader"></span>Processing Signal...{:else}Run {activeTool.label}{/if}</button>
        {#if inputText}<button class="secondary" on:click={()=>copyText(inputText, 'Input copied')}>Copy Input</button>{/if}
      </div>
      {#if error}<p class="error">{error}</p>{/if}
      {#if copiedLabel}<p class="copied">{copiedLabel}</p>{/if}
    </div>

    <div class="output-panel">
      <div class="output-header"><div><p class="eyebrow">OUTPUT</p><h3>Executive-ready response</h3></div>{#if result}<button class="copy-output" on:click={()=>copyText(outputText(), 'Output copied')}>Copy Output</button>{/if}</div>

      {#if loading}
        <LoadingState />
      {:else if !result}
        <EmptyState
        title={activeTool.emptyTitle}
        body={activeTool.emptyBody}
        sample={activeTool.sample}
        onAction={useSample}
        />
      {/if}

     {#if result}

  <ResultBlock
    title={activeTool.label + " Result"}
    content={outputText()}
    onCopy={() => copyText(outputText(), "Output copied")}
/>

{/if}
    </div>
  </section>
</main>

<style>
:global(*){box-sizing:border-box}:global(body){margin:0;min-height:100vh;background:linear-gradient(rgba(255,255,255,.025) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.025) 1px,transparent 1px),radial-gradient(circle at top left,rgba(148,0,211,.35),transparent 30%),radial-gradient(circle at bottom right,rgba(0,245,212,.18),transparent 35%),#090a22;background-size:34px 34px,34px 34px,auto,auto,auto;color:#f7f7ff;font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}.shell{width:min(1180px,calc(100% - 32px));margin:0 auto;padding:32px 0 48px}.hero-grid{display:grid;grid-template-columns:1fr 260px;gap:18px;margin-bottom:18px}.cut{border:1px solid rgba(0,245,212,.42);clip-path:polygon(0 0,calc(100% - 22px) 0,100% 22px,100% 100%,22px 100%,0 calc(100% - 22px));background:linear-gradient(135deg,rgba(26,27,75,.94),rgba(8,9,34,.95));box-shadow:0 0 34px rgba(0,245,212,.10),inset 0 0 0 1px rgba(255,0,127,.10)}.brand-panel{display:flex;gap:22px;padding:32px;align-items:center}.logo-mark{width:86px;height:86px;display:grid;place-items:center;border:1px solid #00F5D4;background:linear-gradient(135deg,rgba(148,0,211,.22),rgba(255,0,127,.12));clip-path:polygon(14% 0,100% 0,100% 86%,86% 100%,0 100%,0 14%);flex:0 0 auto}.logo-mark span{font-size:52px;color:#00F5D4;text-shadow:0 0 16px rgba(0,245,212,.7)}.kicker,.eyebrow,.status-label{color:#00F5D4;letter-spacing:.18em;font-size:.74rem;font-weight:800;margin:0 0 8px}h1{font-size:clamp(2rem,5vw,4.5rem);line-height:.92;margin:0;text-transform:uppercase;letter-spacing:-.06em}.subhead{max-width:700px;color:#D3D3D3;font-size:1.02rem;line-height:1.6;margin:16px 0 0}.status-panel{padding:28px;text-align:center}.status-number{font-size:5rem;line-height:1;color:#FF007F;font-weight:900;margin:4px 0;text-shadow:0 0 20px rgba(255,0,127,.45)}.status-copy{margin:0;color:#D3D3D3;text-transform:uppercase;font-size:.8rem;letter-spacing:.08em}.tool-nav{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:18px}button{font-family:inherit}.tool-nav button,.run-button,.secondary,.mini,.copy-output,.card-heading button{border:1px solid rgba(211,211,211,.24);color:#f7f7ff;background:rgba(26,27,75,.72);padding:14px 16px;cursor:pointer;text-transform:uppercase;font-weight:900;letter-spacing:.04em;clip-path:polygon(0 0,calc(100% - 12px) 0,100% 12px,100% 100%,12px 100%,0 calc(100% - 12px));transition:160ms ease}.tool-nav button{padding:18px;text-align:left}.tool-nav button span{display:block;color:#00F5D4;font-size:.65rem;margin-bottom:6px}.tool-nav button:hover,.tool-nav button.active,.secondary:hover,.mini:hover,.copy-output:hover,.card-heading button:hover{border-color:#FF007F;background:linear-gradient(135deg,rgba(148,0,211,.42),rgba(26,27,75,.95));box-shadow:0 0 24px rgba(255,0,127,.16)}.workspace{display:grid;grid-template-columns:.9fr 1.1fr;gap:24px;padding:24px}h2,h3{margin:0;text-transform:uppercase;letter-spacing:-.03em}h2{font-size:2rem}.description{color:#D3D3D3;line-height:1.55}.panel-top,.output-header,.card-heading,.actions{display:flex;align-items:center;justify-content:space-between;gap:12px}.actions{margin-top:14px;align-items:stretch}textarea{width:100%;min-height:260px;resize:vertical;color:#fff;background:rgba(4,5,25,.88);border:1px solid rgba(0,245,212,.36);padding:18px;outline:none;font-size:.96rem;line-height:1.5;clip-path:polygon(0 0,calc(100% - 16px) 0,100% 16px,100% 100%,16px 100%,0 calc(100% - 16px))}textarea:focus{border-color:#FF007F;box-shadow:0 0 18px rgba(255,0,127,.16)}.run-button{flex:1;background:linear-gradient(90deg,#9400D3,#FF007F);border-color:rgba(255,255,255,.28);text-align:center;display:inline-flex;align-items:center;justify-content:center;gap:10px}.run-button:disabled{opacity:.72;cursor:wait}.secondary,.mini,.copy-output,.card-heading button{font-size:.72rem;color:#00F5D4;background:rgba(4,5,25,.55)}.mini.wide{width:100%;margin-top:12px}.error{color:#FF007F;font-weight:800}.copied{color:#00F5D4;font-weight:900;letter-spacing:.06em;text-transform:uppercase;font-size:.78rem}.output-panel{border-left:1px solid rgba(0,245,212,.2);padding-left:22px;min-width:0}.output-header{margin-bottom:16px;align-items:flex-start}.empty-state,.result-card,.score-block,.cta-strip,.loading-state{background:rgba(4,5,25,.62);border:1px solid rgba(211,211,211,.16);padding:18px;margin-bottom:12px;clip-path:polygon(0 0,calc(100% - 14px) 0,100% 14px,100% 100%,14px 100%,0 calc(100% - 14px))}.enhanced{border-color:rgba(0,245,212,.32)}.empty-tag{color:#FF007F;font-size:.68rem;font-weight:900;letter-spacing:.18em;margin:0 0 8px}.enhanced h4,.loading-state h4{margin:0 0 8px;text-transform:uppercase;letter-spacing:.05em}pre{white-space:pre-wrap;color:#D3D3D3;background:rgba(26,27,75,.42);border-left:2px solid #00F5D4;padding:12px;font-size:.83rem;overflow:auto}.small{color:#9ea2c8;font-size:.84rem}.score-block{display:flex;align-items:center;justify-content:space-between;border-color:rgba(0,245,212,.42)}.score-block span{text-transform:uppercase;letter-spacing:.12em;color:#00F5D4;font-weight:900}.score-block strong{font-size:3.25rem;color:#00F5D4;line-height:1}.result-card h4{margin:0 0 10px;color:#f7f7ff;text-transform:uppercase;letter-spacing:.08em}.result-card p,.result-card li{color:#D3D3D3;line-height:1.55}.kpi-row,.insight-row{border-top:1px solid rgba(0,245,212,.14);padding-top:12px;margin-top:12px}.kpi-row strong,.insight-row strong{display:block;color:#00F5D4;margin-bottom:6px}.kpi-row span{display:inline-block;color:#FF007F;font-weight:900;font-size:.75rem;text-transform:uppercase;letter-spacing:.12em}.cta-strip{border-color:rgba(255,0,127,.45);color:#fff;background:linear-gradient(90deg,rgba(148,0,211,.32),rgba(255,0,127,.18));font-weight:800}.loader{width:15px;height:15px;border:2px solid rgba(255,255,255,.35);border-top-color:#00F5D4;border-radius:50%;animation:spin .8s linear infinite}.loading-state{position:relative;overflow:hidden;min-height:250px;display:grid;place-items:center;text-align:center}.scan{position:absolute;left:0;top:-35%;width:100%;height:40%;background:linear-gradient(180deg,transparent,rgba(0,245,212,.10),transparent);animation:scan 1.8s ease-in-out infinite}.bars{display:grid;grid-template-columns:repeat(3,38px);gap:8px;margin-bottom:8px}.bars span{height:38px;border:1px solid rgba(0,245,212,.35);background:rgba(0,245,212,.08);animation:pulse 1s ease-in-out infinite}.bars span:nth-child(2){animation-delay:.15s}.bars span:nth-child(3){animation-delay:.3s}@keyframes spin{to{transform:rotate(360deg)}}@keyframes scan{0%{top:-35%}100%{top:100%}}@keyframes pulse{0%,100%{opacity:.35;transform:translateY(0)}50%{opacity:1;transform:translateY(-5px)}}@media(max-width:860px){.hero-grid,.workspace{grid-template-columns:1fr}.tool-nav{grid-template-columns:1fr}.output-panel{border-left:0;padding-left:0;border-top:1px solid rgba(0,245,212,.2);padding-top:22px}.brand-panel{align-items:flex-start;flex-direction:column}.actions,.panel-top,.output-header,.card-heading{flex-direction:column;align-items:stretch}}
</style>
