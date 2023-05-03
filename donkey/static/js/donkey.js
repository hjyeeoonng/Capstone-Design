const category_1 = document.getElementById('category_1');
const category_2 = document.getElementById('category_2');
const category_3 = document.getElementById('category_3');
const category_4 = document.getElementById('category_4');

function moveInTabs(evt,tabName) {
    var i,tabcontent,tablinks;

    tabcontent = document.getElementsByClassName("tabcontent");
    for(i=0;i<tabcontent.length; i++) {
        tabcontent[i].style.display="none";
    }

    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}
document.getElementById("defaultOpen").click();