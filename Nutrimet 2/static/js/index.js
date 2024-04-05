import { gym_data_list, yoga_data_list, supplements_data_list } from './data.js';

const gymContainer = document.getElementById('gym_data_container');
const yogaContainer = document.getElementById('yoga_data_container');
const footerYear = document.getElementById('current_Year');
const supplementsContainer = document.getElementById('supplements_data_container');
const cartBadge = document.getElementById('cart_items_badge');
const navbarBadge = document.getElementById('navbar_toggler_icon_badge');

const discountedGymProducts = gym_data_list.filter(product => product.isondiscount);
const discountedYogaProducts = yoga_data_list.filter(product => product.isondiscount);
const discountedSupplementProducts = supplements_data_list.filter(product => product.isondiscount);

const myCart = [];

let gymIndex = 0;
let yogaIndex = 0;
let supplementsIndex = 0;

document.addEventListener('DOMContentLoaded', function() {
    let product_data = JSON.parse([document.getElementById("product-data").textContent]);    
    debugger
    if (window.innerWidth < 1025) {        
        createCards(discountedGymProducts[0], gymContainer);
        createCards(discountedYogaProducts[0], yogaContainer);
        createCards(discountedSupplementProducts[0], supplementsContainer);
    } else {        
        discountedGymProducts.forEach(data => createCards(data, gymContainer));
        discountedYogaProducts.forEach(data => createCards(data, yogaContainer));
        discountedSupplementProducts.forEach(data => createCards(data, supplementsContainer));
    }    
    
    // Add event listeners to the navigation links
    document.querySelectorAll('.index-scroll').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetDiv = document.querySelector(targetId);
            targetDiv.scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    //Setting up add to cart button after all cards are rendered
    handleAddToCart(); 

    //Setting dynamic year value in footer
    footerYear.innerHTML = new Date().getFullYear();
});

//Handling left right click event listeners for card in mobile viewport
document.getElementById('gym_left').addEventListener("click", () => handleNavigation(-1, 'gym', discountedGymProducts, gymContainer));
document.getElementById('gym_right').addEventListener("click", () => handleNavigation(1, 'gym', discountedGymProducts, gymContainer));
document.getElementById('yoga_left').addEventListener("click", () => handleNavigation(-1, 'yoga', discountedYogaProducts, yogaContainer));
document.getElementById('yoga_right').addEventListener("click", () => handleNavigation(1, 'yoga', discountedYogaProducts, yogaContainer));
document.getElementById('supplement_left').addEventListener("click", () => handleNavigation(-1, 'supplements', discountedSupplementProducts, supplementsContainer));
document.getElementById('supplement_right').addEventListener("click", () => handleNavigation(1, 'supplements', discountedSupplementProducts, supplementsContainer));

// Handling navbar cart and sign up on click event
document.getElementById('nav_cart_button').addEventListener("click", () => window.location.href = './html/cart.html?index_page_selected_products=' + JSON.stringify(myCart));
// document.getElementById('nav_login_button').addEventListener("click", () => toggleValidation());

//Functions defined
function createCards(data, container) {   
    // debugger 
    const cardDiv = document.createElement('div');
    cardDiv.className = 'col p-3';
    cardDiv.innerHTML = `
        <div class="card" style="width: 20rem;">
            <img src="${data.imageURL}" id="product_image_${data.productid}" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="product-id d-none">${data.productid}</h5>
                <h5 class="card-title">${data.productname}</h5>
                <h6 class="card-subtitle mb-2 text-body-secondary" style="height: 50px">${data.productdetail}</h6>
                <p class="card-text">
                <span class="text-decoration-line-through text-secondary fw-light">$${data.originalprice}</span>
                <span class="fw-bold text-danger ps-1 fs-5">$${data.discountPrice}</span>
                </p>
            </div>
            <div class="card-footer">
                <button class="btn btn-primary border-0 fw-medium add_to_cart_button" id="add_to_cart_button">Add to cart</button>
            </div>
        </div>
    `;
    container.appendChild(cardDiv);

    //Handling on click event for product images 
    document.getElementById(`product_image_${data.productid}`).addEventListener("click", (event) => {
        window.location.href = `./html/productdetails.html?selected_product=${JSON.stringify(data.productid)}`;
    });
}

function handleNavigation(direction, category, dataList, container) {
    switch (category) {
        case 'gym':
            gymIndex = (gymIndex + direction + dataList.length) % dataList.length;
            showCard(gymIndex, dataList, container);
            break;
        case 'yoga':
            yogaIndex = (yogaIndex + direction + dataList.length) % dataList.length;
            showCard(yogaIndex, dataList, container);
            break;
        case 'supplements':
            supplementsIndex = (supplementsIndex + direction + dataList.length) % dataList.length;
            showCard(supplementsIndex, dataList, container);
            break;
        default:
            console.error('Invalid category');
    }
}

function showCard(index, dataList, container) {
    container.innerHTML = '';
    createCards(dataList[index], container);
}

function handleAddToCart() {
    const addToCartButtons = document.querySelectorAll('.add_to_cart_button');
    addToCartButtons.forEach(button => button.addEventListener("click", (event) => addProductToCart(event)));
}

function addProductToCart(event) {
    //Set add to cart on click to addded for few seconds
    const button = event.target;
    button.innerHTML = `Added <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check-circle-fill" viewBox="0 0 16 16">
    <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0m-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"/>
    </svg>`;
    button.classList.add('added');
    setTimeout(function() {
        button.textContent = 'Add to Cart';
        button.classList.remove('added');
    }, 1000);

    //Add product ID to cart and a list 
    const productID = event.target.closest('.card').querySelector('.product-id').textContent;        
    myCart.push(productID);
    navbarBadge.style.display = 'flex';
    cartBadge.innerHTML = myCart.length;
}

// function toggleValidation() {
    
//     var isValid = sessionStorage.getItem("isValid");

//     // If isValid is null or false, redirect to signup.html
//     if (!isValid || isValid === "false") {
//         // Redirect to signup.html
//         window.location.href = './html/signup.html';
//     } else {
//         // Redirect to products.html
//         window.location.href = './html/details.html';
//     }
// }