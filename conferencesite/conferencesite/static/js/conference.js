//Workshop B in session 1 covers both the session 1 and session 2 time period, so a session 2 workshop can not be selected
// along with workshop B.  This validates that a selection in session 2 is not allowed if workshop B in session 1 is choosen.
function checkIfB(){
    var workshop1El = document.getElementsByName('session1');  // get the radiobuttons from the first session
    var workshop2El = document.getElementsByName('session2'); // get the radio buttons from the second session
    var errorMessage = "The \'Investigations Involving Automobile Media\' workshop from session 1 is an all day workshop." +
        "  You can't choose a workshop in session 2 if you will be participating in " +
        "\'Investigations Involving Automobile Media\'";

    workshop2El[0].required = true; // if workshop B is not selected then one workshop in each session must be taken

    if(workshop1El[1].checked) {
        for(var i = 0; i < workshop2El.length; i++) {
            workshop2El[i].required = false;  // if workshop B is selected, a workshop selection in session 2 is not required
            //check to see if a workshop in session 2 has been selected
        }
        for(var j = 0; j < workshop2El.length; j++){
            if(workshop2El[j].checked) {
                errorMessageWindow(errorMessage, 400, 500);

                workshop2El[j].checked = false; //deselect the selected workshop in session 2
            }
        }
    }
}

//According to the requirements, workshop F in session 2 and workshop H in session 3 must be taken together.  This
//function verifies that a participant chooses F and H only when the other is choosen as well.
function checkIfF(){
    var workshop3El = document.getElementsByName('session3');  // get the radio buttons from session 3
    var workshop2El = document.getElementsByName('session2'); //get the radio buttons from session 2
    var errorMessage = "The \'Security of Biometrics\' workshop from session 2 and the  " +
        "\'Identification and Authentication of Incidents\' workshop from session 3 must be taken together.";

    //if either workshops F or H are selected without the other being selected
        if((workshop2El[2].checked && !workshop3El[1].checked) || (workshop3El[1].checked && !workshop2El[2].checked)){
            //alert("The \'Security of Biometrics\' workshop from session 2 and the  " +
             //   "\'Identification and Authentication of Incidents\' workshop from session 3 must be taken together." )
            errorMessageWindow(errorMessage, 400, 500);
                for(var j = 0; j < workshop3El.length; j++) {
                    workshop3El[j].checked = false; // clear the selected radio button
                }
        }


}

function errorMessageWindow(errorMessage, h, w){
    var top = (screen.height/2)-(h/2);  //center horizontally
    var left = (screen.width/2)-(h/2);  //center vertically
    var errorWindow = window.open("", "", "height="+h+",width="+w+",top="+top+", left="+left+",menubar=no,resizable=0,status=yes,toolbar=no");
    errorWindow.document.writeln("<body bgcolor='#a9a9a9'>");
    errorWindow.document.writeln("</body>");
    errorWindow.document.write(errorMessage);
    errorWindow.document.writeln("<br> <br> <br>");
    errorWindow.document.write("<input type='button' value='close' onclick='window.close()'>");
}

//hold each session div in a variable
session1El = document.getElementById('id_session1');
session2El = document.getElementById('id_session2');
session3El = document.getElementById('id_session3');

//add the event listeners to listen for when a button is selected
session1El.addEventListener('change', checkIfB, false);  //check if workshop B is chosen
session2El.addEventListener('change', checkIfB, false);  //ensure workshop B not chosen
session2El.addEventListener('change', checkIfF, false); //check if workshop F and H selected together
session3El.addEventListener('change', checkIfF, false);  //check if workshop F and H selected together