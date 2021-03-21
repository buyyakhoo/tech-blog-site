// index animation
var i = 0;
var txt = 'Tech-Blog-Site';
var speed = 150;

function typeWriter() {
    if (i < txt.length) {
        if (i == -1) {
            document.getElementById("typing").innerHTML = " ";
            i++;
            setTimeout(typeWriter, speed);
        } else {
            document.getElementById("typing").innerHTML += txt.charAt(i);
            i++;
            setTimeout(typeWriter, speed);
        }
    } else {
        setTimeout(typeWriter, 5000);
        i = -1;
    }
}


window.addEventListener('load', typeWriter);
