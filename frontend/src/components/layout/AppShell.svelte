<script>
  import Sidebar from './Sidebar.svelte';
  import Header from './Header.svelte';
  import Workspace from './Workspace.svelte';

  let activeTool = 'clarity';

  function selectTool(toolId) {
    activeTool = toolId;
  }
</script>

<div class="app-shell">
  <Sidebar
    {activeTool}
    onSelectTool={selectTool}
  />

  <div class="main-area">
    <Header />
    <Workspace
  {activeTool}
  onSelectTool={selectTool}
/>
  </div>
</div>

<style>
  .app-shell {
    min-height: 100vh;
    display: grid;
    grid-template-columns: 300px minmax(0, 1fr);
    background: #050817;
    color: white;
  }

  .main-area {
    min-width: 0;
    display: flex;
    flex-direction: column;
  }

  @media (max-width: 900px) {
    .app-shell {
      grid-template-columns: 1fr;
    }
  }
</style>