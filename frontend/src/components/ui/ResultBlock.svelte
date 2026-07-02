<script>
    export let title = "";
    export let content = "";
    export let onCopy = () => {};
</script>

<div class="result-card">

    <div class="card-heading">

        <h4>{title}</h4>

        <button on:click={onCopy}>
            Copy
        </button>

    </div>

    <pre>{content}</pre>

</div>