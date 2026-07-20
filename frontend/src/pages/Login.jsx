import { Link, useNavigate } from "react-router-dom";
import { useState } from "react";

import api from "../api/axios";
import useAuth from "../hooks/useAuth";

export default function Login() {

    const navigate = useNavigate();

    const { login } = useAuth();

    const [username, setUsername] = useState("");

    const [password, setPassword] = useState("");

    const [error, setError] = useState("");

    const handleSubmit = async (e) => {

        e.preventDefault();

        setError("");

        try {

            const response = await api.post("/api/login", {

                username,

                password,

            });

            login(response.data.token);

            navigate("/dashboard");

        } catch (err) {

            setError(

                err.response?.data?.error ||

                "Login failed"

            );

        }

    };

    return (

        <div className="container">

            <h1>Student Management System</h1>

            <h2>Login</h2>

            <form onSubmit={handleSubmit}>

                <input

                    type="text"

                    placeholder="Username"

                    value={username}

                    onChange={(e) => setUsername(e.target.value)}

                    required

                />

                <input

                    type="password"

                    placeholder="Password"

                    value={password}

                    onChange={(e) => setPassword(e.target.value)}

                    required

                />

                <button type="submit">

                    Login

                </button>

            </form>

            {error && <p>{error}</p>}

            <p>

                Don't have an account?

                <Link to="/register">

                    Register

                </Link>

            </p>

        </div>

    );

}