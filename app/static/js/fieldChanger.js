document.addEventListener('DOMContentLoaded', function () {
    const methodSelect = document.getElementById('method');
    const itemsSelect = document.getElementById('fuel_type');

    if (methodSelect) {
        methodSelect.addEventListener('change', function () {
            const method = this.value;
            fetch(`/get-items?method=${method}`)
                .then(response => response.json())
                .then(data => {
                    itemsSelect.innerHTML = '';
                    data.items.forEach(function (item) {
                        const option = document.createElement('option');
                        option.value = item;
                        option.text = item;
                        itemsSelect.appendChild(option);
                    });
                })
                .catch(error => {
                    console.error('Error fetching items:', error);
                });
        });
    }
});