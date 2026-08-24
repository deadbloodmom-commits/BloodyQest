// Инициализация Telegram Web App
const tg = window.Telegram.WebApp;
tg.expand();

// Данные игрока (можно получить через Telegram initData или заглушку для теста)
const player = {
    name: "Игрок",
    avatar: "https://via.placeholder.com/36/8b0000/ffffff?text=ME"
};

// База данных персонажей квеста
const characters = {
    "alister": {
        name: "Алистер",
        avatar: "https://via.placeholder.com/36/3d101d/ff1a1a?text=A"
    },
    "system": {
        name: "🩸 Тьма",
        avatar: "https://via.placeholder.com/36/000000/ff1a1a?text=!"
    }
};

// Сценарий квеста (жесткая линия сюжета, ведущая к цели)
const storyNodes = {
    "start": {
        messages: [
            { sender: "alister", text: "<strong>Дверь за вашей спиной с тяжелым стуком захлопывается.</strong> Вспыхивает тусклый свет свечи." },
            { sender: "alister", text: "Ну что, путник. Ты всё-таки переступил порог. Обратного пути больше нет." }
        ],
        choices: [
            { text: "Спросить, кто он такой и где мы находимся.", next: "node_1" },
            { text: "Попытаться дернуть за ручку закрытой двери.", next: "node_1" }
        ]
    },
    "node_1": {
        messages: [
            { sender: "system", text: "<strong>Холодный сквознок проносит по коридору шёпот множества голосов.</strong>" },
            { sender: "alister", name: "Алистер", text: "Бесполезно. Дом сам выбирает, кого впустить... и кого отпустить. Следуй за мной, если хочешь выжить." }
        ],
        choices: [
            { text: "Молча пойти следом за Алистером.", next: "node_2" },
            { text: "Отказаться и остаться на месте.", next: "node_2" } // Сюжет все равно вернет по сценарию
        ]
    },
    "node_2": {
        messages: [
            { sender: "alister", text: "<strong>Шаги гулко отдаются в пустом коридоре. Тень впереди начинает принимать странную форму...</strong>" },
            { sender: "alister", text: "Глава 1 завершена. Тьма запомнила твой выбор." }
        ],
        choices: []
    }
};

// Функция отрисовки сообщения в чате
function addMessage(senderKey, text, customName = null) {
    const chatContainer = document.getElementById("chat-messages");
    const char = characters[senderKey] || { name: customName || "Неизвестный", avatar: "https://via.placeholder.com/36" };

    const wrapper = document.createElement("div");
    wrapper.className = "message-wrapper";

    wrapper.innerHTML = `
        <img src="${char.avatar}" class="avatar" alt="avatar">
        <div class="message-content">
            <span class="sender-name">💬 ${char.name}</span>
            <div class="message-bubble">${text}</div>
        </div>
    `;

    chatContainer.appendChild(wrapper);
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

// Функция показа вариантов выбора
function showChoices(choices) {
    const container = document.getElementById("choices-container");
    container.innerHTML = "";

    choices.forEach(choice => {
        const btn = document.createElement("button");
        btn.className = "choice-btn";
        btn.innerText = choice.text;
        btn.onclick = () => {
            // Игрок отправляет свой выбор как сообщение от себя
            addMessage("player", `<strong>Выбор:</strong> ${choice.text}`, player.name);
            // Переходим к следующему шагу сценария
            loadNode(choice.next);
        };
        container.appendChild(btn);
    });
}

// Загрузка узла сценария с задержкой для эффекта живого диалога
function loadNode(nodeKey) {
    document.getElementById("choices-container").innerHTML = "";
    const node = storyNodes[nodeKey];
    if (!node) return;

    let delay = 300;
    node.messages.forEach((msg, index) => {
        setTimeout(() => {
            addMessage(msg.sender, msg.text, msg.name);
            
            // Если это последнее сообщение в узле, показываем кнопки выбора
            if (index === node.messages.length - 1) {
                setTimeout(() => showChoices(node.choices), 400);
            }
        }, delay);
        delay += 1200; // Пауза между сообщениями персонажей
    });
}

// Старт мини-приложения
window.onload = () => {
    // Если игрок открыл из Telegram, подставим его реальное имя
    if (tg.initDataUnsafe && tg.initDataUnsafe.user) {
        player.name = tg.initDataUnsafe.user.first_name || "Игрок";
    }
    loadNode("start");
};
