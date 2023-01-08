/* get element */

const apExam = '2 May 2023'

const daysEl = document.getElementById("days");
const hoursEl = document.getElementById("hours");
const minsEl = document.getElementById("mins");
const secondsEl = document.getElementById("seconds");

function countdown(){
    const currentDate = new Date();
    const apExamDate = new Date(apExam);

    //get total second to the 2 May 2023
    const totalsecond = (apExamDate-currentDate) / 1000;

    const days = Math.floor(totalsecond / 3600 /24);
    const hours = Math.floor(totalsecond /3600) % 24;
    const mins = Math.floor(totalsecond / 60) % 60;
    const seconds = Math.floor(totalsecond) % 60;

    /* console.log( apExamDate - currentDate); */

    daysEl.innerHTML = days;
    hoursEl.innerHTML = formatTime(hours);
    minsEl.innerHTML = formatTime(mins);
    secondsEl.innerHTML = formatTime(seconds);
}

function formatTime(time){
    return time < 10 ? `0${time}` : time;
}

//inital call
countdown();

//every 1s call function countdown
setInterval(countdown,1000);


