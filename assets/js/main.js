(function () {
  var root = document.documentElement;
  var toggle = document.querySelector('.theme-toggle');
  var menuToggle = document.querySelector('.menu-toggle');
  var menu = document.querySelector('.site-nav');
  var meta = document.querySelector('meta[name="theme-color"]');
  var desktopMenuQuery = window.matchMedia('(min-width: 841px)');

  function applyTheme(theme) {
    root.dataset.theme = theme;
    if (meta) {
      meta.setAttribute('content', theme === 'dark' ? '#111411' : '#f3f0e8');
    }
    if (toggle) {
      toggle.setAttribute(
        'aria-label',
        theme === 'dark' ? 'Switch to light theme' : 'Switch to dark theme'
      );
    }
  }

  applyTheme(root.dataset.theme || 'light');

  if (toggle) {
    toggle.addEventListener('click', function () {
      var next = root.dataset.theme === 'dark' ? 'light' : 'dark';
      localStorage.setItem('theme', next);
      applyTheme(next);
    });
  }

  if (menuToggle && menu) {
    function closeMenu() {
      menu.dataset.open = 'false';
      menuToggle.setAttribute('aria-expanded', 'false');
    }

    function syncMenuMode(event) {
      if (event.matches) {
        closeMenu();
      }
    }

    closeMenu();
    if (desktopMenuQuery.addEventListener) {
      desktopMenuQuery.addEventListener('change', syncMenuMode);
    } else {
      desktopMenuQuery.addListener(syncMenuMode);
    }

    menuToggle.addEventListener('click', function () {
      var isOpen = menu.dataset.open === 'true';
      menu.dataset.open = String(!isOpen);
      menuToggle.setAttribute('aria-expanded', String(!isOpen));
    });

    menu.addEventListener('click', function (event) {
      if (event.target.closest('a')) {
        closeMenu();
      }
    });

    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape') {
        closeMenu();
        if (!desktopMenuQuery.matches) {
          menuToggle.focus();
        }
      }
    });
  }
})();
