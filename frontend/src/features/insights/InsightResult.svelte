<script>
    export let result;
    export let onCopy = () => {};
</script>

<div class="result-card">

    <div class="card-heading">

        <h4>Insight Generator Result</h4>

        <button on:click={onCopy}>
            Copy
        </button>

    </div>

    <div class="score-block">

        <span>Insight Type</span>

        <strong>{result.insight_type}</strong>

    </div>

    <div class="result-card">

        <h4>Status</h4>

        <p>{result.label}</p>

    </div>

    <div class="result-card">

        <h4>Executive Insight</h4>

        <pre>{result.result}</pre>

    </div>

</div>