function onEnter(btn) {
    document.querySelector(`#${btn}>img`).setAttribute(`src`, '../../../../static/media/img/Heart Marked.png')
}
function onExit(btn) {
    document.querySelector(`#${btn}>img`).setAttribute(`src`, '../../../../static/media/img/Heart.png')
}

function onClick(btn) {
    const temp = document.getElementById(btn)
    const node = document.querySelector(`#${btn}>p`)

    if (temp.hasAttribute(`onmouseleave`)){
        temp.removeAttribute(`onmouseleave`)
        node.innerHTML = `Added`
    } else {
        temp.setAttribute(`onmouseleave`, `onExit('${btn}')`)
        node.innerHTML = `Add to wish list`
    }
}

