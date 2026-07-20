import { createContext, useEffect, useState } from "react";
import {
    getToken,
    saveToken,
    removeToken,
} from "../utils/auth";

export const AuthContext = createContext();

export function AuthProvider({ children }) {

    const [token, setToken] = useState(null);

    useEffect(() => {
        const storedToken = getToken();

        if (storedToken) {
            setToken(storedToken);
        }
    }, []);

    const login = (jwt) => {
        saveToken(jwt);
        setToken(jwt);
    };

    const logout = () => {
        removeToken();
        setToken(null);
    };

    return (
        <AuthContext.Provider
            value={{
                token,
                login,
                logout,
                authenticated: !!token,
            }}
        >
            {children}
        </AuthContext.Provider>
    );
}