let cart = [];
let total = 0;

const backendURL = "http://127.0.0.1:5000";

window.onload = function () {
  fetchCategories();
  fetchProducts();
};

function fetchCategories() {
  fetch(`${backendURL}/categories`)
    .then(res => res.json())
    .then(categories => {
      const container = document.getElementById("categories");
      if (!container) return;
      container.innerHTML = "<h3>Categories:</h3>";
      categories.forEach(cat => {
        const btn = document.createElement("button");
        btn.innerText = cat;
        btn.onclick = () => fetchProducts(cat);
        container.appendChild(btn);
      });
    })
    .catch(err => console.error("Error fetching categories:", err));
}

function fetchProducts(category = "") {
  fetch(`${backendURL}/products`)
    .then(res => res.json())
    .then(data => {
      const filtered = category ? data.filter(p => p.Category === category) : data;
      displayProducts(filtered);
    })
    .catch(err => console.error("Error fetching products:", err));
}

function displayProducts(products) {
  const container = document.getElementById("products");
  if (!container) return;
  container.innerHTML = "";

  products.forEach(p => {
    const card = document.createElement("div");
    card.className = "product-card";
    card.innerHTML = `
      <img src="${p.ImageURL}" alt="${p.Name}">
      <h3>${p.Name}</h3>
      <p>₹${p.Price}</p>
      <button onclick="addToCart(${p.ProductID}, '${p.Name}', ${p.Price})">Add to Cart</button>
    `;
    container.appendChild(card);
  });
}

function addToCart(id, name, price) {
  const existing = cart.find(item => item.product_id === id);
  if (existing) {
    existing.quantity += 1;
  } else {
    cart.push({ product_id: id, name, price, quantity: 1 });
  }
  updateCart();

  // Show popup message
  showPopup(`${name} added to cart successfully!`);
}

function showPopup(message) {
  const popup = document.createElement("div");
  popup.className = "popup-message";
  popup.innerText = message;

  document.body.appendChild(popup);

  setTimeout(() => {
    popup.remove();
  }, 2000); // 2 seconds
}

function updateCart() {
  const list = document.getElementById("cart-items");
  const totalPrice = document.getElementById("total-price");
  list.innerHTML = "";
  total = 0;

  cart.forEach(item => {
    const li = document.createElement("li");
    li.innerText = `${item.name} x${item.quantity} - ₹${item.price * item.quantity}`;
    list.appendChild(li);
    total += item.price * item.quantity;
  });

  totalPrice.innerText = `₹${total}`;
}

function placeOrder() {
  const payment_mode = document.getElementById("payment-mode").value;
  const customer_id = 1; // static for demo

  if (cart.length === 0) {
    alert("Cart is empty!");
    return;
  }

  if (!payment_mode) {
    alert("Please select a payment mode.");
    return;
  }

  fetch(`${backendURL}/place_order`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      cart,
      payment_mode,
      customer_id
    })
  })
    .then(res => {
      if (!res.ok) {
        throw new Error("Error placing order");
      }
      return res.json();
    })
    .then(data => {
      alert("✅ " + data.message);
      cart = [];
      updateCart();
    })
    .catch(err => {
      console.error("Error placing order:", err);
      alert("❌ Failed to place order. Check console for error.");
    });
}

// Dark Mode Toggle
document.getElementById("dark-mode-toggle").addEventListener("click", () => {
  document.body.classList.toggle("dark-mode");
});

document.getElementById("login-btn").addEventListener("click", () => {
  window.location.href = "login.html"; // or your login URL
});

document.getElementById("search-btn").addEventListener("click", () => {
  const searchTerm = document.getElementById("search-input").value.toLowerCase().trim();
  if (!searchTerm) {
    fetchProducts(); // If empty, show all products
    return;
  }

  fetch(`${backendURL}/products`)
    .then(res => res.json())
    .then(data => {
      const filtered = data.filter(p => p.Name.toLowerCase().includes(searchTerm));
      displayProducts(filtered);
    })
    .catch(err => console.error("Error fetching products:", err));
});
