// Инициализация Telegram WebApp с защитой от запуска в обычном браузере
let heroName = "Тень";
try {
    const tg = window.Telegram.WebApp;
    tg.expand();
    if (tg.initDataUnsafe && tg.initDataUnsafe.user && tg.initDataUnsafe.user.first_name) {
        heroName = tg.initDataUnsafe.user.first_name;
    }
} catch (e) {
    console.log("Запущено вне Telegram, используется имя по умолчанию.");
}

const chatMessages = document.getElementById("chat-messages");
const choicesContainer = document.getElementById("choices-container");
const inputContainer = document.getElementById("input-container");
const userInputField = document.getElementById("user-input-field");
const sendBtn = document.getElementById("send-btn");

function addMessage(sender, text, isHero = false, isSystem = false) {
    const msgDiv = document.createElement("div");
    msgDiv.classList.add("message");
    
    if (isHero) {
        msgDiv.classList.add("hero-message");
    } else if (isSystem) {
        msgDiv.classList.add("system-msg");
    }

    if (sender) {
        const senderSpan = document.createElement("span");
        senderSpan.classList.add("sender-name");
        senderSpan.textContent = sender;
        msgDiv.appendChild(senderSpan);
    }

    const textP = document.createElement("div");
    textP.innerHTML = text;
    msgDiv.appendChild(textP);

    chatMessages.appendChild(msgDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function clearChoices() {
    choicesContainer.innerHTML = "";
}

function showChoices(choices) {
    clearChoices();
    choices.forEach(choice => {
        const btn = document.createElement("button");
        btn.classList.add("choice-btn");
        btn.textContent = choice.text;
        btn.onclick = () => choice.action();
        choicesContainer.appendChild(btn);
    });
}

// Старт сюжетной линии
function startQuest() {
    setTimeout(() => {
        addMessage("Алистер", "Ты всё-таки пришёл... Дверь за тобой заперта. Обратной дороги нет.");
    }, 600);

    setTimeout(() => {
        addMessage("📱 Уведомление", "<i>Алистер печатает сообщение на разбитом смартфоне...</i>", false, true);
    }, 2200);

    setTimeout(() => {
        addMessage("Алистер", "Возьми этот фонарь. Он понадобится, чтобы разогнать мрак в коридоре.");
        
        showChoices([
            { text: "Взять фонарь и спросить, что здесь происходит", action: stepTwoOptions },
            { text: "Оттолкнуть Алистера и попытаться выбить дверь", action: stepTwoForce }
        ]);
    }, 3800);
}

function stepTwoOptions() {
    addMessage(heroName, "Взять фонарь и спросить, что здесь происходит.", true);
    
    setTimeout(() => {
        addMessage("Вэл", "Глупец... Фонарь только привлечет их внимание.");
        
        setTimeout(() => {
            addMessage("Система", "Алистер смотрит на вас в упор. Что вы ему ответите?", false, true);
            inputContainer.classList.remove("hidden");
            
            sendBtn.onclick = () => {
                const userText = userInputField.value.trim();
                if (userText) {
                    addMessage(heroName, userText, true);
                    userInputField.value = "";
                    inputContainer.classList.add("hidden");
                    
                    setTimeout(() => {
                        addMessage("Алистер", `Интересный ответ, ${heroName}... Посмотрим, как ты запоешь дальше.`);
                    }, 1000);
                }
            };
        }, 1500);
    }, 1000);
}

function stepTwoForce() {
    addMessage(heroName, "Оттолкнуть Алистера и попытаться выбить дверь.", true);
    
    setTimeout(() => {
        addMessage("Алистер", "Дерево под твоими руками оказывается холодным и мягким, как плоть...");
    }, 1000);
}

// Запуск при загрузке страницы
window.onload = () => {
    startQuest();
};