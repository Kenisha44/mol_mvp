<script>
  import { tools } from '../../lib/tools.js';
  import HeroBanner from './HeroBanner.svelte';
  import ToolRouter from '../tool/ToolRouter.svelte';
  import { onMount } from 'svelte';
  import { getCloudAnalyses } from '../../lib/analysisCloudStorage.js';

  export let activeTool = 'clarity';
  export let onSelectTool = () => {};

  function getToolNumber(index) {
    return String(index + 1).padStart(2, '0');
  }

  function getToolIcon(toolId) {
    const icons = {
      clarity: '▤',
      'kpi-cleaner': '▥',
      insights: '✦',
      dashboard: '▣',
      'executive-memo': '✎',
      'kpi-health': '♡'
    };

    return icons[toolId] ?? '◇';
  }

let recentAnalyses = [];
let recentLoading = true;

async function loadRecentAnalyses() {
  try {
    const items = await getCloudAnalyses();

    recentAnalyses = (items ?? [])
      .slice(0, 3)
      .map((item) => ({
        id: item.id,
        title: item.title || 'Saved Analysis',
        toolId: item.tool_id,
        createdAt: item.created_at
      }));
  } catch (error) {
    console.error(
      'Unable to load recent analyses:',
      error
    );

    recentAnalyses = [];
  } finally {
    recentLoading = false;
  }
}

function formatRecentDate(value) {
  if (!value) return '';

  return new Date(value).toLocaleDateString([], {
    month: 'short',
    day: 'numeric'
  });
}

onMount(() => {
  loadRecentAnalyses();
});

$: selectedTool =
  tools.find((tool) => tool.id === activeTool) ?? tools[0]; 
</script>

<main class="workspace">

{#if activeTool === 'workspace' || activeTool === 'plans'}

  <section class="tool-workspace standalone">
    <ToolRouter {activeTool} />
  </section>

{:else}

  <HeroBanner />

<section class="tool-launcher">

  <div class="launcher-heading">
    <div>
      <p class="launcher-eyebrow">
        CHOOSE A TOOL
      </p>

      <h2>
        Start an analysis
      </h2>
    </div>

    <span class="tool-count">
      6 executive tools
    </span>
  </div>


  <div class="tool-grid">

    {#each tools as tool, index}

      <button
        type="button"
        class="tool-card"
        class:active={activeTool === tool.id}
        on:click={() => onSelectTool(tool.id)}
      >

        <div class="card-top">

          <div
            class="tool-icon"
            class:purple={tool.id === 'kpi-cleaner'}
            class:cyan={
              tool.id === 'insights' ||
              tool.id === 'kpi-health'
            }
            class:pink={
              tool.id === 'clarity' ||
              tool.id === 'dashboard'
            }
            class:gold={tool.id === 'executive-memo'}
          >
            {getToolIcon(tool.id)}
          </div>

          <span class="tool-number">
            {getToolNumber(index)}
          </span>

        </div>


        <div class="card-copy">

          <h3>
            {tool.title}
          </h3>

          <p>
            {tool.description}
          </p>

        </div>


        <div class="launch-row">

          <span>
            Launch
          </span>

          <span class="arrow">
            →
          </span>

        </div>

      </button>

    {/each}

  </div>

</section>

<section class="dashboard-support">

  <!-- SMART START -->
  <article class="support-card smart-start">

    <div class="support-icon">
      ↗
    </div>

    <div class="support-content">

      <p class="support-eyebrow">
        SMART START
      </p>

      <h3>
        New to MOL?
      </h3>

      <p>
        Start with Executive Clarity using MOL's
        built-in sample data and see how the suite works.
      </p>

      <button
        type="button"
        class="primary-support-action"
        on:click={() => onSelectTool('clarity')}
      >
        Try Executive Clarity
        <span>→</span>
      </button>

    </div>

  </article>


  <!-- RECENT ANALYSES -->
  <article class="support-card recent-card">

    <div class="support-card-header">

      <div>
        <p class="support-eyebrow">
          RECENT ANALYSES
        </p>

        <h3>
          Pick up where you left off.
        </h3>
      </div>

      <button
        type="button"
        class="text-action"
        on:click={() => onSelectTool('workspace')}
      >
        Workspace →
      </button>

    </div>


    {#if recentLoading}

      <div class="recent-empty">
        Loading recent analyses...
      </div>

    {:else if recentAnalyses.length === 0}

      <div class="recent-empty">
        <strong>No saved analyses yet.</strong>

        <span>
          Your latest Workspace activity will appear here.
        </span>
      </div>

    {:else}

      <div class="recent-list">

        {#each recentAnalyses as item}

          <button
            type="button"
            class="recent-item"
            on:click={() => onSelectTool('workspace')}
          >

            <div>
              <strong>
                {item.title}
              </strong>

              <span>
                {formatRecentDate(item.createdAt)}
              </span>
            </div>

            <span class="recent-arrow">
              →
            </span>

          </button>

        {/each}

      </div>

    {/if}

  </article>


  <!-- TIPS -->
  <article class="support-card tips-card">

    <div class="support-icon tips-icon">
      ✦
    </div>

    <div class="support-content">

      <p class="support-eyebrow">
        TIPS & SHORTCUTS
      </p>

      <h3>
        Get more from MOL.
      </h3>

      <ul>
        <li>
          Use sample inputs to explore tools instantly.
        </li>

        <li>
          Save important results to your cloud Workspace.
        </li>

        <li>
          Export analyses as PDF or DOCX.
        </li>

        <li>
          Use Workspace search to revisit prior insights.
        </li>
      </ul>

    </div>

  </article>

</section>

  <section class="active-workspace">

  <div class="workspace-toolbar">

    <div>
      <p class="workspace-eyebrow">
        ACTIVE WORKSPACE
      </p>

      <h2>
        {selectedTool.title}
      </h2>

      <p class="workspace-description">
        {selectedTool.description}
      </p>
    </div>


    <div class="workspace-meta">

      <span>
        {selectedTool.eyebrow}
      </span>

      <span class="workspace-status">
        READY
      </span>

    </div>

  </div>


  <div class="tool-workspace">
  <ToolRouter
  {activeTool}
  onSelectTool={onSelectTool}
  />
  </div>

</section>

{/if}

</main>

<style>
 .workspace {
  width: 100%;
  max-width: none;
  min-width: 0;
  box-sizing: border-box;
  padding: 32px;
  overflow: hidden;
  color: #f7f7ff;
}

.tool-launcher {
  margin-bottom: 22px;
}


.launcher-heading {
  display: flex;

  justify-content: space-between;
  align-items: flex-end;

  gap: 20px;

  margin-bottom: 13px;
}


.launcher-eyebrow {
  margin: 0 0 5px;

  color: #00f5d4;

  font-size: .68rem;
  font-weight: 900;
  letter-spacing: .14em;

  text-transform: uppercase;
}


.launcher-heading h2 {
  margin: 0;

  color: #f7f7ff;

  font-size: 1.08rem;
}


.tool-count {
  color: #7184ad;

  font-size: .68rem;

  text-transform: uppercase;

  letter-spacing: .07em;
}


.tool-grid {
  display: grid;

  grid-template-columns:
    repeat(6, minmax(0, 1fr));

  gap: 11px;
}


.tool-card {
  position: relative;

  min-width: 0;
  min-height: 215px;

  display: flex;
  flex-direction: column;

  padding: 15px;

  overflow: hidden;

  border:
    1px solid rgba(57, 91, 158, .38);

  border-radius: 9px;

  background:
    radial-gradient(
      circle at top left,
      rgba(28, 52, 111, .18),
      transparent 48%
    ),
    linear-gradient(
      155deg,
      #09142d,
      #080e22
    );

  color: white;

  text-align: left;

  font-family: inherit;

  cursor: pointer;

  transition:
    transform .18s ease,
    border-color .18s ease,
    box-shadow .18s ease,
    background .18s ease;
}


.tool-card::after {
  content: '';

  position: absolute;

  inset: 0;

  pointer-events: none;

  opacity: 0;

  background:
    radial-gradient(
      circle at 25% 10%,
      rgba(0, 245, 212, .07),
      transparent 38%
    );

  transition: opacity .18s ease;
}


.tool-card:hover {
  transform: translateY(-3px);

  border-color:
    rgba(0, 245, 212, .5);

  box-shadow:
    0 10px 34px
    rgba(0, 0, 0, .22);
}


.tool-card:hover::after {
  opacity: 1;
}


.tool-card.active {
  border-color:
    rgba(255, 0, 127, .7);

  background:
    radial-gradient(
      circle at top left,
      rgba(255, 0, 127, .10),
      transparent 43%
    ),
    linear-gradient(
      155deg,
      #101735,
      #080e22
    );

  box-shadow:
    inset 0 1px 0
    rgba(255,255,255,.025);
}


.card-top {
  position: relative;

  z-index: 1;

  display: flex;

  justify-content: space-between;
  align-items: flex-start;

  gap: 10px;

  margin-bottom: 15px;
}


.tool-icon {
  width: 42px;
  height: 42px;

  display: grid;
  place-items: center;

  border:
    1px solid rgba(0, 245, 212, .30);

  border-radius: 9px;

  background:
    rgba(0, 245, 212, .07);

  color: #00f5d4;

  font-size: 1.1rem;

  box-shadow:
    0 0 22px
    rgba(0,245,212,.04);
}


.tool-icon.purple {
  border-color:
    rgba(169, 52, 255, .45);

  background:
    rgba(148, 0, 211, .10);

  color: #cf52ff;
}


.tool-icon.pink {
  border-color:
    rgba(255, 0, 127, .42);

  background:
    rgba(255, 0, 127, .09);

  color: #ff52aa;
}


.tool-icon.cyan {
  border-color:
    rgba(0, 245, 212, .38);

  background:
    rgba(0, 245, 212, .075);

  color: #00f5d4;
}


.tool-icon.gold {
  border-color:
    rgba(255, 166, 0, .38);

  background:
    rgba(255, 166, 0, .08);

  color: #ffb12b;
}


.tool-number {
  color: #a5b1ce;

  font-size: .7rem;

  letter-spacing: .08em;
}


.card-copy {
  position: relative;

  z-index: 1;

  flex: 1;
}


.card-copy h3 {
  margin: 0 0 9px;

  color: #f7f7ff;

  font-size: .88rem;

  line-height: 1.28;
}


.card-copy p {
  margin: 0;

  color: #9caaca;

  font-size: .72rem;

  line-height: 1.5;
}


.launch-row {
  position: relative;

  z-index: 1;

  min-height: 34px;

  display: flex;

  justify-content: center;
  align-items: center;

  gap: 8px;

  margin-top: 15px;

  border:
    1px solid rgba(0, 245, 212, .33);

  border-radius: 4px;

  background:
    rgba(0, 245, 212, .025);

  color: #00f5d4;

  font-size: .72rem;
  font-weight: 900;

  transition:
    background .18s ease,
    border-color .18s ease;
}


.tool-card:hover .launch-row {
  border-color:
    rgba(0, 245, 212, .65);

  background:
    rgba(0, 245, 212, .07);
}


.arrow {
  transition:
    transform .18s ease;
}


.tool-card:hover .arrow {
  transform: translateX(3px);
}

 .tool-workspace {
  width: 100%;
  display: block;
  box-sizing: border-box;

  border: 1px solid rgba(0, 245, 212, .3);
  background: #11193D;
  color: #f7f7ff;
}

.tool-workspace.standalone {
  border: 0;
  background: transparent;
}

.dashboard-support {
  display: grid;

  grid-template-columns:
    minmax(240px, .85fr)
    minmax(320px, 1.25fr)
    minmax(260px, .9fr);

  gap: 12px;

  margin-bottom: 24px;
}


.support-card {
  min-width: 0;

  display: flex;

  gap: 15px;

  padding: 20px;

  border:
    1px solid rgba(54, 86, 151, .38);

  border-radius: 9px;

  background:
    linear-gradient(
      145deg,
      rgba(12, 21, 52, .98),
      rgba(6, 11, 30, .98)
    );
}


.smart-start {
  background:
    radial-gradient(
      circle at top left,
      rgba(148, 0, 211, .13),
      transparent 48%
    ),
    linear-gradient(
      145deg,
      rgba(18, 21, 61, .98),
      rgba(7, 11, 31, .98)
    );
}


.support-icon {
  flex: 0 0 42px;

  width: 42px;
  height: 42px;

  display: grid;
  place-items: center;

  border:
    1px solid rgba(210, 92, 255, .35);

  border-radius: 10px;

  background:
    rgba(148, 0, 211, .09);

  color: #d95bff;

  font-size: 1.1rem;
}


.tips-icon {
  border-color:
    rgba(0, 245, 212, .28);

  background:
    rgba(0, 245, 212, .06);

  color: #00f5d4;
}


.support-content {
  min-width: 0;

  flex: 1;
}


.support-eyebrow {
  margin: 0 0 7px;

  color: #00f5d4;

  font-size: .65rem;
  font-weight: 900;
  letter-spacing: .12em;

  text-transform: uppercase;
}


.support-card h3 {
  margin: 0 0 8px;

  color: #f7f7ff;

  font-size: .96rem;
}


.support-card p:not(.support-eyebrow) {
  margin: 0;

  color: #9aa9ca;

  font-size: .75rem;
  line-height: 1.55;
}


.primary-support-action {
  min-height: 38px;

  width: 100%;

  display: flex;

  align-items: center;
  justify-content: center;

  gap: 8px;

  margin-top: 16px;

  border:
    1px solid rgba(255, 0, 127, .42);

  border-radius: 4px;

  background:
    linear-gradient(
      90deg,
      rgba(0, 185, 220, .65),
      rgba(148, 0, 211, .72),
      rgba(255, 0, 127, .75)
    );

  color: white;

  font-family: inherit;
  font-size: .73rem;
  font-weight: 900;

  cursor: pointer;
}


.primary-support-action:hover {
  filter: brightness(1.1);
}


/* RECENT */

.recent-card {
  display: block;
}


.support-card-header {
  display: flex;

  justify-content: space-between;
  align-items: flex-start;

  gap: 15px;

  margin-bottom: 13px;
}


.text-action {
  flex: 0 0 auto;

  padding: 0;

  border: 0;

  background: transparent;

  color: #00f5d4;

  font-family: inherit;
  font-size: .68rem;
  font-weight: 800;

  cursor: pointer;
}


.recent-list {
  display: grid;

  gap: 7px;
}


.recent-item {
  width: 100%;

  display: flex;

  justify-content: space-between;
  align-items: center;

  gap: 12px;

  padding: 10px 11px;

  border:
    1px solid rgba(255, 255, 255, .065);

  background:
    rgba(255, 255, 255, .018);

  color: inherit;

  text-align: left;

  font-family: inherit;

  cursor: pointer;
}


.recent-item:hover {
  border-color:
    rgba(0, 245, 212, .26);

  background:
    rgba(0, 245, 212, .035);
}


.recent-item strong {
  display: block;

  margin-bottom: 3px;

  color: #e6ebf8;

  font-size: .73rem;
}


.recent-item span {
  color: #7184ad;

  font-size: .63rem;
}


.recent-arrow {
  color: #00f5d4 !important;

  font-size: .85rem !important;
}


.recent-empty {
  display: grid;

  gap: 5px;

  padding: 13px;

  border:
    1px dashed rgba(255, 255, 255, .09);

  color: #7184ad;

  font-size: .7rem;
}


.recent-empty strong {
  color: #b9c5de;
}


/* TIPS */

.tips-card ul {
  display: grid;

  gap: 9px;

  margin: 14px 0 0;

  padding: 0;

  list-style: none;
}


.tips-card li {
  position: relative;

  padding-left: 20px;

  color: #a9b6d2;

  font-size: .72rem;

  line-height: 1.45;
}


.tips-card li::before {
  content: '✓';

  position: absolute;

  left: 0;

  color: #00f5d4;

  font-weight: 900;
}

.active-workspace {
  overflow: hidden;

  border:
    1px solid rgba(0, 245, 212, .22);

  border-radius: 10px;

  background:
    linear-gradient(
      145deg,
      rgba(12, 20, 51, .96),
      rgba(6, 11, 30, .98)
    );
}


.workspace-toolbar {
  display: flex;

  justify-content: space-between;
  align-items: flex-start;

  gap: 24px;

  padding: 20px 22px;

  border-bottom:
    1px solid rgba(255, 255, 255, .07);

  background:
    radial-gradient(
      circle at top right,
      rgba(148, 0, 211, .08),
      transparent 34%
    ),
    rgba(7, 13, 34, .72);
}


.workspace-eyebrow {
  margin: 0 0 6px;

  color: #00f5d4;

  font-size: .64rem;
  font-weight: 900;

  letter-spacing: .14em;

  text-transform: uppercase;
}


.workspace-toolbar h2 {
  margin: 0;

  color: #f7f7ff;

  font-size: 1.2rem;
}


.workspace-description {
  max-width: 650px;

  margin: 7px 0 0;

  color: #91a2c5;

  font-size: .74rem;

  line-height: 1.5;
}


.workspace-meta {
  display: flex;

  align-items: center;

  gap: 7px;

  flex: 0 0 auto;
}


.workspace-meta span {
  padding: 6px 8px;

  border:
    1px solid rgba(0, 245, 212, .16);

  background:
    rgba(0, 245, 212, .035);

  color: #8fa5cf;

  font-size: .56rem;
  font-weight: 900;

  letter-spacing: .08em;

  text-transform: uppercase;
}


.workspace-meta .workspace-status {
  border-color:
    rgba(255, 0, 127, .25);

  background:
    rgba(255, 0, 127, .045);

  color: #ff5bad;
}


.tool-workspace {
  width: 100%;

  display: block;

  box-sizing: border-box;

  border: 0;

  background: transparent;

  color: #f7f7ff;
}


@media (max-width: 700px) {
  .workspace-toolbar {
    flex-direction: column;
  }

  .workspace-meta {
    flex-wrap: wrap;
  }
}

@media (max-width: 1150px) {
  .dashboard-support {
    grid-template-columns:
      repeat(2, minmax(0, 1fr));
  }

  .tips-card {
    grid-column: 1 / -1;
  }
}


@media (max-width: 700px) {
  .dashboard-support {
    grid-template-columns: 1fr;
  }

  .tips-card {
    grid-column: auto;
  }
}

@media (max-width: 1350px) {
  .tool-grid {
    grid-template-columns:
      repeat(3, minmax(0, 1fr));
  }
}


@media (max-width: 860px) {
  .tool-grid {
    grid-template-columns:
      repeat(2, minmax(0, 1fr));
  }

  .launcher-heading {
    align-items: flex-start;
    flex-direction: column;
  }
}


@media (max-width: 560px) {
  .tool-grid {
    grid-template-columns: 1fr;
  }

  .tool-card {
    min-height: auto;
  }
}

  @media(max-width: 860px) {
    .tool-nav,
    .tool-workspace {
      grid-template-columns: 1fr;
    }
  }
</style>