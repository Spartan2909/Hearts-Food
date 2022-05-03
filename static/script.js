function showDrink(name) {
    //console.log('running showDrink');

    document.getElementById('drinkHot').style.display = 'none';
    document.getElementById('drinkCold').style.display = 'none';

    document.getElementById(name).style.display = 'block';
}

function showFood(name) {
    //console.log('running showFood');
    
    document.getElementById('foodHot').style.display = 'none';
    document.getElementById('foodCold').style.display = 'none';

    document.getElementById(name).style.display = 'block';
}

function addFood() {
    const choices  = {}
    const options = Array.from(document.getElementsByClassName('foodCount'));
    
    for (let i = 0; i < options.length; i++) {
        if (options[i].value != 0) {
            choices[options[i].id] = options[i].value;
        }
    }

    fetch('/add?origin=food', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(choices)
    }).then(res => {
        console.log('posted items to add, respose:', res);
    });
}

function orderView() {
    orderNum = document.getElementById("orderNum").value
    console.log("viewing order: " + orderNum)
    console.log("going to location: /staff?ordernum=" + orderNum)
    document.location.href = "/staff?ordernum=" + orderNum
}