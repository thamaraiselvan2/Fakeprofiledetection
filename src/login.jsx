import { useState } from "react";

function Login() {

  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [phone, setPhone] = useState("");
  const [password, setPassword] = useState("");

  const handleRegister = async (event) => {

    event.preventDefault();

    try {

      const response = await fetch(
        "http://127.0.0.1:5000/register-user",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            username: username,
            email: email
          })
        }
      );

      const data = await response.json();

      alert(data.message);

      // Clear form after successful registration
      setUsername("");
      setEmail("");
      setPhone("");
      setPassword("");

    }

    catch(error){

      console.error(error);
      alert("Backend connection error");

    }

  };

  return(
        
    <div className="page-slide">
        
      <div className="register-wrapper">

        <div className="register-box">

          <h1>REGISTER NOW</h1>

          <form onSubmit={handleRegister}>

            <input
              type="text"
              placeholder="Enter User ID"
              required
              value={username}
              onChange={(e)=>setUsername(e.target.value)}
            />

            <input
              type="email"
              placeholder="Enter Email"
              required
              value={email}
              onChange={(e)=>setEmail(e.target.value)}
            />

            <input
              type="tel"
              placeholder="Enter Phone Number"
              required
              value={phone}
              onChange={(e)=>setPhone(e.target.value)}
            />

            <input
              type="password"
              placeholder="Enter Password"
              required
              value={password}
              onChange={(e)=>setPassword(e.target.value)}
            />

            <button type="submit">
              Submit
            </button>

          </form>

        </div>

      </div>

    </div>

  );

}

export default Login;