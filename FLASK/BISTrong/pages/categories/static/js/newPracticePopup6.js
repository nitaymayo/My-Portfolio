function addPowerDrill(){

  const dNum = document.getElementById('powerDrills').childElementCount

  const row = document.createElement('div')
  row.classList.add('powerRow')
  row.id = 'powerDrill' + dNum.toString()
  row.innerHTML = `
            <input list='drillsOptions' type="text" onchange="check_datalist(this)" class="drillNameInput" id="nameDrill${dNum}" name="nameDrill${dNum}" placeholder="תרגיל" required>
            <input type="number"  min="1" class="drillSetsInput" id="setsDrill${dNum}" name="setsDrill${dNum}" placeholder="סטים" required>
            <input type="number" min="1" class="drillRepsInput" id="repsDrill${dNum}" name="repsDrill${dNum}" placeholder="חזרות" required>
            <input type="number" min="0" class="drillRestInput" id="restDrill${dNum}" name="restDrill${dNum}" placeholder="מנוחה" required>
            <div class="deleteRow" onclick="deleteRow(this.parentElement)">X</div>
`

  document.getElementById('powerDrills').appendChild(row)
}

function deleteRow(row){
  const container  = document.getElementById('powerDrills');
  const deleteID = row.id[row.id.length-1]
  container.removeChild(row);

  for (let i = deleteID; i<container.children.length; i++){

    const tempRow = container.children[i];
    tempRow.id = 'powerDrill' + i
    tempRow.children[0].id = `nameDrill${i}`
    tempRow.children[1].id = `setsDrill${i}`
    tempRow.children[2].id = `repsDrill${i}`
    tempRow.children[3].id = `restDrill${i}`

    tempRow.children[0].name = `nameDrill${i}`
    tempRow.children[1].name = `setsDrill${i}`
    tempRow.children[2].name = `repsDrill${i}`
    tempRow.children[3].name = `restDrill${i}`
    }
}

function onNewPracticeSubmit(){
  const drillsList = document.querySelectorAll('#drillsOptions>option')
  let res = true
  const drillsInPractice = document.querySelectorAll('#powerDrills>.powerRow')

  let validName = false
  for (let i = 0; i<drillsInPractice.length; i++){
    validName = false
    for(let j = 0; j<drillsList.length; j++){
      if (drillsInPractice[i].children[0].value === drillsList[j].innerText){
        validName = true
      }
    }
    if (!validName){
      res = false
      drillsInPractice[i].children[0].style.borderColor = 'red';
    } else {
      drillsInPractice[i].children[0].style.borderColor = 'initial';
    }
  }

  return res;
}

function clickMuscleGroup(label){
  label.classList.toggle('checked')
  const div = document.querySelectorAll('#muscleGroups .checked')
  const checkNum = div.length
  if (checkNum > 9) {
    label.classList.toggle('checked')
    label.querySelector('input').checked = false
    alert('ניתן לסמן עד 9 קבוצות שרירים')
  }

}




// Simulate clicking on the specified element.


/**
 * Trigger the specified event on the specified element.
 * @param  {Object} elem  the target element.
 * @param  {String} event the type of the event (e.g. 'click').
 */
function triggerEvent( elem, event ) {
  var clickEvent = new Event( event ); // Create the event.
  elem.dispatchEvent( clickEvent );    // Dispatch the event.
}
/*
function switchNewPracticeToRun(){
  document.getElementById('practiceContentData').remove()
}

function switchNewPracticeToPower(){
  const powerContent = document.createElement('div')
  powerContent.id = 'practiceContentData'
  powerContent.innerHTML = `
          <h2>רשימת תרגילים</h2>
          <div id="powerDrills">
              <div class="powerRow" id="powerDrill0">
                <input list="drillsOptions" type="text" class="drillNameInput" id="nameDrill0" placeholder="תרגיל" required>
                <input type="number" min="1" class="drillSetsInput" id="setsDrill0" name="setsDrill0" placeholder="סטים" required>
                <input type="number"  min="1" class="drillRepsInput" id="repsDrill0" name="repsDrill0" placeholder="חזרות" required>
                <input type="number"  min="0" class="drillRestInput" id="restDrill0" name="restDrill0" placeholder="מנוחה" required>
              </div>

              <div class="powerRow" id="powerDrill1">
                <input list="drillsOptions" type="text" class="drillNameInput" id="nameDrill1" name="nameDrill1" placeholder="תרגיל" required>
                <input type="number"  min="1" class="drillSetsInput" id="setsDrill1" name="setsDrill1" placeholder="סטים" required>
                <input type="number"  min="1" class="drillRepsInput" id="repsDrill1" name="repsDrill1" placeholder="חזרות" required>
                <input type="number"  min="0" class="drillRestInput" id="restDrill1" name="restDrill1" placeholder="מנוחה" required>
                <div class="deleteRow" onclick="deleteRow(this.parentElement)">X</div>
              </div>
          </div>
          <div id="moreDrillBtn" onclick="addPowerDrill()">תרגיל נוסף</div>
        `

  document.getElementById('newPracticeForm').appendChild(powerContent)
}
*/
