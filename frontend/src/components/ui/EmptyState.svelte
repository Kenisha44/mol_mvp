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

 <button class="sample-button" on:click={onAction}>
  {buttonText}
</button>
</div>
<style>
  .empty-state {
    min-width: 0;
    max-width: 100%;
    overflow: hidden;
  }

  pre {
    margin: 14px 0;
    width: 100%;
    max-width: 100%;
    box-sizing: border-box;

    white-space: pre-wrap;
    overflow-wrap: anywhere;
    word-break: break-word;

    padding: 14px;
    border-left: 2px solid #00f5d4;

    background: rgba(0, 0, 0, 0.16);
    color: #c7d2ee;

    font-size: 0.78rem;
    line-height: 1.55;
  }
</style>
