function closePopup(){
   const scrollY = document.body.style.top;
    document.body.style.position = '';
    document.body.style.top = '';
    window.scrollTo(0, parseInt(scrollY || '0') * -1);
}
function openPopup(){
    document.body.style.top = `-${window.scrollY}px`;
  document.body.style.position = 'fixed';

}

function check_valid(input) {
    let list = input.list;
    let value = input.value;
    let options = list.children;
    for (option of options){
        if (option.value == value){
            return true
        }
    }
    return false
}

function check_datalist(input) {
    is_in = check_valid(input);
    if (!is_in){
        input.value = "";
    }
}