function mover(params) {
    var animate = document.getElementById('animate');
    var pos = 0;
    var intervalo = setInterval(frame, 5);

    function frame(){
        if(pos == 860){
            clearInterval(intervalo)
        } else {
            pos++;
            animate.style.left = pos + "px";
            animate.style.top = pos + "px";
        }

    }
}