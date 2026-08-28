<script>
  export let message =
    'You have reached your monthly usage limit.';

  export let type = 'analysis';

  export let onUpgrade = () => {};
</script>


<div class="limit-notice">

  <div class="limit-icon">
    ✦
  </div>


  <div class="limit-copy">

    <span class="limit-label">
      FREE PLAN LIMIT
    </span>

    <strong>
      {type === 'export'
        ? 'Monthly export limit reached'
        : 'Monthly analysis limit reached'}
    </strong>

    <p>
      {message}
    </p>

  </div>


  <button
    type="button"
    class="upgrade-action"
    on:click={onUpgrade}
  >
    Explore Pro
    <span>→</span>
  </button>

</div>


<style>
  .limit-notice {
    display: grid;

    grid-template-columns:
      auto
      minmax(0, 1fr)
      auto;

    align-items: center;

    gap: 14px;

    padding: 15px 16px;

    border:
      1px solid rgba(255, 0, 127, .30);

    background:
      linear-gradient(
        90deg,
        rgba(148, 0, 211, .10),
        rgba(255, 0, 127, .055)
      );
  }


  .limit-icon {
    width: 38px;
    height: 38px;

    display: grid;
    place-items: center;

    border:
      1px solid rgba(255, 0, 127, .30);

    background:
      rgba(255, 0, 127, .08);

    color: #ff5bad;

    font-size: 1rem;
  }


  .limit-copy {
    min-width: 0;

    display: grid;

    gap: 4px;
  }


  .limit-label {
    color: #ff5bad;

    font-size: .57rem;
    font-weight: 900;

    letter-spacing: .11em;
  }


  .limit-copy strong {
    color: #f7f7ff;

    font-size: .78rem;
  }


  .limit-copy p {
    margin: 0;

    color: #91a1c3;

    font-size: .68rem;

    line-height: 1.45;
  }


  .upgrade-action {
    min-height: 38px;

    display: flex;
    align-items: center;

    gap: 8px;

    padding: 0 13px;

    border:
      1px solid rgba(0, 245, 212, .34);

    background:
      rgba(0, 245, 212, .055);

    color: #00f5d4;

    font-family: inherit;
    font-size: .66rem;
    font-weight: 900;

    cursor: pointer;
  }


  .upgrade-action:hover {
    background:
      rgba(0, 245, 212, .11);
  }


  @media (max-width: 650px) {
    .limit-notice {
      grid-template-columns:
        auto
        minmax(0, 1fr);
    }


    .upgrade-action {
      grid-column: 1 / -1;

      justify-content: center;

      width: 100%;
    }
  }
</style>