document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('navigation-form');
    const modal = document.getElementById('result-modal');
    const closeBtn = document.querySelector('.close-button');
    const pathwayDiv = document.getElementById('pathway-output');
    const locationsDiv = document.getElementById('locations-output');

    // Close modal when clicking X or outside
    closeBtn.onclick = () => modal.classList.remove('active');
    window.onclick = (e) => {
        if (e.target === modal) {
            modal.classList.remove('active');
        }
    };

    form.addEventListener('submit', (e) => {
        e.preventDefault();

        const age = document.getElementById('age').value;
        const postcode = document.getElementById('postcode').value.toUpperCase().replace(/\s/g, '') || 'SW1A1AA';
        const symptoms = Array.from(document.getElementById('symptoms').selectedOptions).map(o => o.value);

        if (!age || symptoms.length === 0) {
            alert('Please select age group and at least one symptom.');
            return;
        }

        // Get pathway logic
        const pathway = getPathway(age, symptoms);
        pathwayDiv.innerHTML = pathway.message;

        // Mock locations
        const locations = getMockLocations(pathway.serviceType, postcode);
        let list = '<h3>Nearby Services (Demo Data – December 2025)</h3><ul>';
        locations.forEach(l => {
            list += `<li><strong>${l.name}</strong><br>${l.address}<br>Postcode: ${l.postcode}<br>Phone: ${l.phone}</li><hr>`;
        });
        list += '</ul>';
        locationsDiv.innerHTML = list;

        // SHOW MODAL - Now works perfectly
        modal.classList.add('active');
    });
});

function getMockLocations(type = 'pharmacy', postcode = 'SW1A 1AA') {
    const pc = postcode;
    if (type === 'gp') return [
        {name: 'Westminster GP Practice', address: '123 Victoria Street, London', postcode: pc, phone: '020 7123 4567'},
        {name: 'Palace Gardens Surgery', address: '45 Buckingham Gate', postcode: pc, phone: '020 7654 3210'}
    ];
    if (type === 'urgent') return [
        {name: 'St Thomas’ Urgent Treatment Centre', address: 'Westminster Bridge Road', postcode: 'SE1 7EH', phone: '020 7188 8888'}
    ];
    return [
        {name: 'Boots Pharmacy', address: 'High Street Branch', postcode: pc, phone: '020 7000 1111'},
        {name: 'Lloyds Pharmacy', address: 'Shopping Centre', postcode: pc, phone: '020 7222 3333'},
        {name: 'Superdrug Pharmacy', address: 'City Centre', postcode: pc, phone: '020 7333 4444'},
        {name: 'Well Pharmacy', address: 'Victoria Street', postcode: pc, phone: '020 7444 5555'}
    ];
}