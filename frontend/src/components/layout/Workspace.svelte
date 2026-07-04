<script>
  import { tools } from '../../lib/tools.js';
  import HeroBanner from './HeroBanner.svelte';
  import ToolRouter from '../tool/ToolRouter.svelte';

  let activeTool = tools[0];

  function selectTool(tool) {
    activeTool = tool;
  }
</script>

<main class="workspace">
  <HeroBanner />

  <section class="tool-nav">
    {#each tools as tool}
      <button
        class:active={activeTool.id === tool.id}
        on:click={() => selectTool(tool)}
      >
        <span>{tool.eyebrow}</span>
        {tool.label}
      </button>
    {/each}
  </section>

  <section class="tool-workspace">
    <ToolRouter {activeTool} />
  </section>
</main>

<style>
  .workspace {
  flex: 1;
  padding: 32px;
  overflow: auto;
  color: #f7f7ff;
}

  .tool-nav {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
    margin-bottom: 18px;
  }

  .tool-nav button {
    padding: 18px;
    text-align: left;
    background: #1A2146;
    border: 1px solid rgba(0,245,212,.25);
    color: white;
    cursor: pointer;
    font-weight: 800;
  }

  .tool-nav button span {
    display: block;
    color: #00F5D4;
    font-size: .65rem;
    margin-bottom: 6px;
  }

  .tool-nav button.active {
    border-color: #FF007F;
    background: linear-gradient(135deg, rgba(148,0,211,.42), rgba(26,27,75,.95));
  }

  .tool-workspace {
  display: grid;
  grid-template-columns: .9fr 1.1fr;
  gap: 24px;
  padding: 24px;
  border: 1px solid rgba(0,245,212,.3);
  background: #11193D;
  color: #f7f7ff;
}

  @media(max-width: 860px) {
    .tool-nav,
    .tool-workspace {
      grid-template-columns: 1fr;
    }
  }
</style>