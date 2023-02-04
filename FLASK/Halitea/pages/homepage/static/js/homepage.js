




const slider1 = document.getElementById(`carousel`);


const shopBtn = document.getElementById(`shopBtn`);

function scroll1(){
        slider1.scroll(slider1.scrollLeft + 1, 0)
        if (slider1.offsetWidth + slider1.scrollLeft >= slider1.scrollWidth)
            slider1.scroll(0,0)
}

window.setInterval(scroll1, 1)

