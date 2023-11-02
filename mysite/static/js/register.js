//window.onload = function(){
    let id = document.querySelector("input[name='id']");
    let pwd = document.querySelector("input[name='pwd']");
    let btn = document.querySelector(".submit");
    let form = document.querySelector("#regi");
    btn.addEventListener("click",function(){
        if (id.value.length < 5){
            alert("please input five letter");
            return;
        }
        if (pwd.value.length < 8){
            alert("비밀번호를 8글자 이상으로 입력해주세요");
            return;
        }
        form.submit();
    });
//}