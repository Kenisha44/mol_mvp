<script>
  import {
    getSavedAnalyses,
    deleteSavedAnalysis,
    clearSavedAnalyses
  } from "../../lib/analysisStorage.js";

  import { exportAnalysisAsText } from "../../lib/exportUtils.js";
  import { exportAnalysisPDF } from "../../lib/exportService.js";

  let savedAnalyses = [];
  let exportingId = null;
  let exportError = ""; 
  let selectedAnalysis = null;

  let searchTerm = "";
  let toolFilter = "all";
  let sortOrder = "newest";

$: filteredAnalyses = savedAnalyses
  .filter((item) => {
    const matchesTool =
      toolFilter === "all" ||
      item.toolId === toolFilter;

    const searchValue = searchTerm.trim().toLowerCase();

    const matchesSearch =
      !searchValue ||
      item.title?.toLowerCase().includes(searchValue) ||
      item.toolName?.toLowerCase().includes(searchValue) ||
      item.preview?.toLowerCase().includes(searchValue) ||
      item.status?.toLowerCase().includes(searchValue);

    return matchesTool && matchesSearch;
  })
  .sort((a, b) => {
    const first = new Date(a.createdAt ?? 0).getTime();
    const second = new Date(b.createdAt ?? 0).getTime();

    return sortOrder === "oldest"
      ? first - second
      : second - first;
  });

  function loadAnalyses() {
    savedAnalyses = getSavedAnalyses();
  }

  function openAnalysis(item) {
  selectedAnalysis = item;
}

function closeAnalysis() {
  selectedAnalysis = null;
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

  async function downloadPDF(item) {
  if (exportingId) return;

  exportingId = item.id;
  exportError = "";

  try {
    await exportAnalysisPDF(item);
  } catch (err) {
    console.error(err);

    exportError =
      err?.message ||
      "Unable to export PDF.";
  } finally {
    exportingId = null;
  }
}
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
{#if savedAnalyses.length > 0 && !selectedAnalysis}

  <section class="workspace-controls">

    <div class="search-box">
      <label for="workspace-search">
        Search Workspace
      </label>

      <input
        id="workspace-search"
        type="search"
        bind:value={searchTerm}
        placeholder="Search titles, tools, results..."
      />
    </div>


    <div class="filter-box">
      <label for="tool-filter">
        Tool
      </label>

      <select
        id="tool-filter"
        bind:value={toolFilter}
      >
        <option value="all">All Tools</option>
        <option value="clarity">Executive Clarity</option>
        <option value="kpi-cleaner">KPI Cleaner</option>
        <option value="insights">Insight Generator</option>
        <option value="dashboard">Dashboard Narrative</option>
        <option value="executive-memo">Executive Memo</option>
        <option value="kpi-health">KPI Health</option>
      </select>
    </div>


    <div class="filter-box">
      <label for="sort-order">
        Sort
      </label>

      <select
        id="sort-order"
        bind:value={sortOrder}
      >
        <option value="newest">Newest First</option>
        <option value="oldest">Oldest First</option>
      </select>
    </div>

  </section>

{/if}


{#if selectedAnalysis}

  <section class="analysis-viewer">

<div class="viewer-actions">

  <button
    type="button"
    class="export-text-button"
    on:click={() => exportAnalysisAsText(selectedAnalysis)}
  >
    Download TXT
  </button>

  <button
    type="button"
    class="close-viewer"
    on:click={closeAnalysis}
  >
    Back to History
  </button>

</div>


    {#if selectedAnalysis.input}

      <div class="viewer-section">

        <p class="section-label">
          ORIGINAL INPUT
        </p>

        <div class="input-preview">
          {selectedAnalysis.input}
        </div>

      </div>

    {/if}


    <div class="viewer-section">

      <p class="section-label">
        SAVED RESULT
      </p>

      <div class="result-preview">

        {#if selectedAnalysis.toolId === "clarity"}

          <div class="result-block">
            <strong>Clarity Score</strong>
            <p>{selectedAnalysis.result.score}/100</p>
          </div>

          <div class="result-block">
            <strong>Status</strong>
            <p>{selectedAnalysis.result.label}</p>
          </div>

          <div class="result-block">
            <strong>Recommendation</strong>
            <p>{selectedAnalysis.result.recommendation}</p>
          </div>

          <div class="result-block">
            <strong>Refined Executive Copy</strong>
            <p>{selectedAnalysis.result.refined_text}</p>
          </div>


        {:else if selectedAnalysis.toolId === "kpi-cleaner"}

          <div class="result-block">
            <strong>Issues Found</strong>
            <p>{selectedAnalysis.result.issues_found}</p>
          </div>

          <div class="result-block">
            <strong>Status</strong>
            <p>{selectedAnalysis.result.label}</p>
          </div>

          <div class="result-block">
            <strong>Cleaned KPI Output</strong>
            <pre>{selectedAnalysis.result.result}</pre>
          </div>


        {:else if selectedAnalysis.toolId === "insights"}

          <div class="result-block">
            <strong>Primary Insight</strong>
            <p>{selectedAnalysis.result.primary_insight}</p>
          </div>

          <div class="result-block">
            <strong>So What?</strong>
            <p>{selectedAnalysis.result.so_what}</p>
          </div>

          <div class="result-block">
            <strong>Recommended Action</strong>
            <p>{selectedAnalysis.result.recommended_action}</p>
          </div>

          <div class="result-block">
            <strong>Executive Title</strong>
            <p>{selectedAnalysis.result.executive_title}</p>
          </div>

          <div class="result-block">
            <strong>Chart Suggestion</strong>
            <p>{selectedAnalysis.result.chart_suggestion}</p>
          </div>


        {:else if selectedAnalysis.toolId === "dashboard"}

          <div class="result-block">
            <strong>Executive Summary</strong>
            <p>{selectedAnalysis.result.executive_summary}</p>
          </div>

          <div class="result-block">
            <strong>Performance Drivers</strong>
            <p>{selectedAnalysis.result.performance_drivers}</p>
          </div>

          <div class="result-block">
            <strong>Risks & Watch Items</strong>
            <p>{selectedAnalysis.result.risks}</p>
          </div>

          <div class="result-block">
            <strong>Recommended Action</strong>
            <p>{selectedAnalysis.result.recommended_action}</p>
          </div>

          <div class="result-block">
            <strong>Outlook</strong>
            <p>{selectedAnalysis.result.outlook}</p>
          </div>


        {:else if selectedAnalysis.toolId === "executive-memo"}

          <div class="result-block">
            <strong>Executive Summary</strong>
            <p>{selectedAnalysis.result.summary}</p>
          </div>

          <div class="result-block">
            <strong>Background</strong>
            <p>{selectedAnalysis.result.background}</p>
          </div>

          <div class="result-block">
            <strong>Key Findings</strong>
            <p>{selectedAnalysis.result.findings}</p>
          </div>

          <div class="result-block">
            <strong>Business Impact</strong>
            <p>{selectedAnalysis.result.impact}</p>
          </div>

          <div class="result-block">
            <strong>Recommendations</strong>
            <p>{selectedAnalysis.result.recommendations}</p>
          </div>

          <div class="result-block">
            <strong>Next Steps</strong>
            <p>{selectedAnalysis.result.next_steps}</p>
          </div>


        {:else if selectedAnalysis.toolId === "kpi-health"}

          <div class="result-block">
            <strong>Overall Health Score</strong>
            <p>{selectedAnalysis.result.overall_score}/100</p>
          </div>

          <div class="result-block">
            <strong>Executive Assessment</strong>
            <p>{selectedAnalysis.result.summary}</p>
          </div>

          <div class="result-block">
            <strong>Strengths</strong>

            <ul>
              {#each selectedAnalysis.result.strengths ?? [] as item}
                <li>{item}</li>
              {/each}
            </ul>
          </div>

          <div class="result-block">
            <strong>Concerns</strong>

            <ul>
              {#each selectedAnalysis.result.concerns ?? [] as item}
                <li>{item}</li>
              {/each}
            </ul>
          </div>

          <div class="result-block">
            <strong>Recommendations</strong>

            <ul>
              {#each selectedAnalysis.result.recommendations ?? [] as item}
                <li>{item}</li>
              {/each}
            </ul>
          </div>


        {:else}

          <pre>
            {JSON.stringify(selectedAnalysis.result, null, 2)}
          </pre>

        {/if}

      </div>

    </div>

  </section>

{/if}

  {#if !selectedAnalysis && savedAnalyses.length === 0}

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

  {:else if !selectedAnalysis && filteredAnalyses.length > 0}

  <div class="history-grid">
{#if exportError}
  <div class="export-error">
    {exportError}
  </div>
{/if}
      {#each filteredAnalyses as item}
{#if !selectedAnalysis && savedAnalyses.length > 0 && filteredAnalyses.length === 0}

  <div class="no-results">
    <p class="eyebrow">NO MATCHES</p>

    <h3>No saved analyses match your filters.</h3>

    <p>
      Try another search term or select a different MOL tool.
    </p>

    <button
      type="button"
      on:click={() => {
        searchTerm = "";
        toolFilter = "all";
        sortOrder = "newest";
      }}
    >
      Reset Filters
    </button>
  </div>

{/if}
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
                on:click={() => openAnalysis(item)}
                >
                Open
                </button>

                <button
                    type="button"
                    class="pdf-button"
                    on:click={() => downloadPDF(item)}
                    disabled={exportingId === item.id}
                >
                    {#if exportingId === item.id}
                    Exporting...
                    {:else}
                    PDF
                    {/if}
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
  .pdf-button,
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

.analysis-viewer {
  display: grid;
  gap: 20px;

  padding: 26px;

  border: 1px solid rgba(0,245,212,.24);

  background:
    radial-gradient(
      circle at top right,
      rgba(148,0,211,.08),
      transparent 34%
    ),
    rgba(5,10,32,.86);
}

.viewer-header {
  display: flex;

  justify-content: space-between;
  align-items: flex-start;

  gap: 20px;

  padding-bottom: 18px;

  border-bottom:
    1px solid rgba(255,255,255,.08);
}

.viewer-meta {
  display: flex;
  flex-wrap: wrap;

  gap: 8px;

  margin-top: 12px;
}

.viewer-meta span {
  padding: 6px 9px;

  border:
    1px solid rgba(0,245,212,.14);

  background:
    rgba(0,245,212,.035);

  color: #8da2cc;

  font-size: .7rem;
}

.close-viewer {
  flex: 0 0 auto;

  padding: 9px 13px;

  border:
    1px solid rgba(0,245,212,.3);

  background:
    rgba(0,245,212,.05);

  color: #00f5d4;

  font-weight: 800;

  cursor: pointer;
}

.viewer-section {
  display: grid;

  gap: 12px;
}

.section-label {
  margin: 0;

  color: #00f5d4;

  font-size: .7rem;
  font-weight: 900;
  letter-spacing: .12em;
}

.input-preview {
  padding: 18px;

  border-left:
    3px solid #ff007f;

  background:
    rgba(0,0,0,.18);

  color: #dce4f8;

  line-height: 1.65;

  white-space: pre-wrap;
  overflow-wrap: anywhere;
}

.result-preview {
  display: grid;

  gap: 12px;
}

.result-block {
  padding: 18px;

  border:
    1px solid rgba(255,255,255,.08);

  background:
    rgba(16,27,69,.58);
}

.result-block strong {
  display: block;

  margin-bottom: 8px;

  color: #00f5d4;

  font-size: .78rem;
}

.result-block p,
.result-block li,
.result-block pre {
  color: #c8d4f3;

  line-height: 1.65;
}

.result-block p {
  margin: 0;
}

.result-block pre {
  margin: 0;

  white-space: pre-wrap;
  overflow-wrap: anywhere;

  font-family: inherit;
}

.result-block ul {
  margin: 0;

  padding-left: 18px;
}

.workspace-controls {
  display: grid;

  grid-template-columns:
    minmax(260px, 1.4fr)
    minmax(180px, .6fr)
    minmax(170px, .5fr);

  gap: 12px;

  padding: 18px;

  border:
    1px solid rgba(0,245,212,.18);

  background:
    rgba(8,15,43,.72);
}

.search-box,
.filter-box {
  display: grid;
  gap: 7px;
}

.workspace-controls label {
  color: #8193bd;

  font-size: .68rem;
  font-weight: 800;
  letter-spacing: .08em;
  text-transform: uppercase;
}

.workspace-controls input,
.workspace-controls select {
  width: 100%;

  box-sizing: border-box;

  min-height: 42px;

  padding: 0 12px;

  border:
    1px solid rgba(0,245,212,.18);

  background:
    #081027;

  color:
    #f7f7ff;

  font-family:
    inherit;
}

.workspace-controls input::placeholder {
  color:
    #64779f;
}

.workspace-controls input:focus,
.workspace-controls select:focus {
  outline: none;

  border-color:
    rgba(0,245,212,.52);
}

.no-results {
  padding: 30px;

  border:
    1px solid rgba(0,245,212,.16);

  background:
    rgba(5,10,32,.72);
}

.no-results h3 {
  margin-bottom: 8px;
}

.no-results > p:not(.eyebrow) {
  color: #9aabd0;
}

.no-results button {
  margin-top: 14px;

  padding: 9px 13px;

  border:
    1px solid rgba(0,245,212,.3);

  background:
    rgba(0,245,212,.05);

  color:
    #00f5d4;

  font-weight:
    800;

  cursor:
    pointer;
}

.viewer-actions {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 10px;
  flex-wrap: wrap;
}

.export-text-button {
  min-height: 38px;
  padding: 0 13px;

  border: 1px solid rgba(255, 0, 127, .42);

  background:
    linear-gradient(
      90deg,
      rgba(148, 0, 211, .5),
      rgba(255, 0, 127, .5)
    );

  color: #ffffff;

  font-family: inherit;
  font-weight: 800;

  cursor: pointer;
}

.export-text-button:hover {
  border-color: rgba(255, 0, 127, .7);
}

.pdf-button {
  border: 1px solid rgba(255, 0, 127, .35);
  background: rgba(255, 0, 127, .06);
  color: #ff5bad;
}

.pdf-button:hover:not(:disabled) {
  background: rgba(255, 0, 127, .12);
}

.pdf-button:disabled {
  opacity: .5;
  cursor: wait;
}

.export-error {
  padding: 12px 14px;
  border: 1px solid rgba(255, 0, 127, .35);
  background: rgba(255, 0, 127, .06);
  color: #ff7dbd;
  font-size: .8rem;
}

@media (max-width: 640px) {
  .viewer-actions {
    justify-content: flex-start;
  }
}

@media (max-width: 900px) {
  .workspace-controls {
    grid-template-columns: 1fr;
  }
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