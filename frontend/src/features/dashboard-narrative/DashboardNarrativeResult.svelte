<script>
  export let result;

  const sections = [
    {
      label: 'Executive Summary',
      icon: '◐',
      type: 'summary',
      items: null
    },
    {
      label: 'Key Findings',
      icon: '◆',
      type: 'key_findings'
    },
    {
      label: 'Business Risks',
      icon: '!',
      type: 'business_risks'
    },
    {
      label: 'Opportunities',
      icon: '✦',
      type: 'opportunities'
    },
    {
      label: 'Recommendations',
      icon: '✓',
      type: 'recommendations'
    },
    {
      label: 'Action Items',
      icon: '→',
      type: 'action_items'
    }
  ];
</script>

<div class="narrative-report">
  {#each sections as section}
    <section class="report-card">
      <div class="report-heading">
        <span class="report-icon">{section.icon}</span>
        <h4>{section.label}</h4>
      </div>

      {#if section.type === 'summary'}
        <p class="summary">{result.executive_summary}</p>
      {:else}
        <ul>
          {#each result[section.type] as item}
            <li>{item}</li>
          {/each}
        </ul>
      {/if}
    </section>
  {/each}
</div>

<style>
  .narrative-report {
    display: grid;
    gap: 14px;
  }

  .report-card {
    background: rgba(4,5,25,.62);
    border: 1px solid rgba(0,245,212,.28);
    padding: 18px;
    clip-path: polygon(
      0 0,
      calc(100% - 14px) 0,
      100% 14px,
      100% 100%,
      14px 100%,
      0 calc(100% - 14px)
    );
  }

  .report-heading {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 10px;
  }

  .report-icon {
    width: 30px;
    height: 30px;
    display: grid;
    place-items: center;
    border: 1px solid rgba(0,245,212,.45);
    color: #00F5D4;
    background: rgba(0,245,212,.08);
    font-weight: 900;
  }

  h4 {
    margin: 0;
    color: #f7f7ff;
    text-transform: uppercase;
    letter-spacing: .08em;
    font-size: .88rem;
  }

  .summary,
  li {
    color: #D3D3D3;
    line-height: 1.55;
  }

  ul {
    margin: 0;
    padding-left: 20px;
  }

  li {
    margin-bottom: 8px;
  }
</style>