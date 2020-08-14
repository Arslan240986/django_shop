
function changeLanguage(){
    let select = document.querySelector("select")
    for(let elem of select.options){
        if(elem.text == 'tr'){
            elem.text = 'Turkmen ' + `(${elem.text})`
        } else if(elem.text == 'ru'){
            elem.text = 'Русский ' + `(${elem.text})`

        }
    }
}
changeLanguage()
// Header flex top on resize window
HeaderFlex()
function HeaderFlex(){
    let navbar = document.querySelector('.fixed-top')
    document.querySelector('.header').style.marginTop = navbar.clientHeight+'px';

    window.onresize = function(){
        let navbar = document.querySelector('.fixed-top')
        document.querySelector('.header').style.marginTop = navbar.clientHeight+'px';
    }
}

// This all about translation templates into Turkmen and Russian language
// I did that in Js becous i couldnot finde the encoding error solution in django

window.onload = function translations(){
        let select = document.querySelector("select")
        let trans_rus = document.querySelectorAll('.trans_ru')
        let trans_trs = document.querySelectorAll('.trans_tr')
        trans_trs.forEach(elem =>(elem.style.display = 'none'))
        if ( select.value == 'tr'){
            trans_rus.forEach(elem =>(elem.style.display = 'none'))
            trans_trs.forEach(elem =>(elem.style.display = 'inline-block'))
        } else if (select.value == 'ru'){
            trans_rus.forEach(elem =>(elem.style.display = 'inline-block'))
            trans_trs.forEach(elem =>(elem.style.display = 'none'))
        }

}
// language script ajax




