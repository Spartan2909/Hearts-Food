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
    const options = Array.from(document.getElementsByClassName('foodCount'));
    
    for (let i = 0; i < options.length; i++) {

    }
}