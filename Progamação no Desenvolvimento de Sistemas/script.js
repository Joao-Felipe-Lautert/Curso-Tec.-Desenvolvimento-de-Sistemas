// 1. CRIAÇÃO DAS TABELAS (SCHEMA)
alasql(
  "CREATE TABLE itens (id INT, nome STRING, preco INT, icone STRING, estoque INT)"
);
alasql(
  "CREATE TABLE herois (id INT, nome STRING, ouro INT, avatar STRING, fala STRING)"
);

// 2. INSERÇÃO DE DADOS (POPULANDO O BANCO)
alasql("INSERT INTO itens VALUES (1, 'Poção de Vida', 25, '🧪', 15)");
alasql("INSERT INTO itens VALUES (2, 'Espada Longa', 100, '⚔️', 5)");
alasql("INSERT INTO itens VALUES (3, 'Anél Mágico', 250, '💍', 1)");
alasql("INSERT INTO itens VALUES (4, 'Arco Flamejante', 150, '🏹', 3)");
// ... Adicione mais itens aqui depois ...

alasql(
  "INSERT INTO herois VALUES (1, 'Aragorn', 200, '🧝‍♂️', 'Preciso de equipamentos.')"
);
alasql(
  "INSERT INTO herois VALUES (2, 'Gandalf', 1000, '🧙‍♂️', 'Tenho pressa, mercador.')"
);
alasql(
  "INSERT INTO herois VALUES (3, 'Sauron', 5000, '🦹🏿', 'Me de o que você tem de melhor.')"
);
alasql(
  "INSERT INTO herois VALUES (4, 'Ogro da floresta', 50, '🧌', 'Silêncio...')"
);

// Variável para controlar quem está na loja
let heroiAtualId = 1;

// FUNÇÃO: Desenha a tela baseada no Banco de Dados
function atualizarInterface() {
  // Busca itens no banco
  let itens = alasql("SELECT * FROM itens");
  let container = document.getElementById("shop-items");
  container.innerHTML = "";

  // Cria o HTML de cada item (Loop)
  itens.forEach((item) => {
    let div = document.createElement("div");
    div.className = "item-card";
    div.innerHTML = `
            <span class="item-icon">${item.icone}</span>
            <div class="item-name">${item.nome}</div>
            <div class="item-price">💰 ${item.preco}</div>
            <div class="item-stock">Estoque: ${item.estoque}</div>
        `;
    container.appendChild(div);
  });

  // Busca o herói atual
  let heroi = alasql(`SELECT * FROM herois WHERE id = ${heroiAtualId}`)[0];
  document.getElementById("hero-name").innerText = heroi.nome;
  document.getElementById("hero-gold").innerText = heroi.ouro;
  document.querySelector(".hero-avatar").innerText = heroi.avatar;
}

// FUNÇÃO: Troca de Cliente (Lógica de Fila)
function proximoCliente() {
  heroiAtualId++;
  if (heroiAtualId > 4) heroiAtualId = 1; // Volta para o primeiro se acabar
  atualizarInterface();
  alert("Cliente trocado!");
}

// Inicializa o jogo ao carregar a página
window.onload = atualizarInterface;
