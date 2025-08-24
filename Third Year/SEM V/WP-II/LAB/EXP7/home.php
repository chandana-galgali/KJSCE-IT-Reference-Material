<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Perfume Paradise</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>Our Perfume Collection</h1>

    <!-- Form to Add/Edit Perfume -->
    <div id="create-form">
        <h2 id="form-title">Add a New Perfume</h2>
        <form id="perfumeForm">
            <input type="hidden" id="perfumeId">
            <input type="text" id="name" placeholder="Name" required>
            <input type="text" id="brand" placeholder="Brand" required>
            <input type="number" id="price" placeholder="Price" required>
            <textarea id="description" placeholder="Description" required></textarea>
            <button type="button" onclick="handleSave()">Add Perfume</button>
        </form>
    </div>

    <!-- Container to Display Perfume Collection -->
    <div id="perfumes-container" class="perfume-container"></div>

    <script>
        // Fetch and display perfumes
        function fetchPerfumes() {
            fetch('/WP-II/EXP7/api.php/perfumes')
                .then(response => response.json())
                .then(data => {
                    const container = document.getElementById('perfumes-container');
                    container.innerHTML = '';  // Clear previous content

                    data.forEach(perfume => {
                        const item = document.createElement('div');
                        item.className = 'perfume-card';
                        item.innerHTML = `
                            <h2>${perfume.name}</h2>
                            <p><strong>Brand:</strong> ${perfume.brand}</p>
                            <p><strong>Price:</strong> $${perfume.price}</p>
                            <p><strong>Description:</strong> ${perfume.description}</p>
                            <button onclick="deletePerfume(${perfume.id})">Delete</button>
                            <button onclick="editPerfume(${perfume.id}, '${perfume.name}', '${perfume.brand}', ${perfume.price}, '${perfume.description}')">Edit</button>
                        `;
                        container.appendChild(item);
                    });
                })
                .catch(error => console.error('Error fetching data:', error));
        }

        // Function to handle saving (Add or Update based on ID presence)
        function handleSave() {
            const id = document.getElementById('perfumeId').value;
            if (id) {
                updatePerfume(id); // Update if ID exists
            } else {
                createPerfume(); // Add new if ID is empty
            }
        }

        // CREATE: Add a new perfume
        function createPerfume() {
            const name = document.getElementById('name').value;
            const brand = document.getElementById('brand').value;
            const price = document.getElementById('price').value;
            const description = document.getElementById('description').value;

            fetch('/WP-II/EXP7/api.php/perfumes', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name, brand, price, description })
            })
            .then(response => response.json())
            .then(data => {
                alert(data.message);
                resetForm();
                fetchPerfumes(); // Refresh the list
            })
            .catch(error => console.error('Error adding perfume:', error));
        }

        // DELETE: Remove a perfume
        function deletePerfume(id) {
            if (confirm("Are you sure you want to delete this perfume?")) {
                fetch(`/WP-II/EXP7/api.php/perfumes/${id}`, {
                    method: 'DELETE'
                })
                .then(response => response.json())
                .then(data => {
                    alert(data.message);
                    fetchPerfumes(); // Refresh the list
                })
                .catch(error => console.error('Error deleting perfume:', error));
            }
        }

        // EDIT: Populate form with perfume data for editing
        function editPerfume(id, name, brand, price, description) {
            document.getElementById('perfumeId').value = id;
            document.getElementById('name').value = name;
            document.getElementById('brand').value = brand;
            document.getElementById('price').value = price;
            document.getElementById('description').value = description;

            document.getElementById('form-title').textContent = "Edit Perfume";
            document.querySelector('#perfumeForm button').textContent = "Update Perfume";
        }

        // UPDATE: Update a perfume's details
        function updatePerfume(id) {
            const name = document.getElementById('name').value;
            const brand = document.getElementById('brand').value;
            const price = document.getElementById('price').value;
            const description = document.getElementById('description').value;

            fetch(`/WP-II/EXP7/api.php/perfumes/${id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name, brand, price, description })
            })
            .then(response => response.json())
            .then(data => {
                alert(data.message);
                resetForm();
                fetchPerfumes(); // Refresh the list
            })
            .catch(error => console.error('Error updating perfume:', error));
        }

        // Reset the form and switch back to "Add" mode
        function resetForm() {
            document.getElementById('perfumeId').value = '';
            document.getElementById('name').value = '';
            document.getElementById('brand').value = '';
            document.getElementById('price').value = '';
            document.getElementById('description').value = '';
            document.getElementById('form-title').textContent = "Add a New Perfume";
            document.querySelector('#perfumeForm button').textContent = "Add Perfume";
        }

        // Load perfumes on page load
        fetchPerfumes();
    </script>
</body>
</html>