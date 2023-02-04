function loadDrills(){
  
  document.getElementById('practicePopup').style.display='block';
  const details = document.querySelectorAll('.drill>.data');
  const container = document.getElementById('drillsPopupList');

  container.innerHTML = `<tr>
           <th></th>
          <th>שם התרגיל</th>
          <th>סטים/דקות</th>
          <th>מס חזרות</th>
          <th>מנוחה</th>
        </tr>`
  let count = 1
  for (let i = 0; i < details.length/5 ; i++){
    const tr = document.createElement('tr');
    tr.classList.add('drillItem');

    const num = document.createElement('td');
    num.innerHTML = `${count++}.`;


    const name = document.createElement('td');
    name.innerHTML = details[i*5].innerHTML;

    const sets = document.createElement('td');
    sets.innerHTML = details[i*5 + 2].innerHTML;

    const repeats = document.createElement('td');
    repeats.innerHTML = details[i*5 + 3].innerHTML;

    const rest = document.createElement('td');
    rest.innerHTML = details[i*5 + 4].innerHTML;

    tr.appendChild(num);
    tr.appendChild(name);
    tr.appendChild(sets);
    tr.appendChild(repeats);
    tr.appendChild(rest);
    container.appendChild(tr);
  }
}




function deleteWorkout(workout){
  if (confirm(`האם אתה רוצה למחוק את האימון: ${workout}?` )){
    location.href = `/deleteWorkout?workout=${workout}`
  }
}


function insertThisPractice(){
  document.getElementById('insertPracticeContainer').classList.remove('hidden')

  const length = document.getElementById('workoutLength').innerText
  const type = document.getElementById('workoutType').innerText
  const muscleGroups = document.querySelectorAll('#muscleGroupsDataDiv .muscleGroup')

  if (type == 'ריצה'){
    document.getElementById('runTypeInput').click()
  } else {
    document.getElementById('powerTypeInput').click()
  }
  document.getElementById('lengthInput').value = parseInt(length)

  for (let muscleGroup of document.getElementById('muscleGroups').children){
    deleteRow(muscleGroup)
  }

  let counter = 0
  for (let muscle of muscleGroups){
    addMuscleGroup()
    document.querySelector(`#muscleGroupDiv${counter} > input`).value = muscle.innerHTML
    counter++
  }
}

function sendPracticeMail(email, content){
  if (!email){
    email = prompt('בבקשה הכנס כתובת אימייל:')
    if (ValidateEmail(email)) {
      location.href = `/sendPracticeMail?email=${email}&content=${content}`
    }
  } else {
    location.href = `/sendPracticeMail?content=${content}`

  }
}

function ValidateEmail(mail){
 if (/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(mail))
  {
    return (true)
  }
    alert("כתובת מייל שגויה")
    return (false)
}