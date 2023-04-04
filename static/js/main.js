/* Script for page REALISATIONS */
if (window.location.pathname == '/'){
    console.log('lol');
    const projetList = document.querySelectorAll('.element');
    const arrowLeft = document.getElementById('arrow-left');
    const arrowRight = document.getElementById('arrow-right');
    let currentpost = 0;
    projetList[currentpost].removeAttribute('hidden');

    arrowLeft.addEventListener('click', function(event){
        event.preventDefault;
        console.log("left");
        changeVisiblePost(projetList, currentpost, -1);
        if (currentpost == 0) {
            currentpost = projetList.length - 1
        } else {
            currentpost -= 1
        }
    })

    arrowRight.addEventListener('click', function(event){
        event.preventDefault;
        console.log("right");
        changeVisiblePost(projetList, currentpost, 1);
        if (currentpost == projetList.length - 1) {
            currentpost = 0
        } else {
            currentpost += 1
        }
            
    })

}

function changeVisiblePost(list, post, val){
    let postId = post
    list[postId].setAttribute('hidden', 'true')
    if (postId + val < 0){
        list[list.length - 1].removeAttribute('hidden')
    }else if (postId + val == list.length){
        list[0].removeAttribute('hidden')
    } else {
        list[postId + val].removeAttribute('hidden')
    }

    
}       

function scrollToElement(event, elementId) {
    event.preventDefault(); // Prevent the default behavior (URL change)
    var element = document.getElementById(elementId);
    element.scrollIntoView({ behavior: 'smooth' });
  }
