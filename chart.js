// Draw sample counts with D3 and show details on hover or keyboard focus.
const data = [{band:'Minimal',count:1744},{band:'Moderate',count:3155},{band:'High',count:1716},{band:'Very High',count:1385}];
const svg = d3.select('#chart').append('svg').attr('viewBox','0 0 700 320');
const margin = {top:20,right:20,bottom:55,left:60}, width=700-margin.left-margin.right, height=320-margin.top-margin.bottom;
const g=svg.append('g').attr('transform',`translate(${margin.left},${margin.top})`);
const x=d3.scaleBand().domain(data.map(d=>d.band)).range([0,width]).padding(.25);
const y=d3.scaleLinear().domain([0,3500]).range([height,0]);
g.append('g').attr('class','axis').attr('transform',`translate(0,${height})`).call(d3.axisBottom(x).tickSize(0)).call(g=>g.select('.domain').remove());
g.append('g').attr('class','axis').call(d3.axisLeft(y).ticks(4).tickFormat(d3.format(','))).call(g=>g.select('.domain').remove());
g.selectAll('rect').data(data).join('rect').attr('class','bar').attr('x',d=>x(d.band)).attr('y',d=>y(d.count)).attr('width',x.bandwidth()).attr('height',d=>height-y(d.count)).attr('tabindex',0).attr('aria-label',d=>`${d.band}: ${d3.format(',')(d.count)} records`).on('mouseover focus',(_,d)=>d3.select('#chart-detail').text(`${d.band}: ${d3.format(',')(d.count)} records`)).on('mouseout blur',()=>d3.select('#chart-detail').text('Select or hover over a bar to see its count.'));
