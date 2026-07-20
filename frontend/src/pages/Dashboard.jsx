import { Link, useNavigate } from "react-router-dom";

import useAuth from "../hooks/useAuth";

export default function Dashboard() {

    const navigate = useNavigate();

    const { logout } = useAuth();

    const handleLogout = () => {

        logout();

        navigate("/login");

    };

    return (

        <div className="container">

            <h1>Dashboard</h1>

            <p>

                Login Successful 🎉

            </p>

            <Link to="/students">

                Manage Students

            </Link>

            <br /><br />

            <button onClick={handleLogout}>

                Logout

            </button>

        </div>

    );

}