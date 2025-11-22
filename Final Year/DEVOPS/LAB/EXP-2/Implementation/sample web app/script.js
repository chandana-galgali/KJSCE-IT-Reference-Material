// Cart Array
let cart = [];
const cartCountElement = document.getElementById('cart-count');
const cartButton = document.getElementById('cart-button');
const cartModal = document.getElementById('cart-modal');
const closeBtn = document.getElementById('close-btn');
const cartItemsElement = document.getElementById('cart-items');
const totalPriceElement = document.getElementById('total-price');

// Product Data
const products = {
    1: { name: "Fiddle Leaf Fig", price: 25.00, img: "plant1.jpg" },
    2: { name: "Snake Plant", price: 18.00, img: "plant2.jpg" },
    3: { name: "Succulent Garden", price: 15.00, img: "plant3.jpg" },
    4: { name: "Peace Lily", price: 20.00, img: "plant4.jpg" }
};

// Add to Cart Function
const addToCart = (productId) => {
    const product = products[productId];
    cart.push(product);
    updateCart();
};

// Update Cart UI
const updateCart = () => {
    // Update Cart Count
    cartCountElement.innerText = cart.length;

    // Update Cart Modal
    cartItemsElement.innerHTML = '';
    let totalPrice = 0;
    cart.forEach((product, index) => {
        const li = document.createElement('li');
        li.innerHTML = `${product.name} - $${product.price.toFixed(2)} <button onclick="removeFromCart(${index})">Remove</button>`;
        cartItemsElement.appendChild(li);
        totalPrice += product.price;
    });
    totalPriceElement.innerText = totalPrice.toFixed(2);
};

// Remove from Cart Function
const removeFromCart = (index) => {
    cart.splice(index, 1);
    updateCart();
};

// Open Cart Modal
cartButton.addEventListener('click', () => {
    cartModal.style.display = 'flex';
});

// Close Cart Modal
closeBtn.addEventListener('click', () => {
    cartModal.style.display = 'none';
});

// Event Listeners for Add to Cart Buttons
document.querySelectorAll('.add-to-cart').forEach((button) => {
    button.addEventListener('click', (e) => {
        const productId = e.target.getAttribute('data-product');
        addToCart(productId);
    });
});
