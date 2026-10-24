
// Dynamic Canvas Interactive Matrix Particles
const container = document.getElementById('particles-container');
const particleCount = 45;

for (let i = 0; i < particleCount; i++) {
    const particle = document.createElement('div');
    particle.style.position = 'absolute';
    particle.style.width = Math.random() * 4 + 2 + 'px';
    particle.style.height = particle.style.width;
    particle.style.background = Math.random() > 0.5 ? '#00f0ff' : '#bd00ff';
    particle.style.borderRadius = '50%';
    particle.style.opacity = Math.random() * 0.4 + 0.1;
    
    // Distribute randomly across screen viewport width/height
    particle.style.top = Math.random() * 100 + 'vh';
    particle.style.left = Math.random() * 100 + 'vw';
    
    // Add smooth drift animation keyframe mappings directly
    particle.animate([
        { transform: 'translate(0, 0)' },
        { transform: `translate(${Math.random() * 100 - 50}px, ${Math.random() * 100 - 50}px)` }
    ], {
        duration: Math.random() * 6000 + 4000,
        iterations: Infinity,
        direction: 'alternate',
        easing: 'ease-in-out'
    });
    
    container.appendChild(particle);
}
