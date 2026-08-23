<section class="hero">

  <!-- COSMIC BACKGROUND -->
    <div class="nebula"></div>

    <div class="stars stars-one"></div>
    <div class="stars stars-two"></div>


  <!-- LEFT COPY -->
  <div class="hero-copy">

    <p class="eyebrow">
      WELCOME TO
    </p>

    <h2>
      Executive Intelligence,
      <span>Simplified.</span>
    </h2>

    <p class="hero-description">
      Six specialized executive intelligence tools.
      One unified workspace.
    </p>

    <p class="hero-sub">
      Built for speed. Designed for impact.
    </p>

  </div>


  <!-- LARGE PLANET -->
  <div class="planet-scene">

    <div class="planet-glow"></div>

    <div class="planet">

      <div class="planet-light"></div>

      <div class="planet-texture texture-one"></div>
      <div class="planet-texture texture-two"></div>
      <div class="planet-texture texture-three"></div>

    </div>

    <div class="orbit orbit-one"></div>
    <div class="orbit orbit-two"></div>

  </div>


  <!-- RIGHT STATS -->
  <aside class="hero-stats">

    <div class="stat-item">

      <div class="stat-icon cyan">
        ▣
      </div>

      <div>
        <strong>6</strong>

        <h3>
          POWERFUL TOOLS
        </h3>

        <p>
          All-in-one executive toolkit
        </p>
      </div>

    </div>


    <div class="stat-item">

      <div class="stat-icon purple">
        ↗
      </div>

      <div>
        <strong>0</strong>

        <h3>
          ANALYSES TODAY
        </h3>

        <p>
          Ready when you are
        </p>
      </div>

    </div>

    <div class="stat-item">

    <div class="stat-icon pink">
        ◆
    </div>

    <div>
        <strong class="text-stat">
        DECISION-READY
        </strong>

        <p>
        Clear. Focused. Actionable.
        </p>
    </div>

    </div>

  </aside>

</section>


<style>
  .hero {
    position: relative;

    min-height: 320px;

    display: grid;

    grid-template-columns:
      minmax(0, 1.15fr)
      minmax(300px, .85fr);

    overflow: hidden;

    margin-bottom: 26px;

    border:
      1px solid rgba(0, 245, 212, .22);

    border-radius: 10px;

    background:
      radial-gradient(
        circle at 70% 45%,
        rgba(148, 0, 211, .15),
        transparent 32%
      ),
      radial-gradient(
        circle at 45% 25%,
        rgba(0, 245, 212, .04),
        transparent 28%
      ),
      linear-gradient(
        110deg,
        #071127 0%,
        #070c24 48%,
        #100728 100%
      );

    isolation: isolate;
  }


  /* --------------------------------
     STAR FIELD
  -------------------------------- */

  .stars {
    position: absolute;

    inset: 0;

    pointer-events: none;

    z-index: 0;
  }


 .stars-one {
  opacity: .85;

  background-image:
    radial-gradient(circle at 8% 18%, rgba(255,255,255,.95) 0 1px, transparent 1.5px),
    radial-gradient(circle at 17% 72%, rgba(0,245,212,.85) 0 1px, transparent 1.6px),
    radial-gradient(circle at 24% 31%, rgba(255,255,255,.7) 0 .8px, transparent 1.4px),
    radial-gradient(circle at 31% 84%, rgba(255,255,255,.9) 0 1px, transparent 1.5px),
    radial-gradient(circle at 39% 13%, rgba(121,223,255,.8) 0 .9px, transparent 1.5px),
    radial-gradient(circle at 44% 62%, rgba(255,255,255,.75) 0 .8px, transparent 1.4px),
    radial-gradient(circle at 51% 27%, rgba(0,245,212,.8) 0 1px, transparent 1.7px),
    radial-gradient(circle at 58% 77%, rgba(255,255,255,.85) 0 .9px, transparent 1.5px),
    radial-gradient(circle at 64% 18%, rgba(207,125,255,.9) 0 1px, transparent 1.7px),
    radial-gradient(circle at 71% 58%, rgba(255,255,255,.75) 0 .8px, transparent 1.4px),
    radial-gradient(circle at 78% 24%, rgba(0,245,212,.75) 0 .9px, transparent 1.5px),
    radial-gradient(circle at 84% 81%, rgba(255,255,255,.9) 0 1px, transparent 1.5px),
    radial-gradient(circle at 91% 38%, rgba(255,255,255,.7) 0 .8px, transparent 1.4px),
    radial-gradient(circle at 96% 67%, rgba(201,84,255,.85) 0 1px, transparent 1.6px);
}


.stars-two {
  opacity: .55;

  background-image:
    radial-gradient(circle at 12% 49%, rgba(255,255,255,.65) 0 .6px, transparent 1.2px),
    radial-gradient(circle at 21% 9%, rgba(0,245,212,.55) 0 .7px, transparent 1.3px),
    radial-gradient(circle at 28% 58%, rgba(255,255,255,.6) 0 .7px, transparent 1.2px),
    radial-gradient(circle at 36% 39%, rgba(255,255,255,.55) 0 .6px, transparent 1.2px),
    radial-gradient(circle at 47% 91%, rgba(177,94,255,.7) 0 .8px, transparent 1.4px),
    radial-gradient(circle at 55% 48%, rgba(255,255,255,.65) 0 .6px, transparent 1.2px),
    radial-gradient(circle at 62% 69%, rgba(0,245,212,.55) 0 .7px, transparent 1.3px),
    radial-gradient(circle at 69% 7%, rgba(255,255,255,.65) 0 .6px, transparent 1.2px),
    radial-gradient(circle at 76% 92%, rgba(255,255,255,.6) 0 .7px, transparent 1.3px),
    radial-gradient(circle at 87% 13%, rgba(199,108,255,.65) 0 .7px, transparent 1.3px),
    radial-gradient(circle at 93% 72%, rgba(255,255,255,.55) 0 .6px, transparent 1.2px);
}


  /* --------------------------------
     HERO COPY
  -------------------------------- */

  .hero-copy {
    position: relative;

    z-index: 4;

    display: flex;
    flex-direction: column;
    justify-content: center;

    min-width: 0;

    padding:
      48px 34px 48px 38px;
  }


  .eyebrow {
    margin:
      0 0 12px;

    color:
      #00f5d4;

    font-size:
      .72rem;

    font-weight:
      900;

    letter-spacing:
      .16em;

    text-transform:
      uppercase;
  }


  h2 {
    max-width:
      650px;

    margin:
      0;

    color:
      #f7f7ff;

    font-size:
      clamp(
        2.5rem,
        4.1vw,
        4.3rem
      );

    line-height:
      .98;

    letter-spacing:
      -.045em;
  }


  h2 span {
    display:
      block;

    margin-top:
      6px;

    background:
      linear-gradient(
        90deg,
        #00f5d4,
        #20e6d0 48%,
        #c84cff
      );

    -webkit-background-clip:
      text;

    background-clip:
      text;

    color:
      transparent;
  }


  .hero-description {
    max-width:
      520px;

    margin:
      28px 0 0;

    color:
      #e3e8f7;

    font-size:
      .98rem;

    line-height:
      1.6;
  }


  .hero-sub {
    margin:
      4px 0 0;

    color:
      #a2b1d0;

    font-size:
      .91rem;
  }


  /* --------------------------------
     PLANET
  -------------------------------- */

  .planet-scene {
    position:
      absolute;

    z-index:
      1;

    width:
      520px;

    height:
      520px;

    left:
      47%;

    top:
      60px;

    pointer-events:
      none;
  }


  .planet-glow {
    position:
      absolute;

    width:
      400px;

    height:
      400px;

    top:
      25px;

    left:
      42px;

    border-radius:
      50%;

    background:
      radial-gradient(
        circle,
        rgba(129, 47, 255, .26),
        rgba(0, 245, 212, .12) 40%,
        transparent 70%
      );

    filter:
      blur(35px);
  }


  .planet {
    position:
      absolute;

    width:
      410px;

    height:
      410px;

    top:
      0;

    left:
      50px;

    overflow:
      hidden;

    border-radius:
      50%;

    background:
      radial-gradient(
        circle at 30% 35%,
        #4e1591 0%,
        #7425bb 30%,
        #351065 56%,
        #16072f 78%,
        #060919 100%
      );

    box-shadow:
      -13px -2px 16px
        rgba(0, 245, 212, .28),

      -5px -4px 7px
        rgba(0, 245, 212, .88),

      -24px 0 55px
        rgba(0, 245, 212, .18),

      0 0 70px
        rgba(148, 0, 211, .28);
  }


  /* bright teal planetary rim */

  .planet-light {
    position:
      absolute;

    inset:
      0;

    border-radius:
      50%;

    background:
      radial-gradient(
        circle at 6% 46%,
        rgba(255,255,255,.95) 0%,
        rgba(0,245,212,.82) 2%,
        rgba(0,245,212,.22) 7%,
        transparent 17%
      );

    mix-blend-mode:
      screen;
  }


  /* subtle planet surface detail */

  .planet-texture {
    position:
      absolute;

    border:
      1px solid
      rgba(255,255,255,.05);

    border-radius:
      50%;
  }


  .texture-one {
    width:
      170px;

    height:
      90px;

    top:
      90px;

    left:
      135px;

    transform:
      rotate(-16deg);
  }


  .texture-two {
    width:
      130px;

    height:
      62px;

    top:
      235px;

    left:
      105px;

    transform:
      rotate(24deg);
  }


  .texture-three {
    width:
      220px;

    height:
      120px;

    top:
      165px;

    left:
      175px;

    transform:
      rotate(-12deg);
  }


  /* orbital lines */

  .orbit {
    position:
      absolute;

    border-radius:
      50%;

    border:
      1px solid
      rgba(0,245,212,.15);

    transform:
      rotate(-17deg);
  }


  .orbit-one {
    width:
      470px;

    height:
      170px;

    top:
      100px;

    left:
      -65px;
  }


  .orbit-two {
    width:
      520px;

    height:
      220px;

    top:
      78px;

    left:
      -90px;

    border-color:
      rgba(148,0,211,.18);
  }


  /* --------------------------------
     RIGHT STATS
  -------------------------------- */

  .hero-stats {
    position:
      relative;

    z-index:
      5;

    grid-column:
      2;

    justify-self:
      end;

    width:
      min(100%, 330px);

    display:
      grid;

    align-content:
      center;

    gap:
      24px;

    box-sizing:
      border-box;

    padding:
      30px 30px 30px 28px;

    border-left:
      1px solid
      rgba(255,255,255,.09);

    background:
      linear-gradient(
        90deg,
        rgba(5,10,32,.58),
        rgba(5,10,32,.90)
      );

    backdrop-filter:
      blur(5px);
  }


  .stat-item {
    display:
      grid;

    grid-template-columns:
      54px 1fr;

    align-items:
      center;

    gap:
      16px;
  }


  .stat-icon {
    width:
      52px;

    height:
      52px;

    display:
      grid;

    place-items:
      center;

    border-radius:
      14px;

    font-size:
      1.25rem;

    font-weight:
      900;
  }


  .stat-icon.cyan {
    border:
      1px solid
      rgba(0,245,212,.24);

    background:
      rgba(0,245,212,.08);

    color:
      #00f5d4;
  }


  .stat-icon.purple {
    border:
      1px solid
      rgba(177,50,255,.28);

    background:
      rgba(148,0,211,.10);

    color:
      #d559ff;
  }


  .stat-icon.pink {
    border:
      1px solid
      rgba(255,0,127,.24);

    background:
      rgba(255,0,127,.08);

    color:
      #ff4ca0;
  }


  .stat-item strong {
    display:
      block;

    margin-bottom:
      2px;

    color:
      #ffffff;

    font-size:
      1.7rem;

    line-height:
      1;
  }


  .stat-item strong.text-stat {
    font-size:
      1rem;

    letter-spacing:
      .03em;
  }


  .stat-item h3 {
    margin:
      5px 0 3px;

    color:
      #f7f7ff;

    font-size:
      .78rem;

    letter-spacing:
      .05em;
  }


  .stat-item p {
    margin:
      0;

    color:
      #aab5d0;

    font-size:
      .75rem;

    line-height:
      1.45;
  }


  /* --------------------------------
     RESPONSIVE
  -------------------------------- */

  @media (max-width: 1100px) {

    .hero {
      grid-template-columns:
        1fr;
    }


    .planet-scene {
      left:
        45%;

      opacity:
        .65;
    }


    .hero-stats {
      grid-column:
        1;

      width:
        100%;

      grid-template-columns:
        repeat(3, 1fr);

      border-left:
        0;

      border-top:
        1px solid
        rgba(255,255,255,.08);
    }

  }

    .nebula {
    position: absolute;

    inset: 0;

    z-index: 0;

    pointer-events: none;

    background:
        radial-gradient(
        ellipse at 56% 44%,
        rgba(36, 79, 180, .12),
        transparent 34%
        ),
        radial-gradient(
        ellipse at 73% 36%,
        rgba(148, 0, 211, .13),
        transparent 31%
        ),
        radial-gradient(
        ellipse at 43% 82%,
        rgba(0, 245, 212, .045),
        transparent 28%
        );

    filter: blur(10px);
    }

  @media (max-width: 760px) {

    .hero-copy {
      padding:
        34px 24px;
    }


    .planet-scene {
      left:
        40%;

      top:
        120px;

      transform:
        scale(.82);
    }


    .hero-stats {
      grid-template-columns:
        1fr;

      gap:
        18px;
    }

  }
</style>