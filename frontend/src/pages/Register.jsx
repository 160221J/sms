import { useState } from "react";

import { Link, useNavigate } from "react-router-dom";

import api from "../api/axios";

export default function Register() {

    const navigate = useNavigate();

    const [form, setForm] = useState({

        first_name: "",

        last_name: "",

        username: "",

        email: "",

        password: "",

    });

    const [error, setError] = useState("");

    const handleChange = (e) => {

        setForm({

            ...form,

            [e.target.name]: e.target.value,

        });

    };

    const handleSubmit = async (e) => {

        e.preventDefault();

        setError("");

        try {

            await api.post("/api/register", form);

            navigate("/login");

        } catch (err) {

            setError(

                err.response?.data?.error ||

                "Registration failed"

            );

        }

    };

    return (

        <div className="container">

            <h1>Register</h1>

            <form onSubmit={handleSubmit}>

                <input name="first_name" placeholder="First Name" onChange={handleChange} required />

                <input name="last_name" placeholder="Last Name" onChange={handleChange} required />

                <input name="username" placeholder="Username" onChange={handleChange} required />

                <input name="email" type="email" placeholder="Email" onChange={handleChange} required />

                <input name="password" type="password" placeholder="Password" onChange={handleChange} required />

                <button type="submit">

                    Register

                </button>

            </form>

            {error && <p>{error}</p>}

            <p>

                Already have an account?

                <Link to="/login">

                    Login

                </Link>

            </p>

        </div>

    );

}