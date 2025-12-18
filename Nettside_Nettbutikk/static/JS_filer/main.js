
//----------------NAVIGASJON MENY-----------//
// Side menu toggle
const menuBtn = document.querySelector(".menu-btn");
const sideMenu = document.querySelector(".side-menu");
const overlay = document.querySelector(".overlay");

// Toggle menu
menuBtn.onclick = function () {
    sideMenu.classList.toggle("open");
    overlay.style.display = sideMenu.classList.contains("open") ? "block" : "none";
};

// Klikk på overlay → lukk meny
overlay.onclick = function () {
    sideMenu.classList.remove("open");
    overlay.style.display = "none";
};



//----- PRODUKT FUKSJONER------//

// Favoritt-knapp funksjon
function openFavorites() {
    const icon = event.target;
    icon.classList.toggle('active');
    if (icon.classList.contains('active')) {
        icon.style.color = 'red';
        // Her kan du legge til logikk for å legge produktet i favoritter
    } else {
        icon.style.color = '#2d3a4b';
        // Fjerne fra favoritter
    }
}


// Favoritt-knapp (hjerte)
function toggleFavorite(icon) {
  icon.classList.toggle('active');
  if (icon.classList.contains('active')) {
    icon.style.color = 'red';
    icon.style.transform = 'scale(1.3)';
    setTimeout(() => icon.style.transform = 'scale(1)', 200); // liten animasjon
  } else {
    icon.style.color = '#2d3a4b';
  }
}

// Buy-knapp
function toggleBuy(button) {
  button.classList.toggle('added');
  if (button.classList.contains('added')) {
    button.textContent = 'Added!';
    button.style.backgroundColor = '#4caf50';
    button.style.transform = 'scale(1.1)';
    setTimeout(() => button.style.transform = 'scale(1)', 200);
  } else {
    button.textContent = 'Buy now';
    button.style.backgroundColor = ''; // tilbake til original
  }
}


// Vis ekstra info ved klikk på produktkortet
document.querySelectorAll('.product-card').forEach(card => {
    card.addEventListener('click', (e) => {
        if (e.target.classList.contains('buy-btn') || e.target.classList.contains('fa-heart')) return;

        let extraInfo = card.querySelector('.extra-info');
        if (!extraInfo) {
            extraInfo = document.createElement('div');
            extraInfo.classList.add('extra-info');
            extraInfo.innerHTML = '<p>High-quality stickers with vibrant designs, perfect for decorating laptops, phones, notebooks, and personal items. Fun, durable, and made to express your style!</p>';
            card.querySelector('.product-info').appendChild(extraInfo);
        }

        extraInfo.style.display = extraInfo.style.display === 'block' ? 'none' : 'block';
        extraInfo.style.animation = 'fadeIn 0.4s ease-in-out';
    });
});
// Ikoner funksjon
const homeIcon = document.getElementById("home-icon");
const favoritesIcon = document.getElementById("favorites-icon");
const cartIcon = document.getElementById("cart-icon");

const homeSection = document.getElementById("home-section");
const favoritesSection = document.getElementById("favorites-section");
const cartSection = document.getElementById("cart-section");

function hideAll() {
    homeSection.style.display = "none";
    favoritesSection.style.display = "none";
    cartSection.style.display = "none";
}

homeIcon.addEventListener("click", () => {
    hideAll();
    homeSection.style.display = "block";
    document.querySelector(".side-menu").classList.remove("open");
});

favoritesIcon.addEventListener("click", () => {
    hideAll();
    favoritesSection.style.display = "block";
    document.querySelector(".side-menu").classList.remove("open");
});

cartIcon.addEventListener("click", () => {
    hideAll();
    cartSection.style.display = "block";
    document.querySelector(".side-menu").classList.remove("open");
});



//----------------FAQ side-----------//
document.addEventListener("DOMContentLoaded", function() {
  const accordions = document.querySelectorAll(".accordion");

  accordions.forEach(acc => {
    acc.addEventListener("click", function () {
      const parentFaq = this.parentElement;
      parentFaq.classList.toggle("active"); // Legger til/fjerner aktiv klasse for fold
    });
  });
});


//----------------Explore Now-----------//
function scrollToProducts() {
    const productSection = document.querySelector('.product-section');
    productSection.scrollIntoView({ behavior: 'smooth' });
}
