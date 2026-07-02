<script>
  export let title = '';
  export let eyebrow = '';
</script>

<div class="result-card">
  {#if eyebrow || title}
    <div class="card-heading">
      <div>
        {#if eyebrow}
          <p class="eyebrow">{eyebrow}</p>
        {/if}

        {#if title}
          <h4>{title}</h4>
        {/if}
      </div>
    </div>
  {/if}

  <slot />
</div>