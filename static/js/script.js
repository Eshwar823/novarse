// Simple counter animation for statistics on the home page.
document.addEventListener('DOMContentLoaded', function() {
  const counters = document.querySelectorAll('.counter');
  const speed = 200; // lower is faster

  const animateCounter = (counter) => {
    const target = parseFloat(counter.getAttribute('data-target'));
    let current = 0;
    const step = () => {
      // Calculate increment. If target has a decimal part, maintain one decimal place.
      const increment = target / speed;
      current += increment;
      if (current < target) {
        counter.textContent = target % 1 !== 0 ? current.toFixed(2) : Math.ceil(current);
        requestAnimationFrame(step);
      } else {
        counter.textContent = target;
      }
    };
    step();
  };

  // Use IntersectionObserver to start animation when counters are visible
  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        obs.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  counters.forEach(counter => {
    observer.observe(counter);
  });
});