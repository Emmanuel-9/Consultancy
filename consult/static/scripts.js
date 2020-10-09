const counters = document.querySelectorAll('.counter');
const speed = 40;

counters.forEach(counter => {
    const updateCount =() => {
        const target = +counter.getAttribute('data-target');
        const count = +counter.innerText;
        const inc = target / speed;
        console.log(count);
        if(count < target){
          counter.innerText = count + inc; 
          setTimeout(updateCount, 10);
        } else {
            counter.innerText = target;
        }

    }
    updateCount();
}); 

const cookieContainer = document.querySelector('.cookie-container');
const cookieButton = document.querySelector('.cookie-btn');

cookieButton.addEventListener("click", () => {
    cookieContainer.classList.remove("active");
    localStorage.setItem("CookieBannerDisplayed","true");
});

setTimeout(() => {
    if(!localStorage.getItem("CookieBannerDisplayed","true")){
    cookieContainer.classList.add("active");
    }
}, 4000);