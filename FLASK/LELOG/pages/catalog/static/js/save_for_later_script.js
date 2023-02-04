function onEnter(div) {
    document.querySelector(`#${div}>img`).setAttribute(`src`, `../../../static/media/img/Star Marked.png`)
}
function onExit(div) {
    document.querySelector(`#${div}>img`).setAttribute(`src`, `../../../static/media/img/Star.png`)
}
function onClick(div) {
    const temp = document.getElementById(div)
    const node = document.querySelector(`#${div}>p`)

    if (temp.hasAttribute(`onmouseleave`)){
        temp.removeAttribute(`onmouseleave`)
        node.innerHTML = `Saved`
    } else {
        temp.setAttribute(`onmouseleave`, `onExit('${div}')`)
        node.innerHTML = `Save for later`
    }
}