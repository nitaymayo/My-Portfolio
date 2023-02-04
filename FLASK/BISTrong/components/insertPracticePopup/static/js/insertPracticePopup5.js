function addMuscleGroup(){

  const container = document.getElementById('muscleGroups');
  if (container.childElementCount === 9){
    return
  }
  const rowNum = container.childElementCount;

  const row = document.createElement('div')
  row.id = `muscleGroupDiv${rowNum}`
  row.setAttribute('class', `muscleGroupRow`)
  row.innerHTML = `<span class="rowNumber">${parseInt(rowNum) + 1}.</span>
            <input placeholder="קבוצת שרירים" onchange="check_datalist(this)" list="muscleGroupsList" name="nameMuscleGroup${rowNum}" required>
            <span class="close" onclick="deleteRow(this.parentElement)">X</span>`
  container.appendChild(row);
}


function deleteRow(row){
  const container  = document.getElementById('muscleGroups');
  const deleteID = row.id[row.id.length-1]
  container.removeChild(row);
  let tempRow
  for (let i = deleteID; i<container.children.length; i++){
    tempRow = container.children[i];
    tempRow.id = `muscleGroupDiv${i}`
    tempRow.children[0].innerHTML = (parseInt(i) + 1) + '.'
    tempRow.children[1].name = `nameMuscleGroup${i}`
    }
}

function changeToRun(){
  const input = document.getElementById('changingInput')
  input.children[0].innerHTML =  `מרחק(קמ):`
  input.children[1].setAttribute('placeholder', 'מרחק')
  input.children[1].setAttribute('type', 'number')
  input.children[1].setAttribute('name', 'distance')
}

function changeToPower(){
  const input = document.getElementById('changingInput')
  input.children[0].innerHTML =  `מקום:`
  input.children[1].setAttribute('placeholder', 'מקום האימון')
  input.children[1].setAttribute('type', 'text')
  input.children[1].setAttribute('name', 'place')
}
