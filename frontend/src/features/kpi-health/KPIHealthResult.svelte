<script>
    export let result;
</script>

<div class="health-report">

    <div class="score-card">
        <h2>Overall Health Score</h2>
        <div class="score">{result.overall_score}%</div>
        <p>{result.summary}</p>
    </div>

    <div class="grid">

        <section class="panel">
            <h3>Strengths</h3>

            {#each result.strengths as item}
                <div class="success">🟢 {item}</div>
            {/each}
        </section>

        <section class="panel">
            <h3>Concerns</h3>

            {#each result.concerns as item}
                <div class="warning">🟡 {item}</div>
            {/each}
        </section>

    </div>

    <section class="panel">
        <h3>Recommendations</h3>

        {#each result.recommendations as item}
            <div>✓ {item}</div>
        {/each}
    </section>

</div>

<style>

.health-report{
    display:grid;
    gap:22px;
}

.score-card{
    padding:24px;
    border:1px solid rgba(0,245,212,.25);
    background:#11193D;
}

.score{
    font-size:64px;
    font-weight:700;
    color:#00F5D4;
}

.grid{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:18px;
}

.panel{
    padding:20px;
    border:1px solid rgba(0,245,212,.25);
    background:#11193D;
}

.success{
    color:#7CFC98;
    margin-bottom:8px;
}

.warning{
    color:#FFD166;
    margin-bottom:8px;
}

</style>