function clickOnCategory(category){
  let secID = category.id + 'Sec'

  if (category.checked) {
    document.getElementById(secID).classList.remove('hidden')
    category.parentElement.classList.add('checked')
  }
  else {
    document.getElementById(secID).classList.add('hidden')
    category.parentElement.classList.remove('checked')
  }
}
const msgDiv = document.getElementById('msgAlert')
if (msgDiv){
  alert(msgDiv.innerHTML)
}

const drillsList = document.getElementById("shortVersionDrillsList")

function clickOnPractice(practice){


  let exsist = false
  let whatsStr = ""


  for (let i = 0; i<drillsList.childElementCount; i++){
    if (drillsList.children[i].id == practice.children[0].innerHTML){
      exsist = true
    }
  }

  if (exsist){
    practice.children[3].classList.remove('checked')
    practice.children[3].querySelector('span').innerHTML = "הוסף לאימון"
    document.getElementById(practice.children[0].innerHTML).remove();
    const drillsTemp = document.createElement('div');
    drillsTemp.innerHTML = drillsList.innerHTML
    drillsList.innerHTML = '';
    for (let i = 0; i<drillsTemp.children.length; i++){
    const newDrill = document.createElement('span')
    newDrill.classList.add('drillInList')
    newDrill.id = drillsTemp.children[i].id
    newDrill.innerHTML = (i + 1) + '.' + drillsTemp.children[i].id
    drillsList.appendChild(newDrill)
      whatsStr = whatsStr + newDrill.innerHTML + "%0a"
    }
    sendToStr = `${whatsappStr} + ${whatsStr}`
  } else {
    practice.children[3].classList.add('checked')
    practice.children[3].querySelector('span').innerHTML = "הסר מהאימון"
    const newDrill = document.createElement('span')
    newDrill.classList.add('drillInList')
    newDrill.id = practice.children[0].innerHTML
    newDrill.innerHTML = (drillsList.childElementCount + 1) + '.' + practice.children[0].innerHTML
    drillsList.appendChild(newDrill)
    whatsStr = newDrill.innerHTML + "%0a"
    sendToStr = sendToStr + whatsStr

  }

  if (drillsList.children.length === 0){
    document.getElementById('shortVersionDiv').classList.add('hidden');
  } else {
    document.getElementById('shortVersionDiv').classList.remove('hidden');
  }

}
const whatsappBtn = document.getElementById('whatsappBtn')
let sendToStr = ''
const whatsappStr = "whatsapp://send?text=*האימון שלך:*" + "%0a"

function deleteDrill(drill){
  if (confirm(`האם אתה רוצה למחוק את תרגיל: ${drill.children[0].innerText}?` )){
    location.href = `/deleteDrill?drill=${drill.children[0].innerText}`
  }
}

function sendToWhatsapp(){
  let finalStr = `${whatsappStr + sendToStr}`
  sendToStr = ""
  location.href = finalStr
}
