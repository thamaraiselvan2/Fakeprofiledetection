import { useNavigate } from "react-router-dom";
function Top(){
     const navigate = useNavigate();  
    return(
        <>
        <div className="background-animation">
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        </div>
        <div className="main">
            <div className="heading">
            <h1><i>🛡 Fake Profile Detector</i></h1>
            </div>
            <div><button onClick={() => navigate("/login")} className="Registerbutton">Register</button></div>
            
        </div>
        </>
       
    );
}

export default Top;