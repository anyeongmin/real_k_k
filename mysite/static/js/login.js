//window.onload = function(){
    let id = document.querySelector("input[name='id']");
    let pwd = document.querySelector("input[name='pwd']");
    let btn = document.querySelector(".submit");
    let form = document.querySelector("#regi");
    btn.addEventListener("click",function(){
        if (id.value == ""){
            alert("아이디 입력창이 비어있습니다");
            id.focus();
            return;
        }
        if (pwd.value == ""){
            alert("아이디 입력창이 비어있습니다");
            wd.focus();
            return;
        }
        form.submit();
    });
//}