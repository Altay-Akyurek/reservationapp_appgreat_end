document.addEventListener("DOMContentLoaded", function() {
    // Kart Numarası
    document.getElementById("cardNumber").addEventListener("input", function() {
        const cardNumber = this.value.replace(/\s+/g, '').replace(/(\d{4})/g, '$1 ').trim();
        document.getElementById("display-card-number").textContent = cardNumber || "XXXX XXXX XXXX XXXX";
    });

    // Kart Sahibi
    document.getElementById("cardName").addEventListener("input", function() {
        document.getElementById("display-card-name").textContent = this.value || "AD SOYAD";
    });

    // Son Kullanma Tarihi
    document.getElementById("expiry").addEventListener("input", function() {
        document.getElementById("display-expiry").textContent = this.value || "MM/YY";
    });

    // CVV
    document.getElementById("cvv").addEventListener("input", function() {
        // CVV bilgisi genellikle ekranda gösterilmez ama buraya koyabiliriz
        // Örneğin:
        document.getElementById("display-cvv").textContent = this.value || "XXX";
    });
});
