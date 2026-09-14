// Simple client-side helpers for the shop
document.addEventListener('DOMContentLoaded', function () {

  // Live-update the cart total whenever quantities change on the page,
  // giving instant feedback before the form submit reloads the page.
  const cartBody = document.getElementById('cart-body');
  if (cartBody) {
    cartBody.querySelectorAll('.qty-form button').forEach(function (btn) {
      btn.addEventListener('click', function () {
        const row = btn.closest('tr');
        const priceCell = row.querySelector('.item-price');
        const qtySpan = row.querySelector('.item-qty');
        const price = parseFloat(row.dataset.price);
        let qty = parseInt(qtySpan.textContent, 10);

        // Optimistic UI update; the server value is authoritative after reload.
        if (btn.value === 'increase') {
          qty += 1;
        } else if (btn.value === 'decrease') {
          qty = Math.max(qty - 1, 0);
        }
        const subtotalCell = row.querySelector('.item-subtotal');
        if (subtotalCell && !isNaN(price)) {
          subtotalCell.textContent = '$' + (price * qty).toFixed(2);
        }
      });
    });
  }

  // Quantity input on the product detail page cannot exceed available stock.
  const qtyInput = document.getElementById('quantity');
  if (qtyInput) {
    qtyInput.addEventListener('change', function () {
      const max = parseInt(qtyInput.getAttribute('max'), 10);
      const min = parseInt(qtyInput.getAttribute('min'), 10) || 1;
      let val = parseInt(qtyInput.value, 10) || min;
      if (max && val > max) val = max;
      if (val < min) val = min;
      qtyInput.value = val;
    });
  }
});
