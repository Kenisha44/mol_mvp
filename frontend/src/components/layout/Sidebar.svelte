<script>
    import { tools } from "../../lib/tools.js";

    export let activeTool;
    export let onSelect;
</script>

<aside class="sidebar">

    <h3>Tools</h3>

    {#each tools as tool}

        <button
            class:active={activeTool===tool.id}
            on:click={() => onSelect(tool.id)}>

            {tool.title}

        </button>

    {/each}

</aside>

<style>

.sidebar{

    width:260px;

    background:#F8FAFC;

    padding:24px;

    border-right:1px solid #E2E8F0;

}

button{

    width:100%;

    margin-bottom:10px;

    padding:12px;

    border:none;

    background:white;

    border-radius:8px;

    cursor:pointer;

    text-align:left;

}

button.active{

    background:#0F172A;

    color:white;

}

</style>