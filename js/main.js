$(function() {
  // minimal heatmap instance configuration
  var MAX_VALUE = 100;
  var heatmapInstance = h337.create({
    // only container is required, the rest will be defaults
    container: document.querySelector('#heatmap')
  });
  // putHeatmap(heatmapInstance);
  setInterval(update, 1000);
  update();

  function update() {    
    // GET request
    $.getJSON('http://localhost:5000/noise?sort=-_created&max_results=600', 
      function(json){  
        console.log(json._items);
        var data = { 
          max: MAX_VALUE, 
          data: json._items 
        };
        heatmapInstance.setData(data);
      })
    .fail(function(jqxhr, textStatus, error) {
      var err = textStatus + ", " + error;
      console.log( "Request Failed: " + err );
    });

    // putHeatmap(heatmapInstance);
    updateNotifications();
    // drawRoom();
    // console.log("Update");
  }

  function putHeatmap(heatmapInstance) {
    // now generate some random data
    var points = [];
    var max = 100;
    var width = 900;
    var height = 500;
    var len = 500;

    while (len--) {
      var val = Math.floor(Math.random()*100);
      max = Math.max(max, val);
      var point = {
        x: Math.floor(Math.random()*width),
        y: Math.floor(Math.random()*height),
        value: 100
      };
      points.push(point);
    }
    // heatmap data format
    var data = { 
      max: max, 
      data: points 
    };
    // if you have a set of datapoints always use setData instead of addData
    // for data initialization
    heatmapInstance.setData(data);
  }

  function drawRoom() {
    var canvas = $("#heatmap canvas")[0];
    var ctx = canvas.getContext("2d");
    ctx.fillStyle = 'rgba(66,74,93,0.5)';
    ctx.fillRect(0,0,150,75);
  }

  function updateNotifications(name) {
    var time = new Date();
    time = time.toLocaleTimeString();
    var name = "Guilhelm";
    var html = `<div class="desc">
    <div class="thumb">
    <span class="badge bg-theme"><i class="fa fa-clock-o"></i></span>
    </div>
    <div class="details">
    <p><muted>` + time + `</muted><br/>
    <a href="#">` + name + `</a> please shut the f**k up!<br/>
    </p>
    </div>
    </div>`;

    $("#notifications-list").prepend(html);
  };
});