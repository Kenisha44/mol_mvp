<script>
  export let tag = 'READY STATE';
  export let title = '';
  export let body = '';
  export let sample = '';
  export let buttonText = 'Load sample input';
  export let onAction = () => {};
</script>

<div class="empty-state enhanced">
  <p class="empty-tag">{tag}</p>
  <h4>{title}</h4>
  <p>{body}</p>

  {#if sample}
    <pre>{sample}</pre>
  {/if}

  <button class="mini wide" on:click={onAction}>
    {buttonText}
  </button>
</div>