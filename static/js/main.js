if (window.location.pathname == '/'){
    function scrollToElement(event, elementId) {
        event.preventDefault(); // Prevent the default behavior (URL change)
        var element = document.getElementById(elementId);
        console.log(element.offsetTop)
        const targetPosition = element.offsetTop - 70;
        window.scrollTo({ top: targetPosition, behavior: 'smooth' });
    }
    
    
    const button = document.getElementById('button');
    const elements = document.querySelectorAll('.container .element.hide');

    button.addEventListener('click', () => {
        let isHidden = false;
        
        elements.forEach(element => {
        if (element.classList.contains('hide')) {
            isHidden = true;
        }
        element.classList.toggle('hide');
        });

        button.textContent = isHidden ? "Moins" : "Plus";
    });

    

} 