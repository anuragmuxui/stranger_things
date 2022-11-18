var myButton = document.getElementsByName('dynamic');
var myInput = document.getElementsByName('viewMnemonic');
myButton.forEach(function(element, index){
  element.onclick = function(){
      if (myInput[index].type == 'password') {
        var  password = prompt("Enter master password");
      if(password == "1234"){
          myInput[index].setAttribute('type', 'text');
          element.firstChild.textContent = 'Hide';
          element.firstChild.className = "";

      }
      }
      else if(myInput[index].type == 'text') {
           myInput[index].setAttribute('type', 'password');
           element.firstChild.textContent = '';
            element.firstChild.className = "fa fa-eye";
      } 
  }
})