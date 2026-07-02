<script>
    export let title = "";
</script>

<div class="card">
    {#if title}
        <h2>{title}</h2>
    {/if}

    <slot />
</div>

<style>
.card {
    background: white;
    border-radius: 12px;
    padding: 20px;
    border: 1px solid #E5E7EB;
    box-shadow: 0 4px 12px rgba(0,0,0,.05);
}

h2 {
    margin-bottom: 16px;
}
</style>