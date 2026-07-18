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

    async function generate() {
        loading = true;
        error = "";
        result = null;

        try {
            result = await generateExecutiveMemo({
                notes,
                memo_type: memoType,
                audience,
                tone
            });
        } catch (err) {
            console.error(err);
            error = "Unable to generate memo.";
        } finally {
            loading = false;
        }
    }

    function copyMemo() {
        navigator.clipboard.writeText(JSON.stringify(result, null, 2));
    }
</script>

<div class="memo-container">

    <h1>Executive Memo Studio</h1>

    <div class="grid">

        <div>
            <label>Memo Type</label>
            <select bind:value={memoType}>
                <option>Weekly Business Review</option>
                <option>Monthly Report</option>
                <option>Project Update</option>
                <option>Board Memo</option>
            </select>
        </div>

        <div>
            <label>Audience</label>
            <select bind:value={audience}>
                <option>Executive Team</option>
                <option>CEO</option>
                <option>Board</option>
                <option>Managers</option>
            </select>
        </div>

        <div>
            <label>Tone</label>
            <select bind:value={tone}>
                <option>Professional</option>
                <option>Formal</option>
                <option>Strategic</option>
                <option>Concise</option>
            </select>
        </div>

    </div>

    <label>Executive Notes</label>

    <textarea
        rows="10"
        bind:value={notes}
        placeholder="Paste meeting notes, KPI updates, project status..."
    />

    <button on:click={generate} disabled={loading}>
        {#if loading}
            Generating...
        {:else}
            Generate Executive Memo
        {/if}
    </button>

    {#if error}
        <p class="error">{error}</p>
    {/if}

    {#if result}
        <ExecutiveMemoResult
            {result}
            onCopy={copyMemo}
        />
    {/if}

</div>

<style>

.memo-container{
    display:flex;
    flex-direction:column;
    gap:20px;
}

.grid{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:18px;
}

label{
    display:block;
    margin-bottom:6px;
    font-weight:600;
}

select,
textarea{
    width:100%;
    background:#0d1733;
    color:white;
    border:1px solid rgba(0,245,212,.25);
    padding:12px;
    border-radius:8px;
}

button{
    padding:14px;
    border:none;
    background:#00F5D4;
    color:#06111f;
    font-weight:bold;
    border-radius:8px;
    cursor:pointer;
}

button:hover{
    opacity:.9;
}

.error{
    color:#ff7d7d;
}

</style>