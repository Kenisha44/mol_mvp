<script>
  import { supabase } from '../../lib/supabaseClient.js';
  import { passwordRecovery } from '../../stores/authStore.js';

  let password = '';
  let confirmPassword = '';

  let loading = false;
  let message = '';
  let errorMessage = '';

  async function handleResetPassword() {
    errorMessage = '';
    message = '';

    if (!password || !confirmPassword) {
      errorMessage =
        'Enter and confirm your new password.';
      return;
    }

    if (password.length < 6) {
      errorMessage =
        'Password must be at least 6 characters.';
      return;
    }

    if (password !== confirmPassword) {
      errorMessage =
        'Passwords do not match.';
      return;
    }

    loading = true;

    try {
      const { error } =
        await supabase.auth.updateUser({
          password
        });

      if (error) throw error;

      message =
        'Password updated successfully.';

      password = '';
      confirmPassword = '';

      setTimeout(() => {
        passwordRecovery.set(false);
      }, 1000);
    } catch (error) {
      errorMessage =
        error?.message ||
        'Unable to update your password.';
    } finally {
      loading = false;
    }
  }
</script>


<div class="reset-page">

  <section class="reset-card">

    <p class="eyebrow">
      PASSWORD RECOVERY
    </p>

    <h1>
      Create a new password
    </h1>

    <p class="description">
      Enter a new password for your Moon Onyx Labs account.
    </p>


    <form
      on:submit|preventDefault={handleResetPassword}
    >

      <label>
        <span>New Password</span>

        <input
          type="password"
          bind:value={password}
          placeholder="Enter new password"
          autocomplete="new-password"
          minlength="6"
          required
        />
      </label>


      <label>
        <span>Confirm Password</span>

        <input
          type="password"
          bind:value={confirmPassword}
          placeholder="Confirm new password"
          autocomplete="new-password"
          minlength="6"
          required
        />
      </label>


      <button
        type="submit"
        disabled={loading}
      >
        {loading
          ? 'Updating Password...'
          : 'Update Password'}
      </button>

    </form>


    {#if errorMessage}
      <div class="message error">
        {errorMessage}
      </div>
    {/if}


    {#if message}
      <div class="message success">
        {message}
      </div>
    {/if}

  </section>

</div>


<style>
  .reset-page {
    min-height: 100vh;

    display: grid;
    place-items: center;

    padding: 24px;

    background:
      radial-gradient(
        circle at 20% 20%,
        rgba(0, 245, 212, .08),
        transparent 30%
      ),
      radial-gradient(
        circle at 80% 80%,
        rgba(255, 0, 127, .07),
        transparent 30%
      ),
      #05091b;
  }


  .reset-card {
    width: min(100%, 440px);

    padding: 32px;

    border:
      1px solid rgba(0, 245, 212, .2);

    background:
      linear-gradient(
        145deg,
        rgba(18, 27, 68, .94),
        rgba(5, 10, 32, .98)
      );
  }


  .eyebrow {
    margin: 0 0 10px;

    color: #00f5d4;

    font-size: .7rem;
    font-weight: 900;
    letter-spacing: .13em;

    text-transform: uppercase;
  }


  h1 {
    margin: 0;

    color: #f7f7ff;

    font-size: 1.7rem;
  }


  .description {
    margin: 10px 0 24px;

    color: #91a1c3;

    line-height: 1.55;

    font-size: .82rem;
  }


  form {
    display: grid;
    gap: 16px;
  }


  label {
    display: grid;
    gap: 7px;
  }


  label span {
    color: #aebbd8;

    font-size: .72rem;
    font-weight: 800;
  }


  input {
    width: 100%;
    min-height: 46px;

    box-sizing: border-box;

    padding: 0 13px;

    border:
      1px solid rgba(255,255,255,.11);

    border-radius: 4px;

    outline: none;

    background:
      rgba(0,0,0,.18);

    color: #f7f7ff;

    font-family: inherit;
  }


  input:focus {
    border-color:
      rgba(0, 245, 212, .45);

    box-shadow:
      0 0 0 3px
      rgba(0, 245, 212, .05);
  }


  button {
    min-height: 48px;

    margin-top: 4px;

    border:
      1px solid rgba(255, 0, 127, .5);

    border-radius: 4px;

    background:
      linear-gradient(
        90deg,
        rgba(148, 0, 211, .75),
        rgba(255, 0, 127, .75)
      );

    color: white;

    font-family: inherit;
    font-weight: 900;

    cursor: pointer;
  }


  button:disabled {
    opacity: .6;

    cursor: wait;
  }


  .message {
    margin-top: 14px;
    padding: 11px 12px;

    font-size: .76rem;
    line-height: 1.45;
  }


  .message.error {
    border:
      1px solid rgba(255, 0, 127, .3);

    background:
      rgba(255, 0, 127, .06);

    color: #ff6aaa;
  }


  .message.success {
    border:
      1px solid rgba(0, 245, 212, .25);

    background:
      rgba(0, 245, 212, .05);

    color: #00f5d4;
  }


  @media (max-width: 520px) {
    .reset-card {
      padding: 24px;
    }
  }
</style>