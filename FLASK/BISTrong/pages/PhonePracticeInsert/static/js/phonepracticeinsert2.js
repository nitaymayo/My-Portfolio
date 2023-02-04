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
            <input placeholder="קבוצת שרירים" list="muscleGroupsList" name="nameMuscleGroup${rowNum}" required>
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
  const head = document.getElementById('changingInputHead')
  head.innerHTML =  `מרחק`
  input.setAttribute('placeholder', 'אורך(בקמ)')
  input.setAttribute('type', 'number')
  input.setAttribute('name', 'distance')


  document.getElementById('powerLabel').classList.remove('powerLabel')
  document.getElementById('runLabel').classList.add('runLabel')

}

function changeToPower(){
  const input = document.getElementById('changingInput')
  const head = document.getElementById('changingInputHead')
  head.innerHTML =  `מקום`
  input.setAttribute('placeholder', 'מיקום')
  input.setAttribute('type', 'text')
  input.setAttribute('name', 'place')

  document.getElementById('powerLabel').classList.add('powerLabel')
  document.getElementById('runLabel').classList.remove('runLabel')



}

function clickMuscleGroup(label){
  label.classList.toggle('checked')
  const div = document.querySelectorAll('#muscleGroups .checked')
  const checkNum = div.length
  if (checkNum > 9) {
    label.classList.toggle('checked')
    alert('ניתן לסמן עד 9 קבוצות שרירים')
  }

}
