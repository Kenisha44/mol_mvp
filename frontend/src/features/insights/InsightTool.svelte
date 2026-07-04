<script>
import LoadingState from "../../components/ui/LoadingState.svelte";
import EmptyState from "../../components/ui/EmptyState.svelte";
import InsightResult from "./InsightResult.svelte";
import { generateInsight } from "./insightService.js";

export let tool;

let inputText = "";
let result = null;
let loading = false;
let error = "";
let copiedLabel = "";

function useSample(){

    inputText = tool.sample;

    result = null;

    error = "";

}

function outputText(){

    if(!result) return "";

    return [

        "Moon Onyx Labs — Insight Generator",

        "",

        `Insight Type: ${result.insight_type}`,

        `Status: ${result.label}`,

        "",

        result.result

    ].join("\n");

}

async function copyText(text,label="Copied"){

    await navigator.clipboard.writeText(text);

    copiedLabel = label;

    setTimeout(()=>copiedLabel="",1800);

}

async function runTool(){

    if(!inputText.trim()){

        error="Paste data first.";

        return;

    }

    loading=true;

    result=null;

    error="";

    copiedLabel="";

    try{

        const [data]=await Promise.all([

            generateInsight(inputText),

            new Promise(resolve=>setTimeout(resolve,800))

        ]);

        result=data;

    }

    catch{

        error="Backend unavailable.";

    }

    finally{

        loading=false;

    }

}
</script>

<div class="input-panel">

<div class="panel-top">

<p class="eyebrow">{tool.eyebrow}</p>

<button class="mini" on:click={useSample}>

Use sample

</button>

</div>

<h2>{tool.title}</h2>

<p class="description">{tool.description}</p>

<textarea

bind:value={inputText}

placeholder={tool.placeholder}

/>

<div class="actions">

<button

class="run-button"

on:click={runTool}

disabled={loading}>

{#if loading}

<span class="loader"></span>

Processing Signal...

{:else}

Run {tool.label}

{/if}

</button>

</div>

{#if error}

<p class="error">{error}</p>

{/if}

</div>

<div class="output-panel">

<div class="output-header">

<p class="eyebrow">

OUTPUT

</p>

<h3>

Executive Insight

</h3>

</div>

{#if loading}

<LoadingState />

{:else if result}

<InsightResult

{result}

onCopy={()=>copyText(outputText(),"Output copied")}

/>

{:else}

<EmptyState

title={tool.emptyTitle}

body={tool.emptyBody}

sample={tool.sample}

onAction={useSample}

/>

{/if}

</div>