/*
 * A small 2D plasma for the hero: electrons and ions gyrate in a uniform
 * magnetic field (out of the screen), ride a travelling electrostatic wave,
 * and respond to a Debye-screened probe that follows the pointer.
 * Click flips the probe bias. Respects prefers-reduced-motion.
 */
(function () {
  var canvas = document.querySelector(".hero__canvas");
  if (!canvas || !canvas.getContext) return;
  var ctx = canvas.getContext("2d");
  var hero = canvas.parentElement;
  var pauseBtn = document.querySelector(".hero__pause");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)");

  var W = 0, H = 0, dpr = 1, parts = [], running = true, visible = true, t = 0;
  var probe = { x: -1e4, y: -1e4, active: false, sign: 1 }; // sign 1 = positive bias
  var BG = "rgba(15,27,46,";
  var COL = { e: "60,200,214", i: "240,176,79" };

  function species(kind) {
    // q/m ratio sets gyrofrequency; electrons are light and fast, ions slow and heavy.
    return kind === "e"
      ? { kind: "e", q: -1, wc: 0.11, vth: 1.5, r: 1.3 }
      : { kind: "i", q: 1, wc: 0.018, vth: 0.45, r: 1.9 };
  }

  function spawn(kind) {
    var s = species(kind);
    var a = Math.random() * Math.PI * 2, v = s.vth * (0.4 + Math.random());
    return { x: Math.random() * W, y: Math.random() * H, vx: Math.cos(a) * v, vy: Math.sin(a) * v,
             q: s.q, wc: s.wc, vth: s.vth, r: s.r, kind: s.kind };
  }

  function resize() {
    var rect = hero.getBoundingClientRect();
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    W = rect.width; H = rect.height;
    canvas.width = Math.round(W * dpr); canvas.height = Math.round(H * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    var n = Math.round(Math.min(1400, Math.max(350, (W * H) / 1100)));
    parts = [];
    for (var k = 0; k < n; k++) parts.push(spawn(k % 3 === 0 ? "i" : "e"));
    ctx.fillStyle = BG + "1)"; ctx.fillRect(0, 0, W, H);
  }

  function step() {
    t += 1;
    var kx = (2 * Math.PI) / Math.max(W, 1) * 3, om = 0.012;
    var lam = 70; // Debye length in px
    for (var k = 0; k < parts.length; k++) {
      var p = parts[k];
      // Travelling wave E_x = E0 sin(kx - wt), plus a weak drift field E_y
      var ex = 0.035 * Math.sin(kx * p.x - om * t);
      var ey = 0.006;
      if (probe.active) {
        var dx = p.x - probe.x, dy = p.y - probe.y;
        var r2 = dx * dx + dy * dy + 60, r = Math.sqrt(r2);
        if (r < 260) {
          var f = probe.sign * 38 * Math.exp(-r / lam) * (1 / r + 1 / lam) / r;
          ex += f * dx / r; ey += f * dy / r;
        }
      }
      // Half acceleration, magnetic rotation, half acceleration (Boris style)
      var qm = p.q * (p.kind === "e" ? 1 : 0.25);
      p.vx += qm * ex * 0.5; p.vy += qm * ey * 0.5;
      var th = p.q * p.wc, c = Math.cos(th), s = Math.sin(th);
      var vx = p.vx * c - p.vy * s, vy = p.vx * s + p.vy * c;
      p.vx = vx + qm * ex * 0.5; p.vy = vy + qm * ey * 0.5;
      // Gentle collisions keep the temperature bounded
      var sp = Math.sqrt(p.vx * p.vx + p.vy * p.vy), cap = p.vth * 3.2;
      if (sp > cap) { p.vx *= cap / sp; p.vy *= cap / sp; }
      p.x += p.vx; p.y += p.vy;
      if (p.x < 0) p.x += W; else if (p.x >= W) p.x -= W;
      if (p.y < 0) p.y += H; else if (p.y >= H) p.y -= H;
    }
  }

  function draw() {
    ctx.fillStyle = BG + "0.16)";
    ctx.fillRect(0, 0, W, H);
    for (var pass = 0; pass < 2; pass++) {
      var kind = pass === 0 ? "i" : "e";
      ctx.fillStyle = "rgba(" + COL[kind] + "," + (kind === "e" ? 0.85 : 0.9) + ")";
      ctx.beginPath();
      for (var k = 0; k < parts.length; k++) {
        var p = parts[k];
        if (p.kind !== kind) continue;
        ctx.moveTo(p.x + p.r, p.y);
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      }
      ctx.fill();
    }
    if (probe.active) {
      var col = probe.sign > 0 ? "240,176,79" : "60,200,214";
      ctx.strokeStyle = "rgba(" + col + ",0.55)"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.arc(probe.x, probe.y, 70, 0, Math.PI * 2); ctx.stroke();
      ctx.fillStyle = "rgba(232,238,246,0.95)";
      ctx.beginPath(); ctx.arc(probe.x, probe.y, 4, 0, Math.PI * 2); ctx.fill();
      ctx.font = "600 13px 'IBM Plex Sans', system-ui, sans-serif";
      ctx.fillText(probe.sign > 0 ? "+" : "−", probe.x + 9, probe.y - 8);
    }
  }

  function loop() {
    if (running && visible) { step(); draw(); }
    requestAnimationFrame(loop);
  }

  function setRunning(on) {
    running = on;
    if (pauseBtn) { pauseBtn.textContent = on ? "Pause" : "Play"; pauseBtn.setAttribute("aria-pressed", on ? "false" : "true"); }
  }

  function pos(e) {
    var r = canvas.getBoundingClientRect();
    probe.x = e.clientX - r.left; probe.y = e.clientY - r.top;
  }
  hero.addEventListener("pointermove", function (e) { pos(e); probe.active = true; });
  hero.addEventListener("pointerleave", function () { probe.active = false; });
  canvas.addEventListener("pointerdown", function (e) { pos(e); probe.active = true; probe.sign *= -1; });

  if (pauseBtn) pauseBtn.addEventListener("click", function () { setRunning(!running); });

  if ("IntersectionObserver" in window) {
    new IntersectionObserver(function (en) { visible = en[0].isIntersecting; }).observe(hero);
  }
  var rt;
  window.addEventListener("resize", function () { clearTimeout(rt); rt = setTimeout(resize, 150); });

  resize();
  if (reduce.matches) {
    // Settle a static frame and leave the choice to play with the visitor.
    for (var i = 0; i < 120; i++) { step(); draw(); }
    setRunning(false);
  }
  requestAnimationFrame(loop);
})();
