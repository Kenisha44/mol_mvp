<script>
    export let title = "Moon Onyx Labs";
</script>

<header class="header">
    <div>
        <h1>{title}</h1>
        <p>Executive Intelligence Workspace</p>
    </div>

    <div class="version">
        V1
    </div>
</header>

<style>
.header{
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:20px 30px;
    border-bottom:1px solid #e5e7eb;
    background:white;
}

h1{
    margin:0;
    font-size:1.5rem;
}

p{
    margin:4px 0 0;
    color:#64748b;
}

.version{
    background:#0f172a;
    color:white;
    padding:8px 14px;
    border-radius:8px;
    font-size:.8rem;
}
</style>