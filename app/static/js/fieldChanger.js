document.addEventListener('DOMContentLoaded', function () {
    const methodSelect = document.getElementById('method');
    methodSelect.value = '';
    const itemsSelect = document.getElementById('fuel_type');
    itemsSelect.value = '';
    const passengersSelect = document.getElementById('passenger-select');
    passengersSelect.style.display = 'none';

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
            if (this.value == 'Car' || this.value == 'Motorbike' || this.value == 'Scooter') {
                passengersSelect.style.display = 'block';
            }
            else {
                passengersSelect.style.display = 'none';
            }
        });
    }
});