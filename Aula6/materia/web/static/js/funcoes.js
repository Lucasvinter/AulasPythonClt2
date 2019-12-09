

function click_list(){
    alert('clicado')
}

var a = document.getElementById("lista")
console.log(a)
a.addEventListener("click", click_list);