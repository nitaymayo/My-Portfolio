
function openMail(mail){

  let allMail = document.querySelectorAll('.messageBox')
  for (let i = 0; i<allMail.length; i++){
    allMail[i].classList.remove('selected')
  }

  mail.classList.add('opened')
  mail.classList.add('selected')




  let headline = mail.querySelector('.mailHeadline')
  let sender = mail.querySelector('.mailSender')
  let content = mail.querySelector('.mailContent')
  let practice = mail.querySelector('.mailPracticeName')

  if (practice){
    document.getElementById('contentPracticeName').innerHTML = practice.innerHTML
    document.getElementById('contentPractice').style.display = 'block';
  } else{
    document.getElementById('contentPractice').style.display = 'none';
  }

  document.getElementById('contentHeadline').innerText = headline.innerHTML
  document.getElementById('contentSender').innerText = sender.innerHTML
  document.getElementById('contentBody').innerText = content.innerHTML
}

function sentMails(thisBtn){
  document.getElementById('inboxMassagesDiv').classList.add('hidden');
  document.getElementById('sentMassagesDiv').classList.remove('hidden');
  thisBtn.classList.add('selected');
  document.getElementById('inboxBtn').classList.remove('selected');
  document.getElementById('replayBtn').classList.add('hidden')
  openMail(document.getElementById('sentMassagesDiv').children[0]);
}
function inboxMails(thisBtn){
  document.getElementById('inboxMassagesDiv').classList.remove('hidden');
  document.getElementById('sentMassagesDiv').classList.add('hidden');
  thisBtn.classList.add('selected');
  document.getElementById('sentBtn').classList.remove('selected');
  document.getElementById('replayBtn').classList.remove('hidden');
  openMail(document.getElementById('inboxMassagesDiv').children[0]);
}

function deleteMail(sender, DT){
  if (confirm(`האם למחוק את המייל מ${sender}?`)){
    route = `/deleteMail?sender=${sender}&DT=${DT}`
    window.location.href= route
  }
}
