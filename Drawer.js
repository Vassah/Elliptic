d3.select('body')
  .append('svg');

var svg = d3.select("svg");
 
var axisx = svg.append("line")
.attr({
  x1 : 0,
  y1 : 450,
  x2 : 600,
  y2 : 450,
  stroke : 'grey'
}
     );
 
var axisy = svg.append("line")
.attr({
  x1 : 75,
  y1 : 0,
  x2 : 75,
  y2 : 600,
  stroke : 'grey'
}
      );
 
var data = [
  [0,0,1],
  [0,5,1],
  [1,1,1],
  [1,4,1],
  [4,3,1],
  [4,2,1],
  [0,0,0]
  ];
 
var group = svg.selectAll("g")
.data(data)
.enter()
.append('g');
 
group.attr('transform' , function(d, i) {
  var x = 75*d[0] + 75;
  var y = 75*d[1] + 75;
  var z = d[2];
  if (z === 0){
      return 'translate('+[75,265]+')';
  }
  else {
    return 'translate('+[x,y]+')';
  }
}
            );
 
var circles = group.append("circle")
   .attr({
     cx : 0,
     cy : 0,
     r : 5,
     fill : function(d) {
       if (d[2]===0) {
         return 'black'
       }
       else {
         return 'coral'
       }
     },
     stroke : 'black',
     'stroke-width' : 1
   }
         )
 
 
var label_data = ['0', '1', '2', '3', '4']
