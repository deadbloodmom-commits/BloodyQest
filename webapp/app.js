// ==========================================
// ШЁПОТ — TELEGRAM MINI APP
// ГЛАВА I — НАЧАЛО
// ==========================================

const tg = window.Telegram?.WebApp;


// ==========================================
// TELEGRAM
// ==========================================

if (tg) {
    tg.ready();
    tg.expand();
}


// ==========================================
// ЭЛЕМЕНТЫ
// ==========================================

const storyContent =
    document.getElementById("story-content");

const choices =
    document.getElementById("choices");

const exitButton =
    document.getElementById("exit-button");

const backButton =
    document.getElementById("back-button");


// ==========================================
// ИМЯ ИГРОКА
// ==========================================

let playerName = "Ты";

if (
    tg &&
    tg.initDataUnsafe &&
    tg.initDataUnsafe.user &&
    tg.initDataUnsafe.user.first_name
) {
    playerName =
        tg.initDataUnsafe.user.first_name;
}


// ==========================================
// ПЕРСОНАЖИ
// ==========================================

const characters = {

    nina: {
        name: "Нина Крылова",
        avatar: "Н"
    },

    max: {
        name: "Макс Орлов",
        avatar: "М"
    },

    lera: {
        name: "Лера Соколова",
        avatar: "Л"
    },

    ilya: {
        name: "Илья Морозов",
        avatar: "И"
    }

};


// ==========================================
// СОСТОЯНИЕ
// ==========================================

let currentPosition = 0;

let chapterFinished = false;


// ==========================================
// СОХРАНЕНИЕ ПРОГРЕССА
// ==========================================

const PROGRESS_KEY =
    "shepot_quest_01_chapter_01_position";


// ==========================================
// ДОБАВИТЬ ДЕЙСТВИЕ
// ==========================================

function addAction(text) {

    const element =
        document.createElement("div");

    element.className =
        "story-message action";

    element.textContent =
        text;

    storyContent.appendChild(element);
}


// ==========================================
// ДОБАВИТЬ РЕПЛИКУ ПЕРСОНАЖА
// ==========================================

function addCharacterDialogue(character, text) {

    const element =
        document.createElement("div");

    element.className =
        "character-message";


    const avatar =
        document.createElement("div");

    avatar.className =
        "character-avatar";

    avatar.textContent =
        character.avatar;


    const body =
        document.createElement("div");

    body.className =
        "character-body";


    const name =
        document.createElement("div");

    name.className =
        "character-name";

    name.textContent =
        character.name;


    const message =
        document.createElement("div");

    message.className =
        "character-text";

    message.textContent =
        text;


    body.appendChild(name);
    body.appendChild(message);

    element.appendChild(avatar);
    element.appendChild(body);

    storyContent.appendChild(element);
}


// ==========================================
// ДОБАВИТЬ РЕПЛИКУ ИГРОКА
// ==========================================

function addPlayerDialogue(text) {

    const element =
        document.createElement("div");

    element.className =
        "player-message";


    const name =
        document.createElement("div");

    name.className =
        "player-name";

    name.textContent =
        playerName;


    const message =
        document.createElement("div");

    message.className =
        "player-text";

    message.textContent =
        text;


    element.appendChild(name);
    element.appendChild(message);

    storyContent.appendChild(element);
}


// ==========================================
// СИСТЕМНЫЙ ТЕКСТ
// ==========================================

function addSystem(text) {

    const element =
        document.createElement("div");

    element.className =
        "system-message";

    element.textContent =
        text;

    storyContent.appendChild(element);
}


// ==========================================
// СОХРАНЕНИЕ
// ==========================================

function saveProgress(position) {

    localStorage.setItem(
        PROGRESS_KEY,
        String(position)
    );
}


// ==========================================
// ЗАГРУЗКА
// ==========================================

function loadProgress() {

    const saved =
        localStorage.getItem(PROGRESS_KEY);

    if (saved === null) {
        return 0;
    }

    const position =
        Number(saved);

    if (Number.isNaN(position)) {
        return 0;
    }

    return position;
}


// ==========================================
// ГЛАВА I
// ==========================================

const story = [

    // 0
    {
        type: "action",
        text:
            "Ты начинаешь подозревать, что поездка в лагерь была ошибкой ещё до того, как автобус останавливается."
    },

    // 1
    {
        type: "action",
        text:
            "Не потому, что лагерь выглядит заброшенным."
    },

    // 2
    {
        type: "action",
        text:
            "Наоборот."
    },

    // 3
    {
        type: "action",
        text:
            "Слишком обычный."
    },

    // 4
    {
        type: "action",
        text:
            "За окном тянутся сосны, между которыми видны деревянные домики с зелёными крышами. Где-то дальше блестит озеро. На площадке возле столовой несколько вожатых таскают коробки."
    },

    // 5
    {
        type: "action",
        text:
            "Всё выглядит так, будто здесь ничего плохого никогда не происходило."
    },

    // 6
    {
        type: "max",
        text:
            "Мы приехали."
    },

    // 7
    {
        type: "action",
        text:
            "Макс стягивает с головы наушники."
    },

    // 8
    {
        type: "player",
        text:
            "Наконец-то."
    },

    // 9
    {
        type: "action",
        text:
            "Автобус тормозит."
    },

    // 10
    {
        type: "action",
        text:
            "Несколько человек сразу начинают вставать, доставать сумки, переговариваться. Ты ждёшь, пока проход освободится, и только потом выходишь."
    },

    // 11
    {
        type: "action",
        text:
            "Воздух здесь холоднее, чем ты ожидал."
    },

    // 12
    {
        type: "action",
        text:
            "Ты делаешь несколько шагов и останавливаешься."
    },

    // 13
    {
        type: "action",
        text:
            "Перед воротами лагеря стоит старая деревянная табличка."
    },

    // 14
    {
        type: "system",
        text:
            "«СОСНОВОЕ ОЗЕРО»"
    },

    // 15
    {
        type: "action",
        text:
            "Ниже когда-то было написано ещё что-то, но буквы почти полностью стёрлись."
    },

    // 16
    {
        type: "nina",
        text:
            "Что?"
    },

    // 17
    {
        type: "player",
        text:
            "Ничего."
    },

    // 18
    {
        type: "nina",
        text:
            "Просто показалось знакомым."
    },

    // 19
    {
        type: "player",
        text:
            "Ты здесь была?"
    },

    // 20
    {
        type: "nina",
        text:
            "Нет."
    },

    // 21
    {
        type: "action",
        text:
            "Она отвечает слишком быстро."
    },

    // 22
    {
        type: "action",
        text:
            "Ты хочешь переспросить, но Макс уже кричит откуда-то с дороги."
    },

    // 23
    {
        type: "max",
        text:
            "Вы двое! Если хотите занять нормальные комнаты, идите сейчас!"
    },

    // 24
    {
        type: "nina",
        text:
            "Идём."
    },

    // 25
    {
        type: "action",
        text:
            "Вы направляетесь к остальным."
    },

    // 26
    {
        type: "action",
        text:
            "Через несколько минут вас расселяют."
    },

    // 27
    {
        type: "action",
        text:
            "Ты, Макс и Илья получаете один домик."
    },

    // 28
    {
        type: "action",
        text:
            "Нина и Лера — соседний."
    },

    // 29
    {
        type: "action",
        text:
            "Ваш домик стоит почти у самого леса."
    },

    // 30
    {
        type: "action",
        text:
            "Когда ты заходишь внутрь, первое, что замечаешь, — запах сырого дерева."
    },

    // 31
    {
        type: "action",
        text:
            "В комнате четыре кровати."
    },

    // 32
    {
        type: "action",
        text:
            "На стене висит старый плакат с правилами лагеря."
    },

    // 33
    {
        type: "system",
        text:
            "После 22:00 не покидать территорию домика."
    },

    // 34
    {
        type: "system",
        text:
            "Не приближаться к озеру ночью."
    },

    // 35
    {
        type: "system",
        text:
            "Не заходить в заброшенные здания."
    },

    // 36
    {
        type: "action",
        text:
            "Последнее правило почему-то выделено красным."
    },

    // 37
    {
        type: "max",
        text:
            "Смотрите."
    },

    // 38
    {
        type: "action",
        text:
            "Он показывает на нижнюю часть плаката."
    },

    // 39
    {
        type: "action",
        text:
            "Там, под правилами, осталась ещё одна строка."
    },

    // 40
    {
        type: "action",
        text:
            "Почти стёртая."
    },

    // 41
    {
        type: "system",
        text:
            "«Если ночью услышите...»"
    },

    // 42
    {
        type: "max",
        text:
            "Очень гостеприимно."
    },

    // 43
    {
        type: "ilya",
        text:
            "Наверное, про животных."
    },

    // 44
    {
        type: "player",
        text:
            "В этом лесу живут медведи?"
    },

    // 45
    {
        type: "max",
        text:
            "Теперь живут."
    },

    // 46
    {
        type: "action",
        text:
            "Вы смеётесь."
    },

    // 47
    {
        type: "action",
        text:
            "Только Нина не смеётся."
    },

    // 48
    {
        type: "action",
        text:
            "Она стоит в дверях и смотрит на плакат."
    },

    // 49
    {
        type: "action",
        text:
            "В руках у неё камера."
    },

    // 50
    {
        type: "action",
        text:
            "Она снимает плакат."
    },

    // 51
    {
        type: "system",
        text:
            "К вечеру лагерь оживает."
    },

    // 52
    {
        type: "action",
        text:
            "Ужин. Знакомство. Какие-то игры. Музыка возле столовой."
    },

    // 53
    {
        type: "action",
        text:
            "Обычный первый день."
    },

    // 54
    {
        type: "action",
        text:
            "Ты почти перестаёшь думать о странном плакате."
    },

    // 55
    {
        type: "action",
        text:
            "Почти."
    },

    // 56
    {
        type: "nina",
        text:
            "Ты видел здание возле леса?"
    },

    // 57
    {
        type: "player",
        text:
            "Компьютерный клуб?"
    },

    // 58
    {
        type: "nina",
        text:
            "Там ночью горит свет."
    },

    // 59
    {
        type: "max",
        text:
            "Ты серьёзно?"
    },

    // 60
    {
        type: "nina",
        text:
            "Да."
    },

    // 61
    {
        type: "max",
        text:
            "Ты туда заходила?"
    },

    // 62
    {
        type: "nina",
        text:
            "Нет."
    },

    // 63
    {
        type: "max",
        text:
            "Почему?"
    },

    // 64
    {
        type: "nina",
        text:
            "Потому что дверь заперта."
    },

    // 65
    {
        type: "ilya",
        text:
            "Значит, свет тебе показался."
    },

    // 66
    {
        type: "action",
        text:
            "Нина ничего не отвечает."
    },

    // 67
    {
        type: "action",
        text:
            "Она смотрит на тебя."
    },

    // 68
    {
        type: "nina",
        text:
            "Ты тоже видел?"
    },

    // 69
    {
        type: "player",
        text:
            "Не знаю."
    },

    // 70
    {
        type: "action",
        text:
            "Ты вспоминаешь дорогу к домику. Тёмные окна. Старое здание. И один момент, когда тебе действительно показалось, что за стеклом кто-то стоял."
    },

    // 71
    {
        type: "nina",
        text:
            "Ладно."
    },

    // 72
    {
        type: "action",
        text:
            "Теперь ты постоянно думаешь о том здании."
    },

    // 73
    {
        type: "system",
        text:
            "22:00"
    },

    // 74
    {
        type: "action",
        text:
            "Вас отправляют по домикам."
    },

    // 75
    {
        type: "system",
        text:
            "22:17"
    },

    // 76
    {
        type: "action",
        text:
            "Выключается свет."
    },

    // 77
    {
        type: "system",
        text:
            "22:31"
    },

    // 78
    {
        type: "action",
        text:
            "Макс засыпает."
    },

    // 79
    {
        type: "action",
        text:
            "Илья тоже."
    },

    // 80
    {
        type: "action",
        text:
            "Ты лежишь на кровати и смотришь в потолок."
    },

    // 81
    {
        type: "action",
        text:
            "Сон не приходит."
    },

    // 82
    {
        type: "action",
        text:
            "За окном шумят сосны."
    },

    // 83
    {
        type: "action",
        text:
            "Ветер двигает ветки."
    },

    // 84
    {
        type: "action",
        text:
            "Ты переворачиваешься на бок."
    },

    // 85
    {
        type: "action",
        text:
            "И вдруг слышишь звук."
    },

    // 86
    {
        type: "system",
        text:
            "Тук."
    },

    // 87
    {
        type: "action",
        text:
            "Ты открываешь глаза."
    },

    // 88
    {
        type: "system",
        text:
            "Тук."
    },

    // 89
    {
        type: "action",
        text:
            "Теперь громче."
    },

    // 90
    {
        type: "action",
        text:
            "Звук идёт от окна."
    },

    // 91
    {
        type: "action",
        text:
            "Ты несколько секунд просто смотришь на тёмное стекло."
    },

    // 92
    {
        type: "action",
        text:
            "Потом медленно встаёшь."
    },

    // 93
    {
        type: "action",
        text:
            "Подходишь ближе."
    },

    // 94
    {
        type: "action",
        text:
            "Снаружи ничего нет."
    },

    // 95
    {
        type: "action",
        text:
            "Только лес."
    },

    // 96
    {
        type: "action",
        text:
            "Ты уже собираешься вернуться к кровати, когда слышишь:"
    },

    // 97
    {
        type: "system",
        text:
            "— Эй..."
    },

    // 98
    {
        type: "action",
        text:
            "Ты замираешь."
    },

    // 99
    {
        type: "action",
        text:
            "Голос доносится снаружи."
    },

    // 100
    {
        type: "action",
        text:
            "Очень тихий."
    },

    // 101
    {
        type: "player",
        text:
            "Кто там?"
    },

    // 102
    {
        type: "action",
        text:
            "Ответа нет."
    },

    // 103
    {
        type: "action",
        text:
            "Только ветер."
    },

    // 104
    {
        type: "action",
        text:
            "Ты уже хочешь открыть окно, когда замечаешь кое-что странное."
    },

    // 105
    {
        type: "action",
        text:
            "На стекле снаружи отпечаталась ладонь."
    },

    // 106
    {
        type: "action",
        text:
            "Большая."
    },

    // 107
    {
        type: "action",
        text:
            "Человеческая."
    },

    // 108
    {
        type: "action",
        text:
            "Ты отступаешь."
    },

    // 109
    {
        type: "action",
        text:
            "И в этот момент телефон на кровати начинает вибрировать."
    },

    // 110
    {
        type: "system",
        text:
            "Одно сообщение. От Нины."
    },

    // 111
    {
        type: "nina",
        text:
            "Не подходи к окну."
    },

    // 112
    {
        type: "action",
        text:
            "Ты медленно смотришь обратно на стекло."
    },

    // 113
    {
        type: "action",
        text:
            "Ладонь исчезла."
    },

    // 114
    {
        type: "action",
        text:
            "Но теперь там стоит человек."
    },

    // 115
    {
        type: "action",
        text:
            "Мальчик. Примерно твоего возраста."
    },

    // 116
    {
        type: "action",
        text:
            "Он стоит между деревьями и смотрит прямо на тебя."
    },

    // 117
    {
        type: "action",
        text:
            "Ты не можешь разглядеть его лица."
    },

    // 118
    {
        type: "action",
        text:
            "Только одежду."
    },

    // 119
    {
        type: "action",
        text:
            "Старую лагерную форму."
    },

    // 120
    {
        type: "action",
        text:
            "И маленькую белую нашивку на груди."
    },

    // 121
    {
        type: "system",
        text:
            "«Смена 2016»."
    },

    // 122
    {
        type: "action",
        text:
            "Телефон снова вибрирует."
    },

    // 123
    {
        type: "system",
        text:
            "Второе сообщение от Нины."
    },

    // 124
    {
        type: "nina",
        text:
            "Ты тоже его видишь?"
    },

    // 125
    {
        type: "action",
        text:
            "Ты не успеваешь ответить."
    },

    // 126
    {
        type: "action",
        text:
            "Потому что мальчик в лесу поднимает руку."
    },

    // 127
    {
        type: "action",
        text:
            "И показывает пальцем прямо на тебя."
    },

    // 128
    {
        type: "action",
        text:
            "А затем исчезает."
    },

    // 129
    {
        type: "action",
        text:
            "Не убегает."
    },

    // 130
    {
        type: "action",
        text:
            "Не отходит."
    },

    // 131
    {
        type: "action",
        text:
            "Просто исчезает."
    },

    // 132
    {
        type: "action",
        text:
            "Ты стоишь у окна ещё несколько секунд."
    },

    // 133
    {
        type: "action",
        text:
            "Потом замечаешь кое-что на подоконнике."
    },

    // 134
    {
        type: "action",
        text:
            "Там лежит фотография."
    },

    // 135
    {
        type: "action",
        text:
            "Ты точно знаешь, что секунду назад её не было."
    },

    // 136
    {
        type: "action",
        text:
            "На фотографии изображены пятеро подростков."
    },

    // 137
    {
        type: "action",
        text:
            "Двое из них — ты и Нина."
    },

    // 138
    {
        type: "action",
        text:
            "Третий — Макс."
    },

    // 139
    {
        type: "action",
        text:
            "Четвёртый — Илья."
    },

    // 140
    {
        type: "action",
        text:
            "Пятая — Лера."
    },

    // 141
    {
        type: "action",
        text:
            "Вы стоите возле озера."
    },

    // 142
    {
        type: "action",
        text:
            "Все пятеро смотрят в камеру."
    },

    // 143
    {
        type: "action",
        text:
            "А между вами стоит тот самый мальчик."
    },

    // 144
    {
        type: "action",
        text:
            "На обратной стороне фотографии стоит дата:"
    },

    // 145
    {
        type: "system",
        text:
            "18 августа 2016 года."
    },

    // 146
    {
        type: "action",
        text:
            "Ты переворачиваешь фотографию обратно."
    },

    // 147
    {
        type: "action",
        text:
            "И понимаешь самое страшное."
    },

    // 148
    {
        type: "system",
        text:
            "Сегодня тоже 18 августа."
    }

];


// ==========================================
// ПОКАЗ ЭЛЕМЕНТА
// ==========================================

function showItem(index) {

    if (index >= story.length) {

        finishChapter();

        return;
    }

    const item =
        story[index];

    choices.innerHTML = "";


    if (item.type === "action") {

        addAction(item.text);
    }


    else if (item.type === "nina") {

        addCharacterDialogue(
            characters.nina,
            item.text
        );
    }


    else if (item.type === "max") {

        addCharacterDialogue(
            characters.max,
            item.text
        );
    }


    else if (item.type === "lera") {

        addCharacterDialogue(
            characters.lera,
            item.text
        );
    }


    else if (item.type === "ilya") {

        addCharacterDialogue(
            characters.ilya,
            item.text
        );
    }


    else if (item.type === "player") {

        addPlayerDialogue(item.text);
    }


    else if (item.type === "system") {

        addSystem(item.text);
    }


    currentPosition =
        index + 1;

    saveProgress(
        currentPosition
    );


    setTimeout(
        () => {

            showItem(
                currentPosition
            );

        },
        700
    );
}


// ==========================================
// ЗАВЕРШЕНИЕ
// ==========================================

function finishChapter() {

    if (chapterFinished) {
        return;
    }

    chapterFinished = true;

    choices.innerHTML = "";

    addSystem(
        "Глава I завершена."
    );

    addAction(
        "Продолжение следует..."
    );

    saveProgress(
        story.length
    );
}


// ==========================================
// ВЫХОД
// ==========================================

if (backButton) {

    backButton.addEventListener(
        "click",
        () => {

            if (tg) {
                tg.close();
            }

        }
    );
}


if (exitButton) {

    exitButton.addEventListener(
        "click",
        () => {

            if (tg) {
                tg.close();
            }

        }
    );
}


// ==========================================
// ЗАПУСК
// ==========================================

function startChapter() {

    currentPosition =
        loadProgress();

    storyContent.innerHTML = "";

    choices.innerHTML = "";

    chapterFinished = false;


    if (
        currentPosition > 0 &&
        currentPosition < story.length
    ) {

        addSystem(
            "Продолжение с места остановки..."
        );

    }


    showItem(
        currentPosition
    );
}


startChapter();