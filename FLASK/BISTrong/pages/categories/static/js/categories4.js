const categories = document.querySelectorAll('.planImg')
const colors = [ 'OnTheBack1.jpeg', 'plank-1.jpg', 'lunchBack.jpeg', 'pushup1.jpeg', 'lunchBack2.jpeg', 'back1.jpeg', 'OnTheBack2.jpeg', 'parallels1.jpeg', 'superman.jpeg', 'deadliftOneLeg1.jpeg']
for (let i = 0; i<categories.length; i++){
  categories[i].setAttribute('src',`../../static/media/img/fitPhotos/${colors[i%colors.length]}`)
}

const errorMsgDiv = document.getElementById('errorMsg')
if (errorMsgDiv != null){
  alert(errorMsgDiv.innerText)
}

function deleteCategory(category){
  if (confirm(`מחיקת הקטגוריה "${category}" תגרום למחיקה של כל האימונים בקטגוריה זו, מעוניין להמשיך בכל מקרה?`)){
    location.href = `/deleteCategory?category=${category}`
  }
}