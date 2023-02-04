function respondToTrain(train){
    document.getElementById('sendMailContainer').classList.remove('hidden')

  const sendToInput = document.getElementById('sendToInput')
  const trainDTInput =  document.getElementById('mailPracticeInput')
  const trainUploadDT = document.getElementById('trainUploadDTInput')

  sendToInput.setAttribute('readonly', 'readonly')

  const sendToValue = train.querySelector('.traineeName').innerText
  const trainDTValue = train.querySelector('.DT').innerHTML
  const trainUploadDTValue = train.querySelector('.UploadDT').value

  sendToInput.value = sendToValue
  trainDTInput.value = trainDTValue
  trainUploadDT.value = trainUploadDTValue
}

function dateFilterClick(){
  const checkbox = document.getElementById('isDateFilter')
  const checkboxLabel = checkbox.parentElement
  const fromDate = document.getElementById('fromDate')
  const toDate = document.getElementById('toDate')
  const btn = document.getElementById('dateFilterSubmitBtn')
  if (checkbox.checked){
    checkboxLabel.classList.add('checked')
    fromDate.removeAttribute('disabled')
    toDate.removeAttribute('disabled')
    btn.removeAttribute('disabled')
  } else{
    checkboxLabel.classList.remove('checked')
    fromDate.setAttribute('disabled', '')
    toDate.setAttribute('disabled', '')
    btn.setAttribute('disabled', '')
  }
}

function addUser(){
  const container = document.getElementById('users');
  const rowNum = container.childElementCount;

  const row = document.createElement('tr')
  row.id = `user${rowNum}`
  row.setAttribute('class', `user`)
  row.innerHTML = `<td class="rowNumber">${parseInt(rowNum) + 1}.</td>
                <td class="userID"><input min="99999999" max="999999999" placeholder="תז" name="userID${rowNum}" type="number" required></td>
              <td class="isAdmin"><label>
                  <input type="checkbox" name="isAdmin${rowNum}" value="True">
                  מנהל
              </label> </td>
            <td class="deleteUser" onclick="deleteUser(this.parentElement)">X</td>`
  container.appendChild(row);
}

function deleteUser(row){
  const container  = document.getElementById('users');
  const deleteID = row.id[row.id.length-1]
  container.removeChild(row);
  let tempRow
  for (let i = deleteID; i<container.children.length; i++){
    tempRow = container.children[i];
    tempRow.id = `user${i}`
    tempRow.children[0].innerHTML = (parseInt(i) + 1) + '.'
    tempRow.querySelector('[type=number]').name = `userID${i}`
    tempRow.querySelector('[type=checkbox]').name = `isAdmin${i}`
    }
}