// Obtém os elementos necessários
const abrirBtn = document.getElementById('abrir');
const barraLateral = document.getElementById('barra-lateral');
const fecharBtn = document.getElementById('fechar');

// Quando o botão de abrir for clicado, exibe a barra lateral
abrirBtn.addEventListener('click', function() {
    barraLateral.style.width = '250px'; // Expande a barra lateral
});

// Quando o botão de fechar for clicado, esconde a barra lateral
fecharBtn.addEventListener('click', function() {
    barraLateral.style.width = '0'; // Fecha a barra lateral
});
