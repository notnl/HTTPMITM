async function FetchFromServer(){
    try {
        testAwaitObj = await fetch('http://localhost:9090/nexttraffic')
        cText = await testAwaitObj.text()
        return cText
    }
    catch (error) {

        console.log("No Avaliable traffic!")
        console.log(error)
    }
}
function NextTraffic(){
    FetchFromServer().then(
        capturedText => {
            document.open()
            document.write("<button type='button' onclick='NextTraffic()'>Next Traffic</button>");

            document.write("<p>This is the intercepted traffic:</p>");
            var tempDiv = document.createElement('div');
            tempDiv.innerHTML = capturedText;

            document.body.appendChild(tempDiv);
            }
        )
        .catch(
        err => {
           console.log(err) 
        }
    )

}

document.addEventListener("DOMContentLoaded", event => {

  console.log("DOM fully loaded and parsed" + event);
});
