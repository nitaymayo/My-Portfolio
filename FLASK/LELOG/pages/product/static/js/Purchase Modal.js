function change() {
    const div = document.getElementById(`schedule`)
    if (div.style.height === `60px`){
        div.style.height = `0px`;
    } else{
        div.style.height = `60px`;
    }
}