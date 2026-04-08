import { useState } from "react";

function Mid(){

const [username, setUsername] = useState("");

const handleSearch = async () => {

try {

const response1 = await fetch(
"http://127.0.0.1:5000/check-profile",
{
method: "POST",
headers: {
"Content-Type": "application/json"
},
body: JSON.stringify({ username })
}
);

const data1 = await response1.json();


const response2 = await fetch(
"http://127.0.0.1:5000/monitor-username",
{
method: "POST",
headers: {
"Content-Type": "application/json"
},
body: JSON.stringify({ username })
}
);

const data2 = await response2.json();


let message =
"Risk Score: " +
data1.riskScore +
"\nPrediction: " +
data1.prediction;


// ✅ FIXED SECTION HERE
if(data2.alert && data2.matches.length > 0){

const usernames = data2.matches
.map(user => user.username)
.join(", ");

message +=
"\n⚠ Similar usernames detected: " +
usernames;

}

alert(message);

}

catch(error){

console.error(error);
alert("Server error");

}

};


return(

<>
<div className="ai-badge">
🤖 AI Fake Profile Detector
</div>

<div className="input">

<input
placeholder="Enter your id"
value={username}
onChange={(e)=>setUsername(e.target.value)}
/>

<br/>

<button onClick={handleSearch}>
search
</button>

</div>

</>

);

}

export default Mid;