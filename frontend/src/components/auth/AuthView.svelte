<script>
  import { supabase } from '../../lib/supabaseClient.js';

  let mode = 'signin';

  let email = '';
  let password = '';

  $: isSignUp = mode === 'signup';

  function switchMode(nextMode) {
    mode = nextMode;
    email = '';
    password = '';
  }

  let loading = false;
  let message = '';
  let errorMessage = '';

  async function handleSubmit() {
  loading = true;
  message = '';
  errorMessage = '';

  try {
    if (isSignUp) {
      const { error } = await supabase.auth.signUp({
        email,
        password
      });

      if (error) throw error;

      message =
        'Account created. Check your email if confirmation is required.';
    } else {
      const { error } =
        await supabase.auth.signInWithPassword({
          email,
          password
        });

      if (error) throw error;
    }
  } catch (error) {
    errorMessage =
      error?.message ||
      'Unable to complete authentication.';
  } finally {
    loading = false;
  }
}

async function handleForgotPassword() {
  errorMessage = '';
  message = '';

  if (!email) {
    errorMessage =
      'Enter your email address first, then try again.';
    return;
  }

  loading = true;

  try {
    const { error } =
      await supabase.auth.resetPasswordForEmail(
        email,
        {
          redirectTo:
            `${window.location.origin}`
        }
      );

    if (error) throw error;

    message =
      'Password reset instructions were sent to your email.';
  } catch (error) {
    errorMessage =
      error?.message ||
      'Unable to send password reset instructions.';
  } finally {
    loading = false;
  }
}
</script>


<div class="auth-page">

  <section class="auth-intro">

    <div class="brand-mark">
      <span>M</span>
    </div>

    <p class="eyebrow">
      MOON ONYX LABS
    </p>

    <h1>
      Executive intelligence,
      <span>built for clarity.</span>
    </h1>

    <p class="intro-copy">
      Analyze KPIs, uncover business insights, improve
      executive reporting, and keep your analysis organized
      in one intelligent workspace.
    </p>

    <div class="feature-list">

      <div class="feature">
        <span class="feature-number">01</span>

        <div>
          <strong>Executive Intelligence</strong>
          <p>
            Turn business information into clearer,
            decision-ready insights.
          </p>
        </div>
      </div>


      <div class="feature">
        <span class="feature-number">02</span>

        <div>
          <strong>Connected Workspace</strong>
          <p>
            Save and revisit your analyses from your
            MOL account.
          </p>
        </div>
      </div>


      <div class="feature">
        <span class="feature-number">03</span>

        <div>
          <strong>Professional Reporting</strong>
          <p>
            Export analysis into polished PDF and
            Word deliverables.
          </p>
        </div>
      </div>

    </div>

  </section>


  <section class="auth-panel">

    <div class="auth-card">

      <div class="auth-heading">

        <p class="eyebrow">
          {isSignUp ? 'CREATE ACCOUNT' : 'WELCOME BACK'}
        </p>

        <h2>
          {isSignUp
            ? 'Start using MOL'
            : 'Sign in to your workspace'}
        </h2>

        <p>
          {isSignUp
            ? 'Create your account to begin building your executive intelligence workspace.'
            : 'Access your analyses, tools, and MOL workspace.'}
        </p>

      </div>


      <div class="mode-switch">

        <button
          type="button"
          class:active={!isSignUp}
          on:click={() => switchMode('signin')}
        >
          Sign In
        </button>

        <button
          type="button"
          class:active={isSignUp}
          on:click={() => switchMode('signup')}
        >
          Create Account
        </button>

      </div>


      <form
          on:submit|preventDefault={handleSubmit}
      >

        <label>
          <span>Email Address</span>

          <input
            type="email"
            bind:value={email}
            placeholder="you@company.com"
            autocomplete="email"
            required
          />
        </label>


        <label>
          <span>Password</span>

          <input
            type="password"
            bind:value={password}
            placeholder="Enter your password"
            autocomplete={isSignUp
              ? 'new-password'
              : 'current-password'}
            minlength="6"
            required
          />
        </label>

        {#if !isSignUp}
        <div class="forgot-row">
            <button
            type="button"
            class="forgot-button"
            on:click={handleForgotPassword}
            disabled={loading}
            >
            Forgot password?
            </button>
        </div>
        {/if}

        <button
            type="submit"
            class="submit-button"
            disabled={loading}
            >
            {#if loading}
                Please wait...
            {:else}
                {isSignUp
                ? 'Create MOL Account'
                : 'Sign In to MOL'}
            {/if}
            </button>

      </form>

    {#if errorMessage}
    <div class="auth-message error">
        {errorMessage}
    </div>
    {/if}

    {#if message}
    <div class="auth-message success">
        {message}
    </div>
    {/if}

      <div class="auth-footer">

        <span>
          {isSignUp
            ? 'Already have an account?'
            : 'New to MOL?'}
        </span>

        <button
          type="button"
          on:click={() =>
            switchMode(
              isSignUp ? 'signin' : 'signup'
            )}
        >
          {isSignUp
            ? 'Sign In'
            : 'Create Account'}
        </button>

      </div>

    </div>

  </section>

</div>


<style>
  .auth-page {
    min-height: 100vh;

    display: grid;
    grid-template-columns:
      minmax(0, 1.1fr)
      minmax(420px, .9fr);

    background:
      radial-gradient(
        circle at 15% 20%,
        rgba(0, 245, 212, .08),
        transparent 28%
      ),
      radial-gradient(
        circle at 80% 80%,
        rgba(255, 0, 127, .07),
        transparent 28%
      ),
      #05091b;
  }


  .auth-intro {
    display: flex;
    flex-direction: column;
    justify-content: center;

    padding: 70px clamp(40px, 7vw, 110px);
  }


  .brand-mark {
    width: 46px;
    height: 46px;

    display: grid;
    place-items: center;

    margin-bottom: 22px;

    border:
      1px solid rgba(0, 245, 212, .38);

    background:
      rgba(0, 245, 212, .055);

    color: #00f5d4;

    font-weight: 900;
    font-size: 1.15rem;
  }


  .eyebrow {
    margin: 0 0 10px;

    color: #00f5d4;

    font-size: .7rem;
    font-weight: 900;
    letter-spacing: .14em;

    text-transform: uppercase;
  }


  h1 {
    max-width: 650px;

    margin: 0;

    color: #f7f7ff;

    font-size:
      clamp(2.3rem, 4vw, 4.4rem);

    line-height: 1.02;
    letter-spacing: -.04em;
  }


  h1 span {
    display: block;

    color: #ff4ca0;
  }


  .intro-copy {
    max-width: 590px;

    margin: 24px 0 0;

    color: #a7b5d5;

    font-size: .95rem;
    line-height: 1.7;
  }


  .feature-list {
    display: grid;
    gap: 16px;

    max-width: 590px;

    margin-top: 38px;
  }


  .feature {
    display: flex;
    gap: 14px;

    padding-top: 16px;

    border-top:
      1px solid rgba(255, 255, 255, .07);
  }


  .feature-number {
    flex: 0 0 30px;

    color: #00f5d4;

    font-size: .68rem;
    font-weight: 900;
  }


  .feature strong {
    color: #edf1ff;

    font-size: .83rem;
  }


  .feature p {
    margin: 4px 0 0;

    color: #7f90b5;

    font-size: .76rem;
    line-height: 1.5;
  }


  .auth-panel {
    display: grid;
    place-items: center;

    padding: 40px;

    border-left:
      1px solid rgba(255, 255, 255, .07);

    background:
      rgba(8, 14, 38, .62);
  }


  .auth-card {
    width: min(100%, 430px);

    padding: 32px;

    border:
      1px solid rgba(0, 245, 212, .18);

    background:
      linear-gradient(
        145deg,
        rgba(18, 27, 68, .92),
        rgba(5, 10, 32, .97)
      );
  }


  .auth-heading h2 {
    margin: 0;

    color: #f7f7ff;

    font-size: 1.55rem;
  }


  .auth-heading > p:last-child {
    margin: 10px 0 0;

    color: #8fa0c4;

    font-size: .8rem;
    line-height: 1.55;
  }


  .mode-switch {
    display: grid;
    grid-template-columns: 1fr 1fr;

    margin: 26px 0 22px;

    border:
      1px solid rgba(255, 255, 255, .08);

    background:
      rgba(0, 0, 0, .15);
  }


  .mode-switch button {
    min-height: 42px;

    border: 0;

    background: transparent;
    color: #8393b8;

    font-family: inherit;
    font-size: .75rem;
    font-weight: 900;

    cursor: pointer;
  }


  .mode-switch button.active {
    background:
      rgba(0, 245, 212, .08);

    color: #00f5d4;
  }


  form {
    display: grid;
    gap: 17px;
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
      1px solid rgba(255, 255, 255, .11);

    border-radius: 4px;

    outline: none;

    background:
      rgba(0, 0, 0, .18);

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


  input::placeholder {
    color: #58698f;
  }


  .submit-button {
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


  .submit-button:hover {
    filter: brightness(1.08);
  }


  .auth-footer {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 6px;

    margin-top: 22px;

    color: #7889ad;

    font-size: .73rem;
  }


  .auth-footer button {
    padding: 0;

    border: 0;

    background: transparent;
    color: #00f5d4;

    font-family: inherit;
    font-size: inherit;
    font-weight: 900;

    cursor: pointer;
  }


  @media (max-width: 900px) {
    .auth-page {
      grid-template-columns: 1fr;
    }

    .auth-intro {
      padding:
        50px 28px 36px;
    }

    .auth-panel {
      padding: 28px;

      border-left: 0;

      border-top:
        1px solid rgba(255, 255, 255, .07);
    }
  }

.auth-message {
  margin-top: 14px;
  padding: 11px 12px;

  font-size: .76rem;
  line-height: 1.45;
}

.auth-message.error {
  border: 1px solid rgba(255, 0, 127, .3);
  background: rgba(255, 0, 127, .06);
  color: #ff6aaa;
}

.auth-message.success {
  border: 1px solid rgba(0, 245, 212, .25);
  background: rgba(0, 245, 212, .05);
  color: #00f5d4;
}

.forgot-row {
  display: flex;
  justify-content: flex-end;

  margin-top: -8px;
}

.forgot-button {
  padding: 0;

  border: 0;

  background: transparent;
  color: #00f5d4;

  font-family: inherit;
  font-size: .7rem;
  font-weight: 800;

  cursor: pointer;
}

.forgot-button:hover {
  color: #ff4ca0;
}

  @media (max-width: 520px) {
    .auth-card {
      padding: 24px;
    }

    .auth-panel {
      padding: 18px;
    }
  }
</style>