document.addEventListener('DOMContentLoaded', function() {
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    const hoverArea = document.getElementById('hover-area');
    const areaRect = hoverArea.getBoundingClientRect();
    let isHovering = false;
    let hoverStartTime;
    let totalHoverTime = 0;
    let hoverData = [];
    let path = [];
  
    canvas.width = 500;
    canvas.height = 300;
  
    document.addEventListener('mousemove', function(event) {
      const x = event.clientX;
      const y = event.clientY;
      path.push({x, y});
      drawPath(ctx, path);
      const inside = x >= areaRect.left && x <= areaRect.right && y >= areaRect.top && y <= areaRect.bottom;
      
      if (inside && !isHovering) {
        hoverStartTime = Date.now(); // Start hover timer
        isHovering = true;
      } else if (!inside && isHovering) {
        totalHoverTime += Date.now() - hoverStartTime; // Update hover total time
        isHovering = false;
      }
      

        
    });
  
    // Periodically save hover data
    setInterval(function() {
      if (isHovering) {
        totalHoverTime += Date.now() - hoverStartTime; // Update if currently hovering
        hoverStartTime = Date.now();
      }
  
      hoverData.push({
        element: 'hover-area',
        duration: totalHoverTime,
        parcour : path
      });
  
      console.log(JSON.stringify(hoverData)); // Log or save hover data
      totalHoverTime = 0; // Reset hover time after saving
    }, 5000);
  
    function drawPath(ctx, path) {
        ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear previous path
        ctx.beginPath();
        ctx.moveTo(path[0].x, path[0].y);
        for (let point of path) {
          ctx.lineTo(point.x, point.y);
        }
        ctx.stroke();
      }
  });
  