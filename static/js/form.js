// JavaScript code
function updateJudul() {
    const kodeBukuField = document.getElementById('id_kodebuku');
    const judulField = document.getElementById('id_judul');
    
    const selectedKodeBuku = kodeBukuField.value;
    const selectedOption = kodeBukuField.options[kodeBukuField.selectedIndex];
    const selectedJudul = selectedOption.text;
    
    judulField.value = selectedJudul;
}
