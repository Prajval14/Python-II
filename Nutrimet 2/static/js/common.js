document.addEventListener('DOMContentLoaded', function() {
    // Navbar JS
    let navbar_brand = document.getElementById("navbar_brand");
    navbar_brand.src = '/static/media/logo/main.png'

    //Footer JS
    let payment_visa = document.getElementById("payment_visa");
    let payment_mastercard = document.getElementById("payment_mastercard");
    let payment_applepay = document.getElementById("payment_applepay");
    let payment_paypal = document.getElementById("payment_paypal");

    payment_visa.src = '/static/media/payment/visa.png';
    payment_mastercard.src = '/static/media/payment/mastercard.png';
    payment_applepay.src = '/static/media/payment/applepay.png';
    payment_paypal.src = '/static/media/payment/paypal.png';

    const footerYear = document.getElementById('current_Year');
    footerYear.innerHTML = new Date().getFullYear();
});