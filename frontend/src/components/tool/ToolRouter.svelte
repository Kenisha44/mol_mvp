<script>
  import { tools } from '../../lib/tools.js';

  import ClarityTool from '../../features/clarity/ClarityTool.svelte';
  import KpiCleanerTool from '../../features/kpi-cleaner/KpiCleanerTool.svelte';
  import InsightTool from '../../features/insights/InsightTool.svelte';
  import DashboardNarrativeTool from '../../features/dashboard-narrative/DashboardNarrativeTool.svelte';
  import ExecutiveMemoTool from '../../features/executive-memo/ExecutiveMemoTool.svelte';
  import KPIHealthTool from '../../features/kpi-health/KPIHealthTool.svelte';
  import WorkspaceView from '../../features/workspace/WorkspaceView.svelte';
  import PlansView from '../../features/plans/PlansView.svelte';

  export let onSelectTool = () => {};
  export let activeTool = 'clarity';

  $: selectedTool =
    tools.find((tool) => tool.id === activeTool) ?? tools[0];
</script>

{#if activeTool === 'clarity'}
  <ClarityTool
  tool={selectedTool}
  onUpgrade={() => onSelectTool('plans')}
/>

{:else if activeTool === 'kpi-cleaner'}
  <KpiCleanerTool
  tool={selectedTool}
  onUpgrade={() => onSelectTool('plans')}
/>

{:else if activeTool === 'insights'}
  <InsightTool
  tool={selectedTool}
  onUpgrade={() => onSelectTool('plans')}
/>

{:else if activeTool === 'dashboard'}
  <DashboardNarrativeTool
  tool={selectedTool}
  onUpgrade={() => onSelectTool('plans')}
/>

{:else if activeTool === 'executive-memo'}
  <ExecutiveMemoTool
  tool={selectedTool}
  onUpgrade={() => onSelectTool('plans')}
/>

{:else if activeTool === 'kpi-health'}
  <KPIHealthTool
  tool={selectedTool}
  onUpgrade={() => onSelectTool('plans')}
/>

{:else if activeTool === 'workspace'}
  <WorkspaceView />

{:else if activeTool === 'plans'}
  <PlansView />
  
{:else}
  <p>Tool not found: {activeTool}</p>
{/if}