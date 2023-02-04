function userProfileEdit() {
    let inputs = document.querySelectorAll('#profileSec input')
    let a
    document.getElementById('msg').innerHTML = ''
    if (inputs[0].hasAttribute('disabled')) {
        for (a = 0; a < 5; a++) {
            inputs[a].removeAttribute('disabled')
        }
        document.getElementById('update').removeAttribute('hidden')
    } else{
        for (a = 0; a < 5; a++) {
            inputs[a].setAttribute('disabled', '')
            document.getElementById('update').setAttribute('hidden','')
        }
    }
}
function showPass(){
    let passinput = document.getElementById('passwordDatum')
    if (passinput.hasAttribute('hidden')){
        passinput.removeAttribute('hidden')
    } else{
        passinput.setAttribute('hidden','')
    }
}