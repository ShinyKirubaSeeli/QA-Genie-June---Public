document.querySelector("#submit").addEventListener("click",placeOrder);
document.querySelector("input+p").addEventListener("click",resendOTP);
let cartArr = JSON.parse(localStorage.getItem('cartData')) || []
function placeOrder(){
    let Otp=document.querySelector("#otP").value;
    // if(Otp==null){
    //     // alert("Order Placed Successfully!, Thank You.");
    // }
    if(Otp==123){
        alert("Order Placed Successfully ! Thank You.");
        cartArr=[]
        localStorage.setItem("cartData",JSON.stringify(cartArr))
        window.location.href="index.html"

    }else if(Otp!=123){
        alert("Entered Wrong One-time Password (OTP) !")
       document.querySelector("#otP").value="";
    }
}
