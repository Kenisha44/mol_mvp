<script>
  import Sidebar from './Sidebar.svelte';
  import Header from './Header.svelte';
  import Workspace from './Workspace.svelte';
</script>

<div class="app-shell">
  <Sidebar />

  <div class="main-area">
    <Header />
    <Workspace />
  </div>
</div>

<style>
  .app-shell {
    display: grid;
    grid-template-columns: 280px 1fr;
    min-height: 100vh;
    background: #070B1E;
    color: #f7f7ff;
  }

  .main-area {
    min-width: 0;
    display: flex;
    flex-direction: column;
  }
</style>