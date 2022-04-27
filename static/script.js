function showItem(name) {
    document.getElementById('foodHot').style.display = 'none'
    document.getElementById('foodCold').style.display = 'none'
    document.getElementById('drinkHot').style.display = 'none'
    document.getElementById('drinkCold').style.display = 'none'

    document.getElementById(name).style.display = 'block'
}