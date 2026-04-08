import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
function Splash() {

    const navigate = useNavigate();

    useEffect(() => {

        setTimeout(() => {

            navigate("/home");

        }, 3500);

    }, []);

    return (

        <div className="splash-container">

            <h1 className="title">
                FAKE PROFILE DETECTOR
            </h1>

            <p className="subtitle">
                by TechAuraX
            </p>

        </div>

    );
}

export default Splash;