<script>
  import { tools } from '../../lib/tools.js';

  export let activeTool = 'clarity';
  export let onSelectTool = () => {};

  const workspaceItems = [
    { label: 'Workspace', sub: 'Saved analyses & history' },
    { label: 'Exports', sub: 'Download your outputs' },
    { label: 'Settings', sub: 'Preferences & configuration' }
  ];
</script>

<aside class="sidebar">
  <div class="brand">
    <div class="orb"></div>

    <div>
      <p>MOON ONYX LABS</p>
      <h2>Executive Insight Engine</h2>
      <span>Executive Intelligence Workspace</span>
    </div>
  </div>

  <div class="section">
    <h3>Executive Intelligence</h3>

    {#each tools as tool}
      <button
        type="button"
        class="nav-item"
        class:active={activeTool === tool.id}
        on:click={() => onSelectTool(tool.id)}
      >
        <strong>{tool.title}</strong>
        <span>{tool.description}</span>
      </button>
    {/each}
  </div>

  <div class="section">
    <h3>Workspace</h3>

    {#each workspaceItems as item}
      <button
        type="button"
        class="nav-item muted"
        disabled
      >
        <strong>{item.label}</strong>
        <span>{item.sub}</span>
      </button>
    {/each}
  </div>

  <div class="upgrade">
    <strong>Upgrade to Pro</strong>
    <span>Unlock advanced insights, exports, and integrations.</span>
  </div>
</aside>

<style>
  .sidebar {
    border-right: 1px solid rgba(0,245,212,.22);
    background: linear-gradient(180deg, #081024, #050817);
    padding: 26px 18px;
  }

  .brand {
    display: flex;
    gap: 14px;
    align-items: center;
    margin-bottom: 34px;
  }

  .orb {
    width: 44px;
    height: 44px;
    border-radius: 999px;
    background: radial-gradient(
      circle at 30% 30%,
      #00F5D4,
      #9400D3 55%,
      #050817 80%
    );
    box-shadow: 0 0 24px rgba(0,245,212,.45);
  }

  .brand p,
  h3 {
    color: #00F5D4;
    text-transform: uppercase;
    letter-spacing: .12em;
    font-size: .72rem;
    margin: 0 0 6px;
  }

  .brand h2 {
    margin: 0;
    font-size: 1.05rem;
  }

  .brand span,
  .nav-item span,
  .upgrade span {
    color: #b7c4e0;
    font-size: .82rem;
  }

  .section {
    border-top: 1px solid rgba(0,245,212,.16);
    padding-top: 22px;
    margin-top: 22px;
  }

  .nav-item {
    width: 100%;
    display: block;
    padding: 13px 14px;
    border: 1px solid transparent;
    border-radius: 8px;
    margin-bottom: 8px;
    background: transparent;
    text-align: left;
    font: inherit;
    cursor: pointer;
    transition:
      border-color .2s ease,
      background .2s ease,
      transform .2s ease;
  }

  .nav-item:hover:not(:disabled) {
    border-color: rgba(0,245,212,.28);
    background: rgba(0,245,212,.06);
    transform: translateX(2px);
  }

  .nav-item.active {
    border-color: #FF007F;
    background: linear-gradient(
      90deg,
      rgba(255,0,127,.28),
      rgba(148,0,211,.14)
    );
  }

  .nav-item strong {
    display: block;
    color: white;
    margin-bottom: 4px;
  }

  .nav-item.muted {
    opacity: .6;
    cursor: not-allowed;
  }

  .upgrade {
    margin-top: 28px;
    border: 1px solid rgba(0,245,212,.35);
    padding: 16px;
    border-radius: 10px;
    background: rgba(0,245,212,.05);
  }

  .upgrade strong {
    color: #00F5D4;
    display: block;
    margin-bottom: 6px;
  }
</style>