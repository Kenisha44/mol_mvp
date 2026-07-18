<script>
    import { analyzeKPIHealth } from "./kpiHealthService.js";
    import KPIHealthResult from "./KPIHealthResult.svelte";

    let data = "";

    let loading = false;
    let error = "";
    let result = null;

    async function analyze() {

        loading = true;
        error = "";
        result = null;

        try {

            result = await analyzeKPIHealth({
                data
            });

        } catch (err) {

            console.error(err);

            error = "Unable to analyze KPI health.";

        } finally {

            loading = false;

        }

    }
</script>

<div class="container">

    <div class="hero">

        <h1>KPI Health Checker</h1>

        <p>
            Evaluate your business performance and identify
            strengths, concerns, and priority actions.
        </p>

    </div>

    <textarea
        rows="12"
        bind:value={data}
        placeholder="Paste KPI summary, dashboard metrics, or executive report..."
    />

    <button
        on:click={analyze}
        disabled={loading}
    >

        {#if loading}
            Analyzing...
        {:else}
            Analyze KPI Health
        {/if}

    </button>

    {#if error}
        <p class="error">{error}</p>
    {/if}

    {#if result}
        <KPIHealthResult
            {result}
        />
    {/if}

</div>

<style>

.container{

    display:grid;
    gap:22px;

}

.hero{

    display:grid;
    gap:8px;

}

.hero h1{

    margin:0;

}

.hero p{

    color:#B7C4E0;

}

textarea{

    width:100%;
    padding:18px;

    background:#0D1733;

    color:white;

    border:1px solid rgba(0,245,212,.22);

    border-radius:10px;

}

button{

    padding:14px;

    border:none;

    border-radius:10px;

    background:#00F5D4;

    color:#05101F;

    font-weight:700;

    cursor:pointer;

}

button:hover{

    opacity:.92;

}

.error{

    color:#ff8080;

}

</style>