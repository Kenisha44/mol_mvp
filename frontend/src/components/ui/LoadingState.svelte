<div class="loading-state">
  <div class="scan"></div>

  <div>
    <div class="bars">
      <span></span>
      <span></span>
      <span></span>
    </div>

    <h4>Analyzing executive signal...</h4>
    <p>MOL is structuring your input into cleaner, business-ready output.</p>
  </div>
</div>

<style>
  .bars {
    display: grid;
    grid-template-columns: repeat(3, 38px);
    gap: 8px;
    justify-content: center;
    margin-bottom: 8px;
  }

  .bars span {
    height: 38px;
    border: 1px solid rgba(0,245,212,.35);
    background: rgba(0,245,212,.08);
    animation: pulse 1s ease-in-out infinite;
  }

  .bars span:nth-child(2) {
    animation-delay: .15s;
  }

  .bars span:nth-child(3) {
    animation-delay: .3s;
  }

  @keyframes pulse {
    0%, 100% {
      opacity: .35;
      transform: translateY(0);
    }

    50% {
      opacity: 1;
      transform: translateY(-5px);
    }
  }
</style>