const intensity = document.querySelectorAll('#intensity>option')

function onNewCategorySubmit(){
  catIntens = document.getElementById('CategoryLevelInput').value
  let res = false
  for (let i = 0; i<intensity.length; i++){
    if (intensity[i].innerHTML == catIntens){
      res = true
    }
  }
  if (res === false){
    document.getElementById('CategoryLevelInput').style.borderColor = 'red'
  }
  return res
}


