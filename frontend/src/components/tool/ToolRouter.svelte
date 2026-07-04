<script>
    import ClarityTool from "../../features/clarity/ClarityTool.svelte";
    import KpiCleanerTool from "../../features/kpi-cleaner/KpiCleanerTool.svelte";
    import InsightTool from "../../features/insights/InsightTool.svelte";
    import DashboardNarrativeTool from "../../features/dashboard-narrative/DashboardNarrativeTool.svelte";

    export let activeTool;
</script>

{#if activeTool.id === "clarity"}

    <ClarityTool tool={activeTool} />

{:else if activeTool.id === "kpi"}

    <KpiCleanerTool tool={activeTool} />

{:else if activeTool.id === "insights"}

    <InsightTool tool={activeTool} />

{:else if activeTool.id === "dashboard"}

    <DashboardNarrativeTool tool={activeTool} />

{/if}