<script>
    export let text = "";
    export let disabled = false;
    export let type = "button";
</script>

<button {type} {disabled}>
    {text}
</button>

<style>
button {
    width: 100%;
    padding: 12px;
    border: none;
    border-radius: 8px;
    background: #0F172A;
    color: white;
    cursor: pointer;
    font-weight: 600;
    transition: 0.2s;
}

button:hover {
    opacity: 0.9;
}

button:disabled {
    opacity: 0.5;
    cursor: not-allowed;
}
</style>