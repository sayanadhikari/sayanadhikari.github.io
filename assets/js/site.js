(function () {
  var root = document.documentElement;
  var mq = window.matchMedia("(prefers-color-scheme: dark)");

  function stored() { try { return localStorage.getItem("theme"); } catch (e) { return null; } }
  function resolved() {
    var t = root.getAttribute("data-theme");
    if (t === "light" || t === "dark") return t;
    return mq.matches ? "dark" : "light";
  }
  function sync() { root.setAttribute("data-mode", resolved()); }
  sync();
  if (mq.addEventListener) mq.addEventListener("change", sync);

  var tt = document.querySelector(".theme-toggle");
  if (tt) tt.addEventListener("click", function () {
    var next = resolved() === "dark" ? "light" : "dark";
    root.setAttribute("data-theme", next);
    try { localStorage.setItem("theme", next); } catch (e) {}
    sync();
  });

  // Mobile menu
  var nt = document.querySelector(".nav__toggle");
  var nl = document.getElementById("nav-list");
  if (nt && nl) {
    nt.addEventListener("click", function () {
      var open = nl.classList.toggle("is-open");
      nt.setAttribute("aria-expanded", open ? "true" : "false");
      nt.textContent = open ? "Close" : "Menu";
    });
    nl.addEventListener("click", function (e) {
      if (e.target.tagName === "A") { nl.classList.remove("is-open"); nt.setAttribute("aria-expanded", "false"); nt.textContent = "Menu"; }
    });
  }

  // Top bar turns solid once the hero is scrolled past
  var bar = document.querySelector(".topbar--over");
  var hero = document.querySelector(".hero");
  if (bar && hero) {
    var onScroll = function () { bar.classList.toggle("is-scrolled", window.scrollY > hero.offsetHeight - 80); };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  // Publication search and topic filter
  var list = document.getElementById("publist");
  if (list) {
    var items = Array.prototype.slice.call(list.querySelectorAll(".pub"));
    var input = document.getElementById("pub-search");
    var chips = Array.prototype.slice.call(document.querySelectorAll(".chip"));
    var count = document.getElementById("pub-count");
    var empty = document.getElementById("pub-empty");
    var topic = "all";
    var params = new URLSearchParams(window.location.search);
    if (params.get("topic")) topic = params.get("topic");
    if (params.get("q") && input) input.value = params.get("q");

    items.forEach(function (li) { li._text = li.textContent.toLowerCase(); });

    function apply() {
      var q = input ? input.value.trim().toLowerCase() : "";
      var shown = 0;
      items.forEach(function (li) {
        var ok = (topic === "all" || li.getAttribute("data-topic") === topic) && (!q || li._text.indexOf(q) !== -1);
        li.classList.toggle("is-hidden", !ok);
        if (ok) shown++;
      });
      chips.forEach(function (c) { c.setAttribute("aria-pressed", c.getAttribute("data-topic") === topic ? "true" : "false"); });
      if (count) count.textContent = "Showing " + shown + " of " + items.length;
      if (empty) empty.hidden = shown !== 0;
      var u = new URL(window.location.href);
      if (topic === "all") u.searchParams.delete("topic"); else u.searchParams.set("topic", topic);
      if (q) u.searchParams.set("q", q); else u.searchParams.delete("q");
      history.replaceState(null, "", u);
    }
    chips.forEach(function (c) { c.addEventListener("click", function () { topic = c.getAttribute("data-topic"); apply(); }); });
    if (input) input.addEventListener("input", apply);
    apply();
  }
})();
