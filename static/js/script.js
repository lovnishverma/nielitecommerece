// ===== Scroll to Top ==== 
$(window).scroll(function() {
    if ($(this).scrollTop() >= 50) {        // If page is scrolled more than 50px
        $('#return-to-top').fadeIn(200);    // Fade in the arrow
    } else {
        $('#return-to-top').fadeOut(200);   // Else fade out the arrow
    }
});
$('#return-to-top').click(function() {      // When arrow is clicked
    $('body,html').animate({
        scrollTop : 0                       // Scroll to top of body
    }, 500);
});

function toggleMenu() {
            document.querySelector(".nav-links").classList.toggle("active");
        }

function toggleWishlist(productId) {
    // Get the icon element
    let icon = document.getElementById(`wishlist-icon-${productId}`);
    // Determine if the item is currently wishlisted by checking the icon class.
    let isWishlisted = icon.classList.contains("fas"); // "fas" = solid heart, "far" = outline

    // Decide the URL based on the current state
    let url = isWishlisted ? "/removeFromWishlist" : "/addToWishlist";

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
        },
        body: "product_id=" + productId
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === "success") {
            // Toggle the icon classes to reflect the change
            icon.classList.toggle("fas");
            icon.classList.toggle("far");
        } else {
            alert(data.message);
        }
    })
    .catch(error => {
        console.error("Error:", error);
    });
}
