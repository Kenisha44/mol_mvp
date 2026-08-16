<script>
  import {
    getSavedAnalyses,
    deleteSavedAnalysis,
    clearSavedAnalyses
  } from "../../lib/analysisStorage.js";

  let savedAnalyses = [];

  function loadAnalyses() {
    savedAnalyses = getSavedAnalyses();
  }

  function deleteAnalysis(id) {
    savedAnalyses = deleteSavedAnalysis(id);
  }

  function clearAll() {
    savedAnalyses = clearSavedAnalyses();
  }

  function formatDate(value) {
    if (!value) return "";

    return new Date(value).toLocaleString([], {
      month: "short",
      day: "numeric",
      hour: "numeric",
      minute: "2-digit"
    });
  }

  loadAnalyses();
</script>

<div class="workspace-page">

  <div class="workspace-header">
    <div>
      <p class="eyebrow">WORKSPACE</p>
      <h1>Saved Analysis History</h1>

      <p class="description">
        Revisit executive analyses, KPI diagnostics,
        narratives, memos, and prior results.
      </p>
    </div>

    {#if savedAnalyses.length > 0}
      <button
        type="button"
        class="clear-all"
        on:click={clearAll}
      >
        Clear History
      </button>
    {/if}
  </div>


  <div class="stats">

    <div class="stat-card">
      <span>Total Analyses</span>
      <strong>{savedAnalyses.length}</strong>
    </div>

    <div class="stat-card">
      <span>Workspace Status</span>
      <strong>
        {savedAnalyses.length > 0 ? "Active" : "Ready"}
      </strong>
    </div>

    <div class="stat-card">
      <span>Storage</span>
      <strong>Local</strong>
    </div>

  </div>


  {#if savedAnalyses.length === 0}

    <div class="empty-workspace">

      <div class="empty-icon">◇</div>

      <p class="eyebrow">NO SAVED ANALYSES</p>

      <h2>Your workspace is ready.</h2>

      <p>
        Save an analysis from one of MOL's executive intelligence
        tools and it will appear here.
      </p>

      <div class="tool-preview">
        <span>Clarity Analysis</span>
        <span>KPI Cleanup</span>
        <span>Executive Insights</span>
        <span>Dashboard Narratives</span>
        <span>Executive Memos</span>
        <span>KPI Health</span>
      </div>

    </div>

  {:else}

    <div class="history-grid">

      {#each savedAnalyses as item}

        <article class="history-card">

          <div class="card-top">

            <div>
              <p class="tool-label">
                {item.toolName ?? "MOL Analysis"}
              </p>

              <h3>
                {item.title ?? "Saved Analysis"}
              </h3>
            </div>

            <span class="status">
              {item.status ?? "Saved"}
            </span>

          </div>


          {#if item.preview}
            <p class="preview">
              {item.preview}
            </p>
          {/if}


          <div class="card-footer">

            <span>
              {formatDate(item.createdAt)}
            </span>

            <div class="card-actions">

              <button
                type="button"
                class="open-button"
              >
                Open
              </button>

              <button
                type="button"
                class="delete-button"
                on:click={() => deleteAnalysis(item.id)}
              >
                Delete
              </button>

            </div>

          </div>

        </article>

      {/each}

    </div>

  {/if}

</div>


<style>

  .workspace-page {
    display: grid;
    gap: 24px;

    width: 100%;

    color: #f7f7ff;
  }


  .workspace-header {
    display: flex;

    justify-content: space-between;
    align-items: flex-start;

    gap: 20px;

    padding: 28px;

    border:
      1px solid rgba(0,245,212,.24);

    background:
      radial-gradient(
        circle at top right,
        rgba(148,0,211,.09),
        transparent 34%
      ),
      #10183b;
  }


  .eyebrow {
    margin: 0 0 8px;

    color: #00f5d4;

    font-size: .72rem;
    font-weight: 900;
    letter-spacing: .13em;
    text-transform: uppercase;
  }


  h1,
  h2,
  h3 {
    margin: 0;

    color: #f7f7ff;
  }


  h1 {
    font-size: 1.8rem;
  }


  .description {
    max-width: 44rem;

    margin: 12px 0 0;

    color: #aab8d8;

    line-height: 1.6;
  }


  .clear-all {
    padding: 10px 14px;

    border:
      1px solid rgba(255,0,127,.35);

    background:
      rgba(255,0,127,.06);

    color: #ff5bad;

    font-weight: 800;

    cursor: pointer;
  }


  .stats {
    display: grid;

    grid-template-columns:
      repeat(3, minmax(0,1fr));

    gap: 12px;
  }


  .stat-card {
    padding: 18px;

    border:
      1px solid rgba(0,245,212,.16);

    background:
      rgba(14,23,58,.78);
  }


  .stat-card span {
    display: block;

    margin-bottom: 8px;

    color: #8193bd;

    font-size: .72rem;
  }


  .stat-card strong {
    color: #f7f7ff;

    font-size: 1.15rem;
  }


  .empty-workspace {
    display: grid;

    justify-items: start;

    padding: 36px;

    border:
      1px solid rgba(0,245,212,.18);

    background:
      rgba(5,10,32,.74);
  }


  .empty-icon {
    width: 46px;
    height: 46px;

    display: grid;
    place-items: center;

    margin-bottom: 18px;

    border:
      1px solid rgba(0,245,212,.35);

    color: #00f5d4;

    font-size: 1.4rem;
  }


  .empty-workspace h2 {
    margin-bottom: 10px;
  }


  .empty-workspace > p:not(.eyebrow) {
    max-width: 42rem;

    color: #aab8d8;

    line-height: 1.6;
  }


  .tool-preview {
    display: flex;

    flex-wrap: wrap;

    gap: 8px;

    margin-top: 18px;
  }


  .tool-preview span {
    padding: 7px 10px;

    border:
      1px solid rgba(0,245,212,.15);

    background:
      rgba(0,245,212,.035);

    color: #8da2cc;

    font-size: .72rem;
  }


  .history-grid {
    display: grid;

    grid-template-columns:
      repeat(2, minmax(0,1fr));

    gap: 14px;
  }


  .history-card {
    display: grid;

    gap: 16px;

    padding: 20px;

    border:
      1px solid rgba(0,245,212,.18);

    background:
      linear-gradient(
        145deg,
        rgba(18,27,68,.86),
        rgba(5,10,32,.95)
      );
  }


  .card-top,
  .card-footer {
    display: flex;

    justify-content: space-between;
    align-items: flex-start;

    gap: 14px;
  }


  .tool-label {
    margin: 0 0 7px;

    color: #00f5d4;

    font-size: .68rem;
    font-weight: 900;
    letter-spacing: .09em;
    text-transform: uppercase;
  }


  .status {
    flex: 0 0 auto;

    padding: 6px 8px;

    border:
      1px solid rgba(255,0,127,.3);

    background:
      rgba(255,0,127,.06);

    color: #ff5bad;

    font-size: .65rem;
    font-weight: 800;
  }


  .preview {
    margin: 0;

    color: #aebbd8;

    line-height: 1.55;

    font-size: .82rem;
  }


  .card-footer {
    align-items: center;

    padding-top: 12px;

    border-top:
      1px solid rgba(255,255,255,.07);

    color: #7184b0;

    font-size: .7rem;
  }


  .card-actions {
    display: flex;

    gap: 8px;
  }


  .open-button,
  .delete-button {
    padding: 7px 10px;

    font-weight: 800;

    cursor: pointer;
  }


  .open-button {
    border:
      1px solid rgba(0,245,212,.28);

    background:
      rgba(0,245,212,.05);

    color: #00f5d4;
  }


  .delete-button {
    border:
      1px solid rgba(255,0,127,.25);

    background:
      rgba(255,0,127,.04);

    color: #ff5bad;
  }


  @media (max-width: 900px) {

    .history-grid,
    .stats {
      grid-template-columns: 1fr;
    }

  }


  @media (max-width: 640px) {

    .workspace-header,
    .card-top,
    .card-footer {
      flex-direction: column;

      align-items: flex-start;
    }

  }

</style>