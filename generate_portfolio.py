html = """<!doctype html>
<html lang="tr">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Portfolio - Makeup by Iremi</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet" />
  <style>
    :root {
      --bg: #f6f4f0;
      --bg-dark: #111111;
      --ink: #0b0b0b;
      --gold: #c9a97a;
      --muted: #8a8a8a;
      --font-serif: "Playfair Display", serif;
      --font-sans: "Jost", sans-serif;
    }

    * { box-sizing: border-box; }

    html, body {
      margin: 0; padding: 0;
      background: var(--bg);
      color: var(--ink);
      font-family: var(--font-sans);
      -webkit-font-smoothing: antialiased;
      overflow: hidden;
      width: 100vw; height: 100vh;
      overscroll-behavior: none; /* Prevent pull-to-refresh on mobile */
    }

    /* HEADER STYLES COPIED FROM INDEX */
    .site-header {
      position: fixed; top: 0; left: 0; right: 0; z-index: 50;
      display: flex; align-items: center; justify-content: space-between;
      padding: 28px 44px 0; pointer-events: none;
      transition: background-color 0.3s ease, padding 0.3s ease, box-shadow 0.3s ease;
    }
    .site-header.scrolled {
      background-color: var(--bg);
      padding-bottom: 24px; padding-top: 24px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.05);
    }
    .site-header>* { pointer-events: auto; }
    .logo {
      font-family: var(--font-serif); font-weight: 500; font-size: 26px;
      letter-spacing: 0.01em; color: var(--ink); line-height: 1;
      position: relative; z-index: 60; text-decoration: none;
    }
    .logo em { font-style: italic; font-weight: 400; }
    .nav { display: flex; gap: 38px; list-style: none; margin: 0; padding: 0; }
    .nav a {
      font-family: var(--font-sans); font-size: 11px; font-weight: 400;
      letter-spacing: 0.18em; text-transform: uppercase; color: var(--ink);
      text-decoration: none; position: relative; padding-bottom: 4px; transition: color .25s ease;
    }
    .nav a::after {
      content: ""; position: absolute; left: 0; right: 100%; bottom: 0;
      height: 1px; background: var(--ink); transition: right .35s ease;
    }
    .nav a:hover::after { right: 0; }
    .nav a.is-active::after { right: 0; background: var(--gold); }
    
    .hamburger {
      display: none; background: none; border: none; cursor: pointer;
      padding: 0; z-index: 60; position: relative;
    }
    .hamburger span {
      display: block; width: 22px; height: 1.5px; margin: 5px 0;
      background-color: var(--ink); transition: all 0.3s ease-in-out;
    }
    .hamburger.is-active span:nth-child(1) { transform: translateY(6.5px) rotate(45deg); }
    .hamburger.is-active span:nth-child(2) { opacity: 0; }
    .hamburger.is-active span:nth-child(3) { transform: translateY(-6.5px) rotate(-45deg); }

    /* INFINITE CANVAS */
    #viewport {
      position: absolute; top: 0; left: 0; width: 100vw; height: 100vh;
      overflow: hidden; cursor: grab; user-select: none; z-index: 10;
    }
    #viewport:active { cursor: grabbing; }
    
    #world {
      position: absolute; top: 50%; left: 50%; width: 0; height: 0;
      will-change: transform; pointer-events: none;
    }

    .tile {
      position: absolute;
    }

    .tile img {
      position: absolute; 
      object-fit: contain;
      border-radius: 6px; 
      pointer-events: auto; cursor: pointer;
      box-shadow: 0 15px 35px rgba(0,0,0,0.1);
      transition: transform 0.4s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.4s ease;
    }

    .tile img:hover {
      transform: translate(-50%, -50%) scale(1.05) translateZ(0) !important;
      box-shadow: 0 25px 50px rgba(0,0,0,0.2);
      z-index: 10;
    }

    @media (max-width: 900px) {
      .site-header {
        padding: 16px 20px 0; flex-direction: row; justify-content: space-between;
        align-items: center; gap: 16px;
      }
      .site-header.scrolled { padding-top: 16px; padding-bottom: 16px; }
      .hamburger { display: block; }
      .nav-wrap {
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        background: var(--bg); display: flex; flex-direction: column;
        justify-content: center; align-items: center; opacity: 0;
        pointer-events: none; transition: opacity 0.3s ease; z-index: 40;
      }
      .nav-wrap.is-open { opacity: 1; pointer-events: auto; }
      .nav { flex-direction: column; gap: 32px; align-items: center; }
      .nav a { font-size: 16px; }
    }
  </style>
</head>
<body>
  <header class="site-header scrolled" id="siteHeader">
    <button class="hamburger" id="hamburger" aria-label="Menü">
      <span></span><span></span><span></span>
    </button>
    <a href="index.html" class="logo">Makeup <em>by</em> Iremi</a>
    <nav class="nav-wrap" id="navWrap">
      <ul class="nav">
        <li><a href="index.html">Ana Sayfa</a></li>
        <li><a href="index.html#curtain">Hakkımızda</a></li>
        <li><a href="portfolio.html" class="is-active">Portfolyo</a></li>
        <li><a href="index.html#contact">İletişim</a></li>
      </ul>
    </nav>
  </header>

  <div id="viewport">
    <div id="world"></div>
  </div>

  <script>
    // Hamburger Menu
    const hamburgerBtn = document.getElementById('hamburger');
    const navWrapEl = document.getElementById('navWrap');
    hamburgerBtn.addEventListener('click', () => {
      hamburgerBtn.classList.toggle('is-active');
      navWrapEl.classList.toggle('is-open');
    });
    document.querySelectorAll('.nav a').forEach(link => {
      link.addEventListener('click', () => {
        hamburgerBtn.classList.remove('is-active');
        navWrapEl.classList.remove('is-open');
      });
    });

    const images = [
      "img/bridal-1.webp", "img/bridal-2.webp", "img/hair-1.webp", "img/hair-2.webp",
      "img/hero-1.webp", "img/hero-2.webp", "img/hero-3.webp", "img/hero-4.webp",
      "img/hero-5.webp", "img/iremi-portrait.webp", "img/set-1.webp", "img/set-2.webp",
      "img/temp-1.webp", "img/temp-2.webp"
    ];

    // Simple seeded random to keep layout consistent between resizes
    function mulberry32(a) {
      return function() {
        var t = a += 0x6D2B79F5;
        t = Math.imul(t ^ t >>> 15, t | 1);
        t ^= t + Math.imul(t ^ t >>> 7, t | 61);
        return ((t ^ t >>> 14) >>> 0) / 4294967296;
      }
    }

    const viewport = document.getElementById('viewport');
    const world = document.getElementById('world');
    
    let TILE_W, TILE_H;
    let panX = 0, panY = 0;
    let isDragging = false;
    let startX, startY;
    let isMobile = window.innerWidth < 900;

    function buildWorld() {
      world.innerHTML = '';
      const rand = mulberry32(42);
      
      // Shuffle images consistently
      let shuffled = [...images];
      for (let i = shuffled.length - 1; i > 0; i--) {
        const j = Math.floor(rand() * (i + 1));
        [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
      }

      let COLS, ROWS, CELL_W, CELL_H, IMG_H;
      
      if (window.innerWidth < 900) {
        // Mobile layout: Vertical structure
        // 2 columns, 7 rows. Good vertical scrollability.
        COLS = 2;
        ROWS = 7;
        CELL_W = window.innerWidth * 0.8; // 80vw per cell
        CELL_H = 350; // Tighter vertical gaps
        IMG_H = 250; 
      } else {
        // Desktop layout: 7 columns, 2 rows. Good horizontal flow.
        COLS = 7;
        ROWS = 2;
        CELL_W = 800;
        CELL_H = 750;
        IMG_H = 450;
      }

      TILE_W = COLS * CELL_W;
      TILE_H = ROWS * CELL_H;

      const placedImages = [];
      for (let i = 0; i < shuffled.length; i++) {
        const col = i % COLS;
        const row = Math.floor(i / COLS);
        
        const baseX = col * CELL_W + CELL_W / 2;
        const baseY = row * CELL_H + CELL_H / 2;
        
        // Dynamic jitter based on cell size so they don't overlap
        const jitterX = (rand() - 0.5) * (CELL_W * 0.4);
        const jitterY = (rand() - 0.5) * (CELL_H * 0.4);
        
        placedImages.push({
          src: shuffled[i],
          x: baseX + jitterX,
          y: baseY + jitterY
        });
      }

      for (let ty of [-TILE_H, 0, TILE_H]) {
        for (let tx of [-TILE_W, 0, TILE_W]) {
          const tile = document.createElement('div');
          tile.className = 'tile';
          tile.style.width = TILE_W + 'px';
          tile.style.height = TILE_H + 'px';
          tile.style.transform = `translate(${tx - TILE_W/2}px, ${ty - TILE_H/2}px)`;
          
          let imgsHtml = '';
          for (let img of placedImages) {
            imgsHtml += `<img src="${img.src}" style="height: ${IMG_H}px; transform: translate(-50%, -50%); left: ${img.x}px; top: ${img.y}px;" alt="Portfolio">`;
          }
          tile.innerHTML = imgsHtml;
          world.appendChild(tile);
        }
      }
      updateWorld();
    }

    function wrap(val, max) {
      let v = ((val % max) + max) % max;
      if (v > max / 2) v -= max;
      return v;
    }

    function updateWorld() {
      if (!TILE_W) return;
      const wx = wrap(panX, TILE_W);
      const wy = wrap(panY, TILE_H);
      world.style.transform = `translate(${wx}px, ${wy}px)`;
    }

    // Window Resize
    window.addEventListener('resize', () => {
      const newIsMobile = window.innerWidth < 900;
      if (newIsMobile !== isMobile) {
        isMobile = newIsMobile;
        buildWorld(); // rebuild if crossing breakpoint
      }
    });

    // Touch & Mouse Dragging
    viewport.addEventListener('pointerdown', (e) => {
      if (e.button !== 0 && e.pointerType === 'mouse') return;
      isDragging = true;
      startX = e.clientX - panX;
      startY = e.clientY - panY;
      viewport.setPointerCapture(e.pointerId);
    });

    viewport.addEventListener('pointermove', (e) => {
      if (!isDragging) return;
      panX = e.clientX - startX;
      panY = e.clientY - startY;
      updateWorld();
    });

    viewport.addEventListener('pointerup', (e) => {
      isDragging = false;
      viewport.releasePointerCapture(e.pointerId);
    });
    
    viewport.addEventListener('pointercancel', (e) => {
      isDragging = false;
    });

    // Wheel Panning
    viewport.addEventListener('wheel', (e) => {
      panX -= e.deltaX;
      panY -= e.deltaY;
      updateWorld();
    }, { passive: false });

    // Init
    buildWorld();
  </script>
</body>
</html>
"""

with open("portfolio.html", "w") as f:
    f.write(html)
