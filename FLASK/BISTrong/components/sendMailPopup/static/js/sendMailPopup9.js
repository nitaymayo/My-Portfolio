function newMail(){
if (document.getElementById('mailPractice')) {
    document.getElementById('mailPractice').remove()
  }
  document.getElementById('sendMailContainer').classList.remove('hidden');
  document.getElementById('mailContentInput').innerHTML = '';
  document.getElementById('sendToInput').value = '';
  document.getElementById('mailHeadlineInput').value = '';

}

function replay(){
  if (document.getElementById('mailPractice')) {
    document.getElementById('mailPractice').remove()
  }
  document.getElementById('sendMailContainer').classList.remove('hidden');

  let practiceName = document.getElementById('contentPracticeName').innerText
  let sender = document.getElementById('contentSender').innerHTML
  let lastContent = document.getElementById('contentBody').innerText
  let lastHeadline = document.getElementById('contentHeadline').innerText

  document.getElementById('mailHeadlineInput').value = `RE:${lastHeadline}`
  document.getElementById('sendToInput').value =  sender
  document.getElementById(`mailContentInput`).innerHTML = "\n\n" + `------------------------------------` + "\n\n" + `נשלח על ידי:${sender} \n` + "\n" +  lastContent

  document.getElementById(`mailContentInput`).focus()

}