<script>
  import { user } from '../../stores/authStore.js';
  import {
  profile,
  profileLoading
} from '../../stores/profileStore.js';
  import { supabase } from '../../lib/supabaseClient.js';

  let accountOpen = false;
  let whatsNewOpen = false;

    function toggleWhatsNew() {
    whatsNewOpen = !whatsNewOpen;
    }

    async function handleSignOut() {
    accountOpen = false;
    whatsNewOpen = false;

    await supabase.auth.signOut();
    }

  function toggleAccount() {
    accountOpen = !accountOpen;
  }

$: currentPlan =
  $profile?.plan ?? 'free';

$: isPro =
  currentPlan === 'pro';

$: analysisCount =
  Number($profile?.analysis_count ?? 0);

$: exportCount =
  Number($profile?.export_count ?? 0);

$: analysisLimit =
  isPro ? 100 : 5;

$: exportLimit =
  isPro ? null : 3;

</script>

<header class="header">

  <div class="header-copy">

    <p class="eyebrow">
      MOON ONYX LABS
    </p>

    <h1>
      Executive Insight Engine
    </h1>

    <p class="subtitle">
    Executive intelligence tools for clearer insights,
    stronger stories, and smarter decisions.
    </p>

  </div>


  <div class="header-actions">

<div class="whats-new-menu">

  <button
    type="button"
    class="whats-new"
    class:open={whatsNewOpen}
    on:click={toggleWhatsNew}
    aria-expanded={whatsNewOpen}
  >
    ✨ What’s New

    <span
      class="whats-new-chevron"
      class:open={whatsNewOpen}
    >
      ▾
    </span>
  </button>


  {#if whatsNewOpen}

    <div class="whats-new-dropdown">

      <div class="release-header">

        <div>
          <p class="release-eyebrow">
            LATEST RELEASE
          </p>

          <h3>
            MOL Suite V1.0
          </h3>
        </div>

        <span class="release-badge">
          NEW
        </span>

      </div>


      <p class="release-copy">
        MOL is evolving into a connected executive
        intelligence workspace.
      </p>


      <div class="release-list">

        <div class="release-item">
          <span>☁</span>

          <div>
            <strong>Cloud Workspace</strong>

            <p>
              Save and revisit analyses securely
              across your MOL account.
            </p>
          </div>
        </div>


        <div class="release-item">
          <span>◆</span>

          <div>
            <strong>6 Executive Tools</strong>

            <p>
              Clarity, KPI cleanup, insights,
              narratives, memos, and KPI health.
            </p>
          </div>
        </div>


        <div class="release-item">
          <span>⇩</span>

          <div>
            <strong>Professional Exports</strong>

            <p>
              Export analysis as PDF and DOCX.
            </p>
          </div>
        </div>


        <div class="release-item">
          <span>◎</span>

          <div>
            <strong>Secure Accounts</strong>

            <p>
              Authentication, private analysis
              history, and account-isolated storage.
            </p>
          </div>
        </div>

      </div>


      <div class="release-footer">
        MOL V1.0 · August 2026
      </div>

    </div>

  {/if}

</div>

    <div class="account-menu">

  <button
    type="button"
    class="account-chip"
    class:open={accountOpen}
    on:click={toggleAccount}
    aria-expanded={accountOpen}
  >
    <span class="account-icon">◎</span>

    <span>Account</span>

    <span
      class="account-chevron"
      class:open={accountOpen}
    >
      ▾
    </span>
  </button>


  {#if accountOpen}
    <div class="account-dropdown">

      <div class="account-user">

        <div class="account-avatar">
          {$user?.email?.charAt(0)?.toUpperCase() || 'M'}
        </div>

        <div class="account-identity">
          <span>Signed in as</span>

          <strong>
            {$user?.email || 'MOL User'}
          </strong>
        </div>

      </div>


    <div
  class="account-plan"
  class:pro-plan={isPro}
>

  <div>
    <span class="plan-label">
      CURRENT PLAN
    </span>

    <strong>
      {#if $profileLoading}
        Loading...
      {:else}
        {isPro ? 'MOL Pro' : 'Free'}
      {/if}
    </strong>
  </div>

  <span
    class="plan-badge"
    class:pro-badge={isPro}
  >
    {isPro ? 'PRO' : 'FREE'}
  </span>

</div>

<div class="account-usage">

  <div class="usage-heading">
    <span>MONTHLY USAGE</span>

    {#if !isPro}
      <span>FREE PLAN</span>
    {:else}
      <span>PRO PLAN</span>
    {/if}
  </div>


  <div class="usage-item">

    <div class="usage-copy">
      <span>Analyses</span>

      <strong>
        {analysisCount} / {analysisLimit}
      </strong>
    </div>

    <div class="usage-track">
      <div
        class="usage-fill"
        style={`width: ${Math.min(
          (analysisCount / analysisLimit) * 100,
          100
        )}%`}
      ></div>
    </div>

  </div>


  <div class="usage-item">

    <div class="usage-copy">
      <span>Exports</span>

      <strong>
        {#if isPro}
          Unlimited
        {:else}
          {exportCount} / {exportLimit}
        {/if}
      </strong>
    </div>

    {#if !isPro}
      <div class="usage-track">
        <div
          class="usage-fill export-fill"
          style={`width: ${Math.min(
            (exportCount / exportLimit) * 100,
            100
          )}%`}
        ></div>
      </div>
    {/if}

  </div>


  {#if !isPro}
    <div class="upgrade-hint">
      <span>✦</span>

      <p>
        Upgrade to MOL Pro for 100 analyses
        and unlimited exports each month.
      </p>
    </div>
  {/if}

</div>

      <div class="account-note">
        <span>☁</span>

        <p>
          Your analyses are saved to your private
          cloud Workspace.
        </p>
      </div>


      <div class="account-divider"></div>


      <button
        type="button"
        class="signout-action"
        on:click={handleSignOut}
      >
        <span>↪</span>
        Sign Out
      </button>

    </div>
  {/if}

</div>

  </div>

</header>


<style>
  .header {
    display: flex;

    justify-content: space-between;
    align-items: center;

    gap: 24px;

    padding: 28px 34px;

    border-bottom:
      1px solid rgba(0, 245, 212, .15);

    background:
      linear-gradient(
        90deg,
        rgba(11, 16, 48, .98),
        rgba(7, 11, 31, .98)
      );
  }


  .header-copy {
    min-width: 0;
  }


  .eyebrow {
    margin: 0 0 6px;

    color: #00f5d4;

    font-size: .7rem;
    font-weight: 900;
    letter-spacing: .18em;

    text-transform: uppercase;
  }


  h1 {
    margin: 0;

    color: #f7f7ff;

    font-size: 1.8rem;
    letter-spacing: -.02em;
  }


  .subtitle {
    margin: 8px 0 0;

    color: #aebbd8;

    font-size: .88rem;
  }


  .header-actions {
    display: flex;
    align-items: center;

    gap: 10px;

    flex: 0 0 auto;
  }


  .whats-new,
  .account-chip {
    min-height: 42px;

    display: flex;
    align-items: center;
    justify-content: center;

    gap: 8px;

    padding: 0 14px;

    border:
      1px solid rgba(255, 255, 255, .10);

    background:
      rgba(255, 255, 255, .025);

    color: #d8e1f5;

    font-family: inherit;
    font-size: .78rem;
    font-weight: 800;
  }


  .whats-new {
    cursor: pointer;
  }


  .whats-new:hover {
    border-color:
      rgba(0, 245, 212, .28);

    color: #00f5d4;
  }


  .account-chip {
    border-color:
      rgba(0, 245, 212, .18);
  }


  .account-icon {
    color: #00f5d4;

    font-size: 1rem;
  }

.account-menu {
  position: relative;
}


.account-chip {
  cursor: pointer;
}


.account-chip:hover,
.account-chip.open {
  border-color:
    rgba(0, 245, 212, .36);

  background:
    rgba(0, 245, 212, .045);

  color: #f7f7ff;
}


.account-chevron {
  margin-left: 2px;

  color: #7184ad;

  font-size: .7rem;

  transition:
    transform .18s ease;
}


.account-chevron.open {
  transform: rotate(180deg);
}


.account-dropdown {
  position: absolute;

  z-index: 100;

  top: calc(100% + 10px);
  right: 0;

  width: 310px;

  padding: 15px;

  border:
    1px solid rgba(0, 245, 212, .22);

  border-radius: 8px;

  background:
    linear-gradient(
      145deg,
      rgba(14, 22, 55, .99),
      rgba(5, 10, 30, .99)
    );

  box-shadow:
    0 22px 60px
    rgba(0, 0, 0, .42);
}


.account-user {
  display: flex;

  align-items: center;

  gap: 12px;

  padding: 4px 3px 14px;
}


.account-avatar {
  flex: 0 0 42px;

  width: 42px;
  height: 42px;

  display: grid;
  place-items: center;

  border:
    1px solid rgba(0, 245, 212, .35);

  border-radius: 50%;

  background:
    radial-gradient(
      circle at 30% 30%,
      rgba(0, 245, 212, .30),
      rgba(148, 0, 211, .25)
    );

  color: #f7f7ff;

  font-size: .9rem;
  font-weight: 900;
}


.account-identity {
  min-width: 0;

  display: grid;

  gap: 3px;
}


.account-identity span {
  color: #7184ad;

  font-size: .62rem;

  text-transform: uppercase;

  letter-spacing: .07em;
}


.account-identity strong {
  overflow: hidden;

  color: #f7f7ff;

  font-size: .76rem;

  text-overflow: ellipsis;

  white-space: nowrap;
}


.account-plan {
  display: flex;

  justify-content: space-between;
  align-items: center;

  gap: 15px;

  padding: 13px;

  border:
    1px solid rgba(148, 0, 211, .20);

  background:
    rgba(148, 0, 211, .055);
}


.account-plan > div {
  display: grid;

  gap: 4px;
}


.plan-label {
  color: #8f9dbd;

  font-size: .58rem;
  font-weight: 900;

  letter-spacing: .10em;
}


.account-plan strong {
  color: #f7f7ff;

  font-size: .9rem;
}


.plan-badge {
  padding: 5px 8px;

  border:
    1px solid rgba(0, 245, 212, .24);

  color: #00f5d4;

  font-size: .58rem;
  font-weight: 900;

  letter-spacing: .08em;
}


.account-note {
  display: flex;

  gap: 9px;

  margin-top: 11px;

  padding: 10px 11px;

  background:
    rgba(0, 245, 212, .035);
}


.account-note > span {
  color: #00f5d4;
}


.account-note p {
  margin: 0;

  color: #91a1c3;

  font-size: .66rem;

  line-height: 1.45;
}


.account-divider {
  height: 1px;

  margin: 13px 0;

  background:
    rgba(255,255,255,.07);
}


.signout-action {
  width: 100%;
  min-height: 38px;

  display: flex;

  align-items: center;

  gap: 9px;

  padding: 0 11px;

  border:
    1px solid rgba(255, 0, 127, .16);

  background:
    rgba(255, 0, 127, .025);

  color: #c8d2e8;

  font-family: inherit;
  font-size: .7rem;
  font-weight: 800;

  cursor: pointer;
}


.signout-action:hover {
  border-color:
    rgba(255, 0, 127, .38);

  background:
    rgba(255, 0, 127, .06);

  color: #ff67b4;
}

.whats-new-menu {
  position: relative;
}


.whats-new.open {
  border-color:
    rgba(0, 245, 212, .36);

  background:
    rgba(0, 245, 212, .045);

  color: #00f5d4;
}


.whats-new-chevron {
  color: #7184ad;

  font-size: .7rem;

  transition:
    transform .18s ease;
}


.whats-new-chevron.open {
  transform: rotate(180deg);
}


.whats-new-dropdown {
  position: absolute;

  z-index: 100;

  top: calc(100% + 10px);
  right: 0;

  width: 340px;

  padding: 16px;

  border:
    1px solid rgba(0, 245, 212, .22);

  border-radius: 8px;

  background:
    linear-gradient(
      145deg,
      rgba(14, 22, 55, .99),
      rgba(5, 10, 30, .99)
    );

  box-shadow:
    0 22px 60px
    rgba(0, 0, 0, .42);
}


.release-header {
  display: flex;

  justify-content: space-between;
  align-items: flex-start;

  gap: 14px;

  padding-bottom: 12px;

  border-bottom:
    1px solid rgba(255, 255, 255, .07);
}


.release-eyebrow {
  margin: 0 0 5px;

  color: #00f5d4;

  font-size: .58rem;
  font-weight: 900;
  letter-spacing: .11em;

  text-transform: uppercase;
}


.release-header h3 {
  margin: 0;

  color: #f7f7ff;

  font-size: .95rem;
}


.release-badge {
  padding: 5px 8px;

  border:
    1px solid rgba(255, 0, 127, .32);

  background:
    rgba(255, 0, 127, .06);

  color: #ff5bad;

  font-size: .56rem;
  font-weight: 900;

  letter-spacing: .08em;
}

.release-copy {
  margin: 13px 0;

  color: #95a5c7;

  font-size: .7rem;

  line-height: 1.5;
}

.release-list {
  display: grid;

  gap: 8px;
}


.release-item {
  display: grid;

  grid-template-columns:
    28px 1fr;

  gap: 10px;

  padding: 10px;

  border:
    1px solid rgba(255, 255, 255, .055);

  background:
    rgba(255, 255, 255, .015);
}

.release-item > span {
  color: #00f5d4;

  font-size: .85rem;
}


.release-item strong {
  display: block;

  margin-bottom: 3px;

  color: #dfe7f8;

  font-size: .69rem;
}


.release-item p {
  margin: 0;

  color: #7f90b4;

  font-size: .63rem;

  line-height: 1.4;
}

.release-footer {
  margin-top: 12px;

  padding-top: 10px;

  border-top:
    1px solid rgba(255, 255, 255, .07);

  color: #667aa4;

  font-size: .58rem;

  text-align: right;
}

  @media (max-width: 760px) {
    .header {
      align-items: flex-start;
      flex-direction: column;
    }

    .header-actions {
      width: 100%;
    }

    .whats-new,
    .account-chip {
      flex: 1 1 auto;
    }
    .account-menu {
  flex: 1 1 auto;
}

.account-chip {
  width: 100%;
}

.account-dropdown {
  width: min(310px, calc(100vw - 48px));
}

.whats-new-menu {
  flex: 1 1 auto;
}

.whats-new {
  width: 100%;
}

.whats-new-dropdown {
  width: min(340px, calc(100vw - 48px));
}
  }

.account-usage {
  margin-top: 11px;

  padding: 13px;

  border:
    1px solid rgba(255, 255, 255, .065);

  background:
    rgba(255, 255, 255, .018);
}


.usage-heading {
  display: flex;

  justify-content: space-between;
  align-items: center;

  gap: 10px;

  margin-bottom: 13px;

  color: #7184ad;

  font-size: .54rem;
  font-weight: 900;

  letter-spacing: .09em;
}


.usage-item + .usage-item {
  margin-top: 12px;
}


.usage-copy {
  display: flex;

  justify-content: space-between;
  align-items: center;

  gap: 10px;

  margin-bottom: 6px;
}


.usage-copy span {
  color: #9cabc8;

  font-size: .65rem;
}


.usage-copy strong {
  color: #dfe7f8;

  font-size: .65rem;
}


.usage-track {
  height: 4px;

  overflow: hidden;

  background:
    rgba(255, 255, 255, .07);
}


.usage-fill {
  height: 100%;

  background:
    linear-gradient(
      90deg,
      #9400d3,
      #00f5d4
    );

  transition:
    width .3s ease;
}


.export-fill {
  background:
    linear-gradient(
      90deg,
      #9400d3,
      #ff007f
    );
}


.upgrade-hint {
  display: flex;

  gap: 8px;

  margin-top: 13px;

  padding-top: 11px;

  border-top:
    1px solid rgba(255, 255, 255, .06);
}


.upgrade-hint > span {
  color: #ff5bad;
}


.upgrade-hint p {
  margin: 0;

  color: #8596b9;

  font-size: .61rem;

  line-height: 1.45;
}


.account-plan.pro-plan {
  border-color:
    rgba(255, 0, 127, .28);

  background:
    linear-gradient(
      90deg,
      rgba(148, 0, 211, .10),
      rgba(255, 0, 127, .07)
    );
}


.plan-badge.pro-badge {
  border-color:
    rgba(255, 0, 127, .38);

  color: #ff5bad;
}  
</style>