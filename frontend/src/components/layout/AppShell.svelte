<script>

import Header from "./Header.svelte";

import Sidebar from "./Sidebar.svelte";

export let activeTool;

export let onSelect;

</script>

<div class="shell">

<Header />

<div class="body">

<Sidebar
    {activeTool}
    {onSelect}
/>

<main>

<slot />

</main>

</div>

</div>

<style>

.shell{

height:100vh;

display:flex;

flex-direction:column;

}

.body{

display:flex;

flex:1;

overflow:hidden;

}

main{

flex:1;

padding:32px;

overflow:auto;

background:#F1F5F9;

}

</style>