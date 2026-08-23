<script>
  import { tools } from '../../lib/tools.js';
  import { supabase } from '../../lib/supabaseClient.js';

  export let activeTool = 'clarity';
  export let onSelectTool = () => {};

  async function handleSignOut() {
    await supabase.auth.signOut();
  }

  const toolIcons = {
    clarity: '▤',
    'kpi-cleaner': '▥',
    insights: '✦',
    dashboard: '▣',
    'executive-memo': '✎',
    'kpi-health': '♡'
  };

  const workspaceItems = [
    {
      id: 'workspace',
      icon: '⌂',
      label: 'Workspace',
      sub: 'Saved analyses & history'
    },
    {
      id: 'plans',
      icon: '◇',
      label: 'Plans & Services',
      sub: 'Software plans & analytics services'
    },
    {
      id: 'settings',
      icon: '⚙',
      label: 'Settings',
      sub: 'Preferences & configuration'
    }
  ];
</script>


<aside class="sidebar">

  <!-- BRAND -->
  <div class="brand">

    <div class="orb"></div>

    <div class="brand-copy">
      <p>MOON ONYX LABS</p>

      <h2>
        Executive Insight Engine
      </h2>

      <span>
        Executive Intelligence Workspace
      </span>
    </div>

  </div>


  <!-- TOOLS -->
  <section class="section">

    <h3>
      Executive Intelligence
    </h3>

    <div class="nav-list">

      {#each tools as tool}

        <button
          type="button"
          class="nav-item"
          class:active={activeTool === tool.id}
          on:click={() => onSelectTool(tool.id)}
        >

          <span class="nav-icon">
            {toolIcons[tool.id] ?? '◇'}
          </span>


          <span class="nav-copy">

            <strong>
              {tool.title}
            </strong>

            <span>
              {tool.description}
            </span>

          </span>


          <span class="nav-arrow">
            →
          </span>

        </button>

      {/each}

    </div>

  </section>


  <!-- WORKSPACE -->
  <section class="section">

    <h3>
      Workspace
    </h3>

    <div class="nav-list">

      {#each workspaceItems as item}

        <button
          type="button"
          class="nav-item workspace-item"
          class:active={activeTool === item.id}
          on:click={() => onSelectTool(item.id)}
          disabled={item.id === 'settings'}
        >

          <span class="nav-icon workspace-icon">
            {item.icon}
          </span>


          <span class="nav-copy">

            <strong>
              {item.label}
            </strong>

            <span>
              {item.sub}
            </span>

          </span>


          {#if item.id === 'settings'}

            <span class="coming-soon">
              SOON
            </span>

          {:else}

            <span class="nav-arrow">
              →
            </span>

          {/if}

        </button>

      {/each}

    </div>

  </section>


  <!-- PRO -->
  <div class="upgrade">

    <div class="upgrade-heading">

      <span class="pro-symbol">
        ✦
      </span>

      <span class="pro-label">
        MOL PRO
      </span>

    </div>


    <strong>
      Unlock more from MOL.
    </strong>

    <p>
      Expanded analysis capacity, premium features,
      and preferred pricing on eligible MOL services.
    </p>


    <button
      type="button"
      on:click={() => onSelectTool('plans')}
    >
      Explore Pro
      <span>→</span>
    </button>

  </div>


  <!-- SIGN OUT -->
  <button
    type="button"
    class="signout-button"
    on:click={handleSignOut}
  >
    Sign Out
  </button>

</aside>


<style>
  .sidebar {
    min-height: 100vh;

    box-sizing: border-box;

    padding: 26px 18px;

    border-right:
      1px solid rgba(0, 245, 212, .18);

    background:
      radial-gradient(
        circle at 20% 4%,
        rgba(0, 245, 212, .045),
        transparent 24%
      ),
      linear-gradient(
        180deg,
        #081024,
        #050817
      );
  }


  /* BRAND */

  .brand {
    display: flex;

    align-items: center;

    gap: 14px;

    margin-bottom: 28px;

    padding-bottom: 24px;

    border-bottom:
      1px solid rgba(255, 255, 255, .07);
  }


  .orb {
    flex: 0 0 46px;

    width: 46px;
    height: 46px;

    border-radius: 50%;

    background:
      radial-gradient(
        circle at 30% 30%,
        #00f5d4,
        #9400d3 55%,
        #050817 80%
      );

    box-shadow:
      0 0 25px
      rgba(0, 245, 212, .38);
  }


  .brand-copy {
    min-width: 0;
  }


  .brand p {
    margin: 0 0 5px;

    color: #00f5d4;

    font-size: .68rem;
    font-weight: 900;

    letter-spacing: .14em;

    text-transform: uppercase;
  }


  .brand h2 {
    margin: 0;

    color: #f7f7ff;

    font-size: 1rem;

    line-height: 1.25;
  }


  .brand span {
    display: block;

    margin-top: 5px;

    color: #8495b9;

    font-size: .7rem;

    line-height: 1.35;
  }


  /* SECTIONS */

  .section {
    margin-top: 24px;
  }


  .section > h3 {
    margin: 0 6px 11px;

    color: #00f5d4;

    font-size: .66rem;
    font-weight: 900;

    letter-spacing: .12em;

    text-transform: uppercase;
  }


  .nav-list {
    display: grid;

    gap: 7px;
  }


  /* NAV ITEMS */

  .nav-item {
    width: 100%;

    min-height: 68px;

    display: grid;

    grid-template-columns:
      38px
      minmax(0, 1fr)
      auto;

    align-items: center;

    gap: 11px;

    padding: 11px 12px;

    border:
      1px solid transparent;

    border-radius: 8px;

    background: transparent;

    color: inherit;

    text-align: left;

    font: inherit;

    cursor: pointer;

    transition:
      transform .18s ease,
      border-color .18s ease,
      background .18s ease,
      box-shadow .18s ease;
  }


  .nav-item:hover:not(:disabled) {
    transform:
      translateX(2px);

    border-color:
      rgba(0, 245, 212, .22);

    background:
      rgba(0, 245, 212, .045);
  }


  .nav-item.active {
    border-color:
      rgba(255, 0, 127, .62);

    background:
      linear-gradient(
        90deg,
        rgba(255, 0, 127, .17),
        rgba(148, 0, 211, .10),
        rgba(8, 16, 36, .35)
      );

    box-shadow:
      inset 3px 0 0 #ff007f;
  }


  .nav-icon {
    width: 36px;
    height: 36px;

    display: grid;

    place-items: center;

    border:
      1px solid rgba(0, 245, 212, .23);

    border-radius: 8px;

    background:
      rgba(0, 245, 212, .05);

    color: #00f5d4;

    font-size: .9rem;
  }


  .nav-item.active .nav-icon {
    border-color:
      rgba(255, 0, 127, .42);

    background:
      rgba(255, 0, 127, .08);

    color: #ff5bad;
  }


  .workspace-icon {
    border-color:
      rgba(184, 90, 255, .25);

    background:
      rgba(148, 0, 211, .055);

    color: #cb67ff;
  }


  .nav-copy {
    min-width: 0;

    display: block;
  }


  .nav-copy strong {
    display: block;

    margin-bottom: 5px;

    color: #f7f7ff;

    font-size: .8rem;

    line-height: 1.25;
  }


  .nav-copy > span {
    display: block;

    color: #98a7c8;

    font-size: .68rem;

    line-height: 1.4;
  }


  .nav-arrow {
    color: #62769e;

    font-size: .8rem;

    transition:
      color .18s ease,
      transform .18s ease;
  }


  .nav-item:hover .nav-arrow,
  .nav-item.active .nav-arrow {
    transform:
      translateX(2px);

    color: #00f5d4;
  }


  .nav-item:disabled {
    opacity: .45;

    cursor: not-allowed;
  }


  .nav-item:disabled:hover {
    transform: none;

    border-color: transparent;

    background: transparent;
  }


  .coming-soon {
    padding: 4px 6px;

    border:
      1px solid rgba(255, 255, 255, .10);

    color: #7a8aae;

    font-size: .5rem;
    font-weight: 900;

    letter-spacing: .08em;
  }


  /* PRO CARD */

  .upgrade {
    margin-top: 26px;

    padding: 17px;

    border:
      1px solid rgba(148, 0, 211, .32);

    border-radius: 10px;

    background:
      radial-gradient(
        circle at top right,
        rgba(255, 0, 127, .11),
        transparent 44%
      ),
      linear-gradient(
        145deg,
        rgba(19, 19, 60, .96),
        rgba(7, 11, 31, .98)
      );
  }


  .upgrade-heading {
    display: flex;

    align-items: center;

    gap: 7px;

    margin-bottom: 11px;
  }


  .pro-symbol {
    color: #ff5bad;
  }


  .pro-label {
    color: #cb67ff;

    font-size: .62rem;
    font-weight: 900;

    letter-spacing: .12em;

    text-transform: uppercase;
  }


  .upgrade > strong {
    display: block;

    margin-bottom: 7px;

    color: #f7f7ff;

    font-size: .82rem;
  }


  .upgrade p {
    margin: 0;

    color: #94a3c4;

    font-size: .67rem;

    line-height: 1.5;
  }


  .upgrade button {
    width: 100%;

    min-height: 39px;

    display: flex;

    align-items: center;
    justify-content: center;

    gap: 7px;

    margin-top: 14px;

    border:
      1px solid rgba(255, 0, 127, .38);

    border-radius: 5px;

    background:
      linear-gradient(
        90deg,
        rgba(148, 0, 211, .38),
        rgba(255, 0, 127, .38)
      );

    color: white;

    font-family: inherit;

    font-size: .68rem;
    font-weight: 900;

    cursor: pointer;
  }


  .upgrade button:hover {
    filter: brightness(1.12);
  }


  /* SIGN OUT */

  .signout-button {
    width: 100%;

    min-height: 40px;

    margin-top: 11px;

    border:
      1px solid rgba(255, 255, 255, .08);

    border-radius: 5px;

    background:
      rgba(255, 255, 255, .02);

    color: #8c9cbc;

    font-family: inherit;

    font-size: .68rem;
    font-weight: 800;

    cursor: pointer;
  }


  .signout-button:hover {
    border-color:
      rgba(255, 0, 127, .28);

    background:
      rgba(255, 0, 127, .035);

    color: #ff5bad;
  }
</style>