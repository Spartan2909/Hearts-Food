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
    /* Nonfunctional
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
    */
}

function addDrink() {
    
}

function orderView() {
    orderNum = document.getElementById("ordernum").value;
    console.log("viewing order: " + orderNum);
    document.location = "/staff/" + orderNum;
}