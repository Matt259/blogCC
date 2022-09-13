var todaysDay = new Date(); //Date object
//store current year, month and day
var year = String(todaysDay.getFullYear());
var month = String(todaysDay.getMonth() + 1);
var day = String(todaysDay.getDate());


if(month < 10){
    month = '0'.concat(month)
}
if(day < 10){
    day = '0'.concat(day)
}

var maxDate = year.concat("-", month, "-", day);
document.getElementById("maxdate").setAttribute("max", maxDate);   //Finds the element by ID and sets the max atribute
document.getElementById("maxdate2").setAttribute("max", maxDate)



document.getElementById("popup").addEventListener('click', function(){  //opens up the edit popup
    document.querySelector('.bg-modal').style.display = 'flex';
    
});
document.querySelector('.closebtn').addEventListener('click', function(){   //closes the edit popup
    document.querySelector('.bg-modal').style.display = 'none';
})
