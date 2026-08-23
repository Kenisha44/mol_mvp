<script>
  import { onMount } from 'svelte';

  import AppShell from './components/layout/AppShell.svelte';
  import AuthView from './components/auth/AuthView.svelte';

  import ResetPasswordView from './components/auth/ResetPasswordView.svelte'; 

  import {
  user,
  authLoading,
  passwordRecovery,
  initializeAuth
  } from './stores/authStore.js';

  onMount(() => {
    initializeAuth();
  });
</script>


{#if $authLoading}

  <div class="auth-loading">
    Loading MOL...
  </div>

{:else if $passwordRecovery}

  <ResetPasswordView />

{:else if !$user}

  <AuthView />

{:else}

  <AppShell />

{/if}

<style>
  .auth-loading {
    min-height: 100vh;

    display: grid;
    place-items: center;

    background: #05091b;
    color: #00f5d4;

    font-weight: 800;
  }
</style>