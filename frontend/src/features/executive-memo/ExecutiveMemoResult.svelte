<script>
  export let result;
  export let onCopy = () => {};
</script>

<div class="memo-report">

  <div class="memo-header">
    <h2>{result.title}</h2>

    <button on:click={onCopy}>
      Copy Memo
    </button>
  </div>

  <section class="memo-card">
    <h3>Executive Summary</h3>
    <p>{result.summary}</p>
  </section>

  <section class="memo-card">
    <h3>Background</h3>
    <p>{result.background}</p>
  </section>

  <section class="memo-card">
    <h3>Key Findings</h3>
    <p>{result.findings}</p>
  </section>

  <section class="memo-card">
    <h3>Business Impact</h3>
    <p>{result.impact}</p>
  </section>

  <section class="memo-card">
    <h3>Recommendations</h3>
    <p>{result.recommendations}</p>
  </section>

  <section class="memo-card">
    <h3>Next Steps</h3>
    <p>{result.next_steps}</p>
  </section>

</div>

<style>

.memo-report{
    display:grid;
    gap:18px;
}

.memo-header{
    display:flex;
    justify-content:space-between;
    align-items:center;
}

.memo-card{
    background:#11193D;
    border:1px solid rgba(0,245,212,.25);
    padding:20px;
}

.memo-card h3{
    margin-top:0;
    color:#00F5D4;
}

.memo-card p{
    line-height:1.6;
}

</style>