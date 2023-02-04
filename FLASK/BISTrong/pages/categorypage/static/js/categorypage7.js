const workouts = document.querySelectorAll('.practiceImg')
const images = [ 'sideplank-1.jpg', 'restBack.jpeg', 'hamstrings1.jpeg', 'twins-2.PNG', 'squat1.jpeg', 'lowback-2.jpg', 'pushups-4.jpg', 'abs3.jpeg', 'back1.jpeg', 'OnTheBack2.jpeg', 'parallels1.jpeg', 'superman.jpeg']
for (let i = 0; i<workouts.length; i++){
  workouts[i].setAttribute('src',`/static/media/img/fitPhotos/${images[i%images.length]}`)
}



function deleteCategory(category){
  if (confirm(`מחיקת הקטגוריה "${category}" תגרום למחיקה של כל האימונים בקטגוריה זו, מעוניין להמשיך בכל מקרה?`)){
    location.href = `/deleteCategory?category=${category}`
  }
}