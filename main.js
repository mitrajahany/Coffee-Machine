const input = require('sync-input')

let repository = {
    water: 400,
    milk: 540,
    beans: 120,
    cups: 9,
    cash: 550
}

function remove(water, milk, beans, cash) {
    let shortage = [];
    let check = {'water': water, 'milk': milk, 'beans': beans}
    for (let item in check) {
        if (Math.floor(repository[item] / check[item]) < 1) {
            shortage.push(item)
        }
    }

    if (shortage.length > 0) {
        console.log(`Sorry, not enough ${shortage.join(' & ')}!`)
    } else {
        console.log("I have enough resources, making you a coffee!\n")
        repository.water -= water;
        repository.milk -= milk;
        repository.beans -= beans;
        repository.cash += cash;
        repository.cups -= 1;
    }
    action()
}

function buy() {
    let user = Number(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n"));
    switch (user) {
        case 1:
            remove(250, 0, 16, 4);
            break;
        case 2:
            remove(350, 75, 20, 7);
            break;
        case 3:
            remove(200, 100, 12, 6);
            break;
        default:
            break;
    }
}

function fill() {
    let upWater = Number(input("Write how many ml of water you want to add:\n"));
    let upMilk = Number(input('Write how many ml of milk you want to add:\n'));
    let upBeans = Number(input('Write how many grams of coffee beans you want to add:\n'));
    let upCups = Number(input('Write how many disposable coffee cups you want to add:\n'));
    repository.water += upWater;
    repository.milk += upMilk;
    repository.beans += upBeans;
    repository.cups += upCups;
    console.log();
}

function status() {
    console.log(`\nThe coffee machine has:
${repository.water} ml of water
${repository.milk} ml of milk
${repository.beans} g of coffee beans
${repository.cups} disposable cups
$${repository.cash} of money\n`);
}

function action() {
    let action = input("Write action (buy, fill, take, remaining, exit):\n");
    switch (action) {
        case "buy":
            buy();
            break;
        case 'fill':
            fill();
            break;
        case 'take':
            console.log(`I gave you $${repository.cash}\n`);
            repository.cash -= repository.cash;
            break;
        case "remaining":
            status();
            break;
        case 'exit':
            s = false;
            break;
        default:
            console.log('Wrong Input');
    }
}

let s = true;
while (s) {
    action();
}