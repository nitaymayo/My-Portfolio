 google.charts.load("current", {packages:['corechart']});
    google.charts.setOnLoadCallback(drawChart);
    function drawChart() {

      let x = [["שבוע", "כמות אימונים", { role: "style" } ]]

      const content = JSON.parse(document.getElementById('grafDATA').innerHTML)
      for (let i in content){
        x.push([i, content[i], "blue"])
      }

      var data = google.visualization.arrayToDataTable(x);

      var view = new google.visualization.DataView(data);
      view.setColumns([0, 1,
                       { calc: "stringify",
                         sourceColumn: 1,
                         type: "string",
                         role: "annotation" },
                       2]);

      var options = {
        backgroundColor: 'none',
        width: 700,
        height: 210,
        chartArea:{
          left:30,
          top: 10,
          bottom:30,
          right:0
        },
        boxstyle:{boxShadow: 'none'},
        bar: {groupWidth: "60%"},
        legend: { position: "none" },
      };
      var chart = new google.visualization.ColumnChart(document.getElementById("chart_div"));
      chart.draw(view, options);
  }


  function openPersonalPopup(){
      if(document.getElementById('editPersonalDataPopup').classList.contains('hidden')){
        document.body.style.top = `-${window.scrollY}px`;
    document.body.style.position = 'fixed';
    document.body.style.width = '100%';
    document.getElementById('editPersonalData').style.zIndex = '100000';
      } else{
        const scrollY = document.body.style.top;
    document.body.style.position = '';
    document.body.style.top = '';
    window.scrollTo(0, parseInt(scrollY || '0') * -1);
    document.getElementById('editPersonalData').style.zIndex = '0';
      }
    document.getElementById('editPersonalDataPopup').classList.toggle('hidden')
    document.getElementById('popupBgPersonalDataForm').classList.toggle('hidden')
  }