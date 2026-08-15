<script>
    import { generateExecutiveMemo } from "./executiveMemoService.js";
    import ExecutiveMemoResult from "./ExecutiveMemoResult.svelte";

    let notes = "";
    let memoType = "Weekly Business Review";
    let audience = "Executive Team";
    let tone = "Professional";

    let loading = false;
    let error = "";
    let result = null;
    let copiedLabel = "";

    $: wordCount = notes.trim()
        ? notes.trim().split(/\s+/).length
        : 0;

    $: characterCount = notes.length;

    function useSample() {
        notes =
            "Revenue increased 18% in Q1. Customer churn increased from 4.8% to 7.2%. " +
            "Enterprise accounts grew from 35 to 46. Support tickets increased after the onboarding redesign. " +
            "Leadership wants recommendations for the next quarter.";

        result = null;
        error = "";
    }

    function clearNotes() {
        notes = "";
        result = null;
        error = "";
        copiedLabel = "";
    }

    async function generate() {
        if (!notes.trim()) {
            error = "Paste executive notes first so MOL can build the memo.";
            return;
        }

        loading = true;
        error = "";
        result = null;
        copiedLabel = "";

        try {
            result = await generateExecutiveMemo({
                notes,
                memo_type: memoType,
                audience,
                tone
            });
        } catch (err) {
            console.error(err);
            error = "Unable to generate memo. Make sure the backend is running.";
        } finally {
            loading = false;
        }
    }

    async function copyMemo() {
        if (!result) return;

        try {
            await navigator.clipboard.writeText(
                JSON.stringify(result, null, 2)
            );

            copiedLabel = "Memo copied";

            setTimeout(() => {
                copiedLabel = "";
            }, 1800);
        } catch {
            error = "Copy failed. You can manually copy the memo.";
        }
    }
</script>

<div class="memo-tool">

    <section class="input-panel">

        <div class="panel-header">
            <div>
                <p class="eyebrow">TOOL 05</p>
                <h2>Executive Memo Studio</h2>

                <p class="description">
                    Turn executive notes, KPI updates, and meeting observations
                    into structured leadership-ready memos.
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

        <div class="configuration-card">

            <p class="config-label">MEMO CONFIGURATION</p>

            <div class="config-grid">

                <div class="field">
                    <label for="memo-type">Memo Type</label>

                    <select
                        id="memo-type"
                        bind:value={memoType}
                    >
                        <option>Weekly Business Review</option>
                        <option>Monthly Report</option>
                        <option>Project Update</option>
                        <option>Board Memo</option>
                    </select>
                </div>

                <div class="field">
                    <label for="audience">Audience</label>

                    <select
                        id="audience"
                        bind:value={audience}
                    >
                        <option>Executive Team</option>
                        <option>CEO</option>
                        <option>Board</option>
                        <option>Managers</option>
                    </select>
                </div>

                <div class="field">
                    <label for="tone">Tone</label>

                    <select
                        id="tone"
                        bind:value={tone}
                    >
                        <option>Professional</option>
                        <option>Formal</option>
                        <option>Strategic</option>
                        <option>Concise</option>
                    </select>
                </div>

            </div>

        </div>

        <div class="editor-shell">

            <div class="editor-label-row">
                <label for="memo-notes">
                    Executive Notes
                </label>

                <div class="editor-meta">
                    <span>{wordCount} words</span>
                    <span>{characterCount} characters</span>
                </div>
            </div>

            <textarea
                id="memo-notes"
                bind:value={notes}
                placeholder="Paste meeting notes, KPI updates, project status, leadership observations..."
            ></textarea>

            <div class="editor-footer">
                <span>
                    Use raw notes, bullets, meeting takeaways, or business updates.
                </span>

                {#if notes}
                    <button
                        type="button"
                        class="text-action"
                        on:click={clearNotes}
                    >
                        Clear
                    </button>
                {/if}
            </div>

        </div>

        <div class="input-hint">
            <p class="hint-label">Best Inputs</p>

            <div class="hint-grid">
                <span>meeting notes</span>
                <span>KPI updates</span>
                <span>project status</span>
                <span>board prep</span>
            </div>
        </div>

        <div class="actions">

            <button
                type="button"
                class="run-button"
                on:click={generate}
                disabled={loading}
            >
                {#if loading}
                    <span class="loader"></span>
                    Building Executive Memo...
                {:else}
                    Generate Executive Memo
                {/if}
            </button>

        </div>

        {#if error}
            <div class="message error">
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
                <p class="eyebrow">EXECUTIVE COMMUNICATION</p>
                <h3>Leadership-ready memo</h3>
            </div>

            {#if result}
                <span class="status-badge">
                    Memo Complete
                </span>
            {/if}

        </div>

        {#if loading}

            <div class="loading-state">
                <span class="large-loader"></span>

                <div>
                    <strong>Structuring leadership communication</strong>
                    <p>
                        MOL is organizing the notes into an executive-ready memo.
                    </p>
                </div>
            </div>

        {:else if result}

            <ExecutiveMemoResult
                {result}
                onCopy={copyMemo}
            />

        {:else}

            <div class="empty-state">
                <p class="eyebrow">READY STATE</p>

                <h4>Build a leadership-ready memo.</h4>

                <p>
                    Add executive notes, select the memo type, audience,
                    and tone, then generate a structured leadership document.
                </p>

                <div class="empty-preview">
                    <span>Executive Summary</span>
                    <span>Key Findings</span>
                    <span>Business Implications</span>
                    <span>Recommended Actions</span>
                </div>

                <button
                    type="button"
                    class="sample-button"
                    on:click={useSample}
                >
                    Load Sample Notes
                </button>
            </div>

        {/if}

    </section>

</div>


<style>
    .memo-tool {
        display: grid;
        grid-template-columns: minmax(350px, .9fr) minmax(0, 1.45fr);
        min-height: 560px;

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

        border-right:
            1px solid rgba(0, 245, 212, .22);
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

    .eyebrow,
    .config-label,
    .hint-label {
        margin: 0 0 8px;

        color: #00f5d4;

        font-size: .7rem;
        font-weight: 900;
        letter-spacing: .13em;
        text-transform: uppercase;
    }

    h2,
    h3,
    h4 {
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


    /* CONFIGURATION */

    .configuration-card {
        margin-top: 24px;

        padding: 16px;

        border: 1px solid rgba(255, 255, 255, .08);

        background: rgba(255, 255, 255, .025);
    }

    .config-grid {
        display: grid;

        grid-template-columns:
            repeat(3, minmax(0, 1fr));

        gap: 10px;
    }

    .field label {
        display: block;

        margin-bottom: 7px;

        color: #91a3ca;

        font-size: .7rem;
        font-weight: 700;
    }

    select {
        width: 100%;

        box-sizing: border-box;

        padding: 10px;

        border:
            1px solid rgba(0, 245, 212, .18);

        border-radius: 4px;

        background: #081027;
        color: #f7f7ff;
    }


    /* EDITOR */

    .editor-shell {
        margin-top: 16px;

        border:
            1px solid rgba(0, 245, 212, .24);

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

        border-bottom:
            1px solid rgba(255, 255, 255, .08);
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
        min-height: 245px;

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

        border-top:
            1px solid rgba(255, 255, 255, .08);

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


    /* INPUT HINT */

    .input-hint {
        margin-top: 14px;

        padding: 14px;

        border:
            1px solid rgba(255, 255, 255, .07);

        background:
            rgba(255, 255, 255, .025);
    }

    .hint-grid {
        display: flex;

        flex-wrap: wrap;

        gap: 7px;
    }

    .hint-grid span {
        padding: 5px 8px;

        border:
            1px solid rgba(0, 245, 212, .18);

        background:
            rgba(0, 245, 212, .04);

        color: #aab8d8;

        font-size: .7rem;
    }


    /* ACTIONS */

    .actions {
        display: flex;

        margin-top: 18px;
    }

    .run-button {
        width: 100%;

        min-height: 46px;

        border: 1px solid #ff007f;
        border-radius: 6px;

        background:
            linear-gradient(
                90deg,
                #9400d3,
                #ff007f
            );

        color: white;

        font-weight: 800;

        cursor: pointer;
    }

    .run-button:hover:not(:disabled) {
        filter: brightness(1.08);
    }

    .run-button:disabled {
        opacity: .6;
        cursor: wait;
    }


    /* OUTPUT */

    .output-header {
        margin-bottom: 18px;

        padding-bottom: 18px;

        border-bottom:
            1px solid rgba(255, 255, 255, .08);
    }

    .status-badge {
        padding: 7px 10px;

        border:
            1px solid rgba(0, 245, 212, .28);

        background:
            rgba(0, 245, 212, .07);

        color: #00f5d4;

        font-size: .7rem;
        font-weight: 800;
        letter-spacing: .08em;
        text-transform: uppercase;
    }


    /* EMPTY */

    .empty-state {
        padding: 26px;

        border:
            1px solid rgba(0, 245, 212, .16);

        background:
            rgba(3, 8, 27, .38);
    }

    .empty-state > p:not(.eyebrow) {
        max-width: 42rem;

        color: #9aabd0;

        line-height: 1.6;
    }

    .empty-preview {
        display: grid;

        grid-template-columns:
            repeat(2, minmax(0, 1fr));

        gap: 8px;

        margin: 20px 0;
    }

    .empty-preview span {
        padding: 12px;

        border:
            1px solid rgba(255, 255, 255, .07);

        color: #8396c0;

        font-size: .76rem;
    }


    /* LOADING */

    .loading-state {
        display: flex;

        align-items: center;

        gap: 16px;

        min-height: 180px;

        padding: 24px;

        border:
            1px solid rgba(0, 245, 212, .12);

        color: #d7e1f8;
    }

    .loading-state p {
        margin: 5px 0 0;

        color: #8293ba;

        font-size: .8rem;
    }

    .loader,
    .large-loader {
        display: inline-block;

        border:
            2px solid rgba(255, 255, 255, .28);

        border-top-color: #00f5d4;

        border-radius: 999px;

        animation: spin .7s linear infinite;
    }

    .loader {
        width: 10px;
        height: 10px;

        margin-right: 8px;
    }

    .large-loader {
        width: 28px;
        height: 28px;
    }

    @keyframes spin {
        to {
            transform: rotate(360deg);
        }
    }


    /* MESSAGES */

    .message {
        margin-top: 14px;

        padding: 12px 14px;

        font-size: .82rem;
        font-weight: 700;
    }

    .error {
        border:
            1px solid rgba(255, 95, 117, .35);

        background:
            rgba(255, 95, 117, .08);

        color: #ff8fa3;
    }

    .success {
        border:
            1px solid rgba(0, 245, 212, .28);

        background:
            rgba(0, 245, 212, .06);

        color: #00f5d4;
    }


    /* RESPONSIVE */

    @media (max-width: 1100px) {

        .memo-tool {
            grid-template-columns: 1fr;
        }

        .input-panel {
            border-right: 0;

            border-bottom:
                1px solid rgba(0, 245, 212, .22);
        }

    }

    @media (max-width: 720px) {

        .config-grid {
            grid-template-columns: 1fr;
        }

        .panel-header,
        .output-header,
        .editor-label-row,
        .editor-footer {
            flex-direction: column;

            align-items: flex-start;
        }

        .empty-preview {
            grid-template-columns: 1fr;
        }

    }

</style>